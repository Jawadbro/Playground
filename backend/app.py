from flask import Flask, request, jsonify,render_template
from flask_cors import CORS
import os
import google.generativeai as genai
from elevenlabs import save, stream
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
from models.PublicSpeakingCoach import PublicSpeakingCoach
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

elevenlabs_client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
CORS(app)
coach = PublicSpeakingCoach()

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_message = data.get('user_message')
    audio_analysis = data.get('audio_analysis')
    audio_transcript = data.get('audio_transcript')
    
    response_text = coach.send_message(user_message, audio_analysis, audio_transcript)
    return jsonify({"response": response_text})
@app.route('/show_me_how', methods=['POST'])
def show_me_how():
    data = request.json
    user_message = data.get('user_message')
    audio_transcript = data.get('audio_transcript')
    
    response_text = coach.show_me_how(user_message, audio_transcript)
    return jsonify({"response": response_text})
@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    file = request.files['file']
    file_path = os.path.join(os.getcwd(), file.filename)
    file.save(file_path)
    
    audio_file = coach.upload_audio(file_path)
    audio_analysis = coach.analyze_audio(audio_file)
    
    return jsonify({"analysis": audio_analysis})
if __name__ == '__main__':
    app.run(debug=True)
