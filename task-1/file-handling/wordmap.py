text = "This is a sample sentence. This sentence is a sample."
words = text.split()  # Split the text into words

wordmap = {}  # Create an empty dictionary to store word frequencies

for word in words:
    word = word.lower()  # Convert to lowercase to ensure case-insensitive counting
    if word in wordmap:
        wordmap[word] += 1
    else:
        wordmap[word] = 1

print(wordmap)
