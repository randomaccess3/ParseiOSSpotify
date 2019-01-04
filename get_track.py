import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
from sys import argv

script, first = argv

CLIENT_ID='<ENTER CLIENT ID>'
CLIENT_SECRET='<ENTER CLIENT SECRET>'

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#take first argument as trackid
trackid = first
urn = 'spotify:track:'+trackid
track_info = sp.track(urn)
#print (track_info)

#check if its a list, otherwise will miss artists
artist_name = track_info['album']['artists'][0]['name']
song_name = track_info['name']
print (artist_name + ", " + song_name)
