

#from rauth import OAuth2Service


from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

song_url = "http://genius.com/A-ap-rocky-suddenly-lyrics"

response = requests.get(song_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})

#print(response.text)
soup = BeautifulSoup(response.text, "lxml")


print(soup.find("div", class_="song_body-lyrics").get_text())

#	print(verse)


#for tag in soup.find_all("a", class_="referent"):
#	print(tag.get_text())

