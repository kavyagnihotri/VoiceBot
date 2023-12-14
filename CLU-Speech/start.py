import azure.cognitiveservices.speech as speechsdk
import os

# make these environment variables
SPEECH_KEY = "3f1363212b944feb953bfe0038c13d1b"
SPEECH_REGION = "eastus"

ENGLISH = "en-US"
HINDI = "hi-IN"

def recognize_from_microphone(speech_language):
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    # speech_config = speechsdk.SpeechConfig(subscription=os.environ.get(SPEECH_KEY), region=os.environ.get(SPEECH_REGION))
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
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

recognize_from_microphone(ENGLISH)
recognize_from_microphone(HINDI)

def recognize_from_microphone_and_translate(speech_language, output_language):
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    speech_translation_config.speech_recognition_language=speech_language

    target_language=output_language.split("-")[0]
    speech_translation_config.add_target_language(target_language)

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    translation_recognizer = speechsdk.translation.TranslationRecognizer(translation_config=speech_translation_config, audio_config=audio_config)

    print("Speak into your microphone.")
    translation_recognition_result = translation_recognizer.recognize_once_async().get()

    if translation_recognition_result.reason == speechsdk.ResultReason.TranslatedSpeech:
        print("Recognized: {}".format(translation_recognition_result.text))
        print("""Translated into '{}': {}""".format(
            target_language, 
            translation_recognition_result.translations[target_language]))
    elif translation_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(translation_recognition_result.no_match_details))
    elif translation_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = translation_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")

recognize_from_microphone_and_translate(ENGLISH, HINDI)


def synthesize_text(text, voice):
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name=voice

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # Get text from the console and synthesize to the default speaker.
    # print("Enter some text that you want to speak >")
    # text = input()

    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(text))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")


text = "Tell me about ducks"
voice = "en-US-AriaNeural"
synthesize_text(text, voice)

text = "मुझे बत्तखों के बारे में बताएं"
voice = "hi-IN-SwaraNeural"
synthesize_text(text, voice)

LANGUAGE_UNDERSTANDING_KEY = "5ee64c53ab2741709cb76937ca7ea778"
LANGUAGE_UNDERSTANDING_SUBSCRIPTION = "0d62ad5b-0f80-4cde-a734-4f060c0ab9b0"
LANGUAGE_UNDERSTANDING_ENDPOINT = "https://first-instance-0.cognitiveservices.azure.com/"
LANGUAGE_UNDERSTANDING_REGION = "eastus"
AZURE_CONVERSATIONS_PROJECT_NAME = "audio-box"
AZURE_CONVERSATIONS_DEPLOYMENT_NAME = "initial-deploy"

"""
FILE: sample_analyze_conversation_app.py

DESCRIPTION:
    This sample demonstrates how to analyze user query for intents and entities using
    a conversation project with a language parameter.

    For more info about how to setup a CLU conversation project, see the README.

USAGE:
    python sample_analyze_conversation_app.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_CONVERSATIONS_ENDPOINT                       - endpoint for your CLU resource.
    2) AZURE_CONVERSATIONS_KEY                            - API key for your CLU resource.
    3) AZURE_CONVERSATIONS_PROJECT_NAME     - project name for your CLU conversations project.
    4) AZURE_CONVERSATIONS_DEPLOYMENT_NAME  - deployment name for your CLU conversations project.
"""

