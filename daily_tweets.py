# this is a work in progress do not use. 

import csv
import tweepy

# Twitter API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# Authenticate to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Keep track of the last row tweeted
last_row = 0
try:
    with open('last_row.txt', 'r') as file:
        last_row = int(file.read().strip())
except:
    pass

# Open the csv file
with open('tweets.csv', 'r') as file:
    reader = csv.reader(file)
    # Read all rows of the csv file
    rows = [row for row in reader]
    # Check if there are any new rows to tweet
    if last_row < len(rows) - 1:
        # Update the last row tweeted
        last_row += 1
        with open('last_row.txt', 'w') as file:
            file.write(str(last_row))
        # Post the new tweet
        api.update_status(rows[last_row][0])
