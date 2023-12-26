```python
from flask import Flask, request, jsonify
from auth import generate_auth_code, validate_auth_code
from transcription import transcribe_audio
from storage import store_transcription, retrieve_transcription

app = Flask(__name__)

@app.route('/generate_auth', methods=['POST'])
def generate_auth():
    user_id = request.json.get('user_id')
    auth_code = generate_auth_code(user_id)
    return jsonify({'auth_code': auth_code})

@app.route('/transcribe', methods=['POST'])
def transcribe():
    auth_code = request.headers.get('auth_code')
    audio_file = request.files.get('audio_file')

    if not validate_auth_code(auth_code):
        return jsonify({'error': 'Invalid auth code'}), 401

    transcription_id = transcribe_audio(audio_file)
    return jsonify({'transcription_id': transcription_id})

@app.route('/transcription/<transcription_id>', methods=['GET'])
def get_transcription(transcription_id):
    transcription = retrieve_transcription(transcription_id)
    if transcription is None:
        return jsonify({'error': 'Transcription not found'}), 404

    return jsonify({'transcription': transcription})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
```
