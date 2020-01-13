import requests as req

segments = []
audio_data = []

url0 = "https://digitacdn.akamaized.net/hls/live/629243/radiorock/"
url = "https://digitacdn.akamaized.net/hls/live/629243/radiorock/master-128000.m3u8"

response = req.get(url)

data = response.text


parsed = data.splitlines()
for line in parsed:
    if (line[0] == "#"):
        continue
    else:
        segments.append(line)

for i in range(len(segments)):
    print(url0 + segments[i])

    audio = req.get(url0 + segments[i])
    audio_data.append(audio.content)


with open("music.aac", "wb") as target:
    for obj in audio_data:
        target.write(obj)
