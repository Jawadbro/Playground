import google.generativeai as genai

class PublicSpeakingCoach:
     def __init__(self, model_name='models/gemini-1.5-flash-latest'):
        self.model = self.load_model(model_name)
        self.chat=self.model.start_chat(history=[])
        self.steve_jobs_initialized=False
     def __upload_audio(self,audio_file_path):
        audio_file_obj=genai.upload_file(path=audio_file_path)
        return audio_file_obj
     def __analyze_audio(self,audio_file):
         prompt="You are a speech expert and are great at analyzing startup pitches and giving your critique on them. Listen carefully to the uploaded file, and share as much detail as you can identify including timestamps where the speaker can do better. You should share whichever words/phrases the speaker did well on/where the speaker needs to improve."
         response = self.model.generate_content([audio_file, prompt])
         return response.text
     def send_message(self, user_message, audio_analysis=None, audio_transcript=None):
        print ("sending message")

        prompt = ""

        if self.steve_jobs_initialized == False:
            prompt += "You are a public speaking coach, channeling Steve Jobs and his style of talking and coaching! You are the best public speaker in the world, and tech CEOs are looking to get your advice on their startup pitches. You have access to a Speech Analysis expert, and they will share with you their analysis when audio files are shared with them. You also have access to a transcription expert, and you will use that transcript to inform your feedback on speech writing. If the founder asks you to rewrite their script, use the transcript and your observations to share a revised pitch script. You will directly talk to the founders, be encouraging towards them and help them improve on their pitches patiently. You will have access to the entire conversation with the founder, as well as the speech expert's analysis in this prompt. If there are multiple instances of the speech expert's analysis, then only consider the latest one for your feedback. When you are giving feedback, be specific and share details about which parts of their speech they need to improve on, specifiying the timestamps wherever available. Add examples of Steve Jobs's advice, speeches, jokes, and channel his personality in your responses. Be brief in your responses, do not overwhelm the user with your answers. Do not mention that there is a speech expert or transcription expert working with you. Feel free to make assumptions about the founder and their pitch, do not trouble them with many questions. Remove all formatting from your response."            
            self.steve_jobs_initialized = True

        prompt += f"This is the user message: {user_message}\n"

        if audio_analysis:
            prompt += f"A Speech expert has analyzed the user's speech and this is their response: {audio_analysis}\n"

        if audio_transcript:
            prompt += f"An audio transcriber has transcribed the user's speech and this is their response: {audio_transcript}\n"

        response = self.chat.send_message(prompt)
        return response.text

     def show_me_how(self, user_message, audio_transcript=None):
        print ("sending message")

        prompt = ""
        if audio_transcript:
            prompt += f"You need to take the following script, tweak it so that it wows the audience with the depth and richness to the pitch : {audio_transcript}\n"

        response = self.chat.send_message(prompt)
        return response.text
    
  