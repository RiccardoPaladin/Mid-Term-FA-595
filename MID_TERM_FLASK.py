'''
MID-TERM EXAM
FA 595
'''

import flask
import pandas as pd
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
from textblob import Word
nltk.download('punkt')
nltk.download('brown')

app = flask.Flask(__name__)

#1  OK
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
        if (i < 0.5 and i !=0):
            print('Negative sentiment')
        if 0 == 0:
            print('Not classified')
    return df


#2
#Translation of the string

def translate(string):
    blob = TextBlob(string)
    translate = str(blob.translate(to='it'))
    return translate

#3 OK
#From singular to plural and viceversa

def pluralize_sungularize_nouns(string):
    plurals = []
    singulars = []
    blob = TextBlob(string)
    sentence = blob.sentences[0]
    results = pd.DataFrame(blob.sentences[0].tags)
    results.columns = ['words', 'pos']
    sing = [results.loc[results['pos'] == 'NN', 'words'].iloc[0]]
    plur = [results.loc[results['pos'] == 'NNS', 'words'].iloc[0]]
    for word in sing:
        plural = word.pluralize()
        plurals.append(plural)
    for elem in plur:
        singular = elem.singularize()
        singulars.append(singular)
    return f'From singular to plural: {plurals}' , f'From plural to singular: {singulars}'

#4 OK
#Tokenize and identify which part of speech is

def POS(string):
    tag = []
    token = nltk.word_tokenize(string)
    tags = nltk.pos_tag(token)
    tag.append(tags)
    return tag

#5 OK
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

#7 definitions






@app.route('/input_string', services=['POST'])
def input_string():
    post_json = flask.request.json
    string = post_json.get('string', None)
    if string:
        services = post_json.get('services', None)
        if services:
            res_dict = {}
            if 'sentiment' in services:
                res_dict['sentiment'] = Sentiment_Analizer(string) #OK
            if 'translate' in services:
                res_dict['translate'] = translate(string)
            if 'Part of Speech' in services:
                res_dict['Part of Speech'] = POS(string)         #OK
            if 'subjectivity' in services:
                res_dict['subjectivity'] = subjectivity(string)  #OK
            if 'pluralize' in services:
                res_dict['pluralize'] = pluralize_sungularize_nouns(string)   #ok
            if 'sentences' in services:
                res_dict['sentences'] = sentences(string)

            return {"success": True, 'response': res_dict}
        else:
            return {'success': False, 'error': 'No string passed in json payload'}, 400
    else:
        return {'success': False, 'error': 'No string passed in json payload'}, 400
