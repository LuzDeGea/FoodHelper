import requests
from Utente import Utente
#r = requests.get("http://foodhelper.altervista.org/InserisciUtente.php?chat_id='123654789'&nome='pino'&cognome='asd'&sesso='Maschio'&data_nascita='1998/10/10'&altezza='183'&peso='83'&attivita='leggera'&b_diab='0'&b_cole='0'&b_iper='0'&b_ipo='0'")
r=requests.get("http://foodhelper.altervista.org/getUtente.php?chat_id=381741872")
print(r.json())
print(r.json()["chat_id"])

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
    "'&b_diab='"+str(int(utente.get_diabete()))+\
    "'&b_cole='"+str(int(utente.get_colesterolo()))+\
    "'&b_iper='"+str(int(utente.get_iper_tens()))+\
    "'&b_ipo='"+str(int(utente.get_ipo_tens()))+"'"

    print(richiesta)
    r=requests.get(richiesta)

    print(r)
def get_utente(chat_id):
    print("http://foodhelper.altervista.org/getUtente.php?chat_id="+str(chat_id))
    r = requests.get("http://foodhelper.altervista.org/getUtente.php?chat_id="+str(chat_id))
    print(r)
    print(type(r))
    utente =Utente(chat_id)
    print(r.json())
    print(r.json()["chat_id"])
    utente.set_utente(r.json()["nome"],r.json()["cognome"],r.json()["sesso"],r.json()["data_nascita"],r.json()["altezza"],r.json()["peso"],r.json()["attivita"],r.json()["b_diab"],r.json()["b_cole"],r.json()["b_iper"],r.json()["b_ipo"])
    print(utente)
    return utente
