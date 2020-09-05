import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardButton, InlineKeyboardMarkup
from Food_detection import food_detection
from Dialogflow_Api import rispondimi
from Controllo_intenti import controllo_intent
from Utente import Utente, controllo_nome, controllo_formato_data, controllo_altezza, controllo_peso
import time
from Nutrition import get_food, traduzione
from collegamentoSito import inserisci_utente, get_utente, esiste_utente


#Token di collegamento per il bot telegram
TOKEN = "1130648366:AAEPXCisGv8B2Hby_3xuK9ATwMwGKqjPEn8"
#Collegamento al bot tramite token
bot = telepot.Bot(TOKEN)

"""
Stato conversazione serve a conservare a che punto della registrazione utente 
ci si è fermati per avere un punto di ripresa al ritorno sul bot.
"""
stato_conversazione = {"Nome" : 0,"Sesso" : 2,"Eta" : 3,"Altezza" : 4,"Peso" : 5, "Attività" : 6,"Diabete" : 7, "Colesterolo" : 8,"Iper_tens" : 9, "Ipo_tens" : 10,"Nefropatia" : 11,"Anemia_sideropenica" : 12}
utenti = {}
acquisizione_dati = {}

"""
on_chat_message(msg)--> respose
La funzione prende il messaggio dell'utente e come prima cosa identifica il content_type,
in caso il tipo risulti come documento, immagine oppure come stringa (contenete nome di cibo), 
si rimanda alla funzione di risposta per cibo.
Se il tipo corrisponde a testo (e inizia con "/")corrisponderà ad un comando, e si passa
alla sotto-gestione dei comandi.
Se il tipo corrisponde a testo (non cibo, e non comando) ci si rimanda alle risposte 
gestite ed elaborate da DialogFlow. 
"""
def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == "document" or content_type == "photo":
        if content_type == "photo":
            bot.download_file(msg['photo'][0]['file_id'], 'Immagini\\Cibo.png')
        else:
            bot.download_file(msg['document']['file_id'], 'Immagini\\Cibo.png')
        food = food_detection()
        if not food:
            bot.sendMessage(chat_id, "Il cibo non è stato riconosciuto correttamente")
        else:
            bot.sendMessage(chat_id, "Il cibo riconosciuto è: " + str(food))
            if esiste_utente(chat_id):
                bot.sendMessage(chat_id, get_utente(chat_id).can_eat(food))

    elif content_type == "text":
        if msg["text"][0] != '/':
            if not(chat_id in acquisizione_dati):
                bot.sendMessage(chat_id, controllo_intent(rispondimi(msg["text"]), get_utente(chat_id)))
            else:
                new_user(msg, chat_id)


        elif msg["text"].lower() == "/info":
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Informazioni", callback_data="info")],
                [InlineKeyboardButton(text="Contatta uno sviluppatore", callback_data="developer"),
                 InlineKeyboardButton(text="Versione", callback_data="version")]
            ])
            bot.sendMessage(chat_id, "Selezionare uno dei tre comandi disponibili", reply_markup=keyboard)

        elif msg["text"].lower() == "/help":
            bot.sendMessage(chat_id, "Questa è la lista dei comandi disponibili: \n\n"
                                     "/info - mostra le informazioni del bot\n"
                                     "/help - mostra la lista dei comandi \n"
                                     "/new - registrare un nuovo utente\n"
                                     "/user - mostra l'utente \n")

        elif msg["text"].lower() == "/new":
            bot.sendMessage(chat_id, "Ora ti verranno poste alcune domande per la profilazione.\nQual è il tuo nome?")
            acquisizione_dati[chat_id] = stato_conversazione["Nome"]
            utenti[chat_id] = Utente(chat_id)

        elif msg["text"].lower() == "/start":
            bot.sendMessage(chat_id, "Ciao, Sono il tuo FoodHelper! \nPuoi mandarmi le foto di quello "
                                     "che mangi per sapere  se puoi mangiarlo oppure no.\n scrivi /help per altre informazioni."
                                     "\n\nUtilizza /new per registrarti come nuovo utente.")

        elif msg["text"].lower() == "/user":
            show_user(chat_id)

        else:
            bot.sendMessage(chat_id, "Spiacente, non riconosco questo comando.\nPer la lista dei comandi digitare il comando /help.")

    else:
        bot.sendMessage(chat_id,"Questo formato non è supportato.")

