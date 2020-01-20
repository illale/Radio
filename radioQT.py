import sys
from PyQt5.QtWidgets import QApplication, QLabel

SONGURLS = {
	"YLEX": "https://areena.api.yle.fi/v1/songs/current.json?app_id=areena_web_personal_prod&app_key=6c64d890124735033c50099ca25dd2fe&client=yle-areena-web&language=fi&v=7&serviceId=ylex",
	"SUOMI-POP": "https://supla-playlist.nm-services.nelonenmedia.fi/playlist?channel=53&next_token=&limit=20",
	"RADIO ROCK": "https://supla-playlist.nm-services.nelonenmedia.fi/playlist?channel=52&next_token=&limit=20",
	"SUOMI-ROCK": "https://www.radiosuomirock.fi/feed/onair",
	"NRJ": "https://nrj.fi/webplayer/json/energy.json",
	"NOVA": "https://www.radionova.fi/feed/onair",
	"ISKELMÄ": "https://www.iskelma.fi/feed/onair",
	"LOOP": "https://supla-playlist.nm-services.nelonenmedia.fi/playlist?channel=54&next_token=&limit=20",
	"RADIO-AALTO": "https://supla-playlist.nm-services.nelonenmedia.fi/playlist?channel=51&next_token=&limit=20",
	"HIT-MIX": "https://supla-playlist.nm-services.nelonenmedia.fi/playlist?channel=55&next_token=&limit=20",
	"HELMI-RADIO": "https://supla-playlist.nm-services.nelonenmedia.fi/playlist?channel=57&next_token=&limit=20",
	"GROOVE": "https://supla-playlist.nm-services.nelonenmedia.fi/playlist?channel=70&next_token=&limit=20",
    "BASSO-RADIO": "http://api.basso.fi/v1/now_playing.json?c=1"
}

CHANNELS = {
	"YLEX": "https://yleuni-f.akamaihd.net/i/yleliveradiohd_2@113879/index_64_a-p.m3u8?sd=10&rebase=on",
	"NOVA": "http://stream.bauermedia.fi/radionova/radionova_64.aac",
	"SUOMI-ROCK": "http://stream.bauermedia.fi/suomirock/suomirock_64.aac",
	"NRJ": "http://cdn.nrjaudio.fm/adwz1/fi/35001/mp3_128.mp3",
	"ISKELMÄ": "http://stream.bauermedia.fi/iskelma/iskelma_64.aac",
	"PUHE": "https://yleuni-f.akamaihd.net/i/yleliveradiohd_5@113882/index_128_a-p.m3u8?sd=10&rebase=on",
	"HELMI-RADIO": "https://digitacdn.akamaized.net/hls/live/629243/radiohelmi/master-128000.m3u8",
	"RADIO ROCK": "https://digitacdn.akamaized.net/hls/live/629243/radiorock/master.m3u8",
	"SUOMI-POP": "https://digitacdn.akamaized.net/hls/live/629243/radiosuomipop/master-128000.m3u8"
}

def window():
    app = QApplication([])
    b = QLabel("Hello World")
    b.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()
