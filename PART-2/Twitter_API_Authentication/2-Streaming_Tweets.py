"""
Instructions --

- Create your Stream object with authentication by passing to tweepy.Stream() the authentication handler auth and the Stream listener l;
- To filter Twitter Streams, pass to the track argument in stream.filter() a list containing the desired keywords 'clinton', 'trump', 
'sanders', and 'cruz'.
"""

# Initialize Stream listener
l = MyStreamListener()

# Create you Stream object with authentication
stream = tweepy.Stream(auth, l)


# Filter Twitter Streams to capture data by the keywords:
stream.filter(track = ['clinton', 'trump', 'sanders', 'cruz'])
