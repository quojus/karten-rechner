# P&P Kartensystem - Vollständige Dokumentation

---

# TEIL 1: SPIELLEITER-REFERENZ

---

## Grundmechanik

### Attribute (4 Symbole)
| Symbol | Attribut | Farbe |
|--------|----------|-------|
| ♠ | Stärke | Schwarz |
| ♦ | Geschick | Rot |
| ♥ | Wissen | Rot |
| ♣ | Charisma | Schwarz |

### Ablauf einer Probe

```
1. Alle Karten zurück ins Deck, mischen
2. Handkarten ziehen (Spieler sieht sie, behält sie verdeckt)
3. Spielleiter: "Ziehe X, brauche Y [Symbol]" (SL wählt Attribut passend zur Situation)
4. Spieler zieht X weitere Karten
5. Auswertung: Handkarten + Gezogene zusammen zählen
6. → Nächste Probe: zurück zu Schritt 1
```

**Wichtig:** Handkarten werden bei JEDER Probe neu gezogen (Schritt 2). Sie sind nicht persistent – nach der Auswertung gehen alle Karten zurück ins Deck.

### Joker-Regeln

- Ein **Joker zählt als beliebiges Symbol** für die aktuelle Probe
- Joker werden wie normale Karten gezogen und gezählt
- Bei der Auswertung entscheidet der Spieler, welches Symbol der Joker darstellt
- Mehrere Joker können für dasselbe Symbol zählen

### Charaktererstellung: Symbolzuweisung

Jeder Charaktertyp definiert eine **feste Kartenverteilung** (z.B. 7/5/5/3). Der Spieler wählt bei der Charaktererstellung, **welches Symbol welche Anzahl bekommt**.

**Beispiel Typ A (7/5/5/3):**
- Spieler 1: "Meine Stärke ist Charisma" → ♣ bekommt die 7
- Spieler 2: "Ich bin ein Kämpfer" → ♠ bekommt die 7
- Spieler 3: "Ich bin geschickt und weise" → ♦ und ♥ bekommen je 5, die 7 geht an ♠

→ Die **Verteilung** (7/5/5/3) ist fest, die **Spezialisierung** wählt der Spieler.

### Ergebnis-Kategorien

| Ergebnis | Symbole | Bedeutung |
|----------|---------|-----------|
| 💀 **Versagen** | 0 | Katastrophe, Komplikation |
| 😓 **Missgeschick** | 1 bis (Benötigt-1) | Teilerfolg mit Haken |
| ✓ **Gemeistert** | Genau Benötigt | Sauberer Erfolg |
| ⭐ **Hervorragend** | Mehr als Benötigt | Kritischer Erfolg, Bonus |

### Statistische Methodik

Alle Wahrscheinlichkeiten in diesem Dokument wurden mit der **multivariaten hypergeometrischen Verteilung** berechnet. Diese modelliert exakt das Ziehen ohne Zurücklegen aus einem Deck mit mehreren Kategorien (Symbole + Joker). Die Werte sind keine Schätzungen, sondern mathematisch exakte Ergebnisse.

---

## Hilfe-System

Spieler können sich gegenseitig bei Proben unterstützen. Der Spielleiter entscheidet, welche Situation vorliegt.

### Variante 1: Stress-Situation

Kampf, Zeitdruck, Gefahr – Hilfe muss VOR dem Ziehen angemeldet werden.

**Ablauf:**
1. Spieler A braucht Hilfe
2. Spieler B bietet an (VOR As Probe)
3. SL legt fest: B darf bis zu **X Karten** beisteuern
4. B zieht X Karten und legt sie auf seinen **Ablagestapel**
5. A zieht **X Karten weniger** als normal
6. A wertet seine Probe aus

### Variante 2: Entspannte Situation

Keine unmittelbare Gefahr – Hilfe auch NACH dem Ziehen möglich.

**Ablauf:**
1. Spieler A macht seine Probe
2. Bei Misserfolg: Spieler B kann einspringen
3. B macht eine eigene Probe, **eine Stufe schwieriger**
4. Ergebnis-Kombination:

| A's Ergebnis | B's Ergebnis | Gesamtergebnis |
|--------------|--------------|----------------|
| Versagen | Hervorragend | Gemeistert |
| Versagen | Gemeistert | Missgeschick (leicht) |
| Versagen | Missgeschick | Versagen (gemildert) |
| Missgeschick | Hervorragend | Gemeistert |
| Missgeschick | Gemeistert | Gemeistert (knapp) |

Der SL bildet ein Mittel und passt das Ergebnis der Situation an.

### Ablagestapel-Regel

- Alle Karten die B für die Hilfe nutzt, kommen auf seinen **Ablagestapel**
- Diese Karten stehen B bei seiner **nächsten Probe nicht** zur Verfügung
- Erst nach der nächsten Probe werden sie wieder eingemischt
- **Ausnahme:** SL kann situativ sagen: "Ihr erholt euch – neu mischen erlaubt"

### Beispiel

> **Entspannte Situation:** Spieler A (Typ F, Charisma 2) versucht einen Händler zu überreden.
>
> - A macht Normal-Probe → Versagen (0 Charisma-Symbole)
> - B springt ein, macht Schwer-Probe (eine Stufe härter) → Hervorragend
> - **Ergebnis:** B rettet die Situation. Der Händler lässt sich überreden.
> - Bs verwendete Karten liegen auf seinem Ablagestapel bis nach seiner nächsten Probe.

---

## Optionale Regel: Farb-Proben

Der Spielleiter kann statt auf ein Symbol auf eine **Farbe** prüfen:
- **Rot:** ♦ + ♥ zählen zusammen
- **Schwarz:** ♠ + ♣ zählen zusammen

### Wichtig: Symbolzuweisung

Die Kartenverteilung (z.B. 7/5/5/3) ist fest, aber der Spieler wählt, **welches Symbol welche Anzahl bekommt**. Dadurch entsteht eine variable Farbverteilung.

**Beispiel Typ A (7/5/5/3):**
| Zuweisung an Rot (♦♥) | Rot | Schwarz |
|------------------------|-----|---------|
| 7 + 5 | **12** | 8 |
| 7 + 3 oder 5 + 5 | 10 | 10 |
| 5 + 3 | 8 | **12** |

### Referenz-Wahrscheinlichkeiten (20 Karten, ohne Joker/Hand)

**10 Farbkarten (Ausgeglichen):**
| Schwierigkeit | Ziehen | Benötigt | Versagen | Erfolg |
|---------------|--------|----------|----------|--------|
| Trivial | 5 | 1 | 2% | **98%** |
| Leicht | 4 | 1 | 4% | **96%** |
| Normal | 4 | 2 | 4% | **71%** |
| Schwer | 3 | 2 | 11% | **50%** |
| Extrem | 3 | 3 | 11% | **11%** |

**Vergleich zu Symbol-Proben (Normal, Typ G):**
- Symbol-Probe (5 Karten): **65%** Erfolg
- Farb-Probe (10 Karten): **71%** Erfolg

