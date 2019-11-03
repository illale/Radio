import urllib.request as ur

url = "http://cdn.nrjaudio.fm/adwz1/fi/35001/mp3_128.mp3"

conn = ur.urlopen(url)

with open("test.txt", "wb") as target:
	i = 0
	while i < 1000000:
		target.write(conn.read(1024))