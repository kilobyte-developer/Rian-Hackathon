from googletrans import Translator

def translate_text(text, target_languages):
    translator = Translator()
    translations = {}
    for lang in target_languages:
        translated = translator.translate(text, dest=lang)
        translations[lang] = translated.text
    return translations

# Example usage
transcript = "-------"
target_languages = ['hi', 'mr', 'es']  # Hindi, Marathi, Spanish
translations = translate_text(transcript, target_languages)

for lang, translation in translations.items():
    print(f"Translation in {lang}: {translation}")
