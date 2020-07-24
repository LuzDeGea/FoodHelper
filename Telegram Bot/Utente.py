from datetime import datetime, date
import re

class Utente:
    def __init__(self, chat_id):
        self.chat_id = chat_id

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

    def set_nome(self, nome):
        self.nome = nome

    def set_cognome(self, cognome):
        self.cognome = cognome

    def set_sesso(self, sesso):
        if sesso[0].lower() == 'm':
            self.sesso = "maschio"
        elif sesso[0].lower() == 'f':
            self.sesso = "femmina"

    def set_data(self, data_nascita):
        try:
            self.data_nascita = datetime.strptime(data_nascita, "%d/%m/%y")
        except:
            return False

    def set_altezza(self, altezza):
        self.altezza = altezza

    def set_peso(self, peso):
        self.peso = peso

    def get_chat_id(self):
        return self.chat_id

    def get_nome(self):
        return self.nome

    def get_cognome(self):
        return self.cognome

    def get_sesso(self):
        return self.sesso

    def get_data(self):
        return self.data_nascita

    def get_eta(self):
        if date.today().month <= self.data_nascita.month:
            return date.today().year-1 - self.data_nascita.year
        else:
            return date.today().year - self.data_nascita.year

    def get_altezza(self):
        return self.altezza

    def get_peso(self):
        return self.peso

    def __str__(self):
        return "Nome: " + str(self.nome) + "\nCognome: " + str(self.cognome) + "\nSesso: " + str(self.sesso) + \
                "\nEtà: " + str(self.get_eta()) + "\nAltezza: " + str(self.altezza) + "\nPeso: " + str(self.peso)

def controllo_nome(nome):
    regex = re.findall("\D+", nome)
    char = ""
    if regex:
        for c in regex:
            char += c
        return char
    return False

def controllo_formato_data(data):
    try:
        n_data = datetime.strptime(data, "%d/%m/%y")
        if (date.today().year - n_data.year) > 17:
            return data
        return False
    except ValueError:
        return False

def controllo_cifre(numero):
    regex = re.findall("\d", numero)
    char = ""
    if regex:
        for c in regex:
            char += c
        return int(char)
    return False

def controllo_altezza(altezza):
    h = controllo_cifre(altezza)
    if 150 < h < 210:
        return h
    else:
            return False

def controllo_peso(peso):
    w = controllo_cifre(peso)
    if 45 < w < 130:
        return w
    else:
        return False


