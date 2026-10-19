import tiktoken
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

encoding = tiktoken.get_encoding("cl100k_base")  #importing the openai's tokenizer
ids = encoding.encode("Hey buddy, how are you doing today?")  #encoding the text into token IDs
print(ids)
print(encoding.decode(ids))  #decoding the token IDs back into text
 

for text in ["refund", "unsubscribing", "My parcel has not arrived", "मलाई नयाँ कुरा सिक्न मन पर्छ।"]:
    ids = encoding.encode(text)
    print(f"Text: {text}")
    print(f"Token IDs: {ids}")
    print(f"Decoded Text: {encoding.decode(ids)}")


#using llm to produce output based on different temperature
client = Groq(api_key=os.getenv("GROQ_API_KEY"))  #using the Groq client to interact with the API
prompt = [{'role':'user','content':'Write a short poem about the beauty of nature.'}]
#lower temperature means the model will produce more focused and deterministic output, while higher temperature means the model will produce more diverse and creative output.
for temperature in [0.2, 0.5, 0.8]:
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=prompt,
        temperature=temperature,
        max_tokens=100
    )
    print(f"Temperature: {temperature}")
    print(f"Response: {response.choices[0].message.content}\n")
