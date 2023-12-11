from pathlib import Path
import openai
openai.api_key = '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'
speech_file_path = Path(__file__).parent / "speech.mp3"
response = openai.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="انا اسمي وليد."
)
response.stream_to_file(speech_file_path)
