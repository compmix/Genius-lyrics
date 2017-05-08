# GeniusLyrics, a Python lyrics search & scraper.

GeniusLyrics is a Genius.com lyrics scraper written in [Python](https://www.python.org "Python homepage"). It can be run standalone, or integrated into other programs.

### How do I use it standalone?
	- get a Genius API client access token
	- put it into a token.ini file in the same directory
	- run it with Python 3

### How do I use its functions?
	- initialize GeniusLyrics with the token
	- song_url = GeniusLyrics.search(search_query) # grabs the URL of the top search result
	- lyrics = GeniusLyrics.scrape(song_url) # returns the lyrics, cleaned and scraped
	- the rest is up to you
