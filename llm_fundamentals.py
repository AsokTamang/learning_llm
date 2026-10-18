import tiktoken
encoding = tiktoken.get_encoding("cl100k_base")
ids = encoding.encode("Hey buddy, how are you doing today?")
print(ids)
print(encoding.decode(ids))