from Utente import Utente

IPERTESO : float = 1940
NEFRO: float = 0.7
ANEMICO_MASCHIO: int = 15 #valori percentuali
ANEMICO_FEMMINA: int = 20 #valori percentuali

class Food:
    def __init__(self, food_name, nutri):
        self.nome = food_name
        self.item_name = nutri["item_name"] ##test##
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
    Restituisce l item_name del cibo sotto forma di stringa
    '''
    def get_item_name(self):
        return self.item_name


    '''
    Restituisce il nome del cibo sotto forma di stringa
    '''
    def get_nome(self):
        return self.nome

    '''
    Restituisce le kcal sotto forma di float
    '''
    def get_calorie(self):
        return self.calorie

    '''
    Restituisce il totale dei carboidrati in g sotto forma di float
    '''
    def get_carboidrati(self):
        return self.carboidrati

    '''
    Restituisce la quantita di colesterolo in mg sotto forma di float
    '''
    def get_colesterolo(self):
        return self.colesterolo

    '''
    Restituisce i grassi totali in g sotto forma di float
    '''
    def get_grassi(self):
        return self.grassi

    '''
    Restituisce la lista degli ingredienti sotto forma di stringa
    '''
    def get_ingredienti(self):
        return self.ingredienti

    '''
    Restituisce il sodio in mg sotto forma di float
    '''
    def get_sodio(self):
        return self.sodio

    '''
    Restituisce gli zuccheri in g sotto forma di float
    '''
    def get_zuccheri(self):
        return self.zuccheri

    '''
    Se il cibo può essere mangiato da un iperteso restituisce True altrimenti restituisce False
    La soglia per un piatto medio di sodio massima l'abbiamo stimata presso i 485mg di sodio, questo
    perchè un iperteso non può assumere più di 5g di sale al giorno
    
    '''
    def can_eat_iperteso(self):
        if not(self.sodio is None):
            if self.sodio < IPERTESO/4:
                return "Consigliato"
            elif self.sodio < IPERTESO/3:
                return "Sconsigliato"
            else:
                return "Proibito"
        else:
            return "No_info"

    '''
    Per i nefropatici devo considerare il livello di proteine e di sodio.
    Se il livello di proteine è accattabile considero solo il livello di sodio, 
    invece se è pessimo sconsiglio a prescindere il cibo.
    Altrimenti se il livello di proteine non è estramemente consigliabile 
    agisco in base al livello di sodio.
    '''
    def can_eat_nefropatia(self, utente):
        if not(self.proteine is None):
            if self.proteine < (utente.peso * 0.7)/4:
                return self.can_eat_iperteso()
            elif self.proteine < (utente.peso * 0.7)/3:
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
            #"Puoi mangiarlo, ma ti consiglio di assumero alimenti con più ferro!"
        else:
            return "Consigliato"


    def __str__(self):
        food = "Il cibo riconosciuto è: " + str(self.nome) + "\n" \
            + "Calorie: " + str(self.calorie) + " kcal\n" \
            + "Carboidrati: " + str(self.carboidrati) + " g\n" \
            + "Colesterolo: " + str(self.colesterolo) + " mg\n" \
            + "Ferro: " + str(self.ferro) + " %\n" \
            + "Grassi: " + str(self.grassi) + " g\n" \
            + "Proteine: " + str(self.proteine) + " g\n" \
            + "Ingredienti: " + str(self.ingredienti) + " g\n" \
            + "Sodio: " + str(self.sodio) + " mg\n" \
            + "Zuccheri: " + str(self.zuccheri) + "g\n" \
            + "Item_name:" + str(self.item_name)+""  ##test##
        return food

