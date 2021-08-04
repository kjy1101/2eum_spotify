from django.shortcuts import render
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

# Create your views here.
def home(request):
    client_id = "cf0635b8ba9c4fb79c950f97b20e353e"
    client_secret = "e90c4d2d65454b2f8c6f0a801bea8d10"

    lz_uri = 'spotify:artist:6VuMaDnrHyPL1p4EHjYLi7' # Charlie Puth
    # spotify:artist:아티스트ID

    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    results = sp.artist_top_tracks(lz_uri)
    return render(request, 'myspotipy/home.html', {'results':results['tracks'][:10]})