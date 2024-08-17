from langdetect import detect

def detect_language(text):
    return detect(text)

# Example usage
text = " ----------"
language = detect_language(text)
print(f"Detected language: {language}")
