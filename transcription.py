```python
import os
import requests
from pydub import AudioSegment

# Directory to store audio files
AUDIO_DIR = '/tmp/audio'

# Whisper API URL
WHISPER_API_URL = 'https://api.whisper.com/transcribe'

def transcribe_audio(audio_file):
    """
    Transcribe an audio file using the Whisper API.
    The audio file is first converted to the required format (WAV) if necessary.
    The transcription is then stored and its ID is returned.
    """
    # Ensure the audio directory exists
    os.makedirs(AUDIO_DIR, exist_ok=True)

    # Save the audio file
    audio_path = os.path.join(AUDIO_DIR, audio_file.filename)
    audio_file.save(audio_path)

    # Convert the audio file to WAV if necessary
    if not audio_path.endswith('.wav'):
        audio = AudioSegment.from_file(audio_path)
        audio_path = audio_path.rsplit('.', 1)[0] + '.wav'
        audio.export(audio_path, format='wav')

    # Send the audio file to the Whisper API for transcription
    with open(audio_path, 'rb') as f:
        response = requests.post(WHISPER_API_URL, files={'file': f})

    # Check the response status
    if response.status_code != 200:
        raise Exception('Failed to transcribe audio: {}'.format(response.text))

    # Store the transcription and return its ID
    transcription_id = store_transcription(response.text)
    return transcription_id
```
