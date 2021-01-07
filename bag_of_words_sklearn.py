#!/usr/bin/env python3

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from utils import println

documents = [
    'Hello, how are you!',
    'Win money, win from home.',
    'Call me now.',
    'Hello, Call hello you tomorrow?'
]

count_vector = CountVectorizer(
    lowercase = True, token_pattern = '(?u)\\b\\w\\w+\\b', stop_words=None)

count_vector.fit(documents)
feature_names = count_vector.get_feature_names()
println(feature_names)

doc_array = count_vector.transform(documents).toarray()
println(doc_array)

frequency_matrix = pd.DataFrame(
    doc_array, columns=feature_names)
print(frequency_matrix)