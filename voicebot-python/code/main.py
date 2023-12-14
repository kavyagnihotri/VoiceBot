import azure.cognitiveservices.speech as speechsdk
from constants import *
from keys import *
from helper import *
from clu_model import *

def main():
    welcome_msg = "Please choose a language. Say STOP to exit."
    synthesize_text(welcome_msg, TTS_ENGLISH, SPEECH_KEY, SPEECH_REGION)

    # get user input
    response = recognize_from_microphone(STT_ENGLISH, SPEECH_KEY, SPEECH_REGION).lower()

    # check if stop is there
    if 'stop' in response:
        synthesize_text("Goodbye", TTS_ENGLISH, SPEECH_KEY, SPEECH_REGION)
        return

    # get language
    stt_language = get_language(response, languages)

    # tranlator services bool
    translate = False

    # set language for conversation
    if(stt_language != STT_ENGLISH):
        translate = True
        
    ####### can put this into a while loop and check for stop keyword

    # prompt for a topic
    prompt = "What do you want to learn about?"
    if translate:
        prompt = translate_speech_language(prompt, STT_ENGLISH, stt_language, TRANSLATOR_KEY, TRANSLATOR_ENDPOINT, TRANSLATOR_REGION)
    synthesize_text(prompt, stt_to_tts[stt_language], SPEECH_KEY, SPEECH_REGION)

    # get user input
    response = recognize_from_microphone(stt_language, SPEECH_KEY, SPEECH_REGION)

    # translate to english
    if translate:
        response = translate_speech_language(response, stt_language, STT_ENGLISH, TRANSLATOR_KEY, TRANSLATOR_ENDPOINT, TRANSLATOR_REGION)

    # get topic
    response = "why is oxygen important"
    topic = get_top_topic(response, LANGUAGE_UNDERSTANDING_ENDPOINT, LANGUAGE_UNDERSTANDING_KEY, CLU_PROJECT_NAME, CLU_DEPLOYMENT_NAME).lower()
    print(topic)

    if topic is None or topic == "":
        msg = "Sorry, I didn't know understand that."
        if translate:
            msg = translate_speech_language(msg, STT_ENGLISH, stt_language, TRANSLATOR_KEY, TRANSLATOR_ENDPOINT, TRANSLATOR_REGION)
        synthesize_text(msg, stt_to_tts[stt_language], SPEECH_KEY, SPEECH_REGION)
        return

    # get audio url from mongoDB
    audio_url = get_audioURL_from_mongoDB(topic, MONGO_URI, MONDO_DB, MONGO_COLLECTION)
    print(audio_url)

    # play audio
    if audio_url is not None:
        play_azure_blob_audio(audio_url)
    else:
        msg = "Sorry, I don't know about that topic"
        if translate:
            msg = translate_speech_language(msg, STT_ENGLISH, stt_language, TRANSLATOR_KEY, TRANSLATOR_ENDPOINT, TRANSLATOR_REGION)
        synthesize_text(msg, stt_to_tts[stt_language], SPEECH_KEY, SPEECH_REGION)
    ##########

    return

if __name__ == "__main__":
    main()
