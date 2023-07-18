import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# Set up Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='6a3d47087f3a4581bed907de4c13959d',
                                               client_secret='24977ff97ba740b7b3bfcdbce1ace145',
                                               redirect_uri='http://localhost:3005/',
                                               scope='playlist-modify-public'))


def create_sorted_playlist(playlist_id):
    # Fetch the playlist
    playlist = sp.playlist(playlist_id)

    # Get the audio features for each track
    tracks = playlist['tracks']['items']
    features = sp.audio_features([track['track']['id'] for track in tracks])

    # Sort the tracks by BPM and key
    sorted_tracks = sorted(features, key=lambda f: (f['tempo'], f['key']))

    with open('tracks.txt', 'w') as file:
        # Print the BPM and key of each track
        for track in sorted_tracks:
            file.write(f"Track ID: {track['id']}\n")
            file.write(f"BPM:, {track['tempo']}")
            file.write(f"Key: {track['key']}\n")
            file.write('---\n')

    # Create a new playlist
    print("Track details written to tracks.txt")


# Prompt the user for the playlist ID
playlist_id = input("Enter the playlist ID: ")

# Call the function to create the sorted playlist and write track details to a text file
create_sorted_playlist(playlist_id)
