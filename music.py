import vlc

url = "http://www.yle.fi/livestreaming/ylex.asx"

instance = vlc.Instance("--input-repeat=-1", "--fullscreen")

player = instance.media_player_new()
media = instance.media_new("https://yleuni-f.akamaihd.net/i/yleliveradiohd_2@113879/index_64_a-p.m3u8?sd=10&rebase=on")
player.set_media(media)
player.play()	

while True:
	pass