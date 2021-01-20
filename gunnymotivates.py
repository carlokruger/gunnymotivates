import motivations
import random
import tweepy
import secrets

# Authenticate to Twitter
auth = tweepy.OAuthHandler(secrets.APIkey, secrets.APIsecret)
auth.set_access_token(secrets.AccessToken, secrets.AccessSecret)

# Create API object
api = tweepy.API(auth)

# Create a tweet

tweet = random.randint(0, 63)
api.update_status(motivations.tweets[tweet])
