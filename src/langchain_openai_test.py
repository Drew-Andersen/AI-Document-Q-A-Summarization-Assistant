import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

completion = client.chat.completions.create(model='gpt-4',
                                           messages=[
                                               {'role': 'user',
                                                'content': 'Explain embeddings in simple terms'}
                                           ], max_tokens=250, temperature=0, seed=365, stream=True)

for i in completion:
    delta = i.choices[0].delta
    if delta.content:
        print(delta.content, end="")