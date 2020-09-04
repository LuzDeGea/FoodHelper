from Dialogflow_Api import rispondimi
from collegamentoSito import inserisci_utente
from Nutrition import get_food, traduzione
import re

"""
controllo_intent(query_result, utente)--> text_respose
prende il risultato della query e lo confronta con i possibili intenti, 
se l'intento risulta essere "cibo", si andrà nella sezione di rilevazione  cibo,
altrimenti si passa al controllo sulla modifica dei dati dell'utente.
in caso non ci sia una intento adatto oppure alcun intento, si riceverà
la risposta negativa.
"""
def controllo_intent(query_result, utente):
    intent = query_result.intent.display_name
    text = query_result.fulfillment_text
    if intent == "Cibo":
        return rilevazione_cibo(utente, query_result)
    if utente:
        if intent == "Saluto":
            return text + " " + utente.get_nome()
        if intent == "Fame":
            return controllo_fame(utente, text)
        if intent == "Modifica_nome":
            return modifica_nome(utente, query_result)
        elif intent == "Modifica_peso":
            return modifica_peso(utente, query_result)
        elif intent == "Modifica_altezza":
            return modifica_altezza(utente, query_result)
        elif intent == "Modifica_sesso":
            return modifica_sesso(utente, query_result)
        elif intent == "Modifica_data":
            return modifica_data(utente, query_result)
        elif intent == "Modifica_attività":
            return modifica_attività(utente, query_result)
        if text == "":
            return "Al momento non sono in grado di risponderti."
    return text

"""
controllo_fame(utente, text)--> text_respose
prende un utente e le sue patologie, ed eleabora la risposta 
da dare all'utente in merito alla possibilità di mangiare oppure 
no un determinato cibo.
"""
def controllo_fame(utente, text):
    if utente.get_anemia_sideropenica():
        return rispondimi("spuntino ferro").fulfillment_text
    if utente.get_iper_tens():
        return rispondimi("spuntino ipertensione").fulfillment_text
    if utente.get_nefropatia():
        return rispondimi("spuntino nefropatia").fulfillment_text
    else:
        return text

def modifica_nome(utente, result):
    try:
        nome = result.parameters.fields["given-name"].string_value
    except KeyError:
        return "Inserisci correttamente il peso, ad esempio '70kg'."

    if nome == "":
        return "Inserisci correttamente il tuo primo nome"

    utente.set_nome(nome)
    inserisci_utente(utente)
    return result.fulfillment_text

def modifica_peso(utente, result):
    try:
        unit = result.parameters.fields["unit-weight"].struct_value.fields["unit"].string_value
        amount = result.parameters.fields["unit-weight"].struct_value.fields["amount"].number_value
    except KeyError:
        return "Inserisci correttamente il peso, ad esempio '70kg'."

    if not unit == "kg":
        return "Ti preghiamo di inserire il peso in kg."

    if 39 < amount < 201:
        utente.set_peso(amount)
        inserisci_utente(utente)
        return result.fulfillment_text
    else:
        return "Inserisci il tuo peso corretto."

def modifica_altezza(utente, result):
    try:
        unit = result.parameters.fields["unit-length"].struct_value.fields["unit"].string_value
        amount = result.parameters.fields["unit-length"].struct_value.fields["amount"].number_value
    except KeyError:
        return "Inserisci correttamente la tua altezza, ad esempio '180cm'."

    if unit == "cm":
        if 109 < amount < 231:
            utente.set_altezza(amount)
            inserisci_utente(utente)
            return result.fulfillment_text
        else:
            return "Inserisci la tua altezza corretta."

    elif unit == "m":
        if 1.09 < amount < 2.31:
            utente.set_altezza(amount)
            inserisci_utente(utente)
            return result.fulfillment_text
        else:
            return "Inserisci la tua altezza corretta."

    else:
        return "Inserisci la tua altezza in cm o in m."

def modifica_sesso(utente, result):
    try:
        sesso = result.parameters.fields["sesso"].string_value
    except KeyError:
        return "Inserisci correttamente il tuo sesso, ad esempio 'maschio'."

    utente.set_sesso(sesso)
    inserisci_utente(utente)
    return result.fulfillment_text

def modifica_data(utente, result):
    try:
        data = result.parameters.fields["date"].string_value
    except KeyError:
        return "Inserire correttamente la data."

    if data == "":
        return "Inserire correttamente la data, ad esempio: '01/01/90'"
    else:
        data = re.split("T", data)[0]
        utente.set_data(data)
        inserisci_utente(utente)
        return result.fulfillment_text + " " + str(utente.get_eta()) + " anni."

def modifica_attività(utente, result):
    try:
        attivita = result.parameters.fields["attivita"].string_value
    except KeyError:
        return "Inserire correttamente la data."

    if attivita == "":
        return "Inserisci correttamente l'attività tra queste: 'Sedentaria', 'Leggera', 'Moderata', 'Attiva' " \
               "o 'Molto attiva'."
    else:
        utente.set_attivita(attivita)
        inserisci_utente(utente)
        return result.fulfillment_text

"""
rilevazione_cibo(utente, result)--> respose
identifica se l'intento dell'utente è parlare di cibo, se è così restituisce il risultato, 
altrimenti restituisce stringhe di risposta negative sulla scorretta rilevazione del cibo.
"""
def rilevazione_cibo(utente, result):
    try:
        cibo = list(result.parameters.fields["Cibo"].struct_value.fields.values())[0].string_value
        #print(list((result.parameters.fields["Cibo"].struct_value.fields.keys()))[0])  #STAMPA LA CATEGORIA
    except IndexError:
        cibo = result.parameters.fields["Cibo"].string_value

    if cibo == "":
        return "Spiacente, non abbiamo informazione relative a questo cibo."

    food = get_food(cibo)
    if not food:
        food = get_food(traduzione(cibo))
        if not food:
            return "Il cibo non è stato riconosciuto correttamente."
    if utente:
            return str(food) + "\n\n" + utente.can_eat(food)
    else:
        return str(food)
