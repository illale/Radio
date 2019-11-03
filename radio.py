import vlc
import tkinter
import requests as req
import json
import time
from tkinter import font

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
	"GROOVE": "https://supla-playlist.nm-services.nelonenmedia.fi/playlist?channel=70&next_token=&limit=20"
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


CHANNEL_URL = CHANNELS["YLEX"]
PLAY = [True]
CURRENT_CHAN = "YLEX"

def get_song_info(name):
	if (name == "PUHE"):
		return "SONG INFO NOT AVAILABLE"
	url = SONGURLS[name]
	data = req.get(url)
	f = data.text
	jonne = f.split(",")
	song_info = json.loads(f)
	if len(jonne) > 2:
		if name == "YLEX":
			text =  name + "\n" + song_info["data"]["performer"] + ": " + song_info["data"]["title"]
			return text
		elif (name == "RADIO ROCK" or name == "SUOMI-POP" or name == "HELMI-RADIO"):
			text = name + "\n" + song_info["items"][0]["artist"] + ": " + song_info["items"][0]["song"]
			return text
		elif (name == "NOVA" or name == "SUOMI-ROCK" or name == "ISKELMÄ"):
			text = name + "\n" + song_info["song"]["artist"] + ": " + song_info["song"]["title"]
			return text
		elif (name == "NRJ"):
			text = name + "\n" +song_info["current_item"]["artist"] + ": " + song_info["current_item"]["song"]
			return text
		else:
			return name + "\n" + "SONG TITLE NOT AVAILABLE"

def init_Window(title_name="Radio"):
	window = tkinter.Tk()
	window.title(title_name)
	window.geometry("320x480")
	window.resizable(0, 0)
	return window

def create_Label(window, x, y, var):
	return tkinter.Label(window, textvariable=var).grid(row = y, column = x)

def button_Handler(name, var1):
	global CHANNEL_URL, CURRENT_CHAN
	if (name == "||"):
		Player.stop()
	elif (name == "I>"):
		Player.play()
	else:
		CURRENT_CHAN = name
		CHANNEL_URL = CHANNELS[name]
		PLAY[0] = False
		song = get_song_info(name)
		var1.set(song)

def init_Frames(window):
	top_frame = tkinter.Frame(window)
	bot_frame = tkinter.Frame(window)
	return top_frame, bot_frame

def create_Button(string, color, y, x, var1, w=14, h=6):
	return tkinter.Button(text = string, fg = color, width = w, height = h, command=lambda: button_Handler(string, var1)).grid(row = y, column = x)

def main(var):
	quit = False
	Instance = vlc.Instance("--input-repeat=-1", "--fullscreen")
	global Player
	Player = Instance.media_player_new()
	start = time.time()
	while not quit:
		Media = Instance.media_new(CHANNEL_URL)
		Player.set_media(Media)
		Player.play()
		while True:
			if ((time.time() - start) > 10):
				thread_Func(var, CURRENT_CHAN)
				start = time.time()
			if (PLAY[0] == False):
				Player.stop()
				Media = Instance.media_new(CHANNEL_URL)
				Player.set_media(Media)
				Player.play()
				PLAY[0] = True
			try:
				window.update_idletasks()
				window.update()
			except tkinter.TclError:
				quit = True
				break

def thread_Func(var, chan):
	song = get_song_info(chan)
	var.set(song)


if __name__ == "__main__":
	window = init_Window()
	#canvas = tkinter.Frame(window, relief="sunken",height = 140, width = 300, bg="black")
	SONG = tkinter.StringVar()
	myfont = font.Font(family="Helvetica", size=16, weight="bold")
	label3 = tkinter.Label(window, textvariable=SONG, height=6, width=20, font=myfont, bg="black", fg="green", wraplength=200).grid(row=0, column=0, columnspan=3)
	#NAME.set("YLEX")
	SONG.set(get_song_info("YLEX"))
	#for i in range(0,3):
	#	canvas.grid_columnconfigure(i, minsize=100)
	#	canvas.grid_rowconfigure(i, minsize=50)
	#canvas.grid(row = 0, columnspan = 3, pady=8, padx=8)
	button1 = create_Button("NOVA", "black", 3, 0, SONG)
	button2 = create_Button("YLEX", "black", 3, 1, SONG)
	button3 = create_Button("SUOMI-ROCK", "black", 3, 2, SONG)
	button4 = create_Button("PUHE", "black", 4, 0, SONG)
	button5 = create_Button("NRJ", "black", 4, 1, SONG)
	button6 = create_Button("ISKELMÄ", "black", 4, 2, SONG)
	button7 = create_Button("HELMI-RADIO", "black", 5, 0, SONG)
	button8 = create_Button("RADIO ROCK", "black", 5, 1, SONG)
	button9 = create_Button("SUOMI-POP", "black", 5, 2, SONG)
	button10 = create_Button("I>", "black", 1, 0, SONG, w=2, h=1)
	button11 = create_Button("||", "black", 1, 2, SONG, w=2, h=1)
	main(SONG)
