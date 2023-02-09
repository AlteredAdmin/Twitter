# Twitter
 Twitter Scripts

## work in progress do not use.

Create a CSV file with the tweets you want to post. The file should have only one column, which is the tweet text. Each row represents a tweet that you want to post.

Replace the placeholder values in the script with your Twitter API credentials. You can obtain your Twitter API credentials from the Twitter Developer Dashboard (https://developer.twitter.com/en/apps).

Save the script with a .py extension, for example daily_tweets.py.

Open the command line or terminal and navigate to the directory where you saved the script.

Run the script by typing python daily_tweets.py and press enter. If there are any tweets in the CSV file that haven't been posted yet, the script will post the next tweet in the file and store the last row tweeted in the last_row.txt file.

To post a new tweet each day, you can set up a task scheduler or a cron job to run the script automatically at a specific time each day.

Note: Make sure you have the required libraries installed. You can install the tweepy library by running pip install tweepy in the command line or terminal.