# YOU TUBE PROJECT 
from googleapiclient.discovery import build

cid="UCkHdBeQ4DuvBXTahMYZVlMA"

api_key = 'AIzaSyCWSqX8gXL-2fCzkJx4XKjg6QoWAcn38Iw'  # Replace with your generated API key
youtube = build('youtube', 'v3', developerKey=api_key)
request = youtube.channels().list(part=["snippet,contentDetails,statistics"], id=cid)
response = request.execute()
print(response)

# pip install google-api-python-client
