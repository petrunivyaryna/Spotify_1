"""This module is created to parse the json from Spotify.

This module works with json file which is obtained using the Spotify API.
To run this module the user must enter the name of the artist.
Using this name the module can search for artist name, artist ID,
the most popular song of the artist and available markets for this
song. Then the user can choose what the module will show him.

link to github: https://github.com/yarkapetruniv/Spotify_1.git
"""
import os
import base64
import json
from requests import post, get
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    """
    This function should access token, which is used to
    make API calls on behalf the user or application.
    """
    authorization_str = client_id + ":" + client_secret
    authorization_bytes = authorization_str.encode('utf-8')
    authorization_base64 = str(base64.b64encode(authorization_bytes), 'utf-8')

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + authorization_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers = headers, data = data, timeout=1.5)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


def get_authorization_header():
    """
    This function is created to get authorization header
    everytime you have to find some new information using token.
    """
    return {"Authorization": "Bearer " + get_token()}


def search_for_artist(name: str) -> tuple:
    """
    This function input is the artist name. The function
    has to return the tuple that consists of artist name and
    artist ID.
    >>> search_for_artist("Miley Cyrus")
    ('Miley Cyrus', '5YGY8feqx7naU7z4HrwZM6')
    >>> search_for_artist("Жадан і Собаки")
    ('Zhadan i Sobaky', '2Reqc0B9PCsI6t78c9k11o')
    """
    url = "https://api.spotify.com/v1/search"
    query = f"?q={name}&type=artist&limit=1"

    query_url = url + query
    headers = get_authorization_header()
    result = get(query_url, headers = headers, timeout = 1.5)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("There is no artist with this name...")
        return None
    return json_result[0]["name"], json_result[0]["id"]


def get_song(artist_id: str) -> str:
    """
    This function should return the most popular song of the
    artist using artist's ID.
    >>> get_song('5YGY8feqx7naU7z4HrwZM6')
    'Flowers'
    >>> get_song('7Ln80lUS6He07XvHI8qqHH')
    'I Wanna Be Yours'
    """
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
    query = "?country=US"

    query_url = url + query
    headers = get_authorization_header()
    result = get(query_url, headers = headers, timeout = 1.5)
    json_result = json.loads(result.content)["tracks"]
    return json_result[0]["name"]


def get_available_markets(song, artist_id):
    """
    This function should return all countries where you can listen
    to the most popular song of the artist. It finds information about
    a song by its name and then checks that this song was written by the
    appropriate artist.
    >>> get_available_markets('Summertime Sadness', '00FQb4jTyendYWaN8pK0wa')[:15]
    ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO']
    """
    url = "https://api.spotify.com/v1/search"
    query = f"?q={song}&type=track"

    query_url = url + query
    headers = get_authorization_header()
    result = get(query_url, headers = headers, timeout = 1.5)
    json_result = json.loads(result.content)["tracks"]['items']
    for element in json_result:
        for artists in element["artists"]:
            if artists["id"] == artist_id:
                return element["available_markets"]
    return None


def get_all_albums(artist_id):
    """
    This function should return all albums of the
    appropriate artist using artist's ID.
    >>> get_all_albums('5YGY8feqx7naU7z4HrwZM6')
    ['ATTENTION: MILEY LIVE', 'Plastic Hearts', 'SHE IS COMING', 'Younger Now', \
'Miley Cyrus & Her Dead Petz', 'Bangerz (Deluxe Version)', "Can't Be Tamed", \
'The Time Of Our Lives', 'The Time Of Our Lives (International Version)', 'Breakout', \
'Meet Miley Cyrus', 'Flowers', 'Nothing Else Matters', 'WITHOUT YOU (with Miley Cyrus)']
    """
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    headers = get_authorization_header()
    result = get(url, headers = headers, timeout = 1.5)
    json_result = json.loads(result.content)['items']
    albums = []
    for album in json_result:
        if album['name'] not in albums:
            albums.append(album['name'])
    return albums
    
# my_token = get_token()
# name_of_artist = input("Enter the name of the artist: ")
# artist_name = search_for_artist(name_of_artist)[0]
# artist_id = search_for_artist(name_of_artist)[1]
# most_popular_song = get_song(artist_id)
# available_markets = get_available_markets(most_popular_song, artist_id)
# albums = get_all_albums(artist_id)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
