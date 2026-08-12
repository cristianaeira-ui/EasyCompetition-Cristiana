# -*- coding: utf-8 -*-
# Easy Competition - Hauptprogramm
# Hier laeuft der ganze Ablauf: einlesen, erfassen, anzeigen, speichern.

import Teilnehmer as t
import Wettkampf as w
import Datenbank as db

JAHR = 2026                 # Turnierjahr, wird fuer die Altersberechnung gebraucht


# Teilnehmer aus dem CSV-File lesen
# Aufbau einer Zeile:  Startnummer;Vorname;Nachname;Geburtsjahr
def leseTeilnehmer(dateiname):
    liste = []
    try:
        datei = open(dateiname, "r", encoding="utf-8")
        datei.readline()                          # erste Zeile ist die Ueberschrift
        for zeile in datei:
            teile = zeile.strip().split(";")      # Zeile beim Semikolon aufteilen
            neuerTeilnehmer = t.Teilnehmer(int(teile[0]), teile[1], teile[2], int(teile[3]))
            liste.append(neuerTeilnehmer)
        datei.close()
    except FileNotFoundError:
        print("Fehler: Das File " + dateiname + " wurde nicht gefunden.")
    return liste


# Eine Zahl einlesen und pruefen, ob es wirklich eine Zahl ist
def leseZahl(text):
    while True:
        eingabe = input(text)
        try:
            return int(eingabe)
        except ValueError:
            print("      Das war keine Zahl. Bitte nochmals versuchen.")


# Teilnehmerliste mit Kategorie und Faktor ausgeben
def druckeTeilnehmer(wettkampf):
    print()
    print("Nr  Name                      Jahrgang  Kategorie  Faktor")
    print("-" * 60)
    for teilnehmer in wettkampf.getTeilnehmer():
        print(f"{teilnehmer.getStartnummer():>2}  "
              f"{teilnehmer.getVorname() + ' ' + teilnehmer.getNachname():<24}  "
              f"{teilnehmer.getGeburtsjahr():>8}  "
              f"{teilnehmer.getKategorie(JAHR):<9}  "
              f"{teilnehmer.getFaktor(JAHR):>6.2f}")


# Rangliste ausgeben. Ohne Kategorie erscheinen alle Teilnehmer.
def druckeRangliste(wettkampf, titel, kategorie=""):
    print()
    print("=== " + titel + " ===")
    print("Rang  Nr  Name                      Punkte  Faktor    Total")
    print("-" * 60)
    rang = 1
    for teilnehmer in wettkampf.getRangliste(kategorie):
        print(f"{rang:>4}  {teilnehmer.getStartnummer():>2}  "
              f"{teilnehmer.getVorname() + ' ' + teilnehmer.getNachname():<24}  "
              f"{teilnehmer.getPunkte():>6}  "
              f"{teilnehmer.getFaktor(JAHR):>6.2f}  {teilnehmer.getTotal(JAHR):>7.2f}")
        rang = rang + 1


# Schlussrangliste in ein CSV-File schreiben (kann mit Excel geoeffnet werden)
def speichereRangliste(wettkampf, dateiname):
    datei = open(dateiname, "w", encoding="utf-8")
    datei.write("Kategorie;Rang;Startnummer;Vorname;Nachname;Punkte;Faktor;Total\n")
    for kategorie in ["U18", "Elite", "Ue50"]:
        rang = 1
        for teilnehmer in wettkampf.getRangliste(kategorie):
            datei.write(f"{kategorie};{rang};{teilnehmer.getStartnummer()};"
                        f"{teilnehmer.getVorname()};{teilnehmer.getNachname()};"
                        f"{teilnehmer.getPunkte()};{teilnehmer.getFaktor(JAHR):.2f};"
                        f"{teilnehmer.getTotal(JAHR):.2f}\n")
            rang = rang + 1
    datei.close()
    print("Die Schlussrangliste wurde in " + dateiname + " gespeichert.")


def main():
    # 1. Wettkampf erzeugen (nur 3 bis 5 Durchgaenge sind erlaubt)
    try:
        wettkampf = w.Wettkampf("SWS Sommer-Event", JAHR, 3)
    except ValueError as fehler:
        print("Fehler: " + str(fehler))
        return                      # Programm beenden, weil kein Wettkampf da ist

    # 2. Teilnehmer einlesen und anmelden
    for teilnehmer in leseTeilnehmer("teilnehmer.csv"):
        wettkampf.addTeilnehmer(teilnehmer)
    print(wettkampf)

    # 3. Teilnehmerliste mit Kategorie und Faktor anzeigen
    druckeTeilnehmer(wettkampf)

    # 4. Punkte der Durchgaenge erfassen, nach jedem Durchgang den Zwischenstand
    for durchgang in range(1, wettkampf.getAnzahlDurchgaenge() + 1):
        print()
        print("Punkte fuer Durchgang " + str(durchgang) + " eingeben:")
        for teilnehmer in wettkampf.getTeilnehmer():
            punkte = leseZahl("  " + str(teilnehmer) + ": ")
            teilnehmer.addPunkte(punkte)
        druckeRangliste(wettkampf, "Zwischenstand nach Durchgang " + str(durchgang))

    # 5. Schlussrangliste pro Kategorie
    for kategorie in ["U18", "Elite", "Ue50"]:
        druckeRangliste(wettkampf, "Schlussrangliste " + kategorie, kategorie)

    # 6. Speichern: als CSV-File und in der Datenbank
    print()
    speichereRangliste(wettkampf, "schlussrangliste.csv")
    db.erstelleTabellen()
    db.speichereWettkampf(wettkampf)


main()
