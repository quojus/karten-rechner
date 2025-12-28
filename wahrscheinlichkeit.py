# === EINSTELLUNGEN ===
# Karten pro Symbol (Farbe)
HERZ = 6
KARO = 4
PIK = 7
KREUZ = 5
JOKER = 2  # Joker zählen als beliebige Farbe

MAX_DRAW = 10      # Maximale Anzahl gezogener Karten
MAX_REQUIRED = 5   # Maximale Anzahl benötigter Symbole

# Ansichtsmodus: 'absolut' oder 'differenz'
# 'differenz' zeigt Abweichung zur Gleichverteilung (5 pro Farbe, 0 Joker)
MODUS = 'differenz'

OUTPUT_PATH = "output/heatmap_erfolg.png"
# =====================

# Baseline für Differenz-Berechnung
BASELINE_SYMBOL = 5
BASELINE_JOKER = 0
BASELINE_DECK = 20  # 4 * 5

import numpy as np
import matplotlib
matplotlib.use('Agg')  # Headless für Datei-Export, in PyCharm 'QtAgg' verwenden
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from scipy.special import comb
from pathlib import Path


# Custom Colormap: Weiß (0%) -> Rot -> Gelb -> Grün (100%)
CMAP_ABSOLUT = LinearSegmentedColormap.from_list(
    'erfolg',
    [(0.0, 'white'),      # 0% = unmöglich
     (0.01, '#d73027'),   # knapp über 0 = dunkelrot
     (0.25, '#f46d43'),   # 25% = rot
     (0.5, '#fee08b'),    # 50% = gelb
     (0.75, '#a6d96a'),   # 75% = hellgrün
     (1.0, '#1a9850')]    # 100% = dunkelgrün
)

# Divergierende Colormap für Differenz: Rot (schlechter) -> Weiß (gleich) -> Blau (besser)
CMAP_DIFFERENZ = LinearSegmentedColormap.from_list(
    'differenz',
    [(0.0, '#b2182b'),    # -30% = dunkelrot
     (0.25, '#ef8a62'),   # -15% = rot
     (0.5, '#f7f7f7'),    # 0% = weiß (keine Änderung)
     (0.75, '#67a9cf'),   # +15% = blau
     (1.0, '#2166ac')]    # +30% = dunkelblau
)


# Symbol-Konfiguration
SYMBOLE = {
    'Herz': {'count': HERZ, 'color': '#e74c3c', 'symbol': '♥'},
    'Karo': {'count': KARO, 'color': '#e67e22', 'symbol': '♦'},
    'Pik': {'count': PIK, 'color': '#2c3e50', 'symbol': '♠'},
    'Kreuz': {'count': KREUZ, 'color': '#27ae60', 'symbol': '♣'},
}


def deck_size() -> int:
    """Berechnet die Gesamtgröße des Decks."""
    return sum(s['count'] for s in SYMBOLE.values()) + JOKER


def multivariate_hypergeom_pmf(gezogen: int, symbol_gezogen: int,
                                joker_gezogen: int, symbol_count: int,
                                joker_count: int, andere_count: int) -> float:
    """
    Wahrscheinlichkeit für genau (symbol_gezogen, joker_gezogen) bei Ziehung.
    """
    andere_gezogen = gezogen - symbol_gezogen - joker_gezogen

    if andere_gezogen < 0 or andere_gezogen > andere_count:
        return 0.0
    if symbol_gezogen < 0 or symbol_gezogen > symbol_count:
        return 0.0
    if joker_gezogen < 0 or joker_gezogen > joker_count:
        return 0.0

    total = symbol_count + joker_count + andere_count

    zaehler = comb(symbol_count, symbol_gezogen, exact=True) * \
              comb(joker_count, joker_gezogen, exact=True) * \
              comb(andere_count, andere_gezogen, exact=True)
    nenner = comb(total, gezogen, exact=True)

    return zaehler / nenner if nenner > 0 else 0.0


def erfolgswahrscheinlichkeit(gezogen: int, benoetigt: int,
                               symbol_count: int, joker_count: int,
                               total_deck: int) -> float:
    """
    Berechnet P(Symbol + Joker >= benoetigt).
    """
    if benoetigt <= 0:
        return 1.0

    andere_count = total_deck - symbol_count - joker_count

    erfolg = 0.0
    for s in range(min(symbol_count, gezogen) + 1):
        for j in range(min(joker_count, gezogen - s) + 1):
            if s + j >= benoetigt:
                erfolg += multivariate_hypergeom_pmf(
                    gezogen, s, j, symbol_count, joker_count, andere_count
                )

    return min(erfolg, 1.0)


