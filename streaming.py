import openai 
openai.api_key = ' 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'
completion = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "write a 100 word paragraph about why league is such a great game"}
  ],
  stream=True
)

for chunk in completion:
  print(chunk.choices[0].delta)
