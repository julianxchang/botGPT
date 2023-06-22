import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "what is your name."}])
print(completion.choices[0].message.content)