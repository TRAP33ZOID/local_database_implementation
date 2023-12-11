import openai
openai.api_key = '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'

openai.files.create(
  file=open("output.jsonl", "rb"),
  purpose="fine-tune"
)
