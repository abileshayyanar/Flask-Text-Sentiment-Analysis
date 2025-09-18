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

    # Constructor
    def __init__(self):
        self.tweets = []
        self.tweetText = []

    # Function to connect to tweepy api and download tweet data
    def DownloadData(self, keyword, tweets):

        neutral = 0
        polarity = 0

        #variables for positive sentiment
        pos = 0
        strong_pos = 0
        weak_pos = 0
        
        # variables for negative sentiment
        neg = 0
        strong_neg = 0
        weak_neg = 0

        consumerKey = 'get your consumer key from twitter'
        consumerSecret = 'get your consumerSecret from twitter'
        accessToken = 'get your access token from twitter'
        accessTokenSecret = 'get your access token secret from twitter'

        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth, wait_on_rate_limit=True)

        tweets = int(tweets)

        # Search for tweets
        self.tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="en").items(tweets)

        # Open a file to append to
        csvFile = open('results.csv', 'a')
        # Use csv writer
        csvWriter = csv.writer(csvFile)




