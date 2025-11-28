# Kaung Khant Lin
# 6540131
# 541

import nltk
from nltk.corpus import reuters
from collections import Counter

# Download corpus
try:
    reuters.words()
except Exception:
    nltk.download('reuters')

# Get all words
words = reuters.words()
print(f"Total words: {len(words)}")

# Build unigram language model (word frequency counts)
print("\nBuilding unigram language model...")
unigram_model = Counter(words)
print(f"Unique words: {len(unigram_model)}")

# Get top 20 most common words
print("\nTop 20 most common words (unigram model):")
top_20 = unigram_model.most_common(20)
for word, count in top_20:
    print(f"{word}: {count}")

# Generate 20-word sequence using the top 20 most frequent words
print("\n20-word sequence from top frequent words:")
generated_sequence = [word for word, count in top_20]
print(" ".join(generated_sequence))