def sample_analyze_conversation_app(query):
    # [START analyze_conversation_app]
    # import libraries
    import os
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.language.conversations import ConversationAnalysisClient

    # get secrets
    clu_endpoint = LANGUAGE_UNDERSTANDING_ENDPOINT
    clu_key = LANGUAGE_UNDERSTANDING_KEY
    project_name = AZURE_CONVERSATIONS_PROJECT_NAME
    deployment_name = AZURE_CONVERSATIONS_DEPLOYMENT_NAME

    # analyze quey
    client = ConversationAnalysisClient(clu_endpoint, AzureKeyCredential(clu_key))
    with client:
        result = client.analyze_conversation(
            task={
                "kind": "Conversation",
                "analysisInput": {
                    "conversationItem": {
                        "participantId": "1",
                        "id": "1",
                        "modality": "text",
                        "language": "en",
                        "text": query
                    },
                    "isLoggingEnabled": False
                },
                "parameters": {
                    "projectName": project_name,
                    "deploymentName": deployment_name,
                    "verbose": True
                }
            }
        )

    # view result
    print(f"query: {result['result']['query']}")
    print(f"project kind: {result['result']['prediction']['projectKind']}\n")

    print(f"top intent: {result['result']['prediction']['topIntent']}")
    print(f"category: {result['result']['prediction']['intents'][0]['category']}")
    print(f"confidence score: {result['result']['prediction']['intents'][0]['confidenceScore']}\n")

    print("entities:")
    for entity in result['result']['prediction']['entities']:
        print(f"\ncategory: {entity['category']}")
        print(f"text: {entity['text']}")
        print(f"confidence score: {entity['confidenceScore']}")
        if "resolutions" in entity:
            print("resolutions")
            for resolution in entity['resolutions']:
                print(f"kind: {resolution['resolutionKind']}")
                print(f"value: {resolution['value']}")
        if "extraInformation" in entity:
            print("extra info")
            for data in entity['extraInformation']:
                print(f"kind: {data['extraInformationKind']}")
                if data['extraInformationKind'] == "ListKey":
                    print(f"key: {data['key']}")
                if data['extraInformationKind'] == "EntitySubtype":
                    print(f"value: {data['value']}")

    # [END analyze_conversation_app]



query = "I want to know about digestion"
sample_analyze_conversation_app(query=query)

query = "मैं पाचन के बारे में जानना चाहता हूं"
sample_analyze_conversation_app(query=query)

import time
KEYWORD_RECOGNITION_MODEL = "cc120675-5205-4df5-bcaf-1633825dedbb.table"
KEYWORD = "hey class buddy"

def speech_recognize_keyword_locally_from_microphone():
    """runs keyword spotting locally, with direct access to the result audio"""

    # Creates an instance of a keyword recognition model. Update this to
    # point to the location of your keyword recognition model.
    model = speechsdk.KeywordRecognitionModel(KEYWORD_RECOGNITION_MODEL)

    # The phrase your keyword recognition model triggers on.
    keyword = KEYWORD

    # Create a local keyword recognizer with the default microphone device for input.
    keyword_recognizer = speechsdk.KeywordRecognizer()

    done = False
    
    def recognized_cb(evt):
        # Only a keyword phrase is recognized. The result cannot be 'NoMatch'
        # and there is no timeout. The recognizer runs until a keyword phrase
        # is detected or recognition is canceled (by stop_recognition_async()
        # or due to the end of an input file or stream).
        result = evt.result
        if result.reason == speechsdk.ResultReason.RecognizedKeyword:
            print("RECOGNIZED KEYWORD: {}".format(result.text))
        nonlocal done
        done = True
        
    def canceled_cb(evt):
        result = evt.result
        if result.reason == speechsdk.ResultReason.Canceled:
            print('CANCELED: {}'.format(result.cancellation_details.reason))
        nonlocal done
        done = True

    # Connect callbacks to the events fired by the keyword recognizer.
    keyword_recognizer.recognized.connect(recognized_cb)
    keyword_recognizer.canceled.connect(canceled_cb)

    # Start keyword recognition.
    result_future = keyword_recognizer.recognize_once_async(model)
    print('Say something starting with "{}" followed by whatever you want...'.format(keyword))
    result = result_future.get()

    # Read result audio (incl. the keyword).
    if result.reason == speechsdk.ResultReason.RecognizedKeyword:
        time.sleep(2) # give some time so the stream is filled
        result_stream = speechsdk.AudioDataStream(result)
        result_stream.detach_input() # stop any more data from input getting to the stream

        save_future = result_stream.save_to_wav_file_async("AudioFromRecognizedKeyword.wav")
        print('Saving file...')
        saved = save_future.get()

        # If active keyword recognition needs to be stopped before results, it can be done with
        
        stop_future = keyword_recognizer.stop_recognition_async()
        print('Stopping...')
        stopped = stop_future.get()