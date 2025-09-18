from flask import Blueprint, request, render_template
import matplotlib.pyplot as plt
import matplotlib
import os
import tweepy
import csv
from textblob import TextBlob
import re

matplotlib.use('Agg')

sentiments_bp = Blueprint('sentiments', __name__, static_folder="static", template_folder="template")

@sentiments_bp.route("/sentiment_analyzer")
def sentiment_analyzer():
    return render_template('sentiment_analyzer.html')

# Main logic
class SentimentAnalysis:

    # 
    def __init__(self):
        self.tweets = []
        self.tweetText = []


    def DownloadData(self, keyword, tweets):
        consumerKey = 'get your consumer key from twitter'
        consumerSecret = 'get your consumerSecret from twitter'
        accessToken = 'get your access token from twitter'
        accessTokenSecret = 'get your access token secret from twitter'

        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth, wait_on_rate_limit=True)

