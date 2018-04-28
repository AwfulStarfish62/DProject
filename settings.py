#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nltk
from nltk import *
from nltk.corpus import brown
#from nltk.corpus import stopwords
#stopWords = set(stopwords.words('english'))
from stop_words import get_stop_words
stopWords = get_stop_words('russian')

docs = []

# F = open("3.txt",encoding="utf8")
# docs.append(F.read())
# F = open("8.txt",encoding="utf8")
# docs.append(F.read())
# F = open("6.txt",encoding="utf8")
# docs.append(F.read())
# F = open("4.txt",encoding="utf8")
# docs.append(F.read())
# F = open("2.txt",encoding="utf8")
# docs.append(F.read())
# F = open("film.txt",encoding="utf8")
# docs.append(F.read())

F = open("3.txt",encoding="utf8")
FString = F.read()
docs += FString.split('#')

# F = open("8.txt",encoding="utf8")
# FString = F.read()
# docs += FString.split('#')

# F = open("6.txt",encoding="utf8")
# FString = F.read()
# docs += FString.split('#')

# F = open("4.txt",encoding="utf8")
# FString = F.read()
# docs += FString.split('#')

# F = open("2.txt",encoding="utf8")
# FString = F.read()
# docs += FString.split('#')

F = open("film.txt",encoding="utf8")
FString = F.read()
docs += FString.split('#')

for i in range(len(docs)):
    print("-------str№: " + str(i) + "---------")
    #print(docs[i])

stem='russian'
#'danish', 'dutch', 'english', 'finnish', 'french', 'german', 'hungarian', 'italian',
#'norwegian', 'porter', 'portuguese', 'romanian', 'russian', 'spanish', 'swedish'