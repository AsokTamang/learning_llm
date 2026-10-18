import tiktoken
encoding = tiktoken.get_encoding("cl100k_base")
ids = encoding.encode("Hey buddy, how are you doing today?")
print(ids)
print(encoding.decode(ids))


for text in ["refund", "unsubscribing", "My parcel has not arrived", "मलाई नयाँ कुरा सिक्न मन पर्छ।"]:
    ids = encoding.encode(text)
    print(f"Text: {text}")
    print(f"Token IDs: {ids}")
    print(f"Decoded Text: {encoding.decode(ids)}")