from googleapiclient.discovery import build

api_key = 'AIzaSyA8B7HascL7gfk7MVITyfxOONb1IQzp5N8'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
  part = 'statistics',
  forUsername = 'sentdex'
)

response = request.execute()

print(response)


