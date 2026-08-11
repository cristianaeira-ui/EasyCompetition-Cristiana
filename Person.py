# -*- coding: utf-8 -*-
# Klasse Person: Vorname, Nachname und Geburtsjahr.
# Das ist die Basisklasse fuer die Klasse Teilnehmer.

class Person():

    # Konstruktor: wird beim Erzeugen eines Objekts aufgerufen
    def __init__(self, vorname, nachname, geburtsjahr):
        self.__vorname = vorname
        self.__nachname = nachname
        self.__geburtsjahr = geburtsjahr

    def getVorname(self):
        return self.__vorname

    def getNachname(self):
        return self.__nachname

    def getGeburtsjahr(self):
        return self.__geburtsjahr

    # Alter = Turnierjahr minus Geburtsjahr
    def getAlter(self, turnierjahr):
        return turnierjahr - self.__geburtsjahr

    # bestimmt, was bei print(person) ausgegeben wird
    def __str__(self):
        return self.__vorname + " " + self.__nachname
