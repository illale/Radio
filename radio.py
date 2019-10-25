import vlc
import tkinter

CHANNELS = {
	"YLEX": "https://yleuni-f.akamaihd.net/i/yleliveradiohd_2@113879/index_64_a-p.m3u8?sd=10&rebase=on",
	"NOVA": "http://stream.bauermedia.fi/radionova/radionova_64.aac",
	"SUOMI": "http://stream.bauermedia.fi/suomirock/suomirock_64.aac", 
	"NRJ": "http://cdn.nrjaudio.fm/adwz1/fi/35001/mp3_128.mp3",
	"ISKELMÄ": "http://stream.bauermedia.fi/iskelma/iskelma_64.aac",
	"PUHE": "https://yleuni-f.akamaihd.net/i/yleliveradiohd_5@113882/segment157203920_128_a-p.ts?sd=10&rebase=on"
}

CHANNEL_URL = CHANNELS["YLEX"]
PLAY = [True]

def init_Window(title_name="Radio"):
	window = tkinter.Tk()
	window.title(title_name)
	window.geometry("320x480")
	window.resizable(0, 0)
	return window
	
def create_Label(string, window, x, y):
	return tkinter.Label(window, text = string).grid(row = y, column = x)
	
def button_Handler(name):
	global CHANNEL_URL
	CHANNEL_URL = CHANNELS[name]
	print(name)
	PLAY[0] = False
	
def init_Frames(window):
	top_frame = tkinter.Frame(window)
	bot_frame = tkinter.Frame(window)
	return top_frame, bot_frame
		
def create_Button(string, color, y, x):
	return tkinter.Button(text = string, fg = color, width = 14, height = 6, command=lambda: button_Handler(string)).grid(row = y, column = x)
	
def main():
	Instance = vlc.Instance("--input-repeat=-1", "--fullscreen")
	Player = Instance.media_player_new()
	while True:
		Media = Instance.media_new(CHANNEL_URL)
		Player.set_media(Media)
		Player.play()
		while True:
			if (PLAY[0] == False):
				Player.stop()
				Instance = vlc.Instance("--input-repeat=-1", "--fullscreen")
				Player = Instance.media_player_new()
				Media = Instance.media_new(CHANNEL_URL)
				Player.set_media(Media)
				Player.play()
				PLAY[0] = True
			window.update_idletasks()
			window.update()
		
if __name__ == "__main__":
	window = init_Window()
	canvas = tkinter.Canvas(window, bg = "black", width = 100, height = 50).grid(row = 0 , column = 0)	
	button1 = create_Button("NOVA", "black", 1, 0)
	button2 = create_Button("YLEX", "black", 1, 1)
	button3 = create_Button("SUOMI", "black", 1, 2)
	button4 = create_Button("PUHE", "black", 2, 0)
	button5 = create_Button("NRJ", "black", 2, 1)
	button6 = create_Button("ISKELMÄ", "black", 2, 2)
	main()