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
from requests import post
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


my_token = get_token()



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
