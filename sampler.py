from pydub import AudioSegment

def split_audio(file_path, chunk_length_ms):
    audio = AudioSegment.from_wav(file_path)
    chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]
    
    for i, chunk in enumerate(chunks):
        chunk_name = f"chunk{i}.wav"
        chunk.export(chunk_name, format="wav")
        print(f"Exported {chunk_name}")

# Example usage
split_audio("", 20000)  # Split into 20-second chunks
