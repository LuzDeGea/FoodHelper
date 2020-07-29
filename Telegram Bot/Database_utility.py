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
    query = "DELETE FROM utente WHERE chat_id = %s"
    values =(utente.get_chat_id(),)
    mycursor.execute(query, values)
    mydb.commit()
    query = "INSERT INTO utente (chat_id,nome,cognome,sesso,data_nascita,altezza,peso,attivita) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    values =(utente.get_chat_id(),utente.get_nome(),utente.get_cognome(),utente.get_sesso(),utente.get_data(),utente.get_altezza(),utente.get_peso(),utente.get_attivita())
    mycursor.execute(query, values)
    mydb.commit()

def get_utente(chat_id):
    mycursor.execute("SELECT * FROM utente WHERE chat_id = "+str(chat_id))
    result = mycursor.fetchall()
    print(result)
    print(result[0][0])
    utente = Utente(result[0][0])
    utente.set_utente(result[0][1],result[0][2],result[0][3],result[0][4],result[0][5],result[0][6],result[0][7])
    return utente
