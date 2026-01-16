import streamlit as st
from google.cloud import dialogflow_v2 as dialogflow
import uuid
import os

# Set credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_account_key.json"

PROJECT_ID = "79efbf25-ec4c-488c-88a4-e3c5f3b4dfd0"
SESSION_ID = str(uuid.uuid4())

def detect_intent(text):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(PROJECT_ID, SESSION_ID)

    text_input = dialogflow.TextInput(text=text, language_code="en")
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    return response.query_result.fulfillment_text

st.title("🤖 Customer Support Chatbot")

user_input = st.text_input("You:")

if user_input:
    reply = detect_intent(user_input)
    st.text_area("Bot:", value=reply, height=100)
