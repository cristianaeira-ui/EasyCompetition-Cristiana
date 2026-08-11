# Easy Competition

Ein kleines Python-Programm, das Wettkämpfe (z. B. Darts, Luftgewehr,
Bogenschiessen) auswertet. Es liest die Teilnehmenden aus einer CSV-Datei,
erfasst die Punkte pro Durchgang, rechnet altersabhängige Bonuspunkte dazu und
gibt am Schluss die Ranglisten aus. Die Resultate werden zusätzlich als
CSV-Datei und in einer SQLite-Datenbank gespeichert.

Das Programm entstand als Studienarbeit im CAS IT Principles (Berner
Fachhochschule), Modul «Programmierung mit Python».

## Was das Programm macht

1. Liest die Teilnehmerliste aus `teilnehmer.csv` ein.
2. Teilt die Teilnehmenden nach Jahrgang in drei Kategorien ein:
   - **U18** – Wettkampfalter 17 oder jünger
   - **Elite** – 18 bis 49 Jahre
   - **Ue50** – 50 Jahre oder älter
3. Erfasst die Punkte für drei Durchgänge und zeigt nach jedem Durchgang den
   Zwischenstand.
4. Rechnet zum Ausgleich der Alters-Nachteile einen Bonus-Faktor dazu:
   - **U18:** Punkte × (1 + (17 − Alter) / 10)
   - **Ue50:** Punkte × (1 + (Alter − 50) / 50)
   - **Elite:** Faktor 1.0 (kein Bonus)
5. Gibt am Schluss die Rangliste jeder Kategorie aus.
6. Speichert die Schlussrangliste als `schlussrangliste.csv` (für Excel) und
   alle Daten in der Datenbank `wettkampf.db`.

Wichtig: Gespeichert werden immer nur die **Rohpunkte**. Der Bonus-Faktor wird
erst bei der Auswertung dazugerechnet.

## Aufbau

Das Programm besteht aus fünf Python-Dateien und einer Eingabedatei:

| Datei | Aufgabe |
|---|---|
| `Person.py` | Basisklasse: Vorname, Nachname, Geburtsjahr, Alter |
| `Teilnehmer.py` | erbt von `Person`; Startnummer, Punkte, Kategorie, Faktor |
| `Wettkampf.py` | hält die Liste der Teilnehmenden und erstellt die Rangliste |
| `Datenbank.py` | SQLite: Tabellen erzeugen, speichern, lesen |
| `Main.py` | Hauptprogramm: Ablauf, CSV lesen, Ausgabe |
| `teilnehmer.csv` | Eingabedatei mit den Teilnehmenden |

Die Zuständigkeiten sind getrennt: Das **Rechnen** steckt in den Klassen, das
**Anzeigen und der Ablauf** in `Main.py`, und **SQL** ausschliesslich in
`Datenbank.py`.

### Vererbung

`Teilnehmer` erbt von `Person`. Ein Teilnehmer hat dadurch automatisch alles,
was eine Person hat (Name, Geburtsjahr, Alter) und zusätzlich Startnummer und
Punkte.

```
        Person                    Wettkampf
     (Basisklasse)          hat eine Liste von
           ^                      Teilnehmern
           |  erbt von                 |
           |                           v
       Teilnehmer  <--------------------
```

## Starten

Es muss nichts installiert werden. `sqlite3` ist in Python bereits eingebaut.

```bash
python Main.py
```

Das Programm fragt für jeden Teilnehmer und jeden Durchgang die Punkte ab. Gibt
man statt einer Zahl einen Buchstaben ein, fragt das Programm einfach nochmals –
es stürzt nicht ab.

## Erzeugte Dateien

Beim Ausführen entstehen zwei Dateien, die **nicht** im Repository gespeichert
werden (sie stehen in `.gitignore`):

- `schlussrangliste.csv` – die Schlussrangliste, kann mit Excel geöffnet werden
- `wettkampf.db` – die SQLite-Datenbank mit allen Teilnehmenden und Punkten

## Eingabedatei

`teilnehmer.csv` hat eine Überschriftszeile und danach eine Zeile pro Person.
Die Werte sind mit Semikolon getrennt:

```text
Startnummer;Vorname;Nachname;Geburtsjahr
1;Anna;Berger;2010
2;Luca;Frei;2009
```
