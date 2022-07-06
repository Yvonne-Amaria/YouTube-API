import requests
import json
import sqlalchemy as db
import pandas as pd
import pprint

api_key = 'AIzaSyA8B7HascL7gfk7MVITyfxOONb1IQzp5N8'
channelId = input("Enter Channel ID: ")
# videoID = input("Enter Video ID: ")

url = f'https://www.googleapis.com/youtube/v3/search?key={api_key}&channelID={channelId}&part=snippet,id&order=date'

url_json =requests.get(url).json()
channelStats = url_json['items'][0]['snippet']

print('Video Title = ' + url_json['items'][0]['snippet']['title'])
print('Date Uploaded = ' + url_json['items'][0]['snippet']['publishedAt'])


# urlForVideoStats = f'https://www.googleapis.com/youtube/v3/videos?id={videoID}&part=statistics&key={api_key}'
# url_jsonrForVideoStats = requests.get(urlForVideoStats).json()
# pprint.pprint(url_jsonrForVideoStats)
# videoStats = url_jsonrForVideoStats['items'][1]['statistics']

# print('countViews = ' + url_jsonrForVideoStats['items'][1]['statistics']['viewCount'])
# print('countLikes = ' + url_jsonrForVideoStats['items'][1]['statistics']['likeCount'])
# print('countDislikes = ' + url_jsonrForVideoStats['items'][1]['statistics']['dislikeCount'])
# print('countComments = ' + url_jsonrForVideoStats['items'][1]['statistics']['commentCount'])

df = pd.DataFrame(channelStats, index=[0])
print(df)

engine = db.create_engine('sqlite:///df.db')
df.to_sql('df', con=engine, if_exists='replace', index=False)
queryResult = engine.execute("SELECT * FROM df;").fetchall()

# af = pd.DataFrame(videoStats, index=[1])
# print(af)

# engine = db.create_engine('sqlite:///af.db')
# df.to_sql('af', con=engine, if_exists='replace', index=False)
# query_output = engine.execute("SELECT * FROM af;").fetchall()

print(pd.DataFrame(queryResult))
# print(pd.DataFrame(query_output))
