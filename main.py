import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# Set up Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='client_id',
                                               client_secret='client_secret',
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

    # Print the BPM and key of each track
    for track in sorted_tracks:
        print('Track ID:', track['id'])
        print('BPM:', track['tempo'])
        print('Key:', track['key'])
        print('---')

    # Create a new playlist
    user_id = sp.me()['id']  # get the current user's ID
    new_playlist = sp.user_playlist_create(user_id, 'My Sorted Playlist')

    # Add the sorted tracks to the new playlist
    sp.playlist_add_items(new_playlist['id'], [track['id'] for track in sorted_tracks])


# Prompt the user for the playlist ID
playlist_id = input("Enter the playlist ID: ")

# Call the function to create the sorted playlist
create_sorted_playlist(playlist_id)
