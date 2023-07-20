# Spotify Tempo/Key Playlist Sorter (CAPS AT 100 SONGS)

This Python application utilizes the Spotify API to retrieve songs from playlists, extract their tempo and key information, and create a new playlist that progressively increases in tempo. Additionally, it stores the generated playlist in a text file for future reference.

Features:
- Fetches songs from specified Spotify playlists using the Spotify API.
- Retrieves tempo and key information for each song.
- Generates a new playlist with the collected songs.
- Progressively increases the tempo of the playlist for an energetic listening experience.
- Stores the created playlist in a text file for easy access and sharing. (Includes track name and artist name)

This application leverages the Spotipy library, which provides a Python interface for the Spotify Web API. By combining playlist manipulation, audio analysis, and file I/O, it offers a convenient way to curate dynamic and tempo-changing playlists.

Getting started:

1. Go to the Spotify Developer Dashboard: Visit the Spotify Developer Dashboard
2. Login to your Spotify Account: If you're not already logged in, click the 'Log In' button and enter your credentials
3. Create new app details: You'll be prompted to enter a few details about your app:
  - App Name: Enter the name of your app. This can be anything you like.
  - App Description: Enter a brief description of what your app does.
  - Website: Enter the URL of your app's website. If you don't have a website for your app, you can enter a placeholder URL here.
  - Redirect URI: This is the URI where users will be redirected after they authenticate with Spotify. For local development, you can use http://localhost:3005/ or any other local URL.

5. Agree to the terms: Check the box to agree to Spotify's terms and conditions, then click 'Create' button.
6. Get your Client ID and Client Secret: Once your app is created, you'll be taken to a page with your new app's details. Here, you can find your Client ID and Client Secret, which you can use to authenticate with the Spotify API.
7. Clone this repository and then open the app in any IDE that utilizes Python
8. Replace client_id and client_secret in the code with your own ID's that can be found in step 6
9. Run the application, specifying the target playlist and other desired settings.
10. Enjoy your new tempo-progressing playlist that opens up in your Spotify and find the generated playlist stored in a text file for future use.

Feel free to customize and enhance the application according to your needs and preferences. Happy playlist creation and music exploration!
