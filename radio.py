import vlc
import tkinter

CHANNELS = {
	"YLEX": "https://yleuni-f.akamaihd.net/i/yleliveradiohd_2@113879/index_64_a-p.m3u8?sd=10&rebase=on",
	"NOVA": "http://stream.bauermedia.fi/radionova/radionova_64.aac",
	"SUOMI": "http://stream.bauermedia.fi/suomirock/suomirock_64.aac", 
	"NRJ": "http://cdn.nrjaudio.fm/adwz1/fi/35001/mp3_128.mp3",
	"ISKELMÄ": "http://stream.bauermedia.fi/iskelma/iskelma_64.aac",
	"PUHE": "https://yleuni-f.akamaihd.net/i/yleliveradiohd_5@113882/index_128_a-p.m3u8?sd=10&rebase=on",
	"HELMI-RADIO": "https://digitacdn.akamaized.net/hls/live/629243/radiohelmi/master-128000.m3u8",
	"RADIO ROCK": "https://digitacdn.akamaized.net/hls/live/629243/radiorock/master.m3u8",
	"SUOMI-POP": "https://digitacdn.akamaized.net/hls/live/629243/radiosuomipop/master-128000.m3u8"
}

CHANNEL_URL = CHANNELS["YLEX"]
PLAY = [True]

def init_Window(title_name="Radio"):
	window = tkinter.Tk()
	window.title(title_name)
	window.geometry("320x480")
	window.resizable(0, 0)
	return window
	
def create_Label(window, x, y, var):
	return tkinter.Label(window, textvariable=var).grid(row = y, column = x)
	
def button_Handler(name, var):
	global CHANNEL_URL
	CHANNEL_URL = CHANNELS[name]
	var.set(name)
	PLAY[0] = False
	
def init_Frames(window):
	top_frame = tkinter.Frame(window)
	bot_frame = tkinter.Frame(window)
	return top_frame, bot_frame
		
def create_Button(string, color, y, x, var):
	return tkinter.Button(text = string, fg = color, width = 14, height = 6, command=lambda: button_Handler(string, var)).grid(row = y, column = x)
	
def main():
	quit = False
	Instance = vlc.Instance("--input-repeat=-1", "--fullscreen")
	Player = Instance.media_player_new()
	while not quit:
		Media = Instance.media_new(CHANNEL_URL)
		Player.set_media(Media)
		Player.play()
		while True:
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
		
if __name__ == "__main__":
	window = init_Window()
	canvas = tkinter.Canvas(window, height = 150, width = 300, bg="black").grid(row = 0, columnspan = 3)
	var = tkinter.StringVar()
	label1 = create_Label(window, 1, 1, var)
	var.set("YLEX")
	button1 = create_Button("NOVA", "black", 2, 0, var)
	button2 = create_Button("YLEX", "black", 2, 1, var)
	button3 = create_Button("SUOMI", "black", 2, 2, var)
	button4 = create_Button("PUHE", "black", 3, 0, var)
	button5 = create_Button("NRJ", "black", 3, 1, var)
	button6 = create_Button("ISKELMÄ", "black", 3, 2, var)
	button7 = create_Button("HELMI-RADIO", "black", 4, 0, var)
	button8 = create_Button("RADIO ROCK", "black", 4, 1, var)
	button9 = create_Button("SUOMI-POP", "black", 4, 2	, var)
	main()