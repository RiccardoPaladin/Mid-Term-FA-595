'''
MID-TERM EXAM
FA 595
'''
#https://docs.streamlit.io/library/get-started/create-an-app
#AWS Amplify hosting --> Amplify Hosting is a fully managed hosting service for web apps. Connect your repository to build, deploy, and host your web app.



#pip install streamlit

import pandas as pd
import numpy as np
import requests
import streamlit as st

st.title('NLP services')
st.text('In this web app you can use six different services on NLP')

st.text('1ST SERVICE')
st.text('Insert a string and obtain which part of the speech is')
#Tokenize the sentence and return the pos_tag
text_input = st.text_input('Enter string to analyze','')

import nltk
nltk.download('punkt')
tokens = nltk.word_tokenize(text_input)
tag = nltk.pos_tag(tokens)
st.markdown(
    f"""
    {tag}
    """
)

st.text('2ND SERVICE')
st.text('Insert a string and obtain the sentiment analysis')
text_input1 = st.text_input('Enter string to evaluate','')
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
sentiment = sia.polarity_scores(text_input1)

st.markdown(
    f"""
    {sentiment}
    """
)

st.text('3RD SERVICE')
st.text('Insert a string and obtain the italian translation')
text_input2 = st.text_input('Enter string to translate','')
from textblob import TextBlob
blob = TextBlob(text_input2)
translate = str(blob.translate(to='it'))

st.markdown(
    f"""
    {translate}
    """
)

st.text('4TH SERVICE')
st.text('Insert a plural word and obtain the singular')
text_input3 = st.text_input('Enter plural word','')
from textblob import TextBlob
blob1 = TextBlob(text_input3)
sing = blob1.words[0].singularize()

st.markdown(
    f"""
    {sing}
    """
)

st.text('5TH SERVICE')
st.text('Insert a singular word and obtain the plural')
text_input4 = st.text_input('Enter singular word','')
from textblob import TextBlob
blob1 = TextBlob(text_input4)
sing = blob1.words[0].pluralize()

st.markdown(
    f"""
    {sing}
    """
)

st.text('6TH SERVICE')
st.text('Insert a string and count the words')


#streamlit run MID_TERM_FA_595.py    on the terminal


