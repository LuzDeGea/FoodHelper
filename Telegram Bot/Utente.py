from datetime import datetime, date

class Utente:
    def __init__(self, chat_id, nome, cognome, sesso, data_nascita, altezza, peso):
        self.chat_id = chat_id
        self.nome = nome
        self.cognome = cognome
        self.sesso = sesso
        self.data_nascita = datetime.strptime(data_nascita, "%m/%d/%y")
        self.altezza = altezza
        self.peso = peso

    def __init__(self, chat_id):
        self.chat_id = chat_id

    def chat_id(self, chat_id):
        self.chat_id = chat_id

    def set_nome(self, nome):
        self.nome = nome

    def set_cognome(self, cognome):
        self.cognome = cognome

    def set_sesso(self, sesso):
        self.sesso = sesso

    def set_data(self, data_nascita):
        self.data_nascita = datetime.strptime(data_nascita, "%d/%m/%y")

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
