from rauth import OAuth2Service
import json


from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests


song_query = "song name here"

client_access_token='token here'

response = requests.get("http://api.genius.com/search?access_token=" + client_access_token + "&q=" + song_query , headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})

search = json.loads(response.text)

song_url = search['response']['hits'][0]['result']['url']
#print(song_url)

response = requests.get(song_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})

soup = BeautifulSoup(response.text, "lxml")

lyrics = soup.find("div", class_="song_body-lyrics").get_text()
#print(lyrics)


