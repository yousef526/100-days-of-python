from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials,SpotifyOAuth
import pprint

"http://localhost:3000"

str22 = input("Enter date formated like this YYYY-MM-DD: ")
#str22 = "2000-08-30"

bill_board = "https://www.billboard.com/charts/hot-100/"

res = requests.get(bill_board+str22)

soup = BeautifulSoup(res.text,"html.parser")

first_song = soup.find(name="a",class_="c-title__link lrv-a-unstyle-link")
rest_of_songs = soup.find_all(name="h3",id="title-of-a-story",class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
rest_of_songs.insert(0,first_song)

songs_title = [x.get_text(strip=True) for x in rest_of_songs]


##################spotify

CLIENT_ID = "0929ed0edd074819904cc066d0d656e6"
TOKEN = "6cdf9f092a4742fea3294af3cd3ad8fd"


credits = SpotifyOAuth(client_id=CLIENT_ID,client_secret=TOKEN,
                       redirect_uri="http://localhost:3000",
                       scope="playlist-modify-private",
                       show_dialog=True,
                       cache_path="./.cache")


spotify = spotipy.Spotify(auth_manager=credits)


needed_data = spotify.current_user()


#list already created
playlist_id = spotify.user_playlist_create(
    user=needed_data['id'],
    name=f"{str22} Billboard 100",
    public=False,
    description="A project where i get 100 songs on specific day and add them to list")

print()

songs_Links = []

for song_title in songs_title:
    title = "{" + song_title + "}"
    query = f"track:{title}" #year:1999" # i remove year as it may not give precise answers
    song = spotify.search(q=query,limit=1,type="track",market="US",)

    try:
        song_link = song['tracks']['items'][0]['external_urls']['spotify']
        songs_Links.append(song_link)
    except IndexError:
        pass


spotify.playlist_add_items(playlist_id=f"{playlist_id['id']}",items=songs_Links)

"""
{'display_name': 'yousef alaa',
 'external_urls': {
    'spotify': 'https://open.spotify.com/user/31ei3dy3vauocqlas3goqpsrspem'
    },
'href': 'https://api.spotify.com/v1/users/31ei3dy3vauocqlas3goqpsrspem',
'id': '31ei3dy3vauocqlas3goqpsrspem',
'images': [],
'type': 'user', 'uri': 'spotify:user:31ei3dy3vauocqlas3goqpsrspem', 'followers': 
{'href': None, 'total': 0}}"""


"""http://localhost:3000/?code=AQBJQjL5T-Hvl2hXAN7WrhC-0U21_QYShmmuXqwOvp_f2Tjnhv1uOlLkKk1X3dKiviUdEjH2xXXTk6IMxjiCOKxoHKxb2BgJhm54djSDnyEthUS0IukDeaZwgV1wfz4IaMOFJL36WPoA_F9nQcBZn-ZgECNNTotZsQ"""