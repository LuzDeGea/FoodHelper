from datetime import datetime, date

class Utente:
    def __init__(self, nome, cognome, sesso, data_nascita, altezza, peso):
        self.nome = nome
        self.cognome = cognome
        self.sesso = sesso
        self.data_nascita = datetime.strptime(data_nascita, "%m/%d/%y")
        self.altezza = altezza
        self.peso = peso

    def set_name(self, nome):
        self.nome = nome

    def set_cognome(self, nome):
        self.nome = nome

    def set_sesso(self, sesso):
        self.sesso = sesso

    def set_data(self, data_nascita):
        self.data_nascita = date.strftime(data_nascita)

    def set_altezza(self, altezza):
        self.altezza = altezza

    def set_peso(self, peso):
        self.peso = peso

    def get_eta(self):
        if date.today().month <= self.data_nascita.month:
            return date.today().year-1 - self.data_nascita.year
        else:
            return date.today().year - self.data_nascita.year

    def __str__(self):
        return "Nome: " + str(self.nome) + "\nCognome: " + str(self.cognome) + "\nSesso: " + str(self.sesso) + \
                "\nEtà: " + str(self.get_eta()) + "\nAltezza: " + str(self.altezza) + "\nPeso: " + str(self.peso)

marco = Utente("Antonio", "GreenSully", "Femmina" , "10/23/98" ,2.05, 678.3)
print(marco)
