import requests
import io
from pydub import AudioSegment
from pydub.playback import play

def play_azure_blob_audio(audio_url):
    try:
        # Download the audio file from the URL
        response = requests.get(audio_url)
        audio_data = response.content

        # Convert the audio data to an AudioSegment
        audio = AudioSegment.from_file(io.BytesIO(audio_data))

        # Play the audio
        play(audio)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    azure_blob_audio_url = "https://alexaspeak.blob.core.windows.net/alexa/kavya.mp4"
    play_azure_blob_audio(azure_blob_audio_url)
