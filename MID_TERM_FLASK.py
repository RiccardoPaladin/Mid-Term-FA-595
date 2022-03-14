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
    for i in df.iloc[0:,-1]:
        if i >= 0.5:
            print('Positive sentiment ')
        if i < 0.5:
            print('Negative sentiment')
    return df


#2
#Translation of the string

def translate(string):
    blob = TextBlob(string)
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
#Subjectivity from textblob

def subjectivity(string):
        blob = TextBlob(string)
        sub = blob.sentiment[1]
        if sub >=0.5:
            print('Subjective string')
        else:
            print('Objective string')
        return f'Subjectivity rate: {sub}'



#6
#Count repeated words

def repeated(string):
    blob = TextBlob(string)
    blob.tokens
    counts = []
    report = []
    for element in blob.tokens:
        counts = blob.tokens.count(element)
        report
    return report

#7
#find the position of the word

def find_word(string, word):
    blob = TextBlob(string)
    position = blob.find(word)
    return position



@app.route('/input_string', services=['POST'])
def input_string():
    post_json = flask.request.json
    string = post_json.get('string', None)
    if string:
        services = post_json.get('services', None)
        if services:
            res_dict = {}
            if 'sentiment' in services:
                res_dict['sentiment'] = Sentiment_Analizer(string)
            if 'translate' in services:
                res_dict['translate'] = translate(string)
            if 'Part of Speech' in services:
                res_dict['Part of Speech'] = POS(string)
            if 'subjectivity' in services:
                res_dict['subjectivity'] = subjectivity(string)
            if 'pluralize' in services:
                res_dict['pluralize'] = pluralize(string)
            if 'singularize' in services:
                res_dict['singularize'] = singularize(string)
            if 'sentences' in services:
                res_dict['sentences'] = sentences(string)

            return {"success": True, 'response': res_dict}
        else:
            return {'success': False, 'error': 'No string passed in json payload'}, 400
    else:
        return {'success': False, 'error': 'No string passed in json payload'}, 400





#blob.find() look at the position of the word





