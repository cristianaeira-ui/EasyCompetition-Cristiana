# -*- coding: utf-8 -*-
# Klasse Wettkampf: haelt die Liste der Teilnehmer und erstellt die Rangliste.

class Wettkampf():

    def __init__(self, name, jahr, anzahlDurchgaenge):
        self.__name = name
        self.__jahr = jahr
        self.__anzahlDurchgaenge = anzahlDurchgaenge
        self.__teilnehmer = []                # leere Liste fuer die Teilnehmer

    def getName(self):
        return self.__name

    def getJahr(self):
        return self.__jahr

    def getAnzahlDurchgaenge(self):
        return self.__anzahlDurchgaenge

    def addTeilnehmer(self, teilnehmer):
        self.__teilnehmer.append(teilnehmer)

    def getTeilnehmer(self):
        return self.__teilnehmer

    # Rangliste: sortierte Liste der Teilnehmer.
    # Ohne Kategorie kommen alle in die Liste (= Zwischenstand).
    def getRangliste(self, kategorie=""):
        liste = []
        for teilnehmer in self.__teilnehmer:
            if kategorie == "" or teilnehmer.getKategorie(self.__jahr) == kategorie:
                liste.append(teilnehmer)
        liste.sort(key=lambda t: t.getTotal(self.__jahr), reverse=True)
        return liste

    def __str__(self):
        return (self.__name + " " + str(self.__jahr) + ", "
                + str(self.__anzahlDurchgaenge) + " Durchgaenge, "
                + str(len(self.__teilnehmer)) + " Teilnehmer")
