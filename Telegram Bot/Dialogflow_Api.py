"""Install the following requirements:
    dialogflow        0.5.1
    google-api-core   1.4.1
"""
import os
import dialogflow
from google.api_core.exceptions import InvalidArgument
DIALOGFLOW_PROJECT_ID = 'newagent-qwujpw'
DIALOGFLOW_LANGUAGE_CODE = 'en'
GOOGLE_APPLICATION_CREDENTIALS = r'API_key\\Dialogflow_key.json'
SESSION_ID = 'current-user-id'

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'API_key\\Dialogflow_key.json'
session_client = dialogflow.SessionsClient()
def rispondimi(testo):
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=testo, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise
    print("Query text:", response.query_result.query_text)
    print("Detected intent:", response.query_result.intent.display_name)
    print("Detected intent confidence:", response.query_result.intent_detection_confidence)
    print("Fulfillment text:", response.query_result.fulfillment_text)

    if response.query_result.fulfillment_text == "":
        return "Al momento non sono in grado di risponderti"
    else:
        return str(response.query_result.fulfillment_text)
