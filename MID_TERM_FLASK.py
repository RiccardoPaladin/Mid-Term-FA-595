'''
MID-TERM EXAM
FA 595
'''

import pandas as pd
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import nltk
nltk.download('punkt')
nltk.download('brown')


#1
#Sentiment Analysis with SentimentIntensityAnalyzer

def Sentiment_Analizer(string):
    sentiments = []
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(string)
    sentiments.append(scores)
    df = pd.DataFrame(sentiments)
    return df.to_dict()


#2
#Translation of the string

def translate(string):
    blob = TextBlob(string)
    blob.sentences
    translate = str(blob.translate(to='it'))
    return translate

#3
#From singular to plural and viceversa

def sing_plur(string):
    changed_to_plural = []
    changed_to_singular = []
    blob = TextBlob(string)
    for words in range(1,len(blob.words)):
        sing = blob.words[words].singularize()
        plur = blob.words[words].pluralize()
        changed_to_singular.append(sing)
        changed_to_plural.append(plur)
    return changed_to_plural
    return changed_to_singular

#4
#Tokenize and identify which part of speech is

def POS(string):
    tag = []
    token = nltk.word_tokenize(string)
    tags = nltk.pos_tag(token)
    tag.append(tags)
    return tag

#5
#Similarity of the words


#6
#Count repeated words

def repeated(string):
    blob = TextBlob(string)
    blob.tokens
    counts = []
    report = []
    for element in blob.tokens:
        count = blob.tokens.count(element)
        report =
    return report