→ Farb-Proben sind etwa **6% leichter** als Symbol-Proben.

### Vergleichsmatrix (Normal: Ziehe 4, Brauche 2)

| Typ | Rot (Best) | Rot (Worst) | Schwarz (Best) | Schwarz (Worst) | Spanne |
|-----|------------|-------------|----------------|-----------------|--------|
| A | 98% | 81% | 98% | 81% | 17% |
| B | 91% | 70% | 91% | 70% | 20% |
| C | 99% | 99% | 99% | 99% | 0% |
| D | 82% | 82% | 82% | 82% | 0% |
| E | 88% | 63% | 88% | 63% | 25% |
| F | 98% | 81% | 98% | 81% | 17% |
| G | 96% | 96% | 96% | 96% | 0% |
| H | 98% | 81% | 98% | 81% | 17% |
| I | 91% | 70% | 91% | 70% | 20% |
| **J** | **95%** | **47%** | **95%** | **47%** | **49%** |
| K | 100% | 95% | 100% | 95% | 5% |
| L | 98% | 93% | 98% | 93% | 5% |
| M | 94% | 94% | 94% | 94% | 0% |
| N | 80% | 80% | 80% | 80% | 0% |

### Erkenntnisse

**Typ J hat die größte Spanne:**
- Wenn beide 7er auf eine Farbe gelegt werden: **95%** Erfolg
- Wenn beide 3er auf eine Farbe gelegt werden: **47%** Erfolg
- Farb-Proben verstärken Typ Js Polarisierung!

**Generalisten sind immer ausgeglichen:**
- Typen C, D, G, M, N haben identische Rot/Schwarz-Werte
- Die Symbolzuweisung hat keine Auswirkung auf Farb-Proben

**Wann Farb-Proben nutzen:**
- Für **Teamproben** (mehrere Attribute relevant)
- Als **leichtere Alternative** zu Symbol-Proben
- Um **Typ Js Extreme** auszugleichen (bei 7+3 Zuweisung)

---

## Spielleiter-Schwierigkeitstabelle

**Referenz-Spieler:** Ausgewogener Hybrid (5/5/5/5 + 2 Joker + 2 Hand)

### Kurzübersicht (5 Stufen)

| Schwierigkeit | Ziehen | Benötigt | Erfolg | Versagen | Hervorragend |
|---------------|--------|----------|--------|----------|--------------|
| **Trivial** | 5 | 1 | ~95% | 4% | 75% |
| **Leicht** | 4 | 1 | ~90% | 7% | 65% |
| **Normal** | 4 | 2 | ~65% | 7% | 27% |
| **Schwer** | 3 | 2 | ~50% | 11% | 16% |
| **Extrem** | 3 | 3 | ~15% | 11% | 2% |

### Vollständige Tabelle (alle Kombinationen)

| Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|--------|----------|----------|--------------|------------|--------------|--------|
| 3 | 1 | 11% | - | 36% | 53% | 89% |
| 3 | 2 | 11% | 36% | 36% | 16% | 52% |
| 3 | 3 | 11% | 73% | 14% | 2% | 16% |
| 4 | 1 | 7% | - | 28% | 65% | 93% |
| 4 | 2 | 7% | 28% | 38% | 27% | 65% |
| 4 | 3 | 7% | 66% | 18% | 9% | 27% |
| 5 | 1 | 4% | - | 21% | 75% | 96% |
| 5 | 2 | 4% | 21% | 35% | 40% | 75% |
| 5 | 3 | 4% | 56% | 24% | 16% | 40% |
| 6 | 1 | 2% | - | 16% | 82% | 98% |
| 6 | 2 | 2% | 16% | 31% | 51% | 82% |
| 6 | 3 | 2% | 47% | 28% | 23% | 51% |

---

# TEIL 2: CHARAKTERTYPEN

---

## Übersicht aller Charaktertypen

**Hinweis zur Deck-Spalte:** Die Zahlen (z.B. 7/5/5/3) zeigen die **Kartenverteilung**, nicht feste Symbole. Der Spieler entscheidet bei der Charaktererstellung, welches Attribut (♠♦♥♣) welche Anzahl bekommt.

| ID | Name | Deck | Joker | Hand | Karten | Stil |
|----|------|------|-------|------|--------|------|
| A | Fokussierter Planer | 7/5/5/3 | 0 | 2 | 20 | Polarisiert, plant voraus |
| B | Flexibler Spezialist | 7/5/5/3 | 4 | 0 | 24 | Spezialisiert, improvisiert |
| C | Kontrollierter Generalist | 5/5/5/5 | 0 | 4 | 20 | Überall gut, maximale Kontrolle |
| D | Improvisierender Generalist | 5/5/5/5 | 4 | 0 | 24 | Überall okay, flexibel |
| E | Extremer Spezialist | 8/4/4/4 | 2 | 0 | 22 | Ein Ass, drei Schwächen |
| F | Dreifach-Talent | 6/6/6/2 | 0 | 2 | 20 | Drei Stärken, eine Katastrophe |
| G | Ausgewogener Hybrid | 5/5/5/5 | 2 | 2 | 22 | Referenz-Spieler |
| H | Doppel-Fokus Planer | 6/6/4/4 | 0 | 2 | 20 | Zwei Stärken, plant |
| I | Doppel-Fokus Improv | 6/6/4/4 | 4 | 0 | 24 | Zwei Stärken, improvisiert |
| J | Gegensatz-Spezialist | 7/3/7/3 | 2 | 0 | 22 | Zwei super, zwei schlecht |
| K | Extreme Kontrolle | 7/5/5/3 | 0 | 4 | 20 | Einsteiger-freundlich |
| L | Milder Spezialist | 6/5/5/4 | 2 | 2 | 22 | Leichte Unterschiede |
| M | Minimalist | 4/4/4/4 | 0 | 2 | 16 | Kleines Deck |
| N | Maximalist | 6/6/6/6 | 4 | 0 | 28 | Großes Deck |

---

## Vergleichsmatrizen

Die Matrizen zeigen die **Erfolgswahrscheinlichkeit** jedes Charaktertyps pro Schwierigkeit. "Erfolg" bedeutet: mindestens die benötigte Anzahl Symbole gezogen.

### Die Spalten

| Spalte | Bedeutung |
|--------|-----------|
| **Stärke** | Erfolgswahrscheinlichkeit mit der **höchsten Kartenzahl** (z.B. 7 bei 7/5/5/3) |
| **Neutral** | Erfolgswahrscheinlichkeit mit den **mittleren Kartenzahlen** (falls vorhanden) |
| **Schwäche** | Erfolgswahrscheinlichkeit mit der **niedrigsten Kartenzahl** (z.B. 3 bei 7/5/5/3) |
| **Spanne** | Differenz zwischen Stärke und Schwäche |

**Zur Erinnerung:** Der Spieler wählt, welches Symbol (♠♦♥♣) welche Kartenzahl bekommt.

### Was die Spanne aussagt

