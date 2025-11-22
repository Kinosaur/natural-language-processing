import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

text = """Once upon a younger year
When all our shadows disappeared
The animals inside came out to play
Went face to face with all our fears
Learned our lessons through the tears
Made memories we knew would never fade
One day, my father, he told me, "Son, don't let it slip away"
He took me in his arms, I heard him say
"When you get older, your wild heart will live for younger days
Think of me if ever you're afraid"
He said, "One day, you'll leave this world behind
So live a life you will remember"
My father told me when I was just a child
"These are the nights that never die"
My father told me
"When thunderclouds start pouring down
Light a fire they can't put out
Carve your name into those shining stars"
He said, "Go venture far beyond the shores
Don't forsake this life of yours
I'll guide you home no matter where you are"
One day, my father, he told me, "Son, don't let it slip away"
When I was just a kid, I heard him say
"When you get older, your wild heart will live for younger days
Think of me if ever you're afraid"
He said, "One day, you'll leave this world behind
So live a life you will remember"
My father told me when I was just a child
"These are the nights that never die"
My father told me
"These are the nights that never die"
My father told me
My father told me"""

# Tokens
words = word_tokenize(text)

# Stopword removal and cleaning
stop_words = set(stopwords.words('english'))
filtered_words = [w.lower() for w in words if w.lower() not in stop_words and w.isalpha()]

# Stems and Lemmas
ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()

stemmed = [ps.stem(w) for w in filtered_words]
lemmatized = [lemmatizer.lemmatize(w) for w in filtered_words]

# Output formatting
print("Original text:")
print(text)
print("\n" + "="*80 + "\n")

print("Tokens:")
print(words)
print("\n" + "="*80 + "\n")

print("Cleaned:")
print(filtered_words)
print("\n" + "="*80 + "\n")

print("Stems vs Lemmas:")
print(f"{'Word':<15} | {'Stem':<15} | {'Lemma':<15}")
print("-" * 50)
for word, stem, lemma in zip(filtered_words, stemmed, lemmatized):
    print(f"{word:<15} | {stem:<15} | {lemma:<15}")