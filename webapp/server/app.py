from flask import Flask, render_template, request, jsonify
import azure.cognitiveservices.speech as speechsdk
import pymongo
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables
AZURE_SPEECH_KEY = os.getenv("AZURE_SPEECH_KEY")
AZURE_SPEECH_REGION = os.getenv("AZURE_SPEECH_REGION")
MONGO_URI = os.getenv("MONGO_URI")
ENGLISH_VOICE_ID = os.getenv("ENGLISH_VOICE_ID")
ENGLISH_SPEECH_ID = os.getenv("ENGLISH_SPEECH_ID")

def recognize_from_microphone(speech_language):
    # Initialize Azure Speech SDK
    speech_config = speechsdk.SpeechConfig(subscription=AZURE_SPEECH_KEY, region=AZURE_SPEECH_REGION)
    speech_config.speech_recognition_language = speech_language

    audio_config = speechsdk.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
        return speech_recognition_result.text
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized.")
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the Azure Speech subscription key and region values?")
    return None

# def synthesize_text(text, speech_language):
#     # Initialize Azure Text-to-Speech
#     speech_config = speechsdk.SpeechConfig(subscription=AZURE_SPEECH_KEY, region=AZURE_SPEECH_REGION)
#     audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

#     # The language of the voice that speaks.
#     speech_config.speech_synthesis_voice_name = speech_language

#     speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

#     speech_synthesizer.speak_text(text)
def synthesize_text(text, speech_language):
    # Initialize Azure Text-to-Speech
    speech_config = speechsdk.SpeechConfig(subscription=AZURE_SPEECH_KEY, region=AZURE_SPEECH_REGION)
    speech_config.speech_synthesis_voice_name = speech_language

    audio_config = speechsdk.AudioOutputConfig(use_default_speaker=True)

    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    result = synthesizer.speak_text(text)

    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        audio_stream = speechsdk.AudioDataStream(result)

        # Convert audio stream to bytes
        audio_bytes = audio_stream.read_all()
        return audio_bytes

    return None

# Initialize MongoDB client
mongo_client = pymongo.MongoClient(MONGO_URI)
db = mongo_client["speech"]
collection = db["content"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    # Assuming you have a form with a file input field for audio recording
    audio_file = request.files['audio']

    # Process the audio using Azure Speech SDK
    transcribed_text = recognize_from_microphone(ENGLISH_VOICE_ID)  # You can pass the desired language here

    if transcribed_text:
        # Send transcribed_text to another service and get the result
        # You need to implement this part yourself.

        # Store the result in MongoDB
        # db_data = {"transcribed_text": transcribed_text, "result_from_service": "Result placeholder"}
        # collection.insert_one(db_data)

        # Synthesize the result text to speech
        synthesized_audio = synthesize_text("Result placeholder", ENGLISH_SPEECH_ID)

        if synthesized_audio:
            # Return the synthesized audio to the client
            response = speechsdk.Response(synthesized_audio, content_type="audio/wav")
            response.headers['Content-Disposition'] = 'attachment; filename="result_audio.wav"'
            return response
        else:
            return jsonify({"error": "Speech synthesis failed."})
    else:
        return jsonify({"error": "Speech recognition failed."})


if __name__ == '__main__':
    app.run(debug=True)