- **Spanne = 0%** → Generalist: Überall gleich gut (oder gleich schlecht)
- **Spanne ~15-30%** → Moderate Spezialisierung: Spürbare Unterschiede
- **Spanne ~40-55%** → Extreme Spezialisierung: Riesiger Unterschied zwischen Stärke und Schwäche

---

### Trivial (Ziehe 5, Brauche 1)

| ID | Typ | Stärke | Neutral | Schwäche | Spanne |
|----|-----|--------|---------|----------|--------|
| K | Extreme Kontrolle | **100%** | 98% | 94% | 6% |
| A | Fokussierter Planer | 99% | 95% | 82% | 17% |
| H | Doppel-Fokus Planer | 98% | - | 92% | 6% |
| L | Milder Spezialist | 98% | 96% | 94% | 4% |
| C | Kontrollierter Generalist | 98% | 98% | 98% | 0% |
| J | Gegensatz-Spezialist | 97% | - | 85% | 12% |
| F | Dreifach-Talent | 97% | 97% | 65% | 32% |
| B | Flexibler Spezialist | 96% | - | 88% | 8% |
| E | Extremer Spezialist | 96% | - | 86% | 10% |
| G | Ausgewogener Hybrid | 96% | 96% | 96% | 0% |
| M | Minimalist | 96% | 96% | 96% | 0% |
| I | Doppel-Fokus Improv | 95% | - | 90% | 5% |
| D | Improvisierender Generalist | 92% | 92% | 92% | 0% |
| N | Maximalist | 92% | 92% | 92% | 0% |

**Interpretation:** Bei trivialen Aufgaben gelingt fast alles. Selbst Schwächen fallen kaum ins Gewicht. Nur Typ F zeigt deutliche Unterschiede.

---

### Leicht (Ziehe 4, Brauche 1)

| ID | Typ | Stärke | Neutral | Schwäche | Spanne |
|----|-----|--------|---------|----------|--------|
| K | Extreme Kontrolle | **100%** | 97% | 90% | 10% |
| A | Fokussierter Planer | 98% | 92% | 76% | 22% |
| H | Doppel-Fokus Planer | 97% | - | 88% | 9% |
| L | Milder Spezialist | 97% | 93% | 90% | 7% |
| C | Kontrollierter Generalist | 97% | 97% | 97% | 0% |
| J | Gegensatz-Spezialist | 95% | - | 80% | 15% |
| F | Dreifach-Talent | 95% | 95% | 57% | 38% |
| B | Flexibler Spezialist | 95% | - | 84% | 11% |
| E | Extremer Spezialist | 95% | - | 82% | 13% |
| M | Minimalist | 94% | 94% | 94% | 0% |
| G | Ausgewogener Hybrid | 93% | 93% | 93% | 0% |
| I | Doppel-Fokus Improv | 93% | - | 87% | 6% |
| D | Improvisierender Generalist | 90% | 90% | 90% | 0% |
| N | Maximalist | 89% | 89% | 89% | 0% |

**Interpretation:** Immer noch hohe Erfolgsquoten. Typ F's Schwäche (57%) wird spürbar. Die Unterschiede beginnen sich zu zeigen.

---

### Normal (Ziehe 4, Brauche 2)

| ID | Typ | Stärke | Neutral | Schwäche | Spanne |
|----|-----|--------|---------|----------|--------|
| K | Extreme Kontrolle | **90%** | 77% | 57% | 33% |
| A | Fokussierter Planer | 79% | 60% | 31% | 48% |
| L | Milder Spezialist | 77% | 65% | 58% | 19% |
| C | Kontrollierter Generalist | 77% | 77% | 77% | 0% |
| H | Doppel-Fokus Planer | 75% | - | 53% | 22% |
| J | Gegensatz-Spezialist | 70% | - | 39% | 31% |
| B | Flexibler Spezialist | 69% | - | 47% | 22% |
| E | Extremer Spezialist | 69% | - | 43% | 26% |
| F | Dreifach-Talent | 69% | 69% | **11%** | 58% |
| M | Minimalist | 66% | 66% | 66% | 0% |
| G | Ausgewogener Hybrid | 65% | 65% | 65% | 0% |
| I | Doppel-Fokus Improv | 64% | - | 51% | 13% |
| D | Improvisierender Generalist | 58% | 58% | 58% | 0% |
| N | Maximalist | 56% | 56% | 56% | 0% |

**Interpretation:** Die Standardschwierigkeit. Hier zeigen sich die Charakterunterschiede am deutlichsten. Spezialisten dominieren in ihrer Stärke, scheitern aber oft in ihrer Schwäche.

---

### Schwer (Ziehe 3, Brauche 2)

| ID | Typ | Stärke | Neutral | Schwäche | Spanne |
|----|-----|--------|---------|----------|--------|
| K | Extreme Kontrolle | **87%** | 70% | 40% | 47% |
| A | Fokussierter Planer | 73% | 48% | 20% | 53% |
| L | Milder Spezialist | 69% | 52% | 45% | 24% |
| C | Kontrollierter Generalist | 70% | 70% | 70% | 0% |
| H | Doppel-Fokus Planer | 68% | - | 39% | 29% |
| E | Extremer Spezialist | 64% | - | 30% | 34% |
| B | Flexibler Spezialist | 63% | - | 33% | 30% |
| F | Dreifach-Talent | 62% | 62% | **8%** | 54% |
| J | Gegensatz-Spezialist | 61% | - | 25% | 36% |
| M | Minimalist | 55% | 55% | 55% | 0% |
| I | Doppel-Fokus Improv | 54% | - | 39% | 15% |
| G | Ausgewogener Hybrid | 52% | 52% | 52% | 0% |
| D | Improvisierender Generalist | 49% | 49% | 49% | 0% |
| N | Maximalist | 45% | 45% | 45% | 0% |

**Interpretation:** Schwere Proben trennen die Spreu vom Weizen. Typ K bleibt bei Stärke stark (87%), während Typ F's Schwäche praktisch unschaffbar wird (8%).

---

### Extrem (Ziehe 3, Brauche 3)

| ID | Typ | Stärke | Neutral | Schwäche | Spanne |
|----|-----|--------|---------|----------|--------|
| K | Extreme Kontrolle | **57%** | 30% | 10% | 47% |
| A | Fokussierter Planer | 34% | 13% | 2% | 32% |
| L | Milder Spezialist | 31% | 16% | 12% | 19% |
| C | Kontrollierter Generalist | 30% | 30% | 30% | 0% |
| H | Doppel-Fokus Planer | 29% | - | 9% | 20% |
| B | Flexibler Spezialist | 23% | - | 6% | 17% |
| E | Extremer Spezialist | 23% | - | 5% | 18% |
| F | Dreifach-Talent | 23% | 23% | **0%** | 23% |
| J | Gegensatz-Spezialist | 23% | - | 4% | 19% |
| I | Doppel-Fokus Improv | 17% | - | 8% | 9% |
| M | Minimalist | 17% | 17% | 17% | 0% |
| G | Ausgewogener Hybrid | 16% | 16% | 16% | 0% |
| D | Improvisierender Generalist | 13% | 13% | 13% | 0% |
| N | Maximalist | 11% | 11% | 11% | 0% |

