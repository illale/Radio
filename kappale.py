import requests as req
import json
import time

start = time.time()

url = "https://nrj.fi/webplayer/json/energy.json"
data = req.get(url)

f = data.text


jonne = f.split(",")

es = json.loads(f)
print(es["current_item"]["artist"] + ": " + es["current_item"]["song"])
#Radiorock ja Suomi-Pop artisti ja kappale
#print(es["items"][0]["artist"] + ": " + es["items"][0]["song"])

#Suomi-Rockin, Iskelmän ja Novan artisti ja kappale
#print(es["song"]["artist"] + ": " + es["song"]["title"])

#print(es["data"]["performer"] + ": " + es["data"]["title"])

end = time.time()

print(end - start)
