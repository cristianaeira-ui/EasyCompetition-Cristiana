# Anleitung: Repository in PyCharm öffnen

Diese Anleitung zeigt Schritt für Schritt, wie du dieses Projekt direkt von
GitHub in PyCharm holst («klonen») und startest. Du musst dafür nichts von Hand
herunterladen – PyCharm macht das für dich.

**Repository-Adresse (URL):**

```
https://github.com/cristianaeira-ui/EasyCompetition-Cristiana
```

---

## Voraussetzungen

Bevor du beginnst, sollte auf dem Computer installiert sein:

- **PyCharm** (Community Edition genügt, ist gratis)
- **Python** (Version 3.x)
- **Git** – meist schon vorhanden. Falls PyCharm später meldet, dass Git fehlt,
  bietet es an, Git herunterzuladen; das kannst du dort direkt bestätigen.

---

## Schritt 1: Das Klonen-Fenster öffnen

Es gibt zwei Wege – je nachdem, ob PyCharm gerade offen ist oder nicht.

**A) PyCharm ist frisch gestartet (Willkommensbildschirm):**

1. Auf dem Startbildschirm auf **Get from VCS** klicken
   (VCS = Version Control System, also die Versionsverwaltung).

**B) PyCharm hat schon ein Projekt offen:**

1. Oben im Menü auf **Git → Clone…** klicken.
   (In manchen Versionen: **File → Project from Version Control…**)

---

## Schritt 2: Die Repository-Adresse eintragen

1. Bei **Version control** ist **Git** ausgewählt.
2. Ins Feld **URL** die Adresse einfügen:

   ```
   https://github.com/cristianaeira-ui/EasyCompetition-Cristiana
   ```

3. Bei **Directory** steht der Ordner, in den das Projekt gespeichert wird. Den
   Vorschlag kannst du so lassen oder einen eigenen Ordner wählen.
4. Auf **Clone** klicken.

---

## Schritt 3: Bei GitHub anmelden

Wenn PyCharm nach einer Anmeldung fragt:

1. Auf **Log in via GitHub** (oder **Use Token**) klicken.
2. PyCharm öffnet den Browser. Dort bei GitHub einloggen und die Verbindung
   bestätigen.
3. Zurück in PyCharm ist die Anmeldung nun gespeichert.

> Ist das Repository öffentlich, funktioniert das Klonen oft auch ohne
> Anmeldung. Fürs Speichern eigener Änderungen (Push) brauchst du die Anmeldung
> aber in jedem Fall.

---

## Schritt 4: Das Projekt öffnen lassen

1. Nach dem Klonen fragt PyCharm meist: **«Open Project?»** – mit **Yes** /
   **This Window** bestätigen.
2. Beim ersten Öffnen richtet PyCharm eventuell noch den Python-Interpreter ein.
   Den Vorschlag kannst du in der Regel einfach mit **OK** bestätigen.

---

## Schritt 5: Den richtigen Branch auswählen

Der Code liegt aktuell auf dem Branch **`claude/new-session-cf058o`**. Falls du
die Python-Dateien im Projektbaum links **nicht** siehst, wechsle auf diesen
Branch:

1. Unten rechts in der Statusleiste auf den **Branch-Namen** klicken
   (dort steht z. B. `main` oder `Git:`).
2. In der Liste unter **Remote Branches** den Branch
   `origin/claude/new-session-cf058o` auswählen.
3. Auf **Checkout** klicken.

Danach erscheinen links im Projektbaum die Dateien `Person.py`,
`Teilnehmer.py`, `Wettkampf.py`, `Datenbank.py`, `Main.py` und `teilnehmer.csv`.

---

## Schritt 6: Das Programm starten

1. Links im Projektbaum die Datei **`Main.py`** anklicken, damit sie im Editor
   geöffnet wird.
2. Oben rechts auf den grünen **Pfeil (Run)** klicken – oder Rechtsklick auf
   `Main.py` → **Run 'Main'**.
3. Unten öffnet sich das **Run-Fenster**. Dort fragt das Programm die Punkte ab;
   die Zahlen tippst du direkt in dieses Fenster und bestätigst mit Enter.

---

## Später: Änderungen speichern und hochladen

Wenn du am Code etwas änderst und es auf GitHub sichern willst:

1. **Commit:** Oben im Menü **Git → Commit…**, die Änderungen ankreuzen, eine
   kurze Beschreibung schreiben und auf **Commit** klicken.
2. **Push:** Danach **Git → Push…** und auf **Push** klicken. Jetzt sind die
   Änderungen auf GitHub.

---

## Wenn etwas nicht klappt

| Problem | Lösung |
|---|---|
| «Git is not installed» | Auf **Download and Install** klicken, PyCharm holt Git. |
| Dateien fehlen im Projekt | Bist du auf dem richtigen Branch? Siehe Schritt 5. |
| Anmeldung schlägt fehl | In PyCharm unter **Settings → Version Control → GitHub** das Konto neu hinzufügen. |
| Kein Python-Interpreter | **Settings → Project → Python Interpreter**, dort ein installiertes Python auswählen. |
