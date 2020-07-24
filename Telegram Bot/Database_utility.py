import mysql.connector
from Utente import Utente
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

mycursor = mydb.cursor()

mycursor.execute("USE foodhelper")

def inserisci_utente(utente):
    query = "INSERT INTO utente (chat_id,nome,cognome,sesso,data_nascita,altezza,peso) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values =(utente.get_chat_id(),utente.get_nome(),utente.get_cognome(),utente.get_sesso(),utente.get_data_nascita(),utente.get_altezza(),utente.get_peso())
    mycursor.execute(query, values)
    mydb.commit()

def get_cose(query):
    mycursor.execute(query)
    result = mycursor.fetchall()
    return result

pino=Utente(314158265)
pino.set_nome("pino")
pino.set_cognome("abete")
pino.set_sesso("maschio")
pino.set_data("23/10/99")
pino.set_altezza("183")
pino.set_peso("83")
print(pino)

#inserisci_utente(pino)


result=get_cose("SELECT * FROM utente")
for x in result:
    print(x)