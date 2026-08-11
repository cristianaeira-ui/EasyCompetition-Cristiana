# -*- coding: utf-8 -*-
# Klasse Teilnehmer: eine Person, die am Wettkampf teilnimmt.
# Teilnehmer erbt von Person und hat zusaetzlich eine Startnummer
# und eine Liste mit den Punkten der Durchgaenge.

import Person as p


class Teilnehmer(p.Person):

    def __init__(self, startnummer, vorname, nachname, geburtsjahr):
        super().__init__(vorname, nachname, geburtsjahr)   # Konstruktor der Oberklasse
        self.__startnummer = startnummer
        self.__punkte = []                                  # leere Liste

    def getStartnummer(self):
        return self.__startnummer

    # Punkte eines Durchgangs hinten an die Liste anhaengen
    def addPunkte(self, punkte):
        self.__punkte.append(punkte)

    # die ganze Liste (wird fuer die Datenbank gebraucht)
    def getPunkteListe(self):
        return self.__punkte

    # Summe aller Punkte, ohne Bonus
    def getPunkte(self):
        return sum(self.__punkte)

    # Kategorie: U18, Elite oder Ue50
    def getKategorie(self, turnierjahr):
        alter = self.getAlter(turnierjahr)
        if alter <= 17:
            return "U18"
        elif alter >= 50:
            return "Ue50"
        else:
            return "Elite"

    # Bonus-Faktor zum Ausgleich der Alters-Nachteile
    def getFaktor(self, turnierjahr):
        alter = self.getAlter(turnierjahr)
        kategorie = self.getKategorie(turnierjahr)
        if kategorie == "U18":
            return 1 + (17 - alter) / 10
        elif kategorie == "Ue50":
            return 1 + (alter - 50) / 50
        else:
            return 1.0

    # gewertete Punkte = Rohpunkte mal Faktor
    def getTotal(self, turnierjahr):
        return round(self.getPunkte() * self.getFaktor(turnierjahr), 2)

    def __str__(self):
        return str(self.__startnummer) + ": " + super().__str__()