"""
new_user(msg, chat_id)-->user
Gestisce la registrazione per l'utente, riferendosi allo stato di avanzamento corrente, rifacenddosi a 
stato_conversazione, e modificando i dati inviati dall'utente.
lo stato di avanzamento viene aggiornato solo dopo la fine dello stato attuale.
"""
def new_user(msg, chat_id):
    if acquisizione_dati[chat_id] == stato_conversazione["Nome"]:
        nome = controllo_nome(msg["text"])
        if nome == False:
            bot.sendMessage(chat_id, "Per favore inserisci correttamente il nome.")
        else:
            utenti[chat_id].set_nome(nome)
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Maschio", callback_data="sesso_maschio"),
                 InlineKeyboardButton(text="Femmina", callback_data="sesso_femmina")]
            ])
            bot.sendMessage(chat_id, "Sei maschio o femmina?", reply_markup=keyboard)
            acquisizione_dati[chat_id] = stato_conversazione["Sesso"]

    elif acquisizione_dati[chat_id] == stato_conversazione["Sesso"]:
        bot.sendMessage(chat_id, "Qual è la tua data di nascita?")
        acquisizione_dati[chat_id] = stato_conversazione["Eta"]

    elif acquisizione_dati[chat_id] == stato_conversazione["Eta"]:
        data = controllo_formato_data(msg["text"])
        if data == False:
            bot.sendMessage(chat_id, "Inserisci la data correttamente nel formato gg/mm/aaaa.")
        else:
            utenti[chat_id].set_data(data)
            bot.sendMessage(chat_id, "Quanto sei alto?")
            acquisizione_dati[chat_id] = stato_conversazione["Altezza"]

    elif acquisizione_dati[chat_id] == stato_conversazione["Altezza"]:
        altezza = controllo_altezza(msg["text"])
        if altezza == False:
            bot.sendMessage(chat_id, "Per favore inserisci correttamente l'altezza in cm.")
        else:
            utenti[chat_id].set_altezza(altezza)
            bot.sendMessage(chat_id, "Quanto pesi?")
            acquisizione_dati[chat_id] = stato_conversazione["Peso"]

    elif acquisizione_dati[chat_id] == stato_conversazione["Peso"]:
        peso = controllo_peso(msg["text"])
        if peso == False:
            bot.sendMessage(chat_id, "Per favore inserisci correttamente il peso in kg.")
        else:
            utenti[chat_id].set_peso(peso)
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Sedentaria", callback_data="att_sedentaria"),
                 InlineKeyboardButton(text="Leggera", callback_data="att_leggera"),
                 InlineKeyboardButton(text="Moderata", callback_data="att_moderata")],
                [InlineKeyboardButton(text="Attiva", callback_data="att_attiva"),
                 InlineKeyboardButton(text="Molto attiva", callback_data="att_strong")]
            ])
            bot.sendMessage(chat_id, "Descrivi il tuo livello di attività fisica: \n"\
                                     "Sedentaria  -  Lavoro da scrivania e non si pratica sport \n"\
                                     "Leggera  -  Lavoro da scrivania + sport 2, 3 volte la settimana \n"\
                                     "Moderata  -  Lavoro leggero + sport 3, 5 volte la settimana \n"\
                                     "Attiva  -  Lavoro di tipo pesante \n"\
                                     "Molto attiva  -  Lavoro pesante + sport 2, 3 volte la settimana",
                            reply_markup=keyboard)
            acquisizione_dati[chat_id] = stato_conversazione["Attività"]

    elif acquisizione_dati[chat_id] == stato_conversazione["Attività"]:
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Si", callback_data="iper_tens_si"),
                InlineKeyboardButton(text="No", callback_data="iper_tens_no")]
            ])
            bot.sendMessage(chat_id, "Hai l'iper-tensione?", reply_markup=keyboard)
            acquisizione_dati[chat_id] = stato_conversazione["Iper_tens"]
            '''
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Si", callback_data="diabete_si"),
                 InlineKeyboardButton(text="No", callback_data="diabete_no")]
            ])
            bot.sendMessage(chat_id, "Sei diabetico?", reply_markup=keyboard)
            acquisizione_dati[chat_id] = stato_conversazione["Diabete"]
            '''
    elif acquisizione_dati[chat_id] == stato_conversazione["Diabete"]:
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Si", callback_data="colesterolo_si"),
                 InlineKeyboardButton(text="No", callback_data="colesterolo_no")]
            ])
            bot.sendMessage(chat_id, "Hai il colesterolo?", reply_markup=keyboard)
            acquisizione_dati[chat_id] = stato_conversazione["Colesterolo"]

    elif acquisizione_dati[chat_id] == stato_conversazione["Colesterolo"]:
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Si", callback_data="iper_tens_si"),
                 InlineKeyboardButton(text="No", callback_data="iper_tens_no")]
            ])
            bot.sendMessage(chat_id, "Hai l'iper-tensione?", reply_markup=keyboard)
            acquisizione_dati[chat_id] = stato_conversazione["Iper_tens"]

    elif acquisizione_dati[chat_id] == stato_conversazione["Iper_tens"]:
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Si", callback_data="Nefropatia_si"),
                InlineKeyboardButton(text="No", callback_data="Nefropatia_no")]
            ])
            bot.sendMessage(chat_id, "Hai la Nefropatia?", reply_markup=keyboard)
            acquisizione_dati[chat_id] = stato_conversazione["Nefropatia"]
            '''
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Si", callback_data="ipo_tens_si"),
                 InlineKeyboardButton(text="No", callback_data="ipo_tens_no")]
            ])
            bot.sendMessage(chat_id, "Hai l'ipo-tensione?", reply_markup=keyboard)
            acquisizione_dati[chat_id] = stato_conversazione["Ipo_tens"]
            '''
    elif acquisizione_dati[chat_id] == stato_conversazione["Ipo_tens"]:
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Si", callback_data="Nefropatia_si"),
                 InlineKeyboardButton(text="No", callback_data="Nefropatia_no")]
            ])
            bot.sendMessage(chat_id, "Hai la Nefropatia?", reply_markup=keyboard)
            acquisizione_dati[chat_id] = stato_conversazione["Nefropatia"]

    elif acquisizione_dati[chat_id] == stato_conversazione["Nefropatia"]:
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Si", callback_data="Anemia_sideropenica_si"),
                 InlineKeyboardButton(text="No", callback_data="Anemia_sideropenica_no")]
            ])
            bot.sendMessage(chat_id, "Hai l'Anemia_sideropenica?", reply_markup=keyboard)
            acquisizione_dati[chat_id] = stato_conversazione["Anemia_sideropenica"]

    elif acquisizione_dati[chat_id] == stato_conversazione["Anemia_sideropenica"]:
            bot.sendMessage(chat_id, "Grazie per averci fornito dei tuoi dati!")
            acquisizione_dati.pop(chat_id)
            inserisci_utente(utenti.pop(chat_id))

