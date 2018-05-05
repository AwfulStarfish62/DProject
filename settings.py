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

	        # '3', // боевик
            # '8', // драма
            # '6', // комедия
            # '4', // триллер
            # '2'  // фантастика

#filmsGenreNum = [2,3,4,6,8] 10-фильмов, 10-обзоров
filmsGenreNum = [3,4,6,8]
filmsGenre = ["фантастика","боевик","триллер","комедия","драма","наш фильм"]
filmsNum = []

for i in range(0,len(filmsGenreNum)):
	F = open(str(filmsGenreNum[i]) + ".txt",encoding="utf8")
	FString = str(F.read()).split('#')
	filmsNum.append(len(FString))
	docs += FString

F = open("film.txt",encoding="utf8")
FString = str(F.read()).split('#')
filmsNum.append(len(FString))
docs += FString

print(filmsNum)
for i in range(len(docs)):
    print("-------str№: " + str(i) + "---------")
    #print(docs)

stem='russian'
#'danish', 'dutch', 'english', 'finnish', 'french', 'german', 'hungarian', 'italian',
#'norwegian', 'porter', 'portuguese', 'romanian', 'russian', 'spanish', 'swedish'