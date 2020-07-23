import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardButton, InlineKeyboardMarkup
from Food_detection import food_detection
from Dialogflow_Api import rispondimi
from Utente import Utente
import time

TOKEN = "1130648366:AAEPXCisGv8B2Hby_3xuK9ATwMwGKqjPEn8"

bot = telepot.Bot(TOKEN)

stato_conversazione = {"Nome" : 0,"Cognome" : 1,"Sesso" : 2,"Eta" : 3,"Altezza" : 4,"Peso" : 5}
utenti = {}
acquisizione_dati = {}

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == "document":
        bot.download_file(msg['document']['file_id'], 'Immagini\\Cibo.png')
        bot.sendMessage(chat_id, food_detection())


    if content_type == "photo":
        bot.download_file(msg['photo'][0]['file_id'], 'Immagini\\Cibo.png')
        bot.sendMessage(chat_id, food_detection())

    if content_type == "text":
        if msg["text"][0] != '/':
            if not(chat_id in acquisizione_dati):
                bot.sendMessage(chat_id, rispondimi(msg["text"]))
            else:
                new_user(msg,chat_id)

        elif msg["text"].lower() == "/info":
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Informazioni", callback_data="info")],
                [InlineKeyboardButton(text="Contatta uno sviluppatore", callback_data="developer"),
                 InlineKeyboardButton(text="Versione", callback_data="version")]
            ])
            bot.sendMessage(chat_id, "Selezionare uno dei tre comandi disponibili", reply_markup=keyboard)

        elif msg["text"].lower() == "/help":
            bot.sendMessage(chat_id, "Here is the list of available commands: \n\n"
                                     "/info - shows information about the software\n"
                                     "/help - shows the commands list \n"
                                     "/new - acquires information about the user\n"
                                     "/user - show user \n")

        elif msg["text"].lower() == "/new":
            bot.sendMessage(chat_id, "Answer the next questions to record your personal information.\n Qual è il tuo nome?")
            acquisizione_dati[chat_id] = stato_conversazione["Nome"]
            utenti[chat_id] = Utente(chat_id)

        elif msg["text"].lower() == "/start":
            bot.sendMessage(chat_id, "Ciao, Sono il tuo FoodHelper! Puoi mandarmi le foto di quello "
                                     "che mangi per sapere  will reccomand you or not to eat it. Write /help for more information."
                                     "\n\nIt looks like you're an unregistered user. "
                                     "Please first reply next questions.")

        elif msg["text"].lower() == "/user":
            show_user(msg)

        else:
            bot.sendMessage(chat_id, "Spiacente, non riconosco questo comando.\nPer la lista dei comandi digitare il comando /help.")


def new_user(msg, chat_id):
    if acquisizione_dati[chat_id] == stato_conversazione["Nome"]:
        utenti[chat_id].set_nome(msg["text"])
        bot.sendMessage(chat_id, "Qual è il tuo cognome?")
        acquisizione_dati[chat_id] = stato_conversazione["Cognome"]

    elif acquisizione_dati[chat_id] == stato_conversazione["Cognome"]:
        utenti[chat_id].set_cognome(msg["text"])
        bot.sendMessage(chat_id, "Sei maschio o femmina?")
        acquisizione_dati[chat_id] = stato_conversazione["Sesso"]

    elif acquisizione_dati[chat_id] == stato_conversazione["Sesso"]:
        utenti[chat_id].set_sesso(msg["text"])
        bot.sendMessage(chat_id, "Qual è la tua data di nascita?")
        acquisizione_dati[chat_id] = stato_conversazione["Eta"]

    elif acquisizione_dati[chat_id] == stato_conversazione["Eta"]:
        utenti[chat_id].set_data(msg["text"])
        bot.sendMessage(chat_id, "Quanto sei alto?")
        acquisizione_dati[chat_id] = stato_conversazione["Altezza"]

    elif acquisizione_dati[chat_id] == stato_conversazione["Altezza"]:
        utenti[chat_id].set_altezza(msg["text"])
        bot.sendMessage(chat_id, "Quanto pesi?")
        acquisizione_dati[chat_id] = stato_conversazione["Peso"]

    elif acquisizione_dati[chat_id] == stato_conversazione["Peso"]:
        utenti[chat_id].set_peso(msg["text"])
        bot.sendMessage(chat_id, "Grazie per averci fornito dei tuoi dati!")
        acquisizione_dati.pop(chat_id)

def show_user(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    bot.sendMessage(chat_id, "Your personal info:\n\n" + str(utenti[chat_id]))


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor="callback_query")
    if query_data == "info":
        bot.answerCallbackQuery(query_id, "Version Beta 1.0")
        bot.sendMessage(from_id, "Questo bot si occupa di trovare alcune informazioni meteo su una determinata città.\n"
                                 "Basterà digitare il nome della città per avere i risultati relativa ad essa.")
    elif query_data == "developer":
        bot.answerCallbackQuery(query_id)
        bot.sendMessage(from_id, "Per aiutarci a migliorare o per maggiori informazioni contattare: "
                                 "antoniofrancescofiore98@gmail.com")
    elif query_data == "version":
        bot.answerCallbackQuery(query_id, "Version Beta 1.0")


telepot.loop.MessageLoop(bot, {"chat": on_chat_message, "callback_query": on_callback_query}).run_as_thread()

while True:
    time.sleep(2)
