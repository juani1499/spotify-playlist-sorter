import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='CLIENT_ID',
                                               client_secret='CLIENT_SECRET',
                                               redirect_uri='http://localhost:3005/',
                                               scope='playlist-modify-public'))


def create_sorted_playlist(playlist_id):
    # Fetch the playlist
    playlist = sp.playlist(playlist_id)

    # Get the audio features for each track
    tracks = playlist['tracks']['items']

    track_ids = [track['track']['id'] for track in tracks]
    track_names_artists_ids = [{**{'name': track['track']['name'],
                                   'artist': track['track']['artists'][0]['name']},
                                'id': track['track']['id']} for track in tracks]
    features = sp.audio_features(track_ids)

    # Sort the tracks by BPM and key
    sorted_tracks = sorted(zip(track_names_artists_ids, features), key=lambda f: (f[1]['tempo'], f[1]['key']))

    # Prompt the user for the playlist name
    playlist_name = input("What would you like to call the created playlist?: ")

    # Create a new playlist
    user_id = sp.me()['id']  # get the current user's ID
    new_playlist = sp.user_playlist_create(user_id, playlist_name)

    sp.playlist_add_items(new_playlist['id'], [track[0]['id'] for track in sorted_tracks])

    with open('tracks.txt', 'w') as file:
        # Print the BPM and key of each track
        for track, feature in sorted_tracks:
            file.write(f"Track Name: {track['name']}\n")
            file.write(f"Artist: {track['artist']}\n")
            file.write(f"BPM: {feature['tempo']}\n")
            file.write(f"Key: {feature['key']}\n")
            file.write('---\n')

    # Create a new playlist
    print("Track details written to tracks.txt")
    print(f"Playlist '{playlist_name}' created successfully!")


# Prompt the user for the playlist ID
playlist_id = input("Enter the playlist ID you would like to mix: ")

# Call the function to create the sorted playlist and write track details to a text file
create_sorted_playlist(playlist_id)