**Interpretation:** Extreme Proben sind für alle schwer. Nur Typ K hat bei Stärke noch eine faire Chance (57%). Typ F's Schwäche ist unmöglich (0%). Selbst Generalisten liegen unter 20%.

---

# TEIL 3: DETAILLIERTE CHARAKTERBÖGEN

**Hinweis zu den Beispiel-Zuweisungen:** In den folgenden Tabellen sind die Symbole (♠♦♥♣) nur **Beispiele**. Der Spieler wählt bei der Charaktererstellung selbst, welches Symbol welche Kartenzahl bekommt. Die Wahrscheinlichkeiten gelten für die jeweilige **Kartenzahl**, unabhängig vom Symbol.

---

## Typ A: Fokussierter Planer

### Deck-Zusammensetzung
| Komponente | Anzahl |
|------------|--------|
| Attribut A | **7** |
| Attribut B | 5 |
| Attribut C | 5 |
| Attribut D | 3 |
| 🃏 Joker | 0 |
| 🎴 Handkarten | 2 |
| **Gesamt** | **20** |

### Einkaufsliste (Rommé-Blatt)
- 7× beliebige ♠ (z.B. Ass bis 7)
- 5× beliebige ♦
- 5× beliebige ♥
- 3× beliebige ♣

### Wahrscheinlichkeiten nach Schwierigkeit

**7 Karten (höchste):**
| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 1% | - | 15% | 84% | 99% |
| Leicht | 4 | 1 | 2% | - | 19% | 79% | 98% |
| Normal | 4 | 2 | 2% | 19% | 39% | 40% | 79% |
| Schwer | 3 | 2 | 4% | 23% | 39% | 34% | 73% |
| Extrem | 3 | 3 | 4% | 62% | 26% | 8% | 34% |

**5 Karten (mittel):**
| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 5% | - | 28% | 67% | 95% |
| Leicht | 4 | 1 | 8% | - | 32% | 60% | 92% |
| Normal | 4 | 2 | 8% | 32% | 37% | 23% | 60% |
| Schwer | 3 | 2 | 13% | 39% | 35% | 13% | 48% |
| Extrem | 3 | 3 | 13% | 74% | 12% | 1% | 13% |

**3 Karten (niedrigste):**
| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 18% | - | 42% | 40% | 82% |
| Leicht | 4 | 1 | 24% | - | 45% | 31% | 76% |
| Normal | 4 | 2 | 24% | 45% | 26% | 5% | 31% |
| Schwer | 3 | 2 | 32% | 48% | 18% | 2% | 20% |
| Extrem | 3 | 3 | 32% | 66% | 2% | 0% | 2% |

### Farb-Proben (Optionale Regel)

**Mögliche Farbverteilungen:**
| Zuweisung (♦♥) | Rot | Schwarz |
|----------------|-----|---------|
| 7 + 5 | **12** | 8 |
| 7 + 3 oder 5 + 5 | 10 | 10 |
| 5 + 3 | 8 | **12** |

**Rot=12, Schwarz=8 (Stärke auf Rot):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 100% |
| Leicht | 4 | 1 | 99% |
| Normal | 4 | 2 | 85% |
| Schwer | 3 | 2 | 66% |
| Extrem | 3 | 3 | 19% |

**Rot=10, Schwarz=10 (Ausgeglichen):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 98% |
| Leicht | 4 | 1 | 96% |
| Normal | 4 | 2 | 71% |
| Schwer | 3 | 2 | 50% |
| Extrem | 3 | 3 | 11% |

**Rot=8, Schwarz=12 (Stärke auf Schwarz):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 95% |
| Leicht | 4 | 1 | 90% |
| Normal | 4 | 2 | 53% |
| Schwer | 3 | 2 | 34% |
| Extrem | 3 | 3 | 5% |

---

## Typ B: Flexibler Spezialist

### Deck-Zusammensetzung
| Komponente | Anzahl |
|------------|--------|
| Attribut A | **7** |
| Attribut B | 5 |
| Attribut C | 5 |
| Attribut D | 3 |
| 🃏 Joker | **4** |
| 🎴 Handkarten | 0 |
| **Gesamt** | **24** |

### Einkaufsliste
- 7× ♠, 5× ♦, 5× ♥, 3× ♣
- 4× Joker (aus 2 Rommé-Blättern)

### Wahrscheinlichkeiten nach Schwierigkeit

**7 Karten + 4 Joker (höchste):**
| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 4% | - | 23% | 73% | 96% |
| Leicht | 4 | 1 | 5% | - | 26% | 69% | 95% |
| Normal | 4 | 2 | 5% | 26% | 40% | 29% | 69% |
| Schwer | 3 | 2 | 7% | 30% | 40% | 23% | 63% |
| Extrem | 3 | 3 | 7% | 70% | 18% | 5% | 23% |

**3 Karten + 4 Joker (niedrigste):**
| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 12% | - | 34% | 54% | 88% |
| Leicht | 4 | 1 | 16% | - | 37% | 47% | 84% |
| Normal | 4 | 2 | 16% | 37% | 33% | 14% | 47% |
| Schwer | 3 | 2 | 22% | 45% | 27% | 6% | 33% |
| Extrem | 3 | 3 | 22% | 72% | 5% | 1% | 6% |

### Farb-Proben (Optionale Regel)

**Mögliche Farbverteilungen:** Wie Typ A (7/5/5/3)

**Rot=12+4J, Schwarz=8 (Stärke auf Rot):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 100% |
| Leicht | 4 | 1 | 99% |
| Normal | 4 | 2 | 91% |
| Schwer | 3 | 2 | 75% |
| Extrem | 3 | 3 | 28% |

**Rot=10+4J, Schwarz=10 (Ausgeglichen):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 99% |
| Leicht | 4 | 1 | 98% |
| Normal | 4 | 2 | 82% |
| Schwer | 3 | 2 | 63% |
| Extrem | 3 | 3 | 18% |

**Rot=8+4J, Schwarz=12 (Stärke auf Schwarz):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 98% |
| Leicht | 4 | 1 | 95% |
| Normal | 4 | 2 | 70% |
| Schwer | 3 | 2 | 50% |
| Extrem | 3 | 3 | 11% |

---

## Typ C: Kontrollierter Generalist

### Deck-Zusammensetzung
| Komponente | Anzahl |
|------------|--------|
| Attribut A | 5 |
| Attribut B | 5 |
| Attribut C | 5 |
| Attribut D | 5 |
| 🃏 Joker | 0 |
| 🎴 Handkarten | **4** |
| **Gesamt** | **20** |

### Einkaufsliste
- Je 5× von jedem Symbol (♠♦♥♣)

### Wahrscheinlichkeiten (alle Attribute gleich)

| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 2% | - | 17% | 81% | 98% |
| Leicht | 4 | 1 | 3% | - | 20% | 77% | 97% |
| Normal | 4 | 2 | 3% | 20% | 38% | 39% | 77% |
| Schwer | 3 | 2 | 5% | 26% | 40% | 30% | 70% |
| Extrem | 3 | 3 | 5% | 65% | 22% | 8% | 30% |

### Farb-Proben (Optionale Regel)

→ Immer ausgeglichen: Rot=10, Schwarz=10 (keine Wahl nötig)

**Rot=10, Schwarz=10:**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 98% |
| Leicht | 4 | 1 | 96% |
| Normal | 4 | 2 | 71% |
| Schwer | 3 | 2 | 50% |
| Extrem | 3 | 3 | 11% |

---

## Typ D: Improvisierender Generalist

### Deck-Zusammensetzung
| Komponente | Anzahl |
|------------|--------|
| Attribut A | 5 |
| Attribut B | 5 |
| Attribut C | 5 |
| Attribut D | 5 |
| 🃏 Joker | **4** |
| 🎴 Handkarten | 0 |
| **Gesamt** | **24** |

### Einkaufsliste
- Je 5× von jedem Symbol
- 4× Joker

### Wahrscheinlichkeiten (alle Attribute gleich)

| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 8% | - | 29% | 63% | 92% |
| Leicht | 4 | 1 | 10% | - | 32% | 58% | 90% |
| Normal | 4 | 2 | 10% | 32% | 36% | 22% | 58% |
| Schwer | 3 | 2 | 13% | 39% | 36% | 13% | 49% |
| Extrem | 3 | 3 | 13% | 74% | 11% | 2% | 13% |

### Farb-Proben (Optionale Regel)

→ Immer ausgeglichen: Rot=10, Schwarz=10 (keine Wahl nötig)

**Rot=10+4J, Schwarz=10:**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 99% |
| Leicht | 4 | 1 | 98% |
| Normal | 4 | 2 | 82% |
| Schwer | 3 | 2 | 63% |
| Extrem | 3 | 3 | 18% |

---

## Typ E: Extremer Spezialist

### Deck-Zusammensetzung
| Komponente | Anzahl |
|------------|--------|
| Attribut A | **8** |
| Attribut B | 4 |
| Attribut C | 4 |
| Attribut D | 4 |
| 🃏 Joker | 2 |
| 🎴 Handkarten | 0 |
| **Gesamt** | **22** |

### Einkaufsliste
- 8× ♠ (Ass bis 8)
- Je 4× von ♦♥♣
- 2× Joker

### Wahrscheinlichkeiten

**8 Karten (höchste):**
| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 4% | - | 22% | 74% | 96% |
| Leicht | 4 | 1 | 5% | - | 26% | 69% | 95% |
| Normal | 4 | 2 | 5% | 26% | 41% | 28% | 69% |
| Schwer | 3 | 2 | 7% | 30% | 41% | 23% | 64% |
| Extrem | 3 | 3 | 7% | 70% | 18% | 5% | 23% |

**4 Karten (niedrigste):**
| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 14% | - | 35% | 51% | 86% |
| Leicht | 4 | 1 | 18% | - | 39% | 43% | 82% |
| Normal | 4 | 2 | 18% | 39% | 32% | 11% | 43% |
| Schwer | 3 | 2 | 25% | 46% | 25% | 5% | 30% |
| Extrem | 3 | 3 | 25% | 70% | 4% | 1% | 5% |

### Farb-Proben (Optionale Regel)

**Mögliche Farbverteilungen:**
| Zuweisung (♦♥) | Rot | Schwarz |
|----------------|-----|---------|
| 8 + 4 | **12** | 8 |
| 4 + 4 | 8 | **12** |

**Rot=12+2J, Schwarz=8 (Stärke auf Rot):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 100% |
| Leicht | 4 | 1 | 99% |
| Normal | 4 | 2 | 88% |
| Schwer | 3 | 2 | 71% |
| Extrem | 3 | 3 | 24% |

**Rot=8+2J, Schwarz=12 (Stärke auf Schwarz):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 97% |
| Leicht | 4 | 1 | 93% |
| Normal | 4 | 2 | 63% |
| Schwer | 3 | 2 | 43% |
| Extrem | 3 | 3 | 8% |

---

## Typ F: Dreifach-Talent

### Deck-Zusammensetzung
| Komponente | Anzahl |
|------------|--------|
| Attribut A | **6** |
| Attribut B | **6** |
| Attribut C | **6** |
| Attribut D | 2 |
| 🃏 Joker | 0 |
| 🎴 Handkarten | 2 |
| **Gesamt** | **20** |

### Einkaufsliste
- Je 6× von ♠♦♥
- 2× ♣

### Wahrscheinlichkeiten

**6 Karten (höchste, 3x vorhanden):**
| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 3% | - | 22% | 75% | 97% |
| Leicht | 4 | 1 | 5% | - | 26% | 69% | 95% |
| Normal | 4 | 2 | 5% | 26% | 39% | 30% | 69% |
| Schwer | 3 | 2 | 8% | 31% | 39% | 23% | 62% |
| Extrem | 3 | 3 | 8% | 69% | 18% | 5% | 23% |

**2 Karten (niedrigste):**
| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 35% | - | 47% | 18% | 65% |
| Leicht | 4 | 1 | 43% | - | 46% | 11% | 57% |
| Normal | 4 | 2 | 43% | 46% | 10% | 1% | 11% |
| Schwer | 3 | 2 | 48% | 44% | 8% | 0% | 8% |
| Extrem | 3 | 3 | 48% | 52% | 0% | 0% | 0% |

### Farb-Proben (Optionale Regel)

**Mögliche Farbverteilungen:**
| Zuweisung (♦♥) | Rot | Schwarz |
|----------------|-----|---------|
| 6 + 6 | **12** | 8 |
| 6 + 2 | 8 | **12** |

**Rot=12, Schwarz=8 (beide 6er auf Rot):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 100% |
| Leicht | 4 | 1 | 99% |
| Normal | 4 | 2 | 85% |
| Schwer | 3 | 2 | 66% |
| Extrem | 3 | 3 | 19% |

**Rot=8, Schwarz=12 (eine 6er auf jede Farbe):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 95% |
| Leicht | 4 | 1 | 90% |
| Normal | 4 | 2 | 53% |
| Schwer | 3 | 2 | 34% |
| Extrem | 3 | 3 | 5% |

---

## Typ G: Ausgewogener Hybrid (Referenz)

### Deck-Zusammensetzung
| Komponente | Anzahl |
|------------|--------|
| Attribut A | 5 |
| Attribut B | 5 |
| Attribut C | 5 |
| Attribut D | 5 |
| 🃏 Joker | 2 |
| 🎴 Handkarten | 2 |
| **Gesamt** | **22** |

### Einkaufsliste
- Je 5× von jedem Symbol
- 2× Joker

### Wahrscheinlichkeiten (alle Attribute gleich)

| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 4% | - | 21% | 75% | 96% |
| Leicht | 4 | 1 | 7% | - | 28% | 65% | 93% |
| Normal | 4 | 2 | 7% | 28% | 38% | 27% | 65% |
| Schwer | 3 | 2 | 11% | 36% | 36% | 16% | 52% |
| Extrem | 3 | 3 | 11% | 73% | 14% | 2% | 16% |

### Farb-Proben (Optionale Regel)

→ Immer ausgeglichen: Rot=10, Schwarz=10 (keine Wahl nötig)

**Rot=10+2J, Schwarz=10:**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 99% |
| Leicht | 4 | 1 | 97% |
| Normal | 4 | 2 | 77% |
| Schwer | 3 | 2 | 57% |
| Extrem | 3 | 3 | 14% |

---

## Typ K: Extreme Kontrolle

**Hinweis:** Dieser Typ eignet sich gut für Einsteiger. Die hohen Erfolgschancen (auch bei Schwächen) ermöglichen ein frustfreies Spielerlebnis.

### Deck-Zusammensetzung
| Komponente | Anzahl |
|------------|--------|
| Attribut A | **7** |
| Attribut B | 5 |
| Attribut C | 5 |
| Attribut D | 3 |
| 🃏 Joker | 0 |
| 🎴 Handkarten | **4** |
| **Gesamt** | **20** |

### Einkaufsliste
- 7× ♠, 5× ♦, 5× ♥, 3× ♣

### Wahrscheinlichkeiten

**7 Karten + 4 Hand (höchste):**
| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 0% | - | 8% | 92% | 100% |
| Leicht | 4 | 1 | 0% | - | 10% | 90% | 100% |
| Normal | 4 | 2 | 0% | 10% | 30% | 60% | 90% |
| Schwer | 3 | 2 | 1% | 12% | 32% | 55% | 87% |
| Extrem | 3 | 3 | 1% | 42% | 32% | 25% | 57% |

**3 Karten + 4 Hand (niedrigste):**
| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 6% | - | 28% | 66% | 94% |
| Leicht | 4 | 1 | 10% | - | 33% | 57% | 90% |
| Normal | 4 | 2 | 10% | 33% | 36% | 21% | 57% |
| Schwer | 3 | 2 | 18% | 42% | 30% | 10% | 40% |
| Extrem | 3 | 3 | 18% | 72% | 9% | 1% | 10% |

### Farb-Proben (Optionale Regel)

**Mögliche Farbverteilungen:** Wie Typ A (7/5/5/3)

**Rot=12, Schwarz=8 (Stärke auf Rot):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 100% |
| Leicht | 4 | 1 | 99% |
| Normal | 4 | 2 | 85% |
| Schwer | 3 | 2 | 66% |
| Extrem | 3 | 3 | 19% |

**Rot=10, Schwarz=10 (Ausgeglichen):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 98% |
| Leicht | 4 | 1 | 96% |
| Normal | 4 | 2 | 71% |
| Schwer | 3 | 2 | 50% |
| Extrem | 3 | 3 | 11% |

**Rot=8, Schwarz=12 (Stärke auf Schwarz):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 95% |
| Leicht | 4 | 1 | 90% |
| Normal | 4 | 2 | 53% |
| Schwer | 3 | 2 | 34% |
| Extrem | 3 | 3 | 5% |

---

## Typ H: Doppel-Fokus Planer

### Deck-Zusammensetzung
| Komponente | Anzahl |
|------------|--------|
| Attribut A | **6** |
| Attribut B | **6** |
| Attribut C | 4 |
| Attribut D | 4 |
| 🃏 Joker | 0 |
| 🎴 Handkarten | 2 |
| **Gesamt** | **20** |

### Einkaufsliste
- Je 6× von ♠♦
- Je 4× von ♥♣

### Wahrscheinlichkeiten

**6 Karten + 2 Hand (höchste, 2x vorhanden):**
| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 2% | - | 18% | 80% | 98% |
| Leicht | 4 | 1 | 3% | - | 22% | 75% | 97% |
| Normal | 4 | 2 | 3% | 22% | 38% | 37% | 75% |
| Schwer | 3 | 2 | 5% | 27% | 40% | 28% | 68% |
| Extrem | 3 | 3 | 5% | 66% | 22% | 7% | 29% |

**4 Karten + 2 Hand (niedrigste, 2x vorhanden):**
| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 8% | - | 30% | 62% | 92% |
| Leicht | 4 | 1 | 12% | - | 35% | 53% | 88% |
| Normal | 4 | 2 | 12% | 35% | 35% | 18% | 53% |
| Schwer | 3 | 2 | 18% | 43% | 30% | 9% | 39% |
| Extrem | 3 | 3 | 18% | 73% | 8% | 1% | 9% |

### Farb-Proben (Optionale Regel)

**Mögliche Farbverteilungen:**
| Zuweisung (♦♥) | Rot | Schwarz |
|----------------|-----|---------|
| 6 + 6 | **12** | 8 |
| 6 + 4 | 10 | 10 |
| 4 + 4 | 8 | **12** |

**Rot=12, Schwarz=8 (beide 6er auf Rot):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 100% |
| Leicht | 4 | 1 | 99% |
| Normal | 4 | 2 | 85% |
| Schwer | 3 | 2 | 66% |
| Extrem | 3 | 3 | 19% |

**Rot=10, Schwarz=10 (Ausgeglichen):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 98% |
| Leicht | 4 | 1 | 96% |
| Normal | 4 | 2 | 71% |
| Schwer | 3 | 2 | 50% |
| Extrem | 3 | 3 | 11% |

**Rot=8, Schwarz=12 (beide 4er auf Rot):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 95% |
| Leicht | 4 | 1 | 90% |
| Normal | 4 | 2 | 53% |
| Schwer | 3 | 2 | 34% |
| Extrem | 3 | 3 | 5% |

---

## Typ I: Doppel-Fokus Improv

### Deck-Zusammensetzung
| Komponente | Anzahl |
|------------|--------|
| Attribut A | **6** |
| Attribut B | **6** |
| Attribut C | 4 |
| Attribut D | 4 |
| 🃏 Joker | **4** |
| 🎴 Handkarten | 0 |
| **Gesamt** | **24** |

### Einkaufsliste
- Je 6× von ♠♦
- Je 4× von ♥♣
- 4× Joker (aus 2 Rommé-Blättern)

### Wahrscheinlichkeiten

**6 Karten + 4 Joker (höchste, 2x vorhanden):**
| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 5% | - | 25% | 70% | 95% |
| Leicht | 4 | 1 | 7% | - | 29% | 64% | 93% |
| Normal | 4 | 2 | 7% | 29% | 38% | 26% | 64% |
| Schwer | 3 | 2 | 10% | 36% | 37% | 17% | 54% |
| Extrem | 3 | 3 | 10% | 73% | 14% | 3% | 17% |

