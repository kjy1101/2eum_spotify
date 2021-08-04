from django.shortcuts import render
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from django.conf import settings

# Create your views here.
def home(request):
    #client_id = "cf0...53e"
    #client_secret = "e90...d10"

    lz_uri = 'spotify:artist:6OwKE9Ez6ALxpTaKcT5ayv' # 악동뮤지션
    # spotify:artist:아티스트ID

    CLIENT_ID = getattr(settings, 'CLIENT_ID', None)
    CLIENT_SECRET = getattr(settings, 'CLIENT_SECRET', None)
    client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    results = sp.artist_top_tracks(lz_uri)
    return render(request, 'myspotipy/home.html', {'results':results['tracks'][:10]})