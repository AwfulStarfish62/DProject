#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nltk
from nltk import *
from nltk.corpus import brown
#from nltk.corpus import stopwords
#stopWords = set(stopwords.words('english'))
from stop_words import get_stop_words
stopWords = get_stop_words('english')
docs =[
"Human machine interface for ABC computer applications",
"A survey of user opinion of computer system response time",
"The EPS user interface management system",
"System and human system engineering testing of EPS",
"Relation of user perceived response time to error measurement",

"The generation of random, binary, ordered trees",
"The intersection graph of paths in trees",
"Graph minors IV: Widths of trees and well-quasi-ordering",
"Graph minors: A survey"
 ]
stem='english'
#'danish', 'dutch', 'english', 'finnish', 'french', 'german', 'hungarian', 'italian',
#'norwegian', 'porter', 'portuguese', 'romanian', 'russian', 'spanish', 'swedish'