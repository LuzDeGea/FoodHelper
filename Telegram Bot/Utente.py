from datetime import datetime, date
import re

fattore_metabolismo = {"Sedentaria" : 1.2, "Leggera" : 1.375, "Moderata" : 1.55, "Attiva" : 1.725, "Molto attiva" : 1.9}

class Utente:
    def __init__(self, chat_id):
        self.chat_id = chat_id

    def set_utente(self, nome, cognome, sesso, data, altezza, peso, attivita, b_diab, b_cole, b_iper, b_ipo):
        self.nome=nome
        self.cognome=cognome
        self.sesso=sesso
        self.set_data(data)
        self.altezza=int(altezza)
        self.peso=int(peso)
        self.attivita=attivita
        self.diabete = b_diab
        self.colesterolo = b_cole
        self.iper_tens = b_iper
        self.ipo_tens = b_ipo

    def set_diabete(self, b):
        self.diabete = b

    def set_colesterolo(self, b):
        self.colesterolo = b

    def set_iper_tens(self, b):
        self.iper_tens = b

    def set_ipo_tens(self, b):
        self.ipo_tens = b

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

    def set_nome(self, nome):
        self.nome = nome

    def set_cognome(self, cognome):
        self.cognome = cognome

    def set_sesso(self, sesso):
        self.sesso = sesso

    def set_data(self, data_nascita):
        print(data_nascita)
        try:
            self.data_nascita = datetime.strptime(data_nascita, "%d/%m/%Y")
        except:
            try:
                self.data_nascita = datetime.strptime(data_nascita, "%Y-%m-%d")
            except:
                return False

    def set_altezza(self, altezza):
        self.altezza = altezza

    def set_peso(self, peso):
        self.peso = peso

    def set_attivita(self, attivita):
        self.attivita = attivita

    def get_diabete(self):
        return self.diabete

    def get_colesterolo(self):
        return self.colesterolo

    def get_iper_tens(self):
        return self.iper_tens

    def get_ipo_tens(self):
        return self.ipo_tens

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

    def get_attivita(self):
        return self.attivita

    def fabbisogno_calorico(self):
        if self.sesso == "Maschio":
            return ((self.peso*10) + (self.altezza*6.25) - (5*self.get_eta()) + 5) * fattore_metabolismo[self.attivita]
        elif self.sesso == "Femmina":
            return ((self.peso*10) + (self.altezza*6.25) - (5*self.get_eta())-161) * fattore_metabolismo[self.attivita]

    def __str__(self):
        return "Nome: " + str(self.nome) + "\nCognome: " + str(self.cognome) + "\nSesso: " + str(self.sesso) + \
                "\nEtà: " + str(self.get_eta()) + "\nAltezza: " + str(self.altezza) + "\nPeso: " + str(self.peso) +\
                "\nAttività fisica: " + str(self.attivita) + "\nFabbisogno calorico: " + str(self.fabbisogno_calorico())

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
        n_data = datetime.strptime(data, "%d/%m/%Y")
        print(date.today().year)
        print(n_data.year)
        if (date.today().year - n_data.year) > 17:
            return data
        print("brbrbrbrbrbr")
        return False
    except ValueError:
        print("exception")
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

