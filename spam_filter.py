#!/usr/bin/env python3

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from utils import println

df = pd.read_table(
    'sms_span_collection', sep='\t', names=['label', 'sms_message'])
println(df.head())

df['label'] = df.label.map({'ham': 0, 'spam': 1})
println(df.shape)

X_train, X_test, y_train, y_test = train_test_split(
    df['sms_message'], df['label'], random_state=1)

print('number of rows in the total set:', df.shape[0])
print('number of rows in the training set:', X_train.shape[0])
println('number of rows in the test set:', X_test.shape[0])

count_vector = CountVectorizer()
training_data = count_vector.fit_transform(X_train)
testing_data = count_vector.transform(X_test)

naive_bayes = MultinomialNB()
naive_bayes.fit(training_data, y_train)

predictions = naive_bayes.predict(testing_data)

print('accuracy score:', accuracy_score(y_test, predictions))
print('recision score:', precision_score(y_test, predictions))
print('recall score:', recall_score(y_test, predictions))
print('f1 score:', f1_score(y_test, predictions))