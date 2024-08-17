import os

def create_srt(translations, timings, output_dir):
    # Create directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for lang, text in translations.items():
        srt_filename = f"{output_dir}/{lang}_subtitles.srt"
        with open(srt_filename, 'w', encoding='utf-8') as srt_file:
            for i, (start_time, end_time) in enumerate(timings):
                srt_file.write(f"{i + 1}\n")
                srt_file.write(f"{start_time} --> {end_time}\n")
                srt_file.write(f"{text}\n\n")
        print(f"Subtitle file created: {srt_filename}")

# Example usage
translations = {
    'hi': '----------',
    'mr': ' ---------',
    'es': ' ---------'
}
timings = [("00:00:00,000", "00:00:29,000"),  # Adjust timings as needed
           ("00:00:05,000", "00:00:10,000")]
output_dir = "subtitles"

create_srt(translations, timings, output_dir)
