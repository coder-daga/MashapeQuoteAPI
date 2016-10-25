'''
Program: Python code to retrive famous or movie quote using mashape API (https://market.mashape.com/andruxnet/random-famous-quotes)
Python version: 2.7
'''


import unirest
# These code snippets use an open-source library.

category=raw_input("Enter your desired category. Type either 'movies' or 'famous':\n");
print('You have asked for '+category + ' quote.\n');

our_url="https://andruxnet-random-famous-quotes.p.mashape.com/?cat="+category

#enter your own mashape key in place of 'XXXX'. unirest returns a dictionary
response = unirest.post(our_url,
  headers={
    "X-Mashape-Key": "XXXX",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  }
)

#iterating through dictionary
for key in response.body:
	print(key + ' : ' + response.body[key])
