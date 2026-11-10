#importing string module
import string

# Terminal banner divider
BANNER = '=' * 50

# Capture user input
text = input("Enter your paragraph: ")

# Remove punctuation and normalize to lowercase
text = text.translate(str.maketrans("", "", string.punctuation))
text = text.lower()

# Split text into individual words
words = text.split()

# Count word frequency
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

# Display results with terminal banner
print(f"\n{BANNER}")
print("TEXT ANALYZER".center(50))
print(f"{BANNER}\n")

print("Word Frequencies")
print("-" * 50)
for word, count in sorted(frequency.items()):
    print(f"{word}: {count}")

print("-" * 50)
print(f"Total words: {len(words)}")
print(f"Unique words: {len(frequency)}")
print(f"{BANNER}\n")