**4 Karten + 4 Joker (niedrigste, 2x vorhanden):**
| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 10% | - | 32% | 58% | 90% |
| Leicht | 4 | 1 | 13% | - | 36% | 51% | 87% |
| Normal | 4 | 2 | 13% | 36% | 35% | 16% | 51% |
| Schwer | 3 | 2 | 18% | 43% | 31% | 8% | 39% |
| Extrem | 3 | 3 | 18% | 74% | 7% | 1% | 8% |

### Farb-Proben (Optionale Regel)

**Mögliche Farbverteilungen:** Wie Typ H (6/6/4/4)

**Rot=12+4J, Schwarz=8 (beide 6er auf Rot):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 100% |
| Leicht | 4 | 1 | 99% |
| Normal | 4 | 2 | 91% |
| Schwer | 3 | 2 | 75% |
| Extrem | 3 | 3 | 28% |

**Rot=10+4J, Schwarz=10 (Ausgeglichen):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 99% |
| Leicht | 4 | 1 | 98% |
| Normal | 4 | 2 | 82% |
| Schwer | 3 | 2 | 63% |
| Extrem | 3 | 3 | 18% |

**Rot=8+4J, Schwarz=12 (beide 4er auf Rot):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 98% |
| Leicht | 4 | 1 | 95% |
| Normal | 4 | 2 | 70% |
| Schwer | 3 | 2 | 50% |
| Extrem | 3 | 3 | 11% |

---

## Typ J: Gegensatz-Spezialist

### Deck-Zusammensetzung
| Komponente | Anzahl |
|------------|--------|
| Attribut A | **7** |
| Attribut B | 3 |
| Attribut C | **7** |
| Attribut D | 3 |
| 🃏 Joker | 2 |
| 🎴 Handkarten | 0 |
| **Gesamt** | **22** |

### Einkaufsliste
- Je 7× von ♠♥
- Je 3× von ♦♣
- 2× Joker

### Wahrscheinlichkeiten

**7 Karten + 2 Joker (höchste, 2x vorhanden):**
| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 3% | - | 20% | 77% | 97% |
| Leicht | 4 | 1 | 5% | - | 25% | 70% | 95% |
| Normal | 4 | 2 | 5% | 25% | 40% | 30% | 70% |
| Schwer | 3 | 2 | 8% | 31% | 39% | 22% | 61% |
| Extrem | 3 | 3 | 8% | 69% | 18% | 5% | 23% |

**3 Karten + 2 Joker (niedrigste, 2x vorhanden):**
| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 15% | - | 37% | 48% | 85% |
| Leicht | 4 | 1 | 20% | - | 41% | 39% | 80% |
| Normal | 4 | 2 | 20% | 41% | 30% | 9% | 39% |
| Schwer | 3 | 2 | 27% | 48% | 21% | 4% | 25% |
| Extrem | 3 | 3 | 27% | 69% | 4% | 0% | 4% |

### Farb-Proben (Optionale Regel)

**Mögliche Farbverteilungen:**
| Zuweisung (♦♥) | Rot | Schwarz |
|----------------|-----|---------|
| 7 + 7 | **14** | 6 |
| 7 + 3 | 10 | 10 |
| 3 + 3 | 6 | **14** |

**Rot=14+2J, Schwarz=6 (beide 7er auf Rot):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 100% |
| Leicht | 4 | 1 | 100% |
| Normal | 4 | 2 | 95% |
| Schwer | 3 | 2 | 83% |
| Extrem | 3 | 3 | 36% |

**Rot=10+2J, Schwarz=10 (Ausgeglichen):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 99% |
| Leicht | 4 | 1 | 97% |
| Normal | 4 | 2 | 77% |
| Schwer | 3 | 2 | 57% |
| Extrem | 3 | 3 | 14% |

**Rot=6+2J, Schwarz=14 (beide 3er auf Rot):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 92% |
| Leicht | 4 | 1 | 86% |
| Normal | 4 | 2 | 47% |
| Schwer | 3 | 2 | 29% |
| Extrem | 3 | 3 | 4% |

→ **Größte Spanne aller Typen!** Durch Farbzuweisung zwischen 47% und 95% bei Normal.

---

## Typ L: Milder Spezialist

### Deck-Zusammensetzung
| Komponente | Anzahl |
|------------|--------|
| Attribut A | **6** |
| Attribut B | 5 |
| Attribut C | 5 |
| Attribut D | 4 |
| 🃏 Joker | 2 |
| 🎴 Handkarten | 2 |
| **Gesamt** | **22** |

### Einkaufsliste
- 6× ♠
- Je 5× von ♦♥
- 4× ♣
- 2× Joker

### Wahrscheinlichkeiten

**6 Karten + 2 Joker + 2 Hand (höchste):**
| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 2% | - | 16% | 82% | 98% |
| Leicht | 4 | 1 | 3% | - | 20% | 77% | 97% |
| Normal | 4 | 2 | 3% | 20% | 37% | 40% | 77% |
| Schwer | 3 | 2 | 5% | 26% | 39% | 30% | 69% |
| Extrem | 3 | 3 | 5% | 64% | 22% | 9% | 31% |

**5 Karten + 2 Joker + 2 Hand (mittel, 2x vorhanden):**
| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 4% | - | 21% | 75% | 96% |
| Leicht | 4 | 1 | 7% | - | 28% | 65% | 93% |
| Normal | 4 | 2 | 7% | 28% | 38% | 27% | 65% |
| Schwer | 3 | 2 | 11% | 36% | 36% | 16% | 52% |
| Extrem | 3 | 3 | 11% | 73% | 14% | 2% | 16% |

**4 Karten + 2 Joker + 2 Hand (niedrigste):**
| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 6% | - | 26% | 68% | 94% |
| Leicht | 4 | 1 | 10% | - | 32% | 58% | 90% |
| Normal | 4 | 2 | 10% | 32% | 37% | 21% | 58% |
| Schwer | 3 | 2 | 15% | 40% | 33% | 12% | 45% |
| Extrem | 3 | 3 | 15% | 73% | 10% | 2% | 12% |

### Farb-Proben (Optionale Regel)

**Mögliche Farbverteilungen:**
| Zuweisung (♦♥) | Rot | Schwarz |
|----------------|-----|---------|
| 6 + 5 | **11** | 9 |
| 6 + 4 oder 5 + 5 | 10 | 10 |
| 5 + 4 | 9 | **11** |

**Rot=11+2J, Schwarz=9 (Leichte Stärke auf Rot):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 100% |
| Leicht | 4 | 1 | 98% |
| Normal | 4 | 2 | 83% |
| Schwer | 3 | 2 | 64% |
| Extrem | 3 | 3 | 19% |

**Rot=10+2J, Schwarz=10 (Ausgeglichen):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 99% |
| Leicht | 4 | 1 | 97% |
| Normal | 4 | 2 | 77% |
| Schwer | 3 | 2 | 57% |
| Extrem | 3 | 3 | 14% |

