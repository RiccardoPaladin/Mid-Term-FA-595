'''
MID-TERM EXAM
FA 595
'''

import flask
from flask import Flask
from flask import jsonify
import pandas as pd
import numpy as np
import requests
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import word_tokenize
from nltk.probability import FreqDist
from textblob import TextBlob
from textblob import Word
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('punkt')
nltk.download('brown')

app = Flask(__name__)

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


#2 OK
#count the frequency of the words
def frequency_words(string):
    frequency = []
    words = word_tokenize(string)
    fdist = FreqDist(words)
    frequency.append(fdist)
    return frequency


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
    return f'From singular to plural: {plurals}', f'From plural to singular: {singulars}'

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



#6 tf_idf
#term frequency–inverse document frequency it give the importance of the words

def tf_idf(string):
    df_dtm = pd.DataFrame()
    df = pd.DataFrame({'review': ['review1'], 'text':string})
    tfidf = TfidfVectorizer(stop_words='english', norm=None)
    tfidf_matrix = tfidf.fit_transform(df['text'])
    df_dtm = pd.DataFrame(tfidf_matrix.toarray(),
                      index=df['review'].values,
                      columns=tfidf.get_feature_names_out())
    return df_dtm





@app.route('/input_string', methods =['GET','POST'])
def input_string():
    if requests == 'POST':
        post_json = flask.request.json
        string = post_json.get('string', None)
        if string:
            services = post_json.get('services', None)
            if services:
                res_dict = {}
                if 'sentiment' in services:
                    res_dict['sentiment'] = Sentiment_Analizer(string)            #OK
                if 'frequency' in services:
                    res_dict['frequency'] = frequency_words(string)               #OK
                if 'Part of Speech' in services:
                    res_dict['Part of Speech'] = POS(string)                      #OK
                if 'subjectivity' in services:
                    res_dict['subjectivity'] = subjectivity(string)               #OK
                if 'pluralize' in services:
                    res_dict['pluralize'] = pluralize_sungularize_nouns(string)   #OK
                if 'term frequency–inverse document frequency' in services:
                    res_dict['sentences'] = tf_idf(string)                        #OK
                return {"success": True, 'response': res_dict}
            else:
                return {'success': False, 'error': 'No string passed in json payload'}, 400
        else:
            return {'success': False, 'error': 'No string passed in json payload'}, 400
        return jsonify(**request.json)
    else:
        a = 'API'
        return a


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8080)

#export FLASK_APP=MID_TERM_FLASK.py