def erstelle_wahrscheinlichkeits_matrix(symbol_count: int) -> np.ndarray:
    """Erstellt Matrix mit Erfolgswahrscheinlichkeiten für ein Symbol."""
    matrix = np.zeros((MAX_REQUIRED, MAX_DRAW))
    total = deck_size()

    for benoetigt in range(1, MAX_REQUIRED + 1):
        for gezogen in range(1, MAX_DRAW + 1):
            matrix[benoetigt - 1, gezogen - 1] = erfolgswahrscheinlichkeit(
                gezogen, benoetigt, symbol_count, JOKER, total
            )

    return matrix


def erstelle_baseline_matrix() -> np.ndarray:
    """Erstellt Baseline-Matrix (5 pro Farbe, 0 Joker, 20 Karten)."""
    matrix = np.zeros((MAX_REQUIRED, MAX_DRAW))

    for benoetigt in range(1, MAX_REQUIRED + 1):
        for gezogen in range(1, MAX_DRAW + 1):
            matrix[benoetigt - 1, gezogen - 1] = erfolgswahrscheinlichkeit(
                gezogen, benoetigt, BASELINE_SYMBOL, BASELINE_JOKER, BASELINE_DECK
            )

    return matrix


def erstelle_subplot_absolut(ax: plt.Axes, matrix: np.ndarray,
                              name: str, symbol: str, count: int):
    """Erstellt einen Subplot im Absolut-Modus."""
    im = ax.imshow(matrix, cmap=CMAP_ABSOLUT, aspect='auto', vmin=0, vmax=1)

    ax.set_xticks(range(MAX_DRAW))
    ax.set_xticklabels(range(1, MAX_DRAW + 1), fontsize=9)
    ax.set_yticks(range(MAX_REQUIRED))
    ax.set_yticklabels(range(1, MAX_REQUIRED + 1), fontsize=9)

    ax.set_xlabel('Gezogene Karten', fontsize=10)
    ax.set_ylabel('Benötigte Symbole', fontsize=10)
    ax.set_title(f'{symbol} {name} ({count} Karten)', fontsize=11, fontweight='bold')

    for i in range(MAX_REQUIRED):
        for j in range(MAX_DRAW):
            wert = matrix[i, j]
            if wert == 0:
                textfarbe = 'gray'
            elif wert < 0.35 or wert > 0.7:
                textfarbe = 'white'
            else:
                textfarbe = 'black'
            ax.text(j, i, f'{wert*100:.0f}%', ha='center', va='center',
                   color=textfarbe, fontsize=8, fontweight='bold')

    return im


def erstelle_subplot_differenz(ax: plt.Axes, matrix: np.ndarray,
                                baseline: np.ndarray, name: str,
                                symbol: str, count: int):
    """Erstellt einen Subplot im Differenz-Modus."""
    diff = matrix - baseline

    # Differenz-Range: -30% bis +30%
    im = ax.imshow(diff, cmap=CMAP_DIFFERENZ, aspect='auto', vmin=-0.3, vmax=0.3)

    ax.set_xticks(range(MAX_DRAW))
    ax.set_xticklabels(range(1, MAX_DRAW + 1), fontsize=9)
    ax.set_yticks(range(MAX_REQUIRED))
    ax.set_yticklabels(range(1, MAX_REQUIRED + 1), fontsize=9)

    ax.set_xlabel('Gezogene Karten', fontsize=10)
    ax.set_ylabel('Benötigte Symbole', fontsize=10)

    # Zeige Differenz im Titel
    diff_symbol = "+" if count > BASELINE_SYMBOL else "" if count == BASELINE_SYMBOL else ""
    diff_count = count - BASELINE_SYMBOL
    diff_text = f" ({diff_symbol}{diff_count:+d})" if diff_count != 0 else ""
    ax.set_title(f'{symbol} {name} ({count} Karten){diff_text}',
                 fontsize=11, fontweight='bold')

    for i in range(MAX_REQUIRED):
        for j in range(MAX_DRAW):
            wert = diff[i, j]
            # Textfarbe basierend auf Hintergrund
            if abs(wert) < 0.05:
                textfarbe = 'gray'
            elif abs(wert) > 0.15:
                textfarbe = 'white'
            else:
                textfarbe = 'black'

            # Vorzeichen anzeigen
            if wert > 0.001:
                text = f'+{wert*100:.0f}%'
            elif wert < -0.001:
                text = f'{wert*100:.0f}%'
            else:
                text = '±0%'

            ax.text(j, i, text, ha='center', va='center',
                   color=textfarbe, fontsize=7, fontweight='bold')

    return im


