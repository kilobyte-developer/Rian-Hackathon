from pydub import AudioSegment

def convert_mp3_to_wav(mp3_file, wav_file):
    audio = AudioSegment.from_mp3(mp3_file)
    audio.export(wav_file, format="wav")

# Convert MP3 to WAV
convert_mp3_to_wav("google_1.mp3", "google_1_x.wav")
