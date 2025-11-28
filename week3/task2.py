# Kaung Khant Lin
# 6540131
# 541

import random
from nltk import bigrams
from nltk.corpus import reuters
from collections import defaultdict

# Get all words from reuters corpus
words = list(reuters.words())

# Create bigrams
bi_grams = list(bigrams(words))

# Structure: model[current_word][next_word] = probability
model = defaultdict(lambda: defaultdict(lambda: 0))

for w1, w2 in bi_grams:
    model[w1][w2] += 1

for w1 in model:
    # Sum of all times w1 was followed by ANYTHING
    total_count = float(sum(model[w1].values()))
    
    # Divide each follow-up word count by total to get probability
    for w2 in model[w1]:
        model[w1][w2] /= total_count

# Generate a 20-word sequence
current_word = random.choice(words)
sequence = [current_word]

for _ in range(19):
    next_words = list(model[current_word].keys())
    next_probs = list(model[current_word].values())
    if next_words:
        next_word = random.choices(next_words, weights=next_probs)[0]
    else:
        next_word = random.choice(words)
    sequence.append(next_word)
    current_word = next_word

print("Bigram 20-word sequence:")
print(' '.join(sequence))


