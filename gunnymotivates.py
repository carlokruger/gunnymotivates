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


# Add code to post to mastodon

from mastodon import Mastodon

mastodon = Mastodon(
    client_id = secrets.Mastodon_client_id,
    client_secret = secrets.Mastodon_client_secret,
    access_token = secrets.Mastodon_access_token,
    api_base_url = 'https://mastodon.social'
)

mastodon.toot(motivations.tweets[tweet])
