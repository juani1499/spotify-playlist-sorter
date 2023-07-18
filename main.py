import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# Set up Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='CLIENT_ID',
                                               client_secret='CLIENT_SECRET',
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

    # Prompt the user for the playlist name
    playlist_name = input("What would you like to call the created playlist?: ")

    # Create a new playlist
    user_id = sp.me()['id']  # get the current user's ID
    new_playlist = sp.user_playlist_create(user_id, playlist_name)

    sp.playlist_add_items(new_playlist['id'], [track['id'] for track in sorted_tracks])

    with open('tracks.txt', 'w') as file:
        # Print the BPM and key of each track
        for track in sorted_tracks:
            file.write(f"Track ID: {track['id']}\n")
            file.write(f"BPM: {track['tempo']}\n")
            file.write(f"Key: {track['key']}\n")
            file.write('---\n')

    # Create a new playlist
    print("Track details written to tracks.txt")
    print(f"Playlist '{playlist_name}' created successfully!")


# Prompt the user for the playlist ID
playlist_id = input("Enter the playlist ID you would like to mix: ")

# Call the function to create the sorted playlist and write track details to a text file
create_sorted_playlist(playlist_id)
