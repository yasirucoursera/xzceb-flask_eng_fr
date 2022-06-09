
"""translator module"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """English to french translation"""
    #write the code here
    model_id='en-fr'
    french_text=language_translator.translate(
        text=english_text,
        model_id=model_id).get_result()
    return french_text["translations"][0]["translation"]

def french_to_english(french_text):
    """French to English translation"""
    #write the code here
    model_id='fr-en'
    english_text=language_translator.translate(
        text=french_text,
        model_id=model_id).get_result()
    return english_text["translations"][0]["translation"]
    