**Rot=9+2J, Schwarz=11 (Leichte Stärke auf Schwarz):**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 98% |
| Leicht | 4 | 1 | 95% |
| Normal | 4 | 2 | 71% |
| Schwer | 3 | 2 | 50% |
| Extrem | 3 | 3 | 11% |

---

## Typ M: Minimalist

### Deck-Zusammensetzung
| Komponente | Anzahl |
|------------|--------|
| Attribut A | 4 |
| Attribut B | 4 |
| Attribut C | 4 |
| Attribut D | 4 |
| 🃏 Joker | 0 |
| 🎴 Handkarten | 2 |
| **Gesamt** | **16** |

### Einkaufsliste
- Je 4× von jedem Symbol
- Keine Joker

### Wahrscheinlichkeiten (alle Attribute gleich)

| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 4% | - | 23% | 73% | 96% |
| Leicht | 4 | 1 | 6% | - | 28% | 66% | 94% |
| Normal | 4 | 2 | 6% | 28% | 38% | 28% | 66% |
| Schwer | 3 | 2 | 10% | 35% | 38% | 17% | 55% |
| Extrem | 3 | 3 | 10% | 73% | 14% | 3% | 17% |

**Besonderheit:** Kleinstes Deck (16 Karten). Höhere Trefferquote pro Symbol, aber weniger Varianz durch fehlende Joker.

### Farb-Proben (Optionale Regel)

→ Immer ausgeglichen: Rot=8, Schwarz=8 (keine Wahl nötig)

**Rot=8, Schwarz=8:**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 99% |
| Leicht | 4 | 1 | 96% |
| Normal | 4 | 2 | 72% |
| Schwer | 3 | 2 | 50% |
| Extrem | 3 | 3 | 10% |

---

## Typ N: Maximalist

### Deck-Zusammensetzung
| Komponente | Anzahl |
|------------|--------|
| Attribut A | 6 |
| Attribut B | 6 |
| Attribut C | 6 |
| Attribut D | 6 |
| 🃏 Joker | **4** |
| 🎴 Handkarten | 0 |
| **Gesamt** | **28** |

### Einkaufsliste
- Je 6× von jedem Symbol
- 4× Joker (aus 2 Rommé-Blättern)

### Wahrscheinlichkeiten (alle Attribute gleich)

| Schwierigkeit | Ziehen | Benötigt | Versagen | Missgeschick | Gemeistert | Hervorragend | Erfolg |
|---------------|--------|----------|----------|--------------|------------|--------------|--------|
| Trivial | 5 | 1 | 8% | - | 29% | 63% | 92% |
| Leicht | 4 | 1 | 11% | - | 33% | 56% | 89% |
| Normal | 4 | 2 | 11% | 33% | 35% | 21% | 56% |
| Schwer | 3 | 2 | 15% | 40% | 34% | 11% | 45% |
| Extrem | 3 | 3 | 15% | 74% | 10% | 1% | 11% |

**Besonderheit:** Größtes Deck (28 Karten). Mehr Joker-Flexibilität, aber jedes einzelne Symbol hat geringere Trefferchance. Generalist mit hoher Varianz.

### Farb-Proben (Optionale Regel)

→ Immer ausgeglichen: Rot=12, Schwarz=12 (keine Wahl nötig)

**Rot=12+4J, Schwarz=12:**
| Schwierigkeit | Ziehen | Benötigt | Erfolg |
|---------------|--------|----------|--------|
| Trivial | 5 | 1 | 99% |
| Leicht | 4 | 1 | 98% |
| Normal | 4 | 2 | 80% |
| Schwer | 3 | 2 | 61% |
| Extrem | 3 | 3 | 17% |

---

# TEIL 4: EINKAUFSLISTEN

---

## Karten-Übersicht pro Charaktertyp

| Typ | ♠ | ♦ | ♥ | ♣ | 🃏 | Gesamt | Benötigt |
|-----|---|---|---|---|-----|--------|----------|
| A | 7 | 5 | 5 | 3 | 0 | 20 | 1 Rommé-Blatt |
| B | 7 | 5 | 5 | 3 | 4 | 24 | 2 Rommé-Blätter |
| C | 5 | 5 | 5 | 5 | 0 | 20 | 1 Rommé-Blatt |
| D | 5 | 5 | 5 | 5 | 4 | 24 | 2 Rommé-Blätter |
| E | 8 | 4 | 4 | 4 | 2 | 22 | 1 Rommé-Blatt |
| F | 6 | 6 | 6 | 2 | 0 | 20 | 1 Rommé-Blatt |
| G | 5 | 5 | 5 | 5 | 2 | 22 | 1 Rommé-Blatt |
| H | 6 | 6 | 4 | 4 | 0 | 20 | 1 Rommé-Blatt |
| I | 6 | 6 | 4 | 4 | 4 | 24 | 2 Rommé-Blätter |
| J | 7 | 3 | 7 | 3 | 2 | 22 | 1 Rommé-Blatt |
| K | 7 | 5 | 5 | 3 | 0 | 20 | 1 Rommé-Blatt |
| L | 6 | 5 | 5 | 4 | 2 | 22 | 1 Rommé-Blatt |
| M | 4 | 4 | 4 | 4 | 0 | 16 | 1 Rommé-Blatt |
| N | 6 | 6 | 6 | 6 | 4 | 28 | 2 Rommé-Blätter |

---

## Welche Karten konkret?

**Ein Rommé-Blatt enthält:**
- 2× 13 Karten pro Symbol (Ass bis König)
- 2-3 Joker

**Empfehlung:** Nummerierte Karten (2-10) nutzen, Bildkarten weglassen (übersichtlicher).

| Anzahl benötigt | Karten verwenden |
|-----------------|------------------|
| 2 | 2, 3 |
| 3 | 2, 3, 4 |
| 4 | 2, 3, 4, 5 |
| 5 | 2, 3, 4, 5, 6 |
| 6 | 2, 3, 4, 5, 6, 7 |
| 7 | 2, 3, 4, 5, 6, 7, 8 |
| 8 | 2, 3, 4, 5, 6, 7, 8, 9 |

---

# TEIL 5: ZUSAMMENFASSUNG

---

## Quick-Reference für Spielleiter

### Schwierigkeit ansagen:
| Stufe | Sage | Bedeutung |
|-------|------|-----------|
| Trivial | "Ziehe 5, brauche 1" | Fast automatisch |
| Leicht | "Ziehe 4, brauche 1" | Sollte klappen |
| Normal | "Ziehe 4, brauche 2" | Faire Chance |
| Schwer | "Ziehe 3, brauche 2" | Riskant |
| Extrem | "Ziehe 3, brauche 3" | Unwahrscheinlich |

### Charakter-Auswahl Empfehlung:

| Spielstil | Empfohlene Typen |
|-----------|------------------|
| "Ich plane gern" | A, C, K |
| "Ich improvisiere" | B, D, I |
| "Ich will überall gut sein" | C, G, L |
| "Ich will ein Spezialist sein" | A, E, K |
| "Ich mag Extreme" | E, F, J |
