import openai
import json
openai.api_key = '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'

completion = openai.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "how many continents are there?"}
  ]
)

print("Total Tokens:", completion.usage.total_tokens)
print('the answer is: ', completion.choices[0].message.content)
