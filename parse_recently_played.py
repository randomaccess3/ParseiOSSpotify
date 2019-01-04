
# Script to parse the recently_played.bnk protobuf encoded file from an iOS backup
# Partially appropriated from the protobuf AddressBook example - Thanks Google for providing that

# Copyright 2019 Phill Moore - randomaccess3@gmail.com

import recently_played_pb2
import sys
from datetime import datetime


#timestamps are recorded in UTC

def ListRecents(spotify):
	for a1 in spotify.a:
		timestamp = str(a1.timestamp)
		timestamp_formatted = datetime.utcfromtimestamp(a1.timestamp).strftime('%Y-%m-%d %H:%M:%S')
		album = a1.album
		track = a1.track
		if (track == ""):
			track_url = ""
		else:
			track_url = "http://embed.spotify.com/?uri=" + track
			
		list = "album_list"
		
		print (timestamp + "," + timestamp_formatted + "," + album + "," + track + "," + track_url+ "," + list)
		
	for t1 in spotify.t:
		timestamp = str(t1.timestamp)
		timestamp_formatted = datetime.utcfromtimestamp(t1.timestamp).strftime('%Y-%m-%d %H:%M:%S')
		album = ""
		track = t1.track
		if (track == ""):
			track_url = ""
		else:
			track_url = "http://embed.spotify.com/?uri=" + track
		list = "track_list"
		print (timestamp + "," + timestamp_formatted + "," + album + "," + track + "," + track_url+ "," + list)
	

# Main procedure:  Reads the entire contents from a file and prints all
#   the information inside.
if len(sys.argv) != 2:
	print("Usage:", sys.argv[0], "spotify_FILE")
	sys.exit(-1)

spotify = recently_played_pb2.recently_played()

# Read the existing file
with open(sys.argv[1], "rb") as f:
	spotify.ParseFromString(f.read())

ListRecents(spotify)
