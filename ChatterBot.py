# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "08EqISwEDtqFEkVcBhuyOanW9"
consumer_secret = "em4eZfyTs8AQoK7wrujJ5ASVjTgduUYqvJkE29bsEqfMmrHwbS"
access_token = "971208969124327425-NVqSLKf93E0DsaMMFYJY4MwJrIUPULD"
access_token_secret = "4UFYtnJCuTd6tzDtAOwxQtpOjHSGrhjzn7A2c2LnRHCeg"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE