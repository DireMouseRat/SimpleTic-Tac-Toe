text = input()
words = text.split()
prefixes = ("https://", "http://", "www.")
for word in words:
    if word.lower().startswith(prefixes):
        print(word)
