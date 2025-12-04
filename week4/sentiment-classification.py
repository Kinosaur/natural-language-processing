import nltk, random
from nltk.corpus import movie_reviews
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print(len(movie_reviews.fileids())) # number of documents
print(movie_reviews.categories())   # categories
print(movie_reviews.words()[:100])  # the first 100 words
print(movie_reviews.fileids()[:10]) # the first 10 file names

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.seed(123)
random.shuffle(documents)

print('Number of Reviews/Documents: {}'.format(len(documents)))
print('Corpus Size (words): {}'.format(np.sum([len(d) for (d,l) in documents])))
print('Sample Text of Doc 1:')
print('-'*30)
print(' '.join(documents[0][0][:50])) # first 50 words of the first document

from collections import Counter
sentiment_distr = Counter([label for (words, label) in documents])
print(sentiment_distr)

from sklearn.model_selection import train_test_split
train, test = train_test_split(documents, test_size = 0.33, random_state=42)
## Sentiment Distrubtion for Train and Test
print(Counter([label for (words, label) in train]))
print(Counter([label for (words, label) in test]))

X_train = [' '.join(words) for (words, label) in train]
X_test = [' '.join(words) for (words, label) in test]
y_train = [label for (words, label) in train]
y_test = [label for (words, label) in test]

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
## Feature Extraction
tfidf_vec = TfidfVectorizer(min_df = 10, token_pattern = r'[a-zA-Z]+')
X_train_bow = tfidf_vec.fit_transform(X_train) # fit train
X_test_bow = tfidf_vec.transform(X_test) # transform test

## Model Training
from sklearn.naive_bayes import GaussianNB
import sklearn.model_selection
model_gnb = GaussianNB()
model_gnb.fit(X_train_bow.toarray(), y_train)
# model_gnb_acc = cross_val_score(estimator=model_gnb, X=X_train_bow.toarray(), y=y_train, cv=5, n_jobs=-1)
# print(model_gnb_acc)
model_gnb.predict(X_test_bow[:10].toarray())

## Evaluation
print(model_gnb.score(X_test_bow.toarray(), y_test))
# F1
from sklearn.metrics import f1_score
y_pred = model_gnb.predict(X_test_bow.toarray())

f1_score(y_test, y_pred, 
         average=None, 
         labels = movie_reviews.categories())

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
cm = confusion_matrix(y_test, y_pred)
print(cm)
# plot_confusion_matrix(model_gnb, X_test_bow, y_test, normalize='all')
# disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=clf.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model_gnb.classes_)
disp.plot()
plt.show()