"""
show_user(chat_id)-->Text
Mostra le informazioni dell'utente leggendole dal DataBase, se l'utente
non è registrato, restituisce un messaggio di richiesta di registrazione.
"""
def show_user(chat_id):
    info = get_utente(chat_id)
    if info:
        bot.sendMessage(chat_id, "Your personal info:\n\n" + str(info))
    else:
        bot.sendMessage(chat_id, "Non sei ancora registrato, usa /new per registrarti \n")

"""
Gestisce l'evento alla pressione dei pulsanti o all'uso dei comandi.
"""
def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor="callback_query")
    if query_data == "info":
        bot.answerCallbackQuery(query_id, "Version Beta 1.0")
        bot.sendMessage(from_id, "Questo bot si occupa di trovare alcune informazioni meteo su una determinata città.\n"
                                 "Basterà digitare il nome della città per avere i risultati relativa ad essa.")
    elif query_data == "developer":
        bot.answerCallbackQuery(query_id)
        bot.sendMessage(from_id, "Per aiutarci a migliorare o per maggiori informazioni contattare: "
                                 "antoniofrancescofiore98@gmail.com"
                                 "vinci19997@gmail.com"
                                 "antoniogrisulli23@gamil.com")
    elif query_data == "version":
        bot.answerCallbackQuery(query_id, "Version Beta 1.0")

    elif query_data == "sesso_maschio":
        bot.answerCallbackQuery(query_id)
        utenti[from_id].set_sesso("Maschio")
        new_user(msg, from_id)

    elif query_data == "sesso_femmina":
        bot.answerCallbackQuery(query_id)
        utenti[from_id].set_sesso("Femmina")
        new_user(msg, from_id)

    elif query_data == "att_sedentaria":
        bot.answerCallbackQuery(query_id)
        utenti[from_id].set_attivita("Sedentaria")
        new_user(msg, from_id)

    elif query_data == "att_leggera":
        bot.answerCallbackQuery(query_id)
        utenti[from_id].set_attivita("Leggera")
        new_user(msg, from_id)

    elif query_data == "att_moderata":
        bot.answerCallbackQuery(query_id)
        utenti[from_id].set_attivita("Moderata")
        new_user(msg, from_id)

    elif query_data == "att_attiva":
        bot.answerCallbackQuery(query_id)
        utenti[from_id].set_attivita("Attiva")
        new_user(msg, from_id)

    elif query_data == "att_strong":
        bot.answerCallbackQuery(query_id)
        utenti[from_id].set_attivita("Molto attiva")
        new_user(msg, from_id)

    elif query_data == "diabete_si":
        bot.answerCallbackQuery(query_id)
        utenti[from_id].set_diabete(True)
        new_user(msg, from_id)

    elif query_data == "diabete_no":
        bot.answerCallbackQuery(query_id)
        utenti[from_id].set_diabete(False)
        new_user(msg, from_id)

    elif query_data == "colesterolo_si":
        bot.answerCallbackQuery(query_id)
        utenti[from_id].set_colesterolo(True)
        new_user(msg, from_id)

    elif query_data == "colesterolo_no":
        bot.answerCallbackQuery(query_id)
        utenti[from_id].set_colesterolo(False)
        new_user(msg, from_id)

    elif query_data == "iper_tens_si":
        bot.answerCallbackQuery(query_id)
        utenti[from_id].set_iper_tens(True)
        new_user(msg, from_id)

    elif query_data == "iper_tens_no":
        bot.answerCallbackQuery(query_id)
        utenti[from_id].set_iper_tens(False)
        new_user(msg, from_id)

    elif query_data == "ipo_tens_si":
        bot.answerCallbackQuery(query_id)
        utenti[from_id].set_ipo_tens(True)
        new_user(msg, from_id)

    elif query_data == "ipo_tens_no":
        bot.answerCallbackQuery(query_id)
        utenti[from_id].set_ipo_tens(False)
        new_user(msg, from_id)

    elif query_data == "Nefropatia_si":
        bot.answerCallbackQuery(query_id)
        utenti[from_id].set_nefropatia(True)
        new_user(msg, from_id)

    elif query_data == "Nefropatia_no":
        bot.answerCallbackQuery(query_id)
        utenti[from_id].set_nefropatia(False)
        new_user(msg, from_id)

    elif query_data == "Anemia_sideropenica_si":
        bot.answerCallbackQuery(query_id)
        utenti[from_id].set_anemia_sideropenica(True)
        new_user(msg, from_id)

    elif query_data == "Anemia_sideropenica_no":
        bot.answerCallbackQuery(query_id)
        utenti[from_id].set_anemia_sideropenica(False)
        new_user(msg, from_id)



telepot.loop.MessageLoop(bot, {"chat": on_chat_message, "callback_query": on_callback_query}).run_as_thread()

while True:
    time.sleep(2)
