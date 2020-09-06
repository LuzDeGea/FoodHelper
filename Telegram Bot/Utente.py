from datetime import datetime, date
import re

'''
Ad ogni tipo di attività viene associata una costante per il calcolo del fabbisogno calorico.
'''

fattore_metabolismo = {"Sedentaria": 1.2, "Leggera": 1.375, "Moderata": 1.55, "Attiva": 1.725, "Molto attiva": 1.9}

'''
La classe Utente rappresenta l'utente considerando dati come il nome, sesso, età,
altezza, peso, il tipo di attività che esso svolge e le patologia che esso possiede.
Alcune patologie non sono state completamente inserite (es.colesterolo).
'''

class Utente:

    '''
    Utente(int) --> Utente
    Costruttore della classe Utente.
    Il costruttore prende in input un intero che rappresenta il numero di chat_id
    per identificare univocamente un singolo utente.
    '''
    def __init__(self, chat_id):
        self.chat_id = chat_id

    '''
    set_utente(stringa, stringa, stringa, data, intero, intero, stringa, bool, bool, bool) --> void 
    Funzione che completa la l'inserimento dell'utente inserendo i relativi dati.
    '''
    def set_utente(self, nome, sesso, data, altezza, peso, attivita, b_iper, nefropatia, anemia_sideropenica):
        self.nome=nome
        self.sesso=sesso
        self.set_data(data)
        self.altezza=int(altezza)
        self.peso=int(peso)
        self.attivita=attivita
        #self.diabete = b_diab
        #self.colesterolo = b_cole
        self.iper_tens = bool(int(b_iper))
        #self.ipo_tens = b_ipo
        self.nefropatia = bool(int(nefropatia))
        self.anemia_sideropenica = bool(int(anemia_sideropenica))

    '''
    set_chat_id(int) --> void
    '''
    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

    '''
    set_nome(stringa) --> void
    '''
    def set_nome(self, nome):
        self.nome = nome

    '''
    set_sesso(stringa) --> void
    '''
    def set_sesso(self, sesso):
        self.sesso = sesso

    '''
    set_data(data) --> void
    '''
    def set_data(self, data_nascita):
        try:
            self.data_nascita = datetime.strptime(data_nascita, "%d/%m/%Y")
        except:
            try:
                self.data_nascita = datetime.strptime(data_nascita, "%Y-%m-%d")
            except:
                return False

    '''
    set_altezza(int) --> void
    '''
    def set_altezza(self, altezza):
        self.altezza = altezza

    '''
    set_peso(int) --> void
    '''
    def set_peso(self, peso):
        self.peso = peso

    '''
    set_attivita(stringa) --> void
    '''
    def set_attivita(self, attivita):
        self.attivita = attivita

    '''
        set_diabete(bool) --> void
        '''

    def set_diabete(self, b):
        self.diabete = bool(b)

    '''
    set_colesterolo(bool) --> void
    '''

    def set_colesterolo(self, b):
        self.colesterolo = bool(b)

    '''
    set_iper_tens(bool) --> void
    '''

    def set_iper_tens(self, b):
        self.iper_tens = bool(b)

    '''
    set_ipo_tens(bool) --> void
    '''

    def set_ipo_tens(self, b):
        self.ipo_tens = bool(b)

    '''
    set_nefropatia(bool) --> void
    '''
    def set_nefropatia(self, nefropatia):
        self.nefropatia = bool(nefropatia)

    '''
    set_anemia_sideropenica(bool) --> void
    '''
    def set_anemia_sideropenica(self, anemia_sideropenica):
        self.anemia_sideropenica = bool(anemia_sideropenica)

    '''
    get_chat_id() --> int
    '''
    def get_chat_id(self):
        return self.chat_id

    '''
    get_nome() --> stringa
    '''
    def get_nome(self):
        return self.nome

    '''
    get_sesso() --> stringa
    '''
    def get_sesso(self):
        return self.sesso

    '''
    get_data() --> data
    '''
    def get_data(self):
        return self.data_nascita

    '''
    get_eta() --> int
    Restituisce l'età dell'utente utilizzando la data di nascita.
    '''
    def get_eta(self):
        if date.today().month <= self.data_nascita.month:
            return date.today().year-1 - self.data_nascita.year
        else:
            return date.today().year - self.data_nascita.year

    '''
    get_altezza() --> int
    '''
    def get_altezza(self):
        return self.altezza

    '''
    get_peso() --> int
    '''
    def get_peso(self):
        return self.peso

    '''
    get_attivita() --> stringa
    '''
    def get_attivita(self):
        return self.attivita

    '''
        get_diabete() --> bool
        '''

    def get_diabete(self):
        return self.diabete

    '''
    get_colesterolo() --> bool
    '''

    def get_colesterolo(self):
        return self.colesterolo

    '''
    get_iper_tens() --> bool
    '''

    def get_iper_tens(self):
        return self.iper_tens

    '''
    get_ipo_tens() --> bool
    '''

    def get_ipo_tens(self):
        return self.ipo_tens

    '''
    get_nefropatia() --> bool
    '''
    def get_nefropatia(self):
        return bool(self.nefropatia)

    '''
    get_anemia_sideropenica() --> bool
    '''
    def get_anemia_sideropenica(self):
        return bool(self.anemia_sideropenica)

    '''
    get_fabbisogno_calorico() --> int
    Calcola il fabbisogno giornaliero calorico dell'utente controllando il sesso, 
    l'altezza il peso e il tipo di attivita che esso svolge.
    '''
    def fabbisogno_calorico(self):
        if self.sesso == "Maschio":
            return ((self.peso*10) + (self.altezza*6.25) - (5*self.get_eta()) + 5) * fattore_metabolismo[self.attivita]
        elif self.sesso == "Femmina":
            return ((self.peso*10) + (self.altezza*6.25) - (5*self.get_eta())-161) * fattore_metabolismo[self.attivita]

    '''
    toString() --> stringa
    '''
    def __str__(self):
        return "Nome: " + str(self.nome) + "\nSesso: " + str(self.sesso) + \
                "\nEtà: " + str(self.get_eta()) + "\nAltezza: " + str(self.altezza) + "cm\nPeso: " + str(self.peso) +\
                "kg\nAttività fisica: " + str(self.attivita) + "\nFabbisogno calorico: " +\
                str(round(self.fabbisogno_calorico(), 2))

    '''
    can_eat(Food) --> stringa
    La funzione prende in input l'oggetto di classe Food e stabilisce se l'utente 
    in base alla patologia che l'utente ha può mangiare o meno il cibo.
    Restituisce la stringa che spiega se l'utente può o non può mangiare quella determinata pietanza.
    '''
    def can_eat(self, cibo):
        feedback = ""

        if self.get_nefropatia():
            risposta = cibo.can_eat_nefropatia(self)
            if risposta == "Sconsigliato":
                feedback = "Puoi mangiare questo piatto ma ti sconsigliamo di mangiare altri piatti contenente troppe proteine o sodio."
            elif risposta == "Proibito":
                return "Questo piatto contiene troppe proteine e sodio per il tuo metabolismo, ti consigliamo di non mangiarlo."
            elif risposta == "No_info":
                return "Non ho abbastanza informazioni su questa pietanza."
        elif self.get_iper_tens():
            risposta = cibo.can_eat_iperteso()
            if risposta == "Sconsigliato":
                feedback = "Puoi mangiare questo piatto ma ti sconsigliamo di mangiare altri piatti contenente troppo sodio."
            elif risposta == "Proibito":
                return "Questo piatto contiene troppo sodio per il tuo metabolismo, ti consigliamo di non mangiarlo."
            elif risposta == "No_info":
                return "Non ho abbastanza informazioni su questa pietanza."
        if self.get_anemia_sideropenica():
            risposta = cibo.can_eat_anemico(self)
            if risposta == "Sconsigliato":
                feedback = "Puoi mangiare questo piatto ma ti consigliamo di mangiare anche piatti aventi più ferro."
            elif risposta == "No_info":
                return "Non ho abbastanza informazioni su questa pietanza."
        if feedback == "":
            return "Puoi mangiare tranquillamente questo cibo!"
        else:
            return feedback
            
    '''
    controllo_nome(stringa) --> bool | controllo_nome(stringa) --> stringa
    Attraverso l'utilizzo di espressioni regolari restituisce il nome dell'utente correttamente.
    Vengono eliminati tutti i caratteri che non possono essere contenuti in un nome.
    '''
