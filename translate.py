import openai
openai.api_key = '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'

audio_file = open("speech.mp3", "rb")
transcript = openai.audio.translations.create(
  model="whisper-1", 
  file=audio_file
)
print(transcript.text)