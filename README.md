# ParseiOSSpotify

Quick script to parse the recently_played.bnk file found in the iOS Spotify app directory.

Three scripts.
build_proto.bat builds the proto file using the protoc executable from Google.
parse_recently_played.py uses the outputted python library to parse a recently_played.bnk file from an iOS backup
get_track.py queries a track listing using the Spotify API (requires you to register a developer app and put in the api key and secret)
