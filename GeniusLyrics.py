from rauth import OAuth2Service
import json

from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests


class GeniusLyrics:
    def __init__(self, client_access_token):
        self.client_access_token = client_access_token

    def search(self, song_query):
        # Generate search request
        response = requests.get("http://api.genius.com/search?access_token=" + self.client_access_token + "&q=" + song_query , headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})
        search_json = json.loads(response.text)
        song_url = search_json['response']['hits'][0]['result']['url']

        print("Retrieving lyrics from " + song_url)
        
        # Get raw lyrics for first song result
        response = requests.get(song_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})

        # Clean up html
        soup = BeautifulSoup(response.text, "html.parser")
        soup = soup.find("lyrics", class_="lyrics")
        lyrics = soup.get_text().strip()

        return lyrics


if __name__ == '__main__':
    f = open('token.ini', 'r+')
    tok = f.readline()
    genius = GeniusLyrics(tok)

    while True:
        query = input('What song to search lyrics for? ')
        
        try:
            lyrics = genius.search(query)
            print(lyrics + '\n')
        except:
            print("Error obtaining lyrics")

#TODO: fix proper authentication
