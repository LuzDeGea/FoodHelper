import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardButton, InlineKeyboardMarkup
import time

TOKEN = "1130648366:AAEPXCisGv8B2Hby_3xuK9ATwMwGKqjPEn8"

bot = telepot.Bot(TOKEN)


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == "text":

        if msg["text"].lower() == "/info":
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
            bot.sendMessage(chat_id, "Answer the next questions to record your personal information.")
            new_user(msg)

        elif msg["text"].lower() == "/start":
            bot.sendMessage(chat_id, "Hi, I'm FoodHelper! You can send me a photo or write me a name of a dish and I"
                                     " will reccomand you or not to eat it. Write /help for more information."
                                     "\n\nIt looks like you're an unregistered user. "
                                     "Please first reply next questions.")
            new_user(msg)

        elif msg["text"].lower() == "/user":
            show_user(msg)


def new_user(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    bot.sendMessage(chat_id, "\n\nHow old are you?")


def show_user(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    bot.sendMessage(chat_id, "Your personal info:\n\n")


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
