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

st.text('FIRST SERVICE')
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

st.text('SECOND SERVICE')
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
st.text('THIRD SERVICE')
st.text('Insert two words to see at the similarity')
text_input2 = st.text_input('Enter  word','')
text_input3 = st.text_input('Enter a word','')

import spacy
spacy.load('en_core_web_sm')
token1 = nlp(text_input2)
token1.vector
token2 = nlp(text_input3)
token2.vector
similarity = token1.similarity(token2)
st.markdown(
    f"""
    {similarity}
    """
)


#streamlit run MID_TERM_FA_595    on the terminal
#Local URL: http://localhost:8501
#Network URL: http://192.168.12.117:8501

