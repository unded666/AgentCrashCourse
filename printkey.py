import os

key = os.environ.get('GEMINI_API_KEY')
print(f'GEMINI_API_KEY: {key}')
key2 = os.environ.get('GEMINI_PLAYGROUND_KEY')
print(f'GEMINI_PLAYGROUND_KEY: {key2}')
key3 = os.environ.get('CHATGPT_KEY')
print(f'CHATGPT_KEY: {key3}')