def erstelle_heatmap() -> plt.Figure:
    """Erstellt 2x2 Subplot-Grid für alle Symbole."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    baseline = erstelle_baseline_matrix() if MODUS == 'differenz' else None

    ims = []
    for idx, (name, config) in enumerate(SYMBOLE.items()):
        ax = axes[idx // 2, idx % 2]
        matrix = erstelle_wahrscheinlichkeits_matrix(config['count'])

        if MODUS == 'differenz':
            im = erstelle_subplot_differenz(
                ax, matrix, baseline, name,
                config['symbol'], config['count']
            )
        else:
            im = erstelle_subplot_absolut(
                ax, matrix, name,
                config['symbol'], config['count']
            )
        ims.append(im)

    # Titel
    joker_text = f", {JOKER} Joker" if JOKER > 0 else ""
    if MODUS == 'differenz':
        titel = f'Abweichung zur Baseline (5/5/5/5, 0 Joker) — Aktuell: {deck_size()} Karten{joker_text}'
    else:
        titel = f'Erfolgswahrscheinlichkeit (Deck: {deck_size()} Karten{joker_text})'

    fig.suptitle(titel, fontsize=13, fontweight='bold', y=0.98)

    fig.subplots_adjust(left=0.06, right=0.88, top=0.92, bottom=0.08,
                        wspace=0.25, hspace=0.3)

    # Colorbar
    cbar_ax = fig.add_axes([0.91, 0.15, 0.02, 0.7])
    cbar = fig.colorbar(ims[0], cax=cbar_ax)

    if MODUS == 'differenz':
        cbar.set_label('Differenz zur Baseline')
        cbar.set_ticks([-0.3, -0.15, 0, 0.15, 0.3])
        cbar.set_ticklabels(['-30%\n(schlechter)', '-15%', '±0%\n(gleich)', '+15%', '+30%\n(besser)'])
    else:
        cbar.set_label('Wahrscheinlichkeit')
        cbar.set_ticks([0, 0.25, 0.5, 0.75, 1.0])
        cbar.set_ticklabels(['0%\n(unmöglich)', '25%', '50%', '75%', '100%'])

    return fig


def drucke_tabellen():
    """Gibt Wahrscheinlichkeitstabellen für alle Symbole aus."""
    print(f"\nDeck-Konfiguration:")
    print(f"  Herz:  {HERZ} Karten")
    print(f"  Karo:  {KARO} Karten")
    print(f"  Pik:   {PIK} Karten")
    print(f"  Kreuz: {KREUZ} Karten")
    print(f"  Joker: {JOKER} (zählen als beliebige Farbe)")
    print(f"  Gesamt: {deck_size()} Karten")
    print(f"\nModus: {MODUS.upper()}")

    if MODUS == 'differenz':
        print(f"Baseline: {BASELINE_SYMBOL} pro Farbe, {BASELINE_JOKER} Joker, {BASELINE_DECK} Karten")

    baseline = erstelle_baseline_matrix() if MODUS == 'differenz' else None

    for name, config in SYMBOLE.items():
        print(f"\n{'='*70}")
        print(f"{config['symbol']} {name} ({config['count']} Karten)")
        print(f"{'='*70}")

        matrix = erstelle_wahrscheinlichkeits_matrix(config['count'])

        header = "     " + "".join(f"{i:7d}" for i in range(1, MAX_DRAW + 1))
        print(header)
        print("-" * len(header))

        for i, row in enumerate(matrix):
            if MODUS == 'differenz' and baseline is not None:
                diff_row = row - baseline[i]
                zeile = f"{i+1}  | " + " ".join(f"{v*100:+5.0f}%" for v in diff_row)
            else:
                zeile = f"{i+1}  | " + " ".join(f"{v*100:5.1f}%" for v in row)
            print(zeile)


def main():
    Path("output").mkdir(exist_ok=True)

    print("Berechne Wahrscheinlichkeiten...")
    drucke_tabellen()

    print(f"\nErstelle Heatmap...")
    fig = erstelle_heatmap()
    fig.savefig(OUTPUT_PATH, dpi=150, bbox_inches='tight')
    print(f"Gespeichert: {OUTPUT_PATH}")
    plt.close(fig)


if __name__ == "__main__":
    main()
