"""
Instructions --

- Within the for loop for index, row in df.iterrows():, the code currently increases the value of clinton by 1 each time a tweet 
mentioning 'Clinton' is encountered; complete the code so that the same happens for trump, sanders and cruz.
"""

# Initialize list to store tweet counts
[clinton, trump, sanders, cruz] = [0, 0, 0, 0]

# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])
