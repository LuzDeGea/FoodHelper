import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

mycursor = mydb.cursor()
mycursor.execute("DROP DATABASE IF EXISTS foodhelper")
mycursor.execute("CREATE DATABASE foodhelper")
mycursor.execute("USE foodhelper")

mycursor.execute("CREATE TABLE utente (chat_id INT PRIMARY KEY,nome VARCHAR(55),cognome VARCHAR(55),sesso VARCHAR(8),data_nascita DATE,altezza SMALLINT,peso SMALLINT,attivita VARCHAR(25),b_diab BOOLEAN, b_cole BOOLEAN, b_iper BOOLEAN, b_ipo BOOLEAN)")

