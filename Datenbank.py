# -*- coding: utf-8 -*-
# SQLite-Datenbank: zwei Tabellen, teilnehmer und resultat.
# SQLite braucht keinen Server, die Datenbank ist die Datei wettkampf.db.

import sqlite3

dbName = "wettkampf.db"

createTeilnehmer = """CREATE TABLE IF NOT EXISTS teilnehmer (
                        id          INTEGER PRIMARY KEY,
                        vorname     TEXT,
                        nachname    TEXT,
                        geburtsjahr INTEGER,
                        kategorie   TEXT)"""

createResultat = """CREATE TABLE IF NOT EXISTS resultat (
                        teilnehmer_id INTEGER,
                        durchgang     INTEGER,
                        punkte        INTEGER,
                        FOREIGN KEY (teilnehmer_id) REFERENCES teilnehmer (id))"""


# Die beiden Tabellen erzeugen, falls es sie noch nicht gibt
def erstelleTabellen():
    try:
        with sqlite3.connect(dbName) as verbindung:
            cursor = verbindung.cursor()
            cursor.execute(createTeilnehmer)
            cursor.execute(createResultat)
        print("Die Datenbank-Tabellen sind bereit.")
    except sqlite3.Error as fehler:
        print("Datenbank-Fehler: " + str(fehler))


# Alle Teilnehmer und ihre Punkte in die Datenbank schreiben
def speichereWettkampf(wettkampf):
    try:
        with sqlite3.connect(dbName) as verbindung:
            cursor = verbindung.cursor()
            cursor.execute("DELETE FROM resultat")           # alte Daten loeschen
            cursor.execute("DELETE FROM teilnehmer")
            for teilnehmer in wettkampf.getTeilnehmer():
                cursor.execute("INSERT INTO teilnehmer VALUES (?, ?, ?, ?, ?)",
                               (teilnehmer.getStartnummer(),
                                teilnehmer.getVorname(),
                                teilnehmer.getNachname(),
                                teilnehmer.getGeburtsjahr(),
                                teilnehmer.getKategorie(wettkampf.getJahr())))
                durchgang = 1
                for punkte in teilnehmer.getPunkteListe():
                    cursor.execute("INSERT INTO resultat VALUES (?, ?, ?)",
                                   (teilnehmer.getStartnummer(), durchgang, punkte))
                    durchgang = durchgang + 1
        print("Der Wettkampf wurde in der Datenbank gespeichert.")
    except sqlite3.Error as fehler:
        print("Datenbank-Fehler: " + str(fehler))


# Zur Kontrolle: alle Zeilen der Tabelle teilnehmer wieder lesen
def zeigeDatenbank():
    try:
        with sqlite3.connect(dbName) as verbindung:
            cursor = verbindung.cursor()
            cursor.execute("SELECT * FROM teilnehmer ORDER BY id")
            for zeile in cursor.fetchall():
                print(zeile)
    except sqlite3.Error as fehler:
        print("Datenbank-Fehler: " + str(fehler))
