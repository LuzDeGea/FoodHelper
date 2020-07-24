import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

print(mydb)

mycursor = mydb.cursor()
mycursor.execute("DROP DATABASE IF EXISTS foodhelper")
mycursor.execute("CREATE DATABASE foodhelper")
mycursor.execute("USE foodhelper")

mycursor.execute("CREATE TABLE utente (chat_id INT PRIMARY KEY,nome VARCHAR(255),cognome VARCHAR(255),sesso VARCHAR(8),data_nascita DATE,altezza SMALLINT,peso SMALLINT)")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()