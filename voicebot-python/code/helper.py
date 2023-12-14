import azure.cognitiveservices.speech as speechsdk
import requests
import io
import pymongo
from constants import *
from pydub import AudioSegment
from pydub.playback import play
from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem
from azure.core.exceptions import HttpResponseError


def recognize_from_microphone(speech_language, speech_key, speech_region):
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
    speech_config.speech_recognition_language=speech_language

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
    return speech_recognition_result.text


def translate_speech_language(text, speech_language, output_language, translator_key, translator_endpoint, translator_region):
    key = translator_key
    endpoint = translator_endpoint
    region = translator_region

    credential = TranslatorCredential(key, region)
    text_translator = TextTranslationClient(endpoint=endpoint, credential=credential)

    try:
        source_language = speech_language
        target_language = output_language.split("-")[0]
        input_text_elements = [ InputTextItem(text = text) ]

        response = text_translator.translate(content = input_text_elements, to = target_language, from_parameter = source_language)
        translation = response[0] if response else None

        if translation:
            for translated_text in translation.translations:
                print(f"Text was translated to: '{translated_text.to}' and the result is: '{translated_text.text}'.")
                return translated_text.text

    except HttpResponseError as exception:
        print(f"Error Code: {exception.error.code}")
        print(f"Message: {exception.error.message}")


def synthesize_text(text, voice, speech_key, speech_region):
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name=voice

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # Get text from the console and synthesize to the default speaker.
    # print("Enter some text that you want to speak >")
    # text = input()

    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        # print("Speech synthesized for text [{}]".format(text))
        print(f"{text}")
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")



def get_audioURL_from_mongoDB(topic, mongo_uri, mongo_db, mongo_collection):
    client = pymongo.MongoClient(mongo_uri)
    db = client[mongo_db]
    collection = db[mongo_collection]

    document = collection.find_one({"name": topic})
    if document:
        print(document)
        return document.get('url')
    else:
        return None


def play_azure_blob_audio(audio_url):
    try:
        response = requests.get(audio_url)
        audio_data = response.content
        audio = AudioSegment.from_file(io.BytesIO(audio_data))
        play(audio)
    except Exception as e:
        print(f"Error: {e}")


def get_language(query, languages):
    for language in languages:
        if language in query:
            return languages[language]
    return STT_HINDI


# def recognize_from_microphone_and_translate(speech_language, output_language, speech_key, speech_region):
#     speech_translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=speech_key, region=speech_region)
#     speech_translation_config.speech_recognition_language=speech_language

#     target_language=output_language.split("-")[0]
#     speech_translation_config.add_target_language(target_language)

#     audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
#     translation_recognizer = speechsdk.translation.TranslationRecognizer(translation_config=speech_translation_config, audio_config=audio_config)

#     print("Speak into your microphone.")
#     translation_recognition_result = translation_recognizer.recognize_once_async().get()

#     if translation_recognition_result.reason == speechsdk.ResultReason.TranslatedSpeech:
#         print("Recognized: {}".format(translation_recognition_result.text))
#         print("""Translated into '{}': {}""".format(
#             target_language, 
#             translation_recognition_result.translations[target_language]))
#     elif translation_recognition_result.reason == speechsdk.ResultReason.NoMatch:
#         print("No speech could be recognized: {}".format(translation_recognition_result.no_match_details))
#     elif translation_recognition_result.reason == speechsdk.ResultReason.Canceled:
#         cancellation_details = translation_recognition_result.cancellation_details
#         print("Speech Recognition canceled: {}".format(cancellation_details.reason))
#         if cancellation_details.reason == speechsdk.CancellationReason.Error:
#             print("Error details: {}".format(cancellation_details.error_details))
#             print("Did you set the speech resource key and region values?")