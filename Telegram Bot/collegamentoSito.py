import requests
from pprint import pprint
from Utente import Utente
#r = requests.get("http://foodhelper.altervista.org/InserisciUtente.php?chat_id='123654789'&nome='pino'&cognome='asd'&sesso='Maschio'&data_nascita='1998/10/10'&altezza='183'&peso='83'&attivita='leggera'&b_diab='0'&b_cole='0'&b_iper='0'&b_ipo='0'")
#r=requests.get("http://foodhelper.altervista.org/getUtente.php?chat_id=381741872")
#print(r.json())
#print(r.json()["chat_id"])

def inserisci_utente(utente):
    richiesta="http://foodhelper.altervista.org/InserisciUtente.php?"+\
    "chat_id='"+str(utente.get_chat_id())+\
    "'&nome='"+utente.get_nome()+\
    "'&cognome='"+utente.get_cognome()+\
    "'&sesso='"+utente.get_sesso()+\
    "'&data_nascita='"+str(utente.get_data())+\
    "'&altezza='"+str(utente.get_altezza())+\
    "'&peso='"+str(utente.get_peso())+\
    "'&attivita='"+str(utente.get_attivita())+\
    "'&b_iper='"+str(int(utente.get_iper_tens()))+ \
    "'&nefropatia='" + str(int(utente.get_nefropatia())) + \
    "'&anemia_sideropenica='"+str(int(utente.get_anemia_sideropenica()))+"'"
    requests.get(richiesta)

def get_utente(chat_id):
    #print("http://foodhelper.altervista.org/getUtente.php?chat_id="+str(chat_id))
    r = requests.get("http://foodhelper.altervista.org/getUtente.php?chat_id="+str(chat_id))
    pprint(r.json())
    utente = Utente(chat_id)
    utente.set_utente(r.json()["nome"],r.json()["cognome"],r.json()["sesso"],r.json()["data_nascita"],r.json()["altezza"],r.json()["peso"],r.json()["attivita"],int(r.json()["b_iper"]),int(r.json()["nefropatia"]),int(r.json()["anemia_sideropenica"]))
    return utente

def esiste_utente(chat_id):
    r = requests.get("http://foodhelper.altervista.org/getUtente.php?chat_id=" + str(chat_id))
    return not(r.json() is None)

