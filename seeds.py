#LOGIC OF SEEDS
import os
from dotenv import load_dotenv
load_dotenv()
#WITHOUT USING SEED
from groq import Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
prompt = [{"role": "user", "content": "Suggest a name for a cafe. Reply with the name only."}]
for i in range(3):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=prompt,
        temperature=1)
    print(response.choices[0].message.content)


    