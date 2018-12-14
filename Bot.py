import tweepy

consumer_key = 'EkvQKOF6xSoii3zbHitaRXLdj'
consumer_secret_key = 'awU4fu6vT0IrMXCsorzLCTJ4aYXQ5Uz5pzoUUkZVEaz8lKC3UZ'
access_token = '1072357974331539456-6WcRGW7aj7hI8uzGhrTWMjx4PSuxlm'
access_token_secret = '2mkWmYZO1OUUcWaM2UvVh7NvXyuKZDFtTB7JZtRhsHG3M'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()

userIDList = []

def reTweeter():
    search_word = "Christmas"
    number_of_tweets = 50
    for tweet in tweepy.Cursor(api.search, search_word).items(number_of_tweets):
        try:
            tweet.retweet()
            userIDList.append(tweet.user.id)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


reTweeter()
for ID in userIDList:
    try:
        api.send_direct_message(ID, 'Merry Christmas')
    except tweepy.error.TweepError:
        print('whoops fake ID')
    finally:
        break

print('done tweeting')