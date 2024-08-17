import speech_recognition as sr

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        return text

# Transcribe WAV file
transcript = transcribe_audio("let_her_go_x.wav")
print("Transcript:", transcript)
