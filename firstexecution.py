from googleapiclient.discovery import build

api_key = 'AIzaSyA8B7HascL7gfk7MVITyfxOONb1IQzp5N8'

youtube = build('youtube', 'v3', developerKey=api_key)

detailsrequest = youtube.channels().list(
  part = 'contentDetails, statistics',
  forUsername = 'sentdex'
)

playlistrequest = youtube.playlists().list(
  part = 'contentDetails, snippet',
  channelId = "UCfzlCWGWYyIQ0aLC5w48gBQ"
)

oneplaylistrequest = youtube.playlistItems().list(
  part = 'contentDetails',
  playlistId = "PLQVvvaa0QuDcBby2qVDsDv41GghEQfr5E"
)

detailsresponse = detailsrequest.execute()
playlistresponse = playlistrequest.execute()
oneplaylistresponse = oneplaylistrequest.execute()

print(detailsresponse)
print(playlistresponse)
print(oneplaylistresponse)

for item in playlistresponse['items']:
  print(item)
  print()

for item in oneplaylistresponse['items']:
  videoId = item['contentDetails']['videoId']
  print(videoId)
  print()
