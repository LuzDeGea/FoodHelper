import requests
from Utente import Utente

"""
inserisci_utente(oggetto_utente)
inserisce un utente nel database sovrascrivendo se già presente
"""
def inserisci_utente(utente):
    richiesta="http://foodhelper.altervista.org/InserisciUtente.php?"+\
    "chat_id='"+str(utente.get_chat_id())+\
    "'&nome='"+utente.get_nome()+\
    "'&sesso='"+utente.get_sesso()+\
    "'&data_nascita='"+str(utente.get_data())+\
    "'&altezza='"+str(utente.get_altezza())+\
    "'&peso='"+str(utente.get_peso())+\
    "'&attivita='"+str(utente.get_attivita())+\
    "'&b_iper='"+str(int(utente.get_iper_tens()))+ \
    "'&nefropatia='" + str(int(utente.get_nefropatia())) + \
    "'&anemia_sideropenica='"+str(int(utente.get_anemia_sideropenica()))+"'"
    requests.get(richiesta)

"""
get_utente(chat_id)-->Utente
restituisce l'utente con identificativo chat_id prendendolo dal database
"""
def get_utente(chat_id):
    r = requests.get("http://foodhelper.altervista.org/getUtente.php?chat_id="+str(chat_id))
    if r.json() is None:
        return None
    utente = Utente(chat_id)
    utente.set_utente(r.json()["nome"],r.json()["sesso"],r.json()["data_nascita"],r.json()["altezza"],r.json()["peso"],r.json()["attivita"],int(r.json()["b_iper"]),int(r.json()["nefropatia"]),int(r.json()["anemia_sideropenica"]))
    return utente

"""
esiste_utente(chat_id)-->bool
restituisce true se l'utente con identificativo chat_id è presente nel database false altrimenti
"""
def esiste_utente(chat_id):
    r = requests.get("http://foodhelper.altervista.org/getUtente.php?chat_id=" + str(chat_id))
    return not(r.json() is None)

