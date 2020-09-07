'''
Stima valori medi.
'''
IPERTESO: float = 1940
NEFRO: float = 0.7
ANEMICO_MASCHIO: int = 15  # valori percentuali
ANEMICO_FEMMINA: int = 20  # valori percentuali

'''
La classe Food rappresenta il cibo considerando dati come il nome, le calorie, carboidrati, colesterolo,
ferro, grassi, la lista degli ingredienti, le proteini, il sodio, e gli zuccheri.
'''
class Food:

    '''
    Food(stringa, dizionario) --> Food
    Costruttore della classe Food.
    Food_name rappresenta il nome del cibo riconosciuto.
    Nutri è il dizionario contente le informazioni sul cibo.
    '''
    def __init__(self, food_name, nutri):
        self.nome = food_name
        self.item_name = nutri["item_name"]  ##test##
        self.calorie = nutri["nf_calories"]
        self.carboidrati = nutri["nf_total_carbohydrate"]
        self.colesterolo = nutri["nf_cholesterol"]
        self.ferro = nutri["nf_iron_dv"]
        self.grassi = nutri["nf_total_fat"]
        self.ingredienti = nutri["nf_ingredient_statement"]
        self.proteine = nutri["nf_protein"]
        self.sodio = nutri["nf_sodium"]
        self.zuccheri = nutri["nf_sugars"]

    '''
    get_chat_id() --> stringa
    '''
    def get_item_name(self):
        return self.item_name

    '''
    get_nome() --> stringa
    '''
    def get_nome(self):
        return self.nome

    '''
    get_calorie() --> float
    Restituisce le kcal.
    '''
    def get_calorie(self):
        return self.calorie

    '''
    get_carboidrati() --> float
    Restituisce il totale dei carboidrati in g.
    '''
    def get_carboidrati(self):
        return self.carboidrati

    '''
    get_colesterolo() --> float
    Restituisce la quantita di colesterolo in mg.
    '''
    def get_colesterolo(self):
        return self.colesterolo

    '''
    get_grassi() --> float
    Restituisce i grassi totali in g.
    '''
    def get_grassi(self):
        return self.grassi

    '''
    get_ingredienti() --> stringa
    Restituisce la lista degli ingredienti sotto forma di stringa.
    '''

    def get_ingredienti(self):
        return self.ingredienti

    '''
    get_sodio() --> float
    Restituisce il sodio in mg.
    '''

    def get_sodio(self):
        return self.sodio

    '''
    get_zuccheri() --> float
    Restituisce gli zuccheri in g.
    '''

    def get_zuccheri(self):
        return self.zuccheri

    '''
    can_eat_iperteso() --> stringa
    Restituisce una stringa che indica se un iperteso può mangiare o meno questo alimento.
    La soglia per un piatto medio di sodio massima l'abbiamo stimata presso i 485mg di sodio, questo
    perchè un iperteso non può assumere più di 5g di sale al giorno
    '''

    def can_eat_iperteso(self):
        if not (self.sodio is None):
            if self.sodio < IPERTESO / 10:
                return "Consigliato"
            elif self.sodio < IPERTESO / 6:
                return "Sconsigliato"
            else:
                return "Proibito"
        else:
            return "No_info"

    '''
    can_eat_nefropatia(utente) --> stringa
    Restituisce una stringa che indica se un nefropatico può mangiare o meno questo alimento.
    Per i nefropatici devo considerare il livello di proteine e di sodio.
    Se il livello di proteine è accattabile considero solo il livello di sodio, 
    invece se è pessimo sconsiglio a prescindere il cibo.
    Altrimenti se il livello di proteine non è estramemente consigliabile 
    agisco in base al livello di sodio.
    '''

    def can_eat_nefropatia(self, utente):
        if not (self.proteine is None):
            if self.proteine < (utente.peso * 0.7) / 4:
                return self.can_eat_iperteso()
            elif self.proteine < (utente.peso * 0.7) / 3:
                if self.can_eat_iperteso() == "Consigliato":
                    return "Sconsigliato"
                elif self.can_eat_iperteso() == "No_info":
                    return "No_info"
                else:
                    return "Proibito"
            else:
                return "Proibito"
        else:
            return "No_info"

    '''
    can_eat_anemico(utente) --> stringa
    Restituisce una stringa che indica se una persona anemica può mangiare o meno questo alimento.
    Considero il livello di ferro da assumere in base al sesso del utente
    e se l'utente è o meno in menopausa.
    '''
    def can_eat_anemico(self, utente):
        if utente.get_sesso() == "Femmina" and utente.get_eta() < 50:
            ferro_consigliato = ANEMICO_FEMMINA
        else:
            ferro_consigliato = ANEMICO_MASCHIO
        if self.ferro < ferro_consigliato:
            return "Sconsigliato"
            # "Puoi mangiarlo, ma ti consiglio di assumero alimenti con più ferro!"
        else:
            return "Consigliato"

    '''
    toString() --> stringa
    '''
    def __str__(self):
        food = str(self.nome) + "\n"
        if self.calorie is not None:
            food += "Calorie: " + str(self.calorie) + " kcal\n"
        if self.carboidrati is not None:
            food += "Carboidrati: " + str(self.carboidrati) + " g\n"
        if self.colesterolo is not None:
            food += "Colesterolo: " + str(self.colesterolo) + " mg\n"
        if self.ferro is not None:
            food += "Ferro: " + str(self.ferro) + " %\n"
        if self.grassi is not None:
            food += "Grassi: " + str(self.grassi) + " g\n"
        if self.proteine is not None:
            food += "Proteine: " + str(self.proteine) + " g\n"
        if self.ingredienti is not None:
            food += "Ingredienti: " + str(self.ingredienti) + " g\n"
        if self.sodio is not None:
            food += "Sodio: " + str(self.sodio) + " mg\n"
        if self.zuccheri is not None:
            food += "Zuccheri: " + str(self.zuccheri) + "g"
        #if self.item_name is not None:
            #food += "Item_name:" + str(self.item_name) + ""  ##test##
        return food