def controllo_nome(nome):
    regex = re.findall("\D+", nome)
    char = ""
    if regex:
        for c in regex:
            char += c
        return char
    return False

    '''
    controllo_formato_data(data) --> bool | controllo_formato_data(data) --> data
    Viene restituita la data se è stata inserita correttamente altrimenti restituisce False.
    '''
def controllo_formato_data(data):
    try:
        n_data = datetime.strptime(data, "%d/%m/%Y")
        if (date.today().year - n_data.year) > 13:
            return data
        return False
    except ValueError:
        return False

    '''
    controllo_cifre(int) --> bool |  controllo_cifre(int) --> int
    Effettua un controllo sul numero.
    '''
def controllo_cifre(numero):
    regex = re.findall("[\d]*\.[\d]*|\d+", numero)
    char = ""
    if regex:
        for c in regex:
            char += c
        return float(char)
    return False

    '''
    controllo_altezza(int) --> bool |  controllo_altezza(int) --> int
    Effettua un controllo sui limiti dell'altezza.
    '''
def controllo_altezza(altezza):
    h = controllo_cifre(altezza)
    if 150 < h < 210:
        return h
    else:
        return False

    '''
    controllo_peso(int) --> bool |  controllo_cifre(int) --> int
    Effettua un controllo sui limiti del peso.
    '''
def controllo_peso(peso):
    w = controllo_cifre(peso)
    if 40 < w < 150:
        return w
    else:
        return False
