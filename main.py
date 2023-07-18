import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='6a3d47087f3a4581bed907de4c13959d',
                                               client_secret='24977ff97ba740b7b3bfcdbce1ace145',
                                               redirect_uri='your-app-redirect-url',
                                               scope='playlist-modify-public'))

# Fetches the playlist
playlist_id = 'https://open.spotify.com/playlist/7M9KR4x7tVyl6wi9t9vHNB?si=663ac5f3d2e9414c'
playlist = sp.playlist(playlist_id)

# Get the audio features for each track
tracks = playlist['tracks']['items']
features = sp.audio_features([track['track']['id'] for track in tracks])

# Sort the tracks by BPM and key
sorted_tracks = sorted(features, key=lambda f: (f['tempo'], f['key']))

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
