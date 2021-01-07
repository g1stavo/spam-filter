#!/usr/bin/env python3

import pprint
import re
from collections import Counter
from utils import println

documents = [
    'Hello, how are you!',
    'Win money, win from home.',
    'Call me now.',
    'Hello, Call hello you tomorrow?'
]

lower_case_documents = []

for i in documents:
    lower_case_documents.append(i.lower())
println(lower_case_documents)

sans_punctuation_documents = []

for i in lower_case_documents:
    spd = re.sub(",|!|\.|\?", "", i)
    sans_punctuation_documents.append(spd)
println(sans_punctuation_documents)

preprocessed_documents = []

for i in sans_punctuation_documents:
    preprocessed_documents.append(i.split())
println(preprocessed_documents)

frequency_list = []

for i in preprocessed_documents:
    frequency_list.append(Counter(i))
pprint.pprint(frequency_list)