from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import Stream
import json
from textblob import TextBlob
import time
from unidecode import unidecode
import sqlite3
#
# analyzer = SentimentIntensityAnalyzer()

conn = sqlite3.connect('twitter.db')
c = conn.cursor()

def create_table():
    try:
        c.execute("CREATE TABLE IF NOT EXISTS sentiment(unix REAL, tweet TEXT, sentiment REAL)")
        c.execute("CREATE INDEX fast_unix ON sentiment(unix)")
        c.execute("CREATE INDEX fast_tweet ON sentiment(tweet)")
        c.execute("CREATE INDEX fast_sentiment ON sentiment(sentiment)")
        conn.commit()
    except Exception as e:
        print(str(e))

create_table()


consumer_key = 'fYrSFNIsqi7Gh9vE19uHa82Ux' #(API key)
consumer_secret = 'cd6J6hclqgOuwY4yhDQ1O5ophBHs2GdRbJEwiDeKSUC8j1S9IH' #(API secret key)
key = '40715507-SO1piyUsNBCp7aQBLRbqbBQ3QrHi4U8UyOroCce9S' #(Access token)
secret = 'bXPyWGK09gKKf5juToW9V0FePih5OVlQe7ZoLZ2vm4tyJ' #(Access token secret)

class listener(Stream):
    def on_data(self, data):
        try:
            data = json.loads(data)
            tweet = TextBlob(unidecode(data['text']))
            time_ms = data['timestamp_ms']

            if tweet.detect_language() != 'en':
                analysis = tweet.translate(to='en')
            else:
                analysis = TextBlob(tweet)
            sentiment = analysis.sentiment.polarity
            print(time_ms, tweet,  sentiment)
            c.execute("INSERT INTO sentiment (unix,  tweet, sentiment) VALUES (?, ?, ?)",
                                             (time_ms, tweet, sentiment))
            conn.commit()
        except KeyError as e:
            print(str(e))
        return True

    def on_error(self, status):
        print(status)

while True:
    try:
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(key, secret)
        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=["a", "e", "i", "o", "u"])
    except Exception as e:
        print(str(e))
        time.sleep(5)
