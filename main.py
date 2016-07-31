from rauth import OAuth2Service
import json

from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests


class GeniusLyrics:
	def __init__(self, client_access_token):
		self.client_access_token = client_access_token

	def search(self, song_query):
		response = requests.get("http://api.genius.com/search?access_token=" + self.client_access_token + "&q=" + song_query , headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})
		search_json = json.loads(response.text)
		song_url = search_json['response']['hits'][0]['result']['url']
		response = requests.get(song_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})
		soup = BeautifulSoup(response.text, "lxml")
		lyrics = soup.find("div", class_="song_body-lyrics").get_text()
		return lyrics


if __name__ == '__main__':
	f = open('token.ini', 'r+')
	tok = f.readline()
	genius = GeniusLyrics(tok)

	print(tok)

	while True:
		query = input('What song to search lyrics for? ')
		lyrics = genius.search(query)
		print(lyrics)
