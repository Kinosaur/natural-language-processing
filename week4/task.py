# Kaung Khant Lin
# 6540131
# 541

import nltk
import random
from nltk.corpus import movie_reviews
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay, classification_report

# Download movie_reviews corpus
nltk.download('movie_reviews')

# Load and explore data
print(len(movie_reviews.fileids()))  # number of documents
print(movie_reviews.categories())  # categories
print(movie_reviews.words()[:100])  # the first 100 words
print(movie_reviews.fileids()[:10])  # the first 10 file names

documents = [
    (list(movie_reviews.words(fileid)), category)
    for category in movie_reviews.categories()
    for fileid in movie_reviews.fileids(category)
]
random.seed(123)
random.shuffle(documents)

print("Number of Reviews/Documents: {}".format(len(documents)))
print("Corpus Size (words): {}".format(np.sum([len(d) for (d, label) in documents])))
print("Sample Text of Doc 1:")
print("-" * 30)
print(" ".join(documents[0][0][:50]))  # first 50 words of the first document

# Check sentiment distribution
sentiment_distr = Counter([label for (words, label) in documents])
print("Sentiment Distribution:", sentiment_distr)


# Function to train and evaluate model with specified vectorizer
def train_and_evaluate(train, test, vectorizer_type='tfidf'):
    # Prepare data
    X_train = [' '.join(words) for (words, label) in train]
    X_test = [' '.join(words) for (words, label) in test]
    y_train = [label for (words, label) in train]
    y_test = [label for (words, label) in test]
    
    # Feature extraction
    if vectorizer_type == 'tfidf':
        vectorizer = TfidfVectorizer(min_df=10, token_pattern=r'[a-zA-Z]+')
    else:  # bow
        vectorizer = CountVectorizer()
    
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    
    # Train Naive Bayes classifier
    model = GaussianNB()
    model.fit(X_train_vec.toarray(), y_train)
    
    # Predictions
    y_pred = model.predict(X_test_vec.toarray())
    
    # Evaluation metrics
    accuracy = model.score(X_test_vec.toarray(), y_test)
    precision = precision_score(y_test, y_pred, average=None, labels=movie_reviews.categories())
    recall = recall_score(y_test, y_pred, average=None, labels=movie_reviews.categories())
    f1 = f1_score(y_test, y_pred, average=None, labels=movie_reviews.categories())
    
    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    
    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'cm': cm,
        'y_test': y_test,
        'y_pred': y_pred
    }


# Store results for comparison
results = {}

# Test with different split ratios
split_ratios = [0.30, 0.20, 0.10]  # test sizes for 70:30, 80:20, 90:10

for test_size in split_ratios:
    split_name = f"{int((1-test_size)*100)}:{int(test_size*100)}"
    print(f"\n{'='*60}")
    print(f"Train/Test Split: {split_name}")
    print('='*60)
    
    # Split data ONCE for this ratio (same split for both vectorizers)
    train, test = train_test_split(documents, test_size=test_size, random_state=42)
    print(f"Train size: {len(train)}, Test size: {len(test)}")
    print(f"Train distribution: {Counter([label for (words, label) in train])}")
    print(f"Test distribution: {Counter([label for (words, label) in test])}")
    
    # Test with both vectorizers on the SAME split
    for vec_type in ['bow', 'tfidf']:
        vec_name = "Bag of Words" if vec_type == 'bow' else "TF-IDF"
        print(f"\n--- {vec_name} ---")
        
        result = train_and_evaluate(train, test, vectorizer_type=vec_type)
        results[(split_name, vec_type)] = result
        
        print(f"Accuracy: {result['accuracy']:.4f}")
        print("\nPer-class metrics:")
        for i, cat in enumerate(movie_reviews.categories()):
            print(f"  {cat}: Precision={result['precision'][i]:.4f}, Recall={result['recall'][i]:.4f}, F1={result['f1'][i]:.4f}")
        print(f"\nConfusion Matrix:\n{result['cm']}")


# Summary comparison table
print("\n" + "="*80)
print("SUMMARY COMPARISON TABLE")
print("="*80)
print(f"{'Split':<10} {'Vectorizer':<15} {'Accuracy':<10} {'Neg F1':<10} {'Pos F1':<10}")
print("-"*55)

for test_size in split_ratios:
    split_name = f"{int((1-test_size)*100)}:{int(test_size*100)}"
    for vec_type in ['bow', 'tfidf']:
        vec_name = "BoW" if vec_type == 'bow' else "TF-IDF"
        r = results[(split_name, vec_type)]
        print(f"{split_name:<10} {vec_name:<15} {r['accuracy']:<10.4f} {r['f1'][0]:<10.4f} {r['f1'][1]:<10.4f}")


# Plot confusion matrices for all combinations
fig, axes = plt.subplots(2, 3, figsize=(15, 8))

for col, test_size in enumerate(split_ratios):
    split_name = f"{int((1-test_size)*100)}:{int(test_size*100)}"
    
    for row, vec_type in enumerate(['bow', 'tfidf']):
        vec_name = "Bag of Words" if vec_type == 'bow' else "TF-IDF"
        cm = results[(split_name, vec_type)]['cm']
        
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=movie_reviews.categories())
        disp.plot(ax=axes[row, col], cmap='Blues')
        axes[row, col].set_title(f'{vec_name}\nSplit {split_name}')

plt.tight_layout()
plt.savefig('confusion_matrices.png', dpi=150)
plt.show()

print("\nConfusion matrices saved to 'confusion_matrices.png'")
