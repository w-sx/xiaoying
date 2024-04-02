import base.network as network
import base.file as file
import base.media as media

API = 'http://dict.youdao.com/dictvoice?'

def get_src(word,type):
	return API+'audio='+word+'&type='+str(type)

def get_dst(word,type):
	return 'cache/audio/yd_'+str(type)+'_'+word+'.mp3'

def get_audio(word,type):
	src = get_src(word,type)
	dst = get_dst(word,type)
	if not file.exists(dst): return network.get_file(src=src,dst=dst)
	return dst

	def youdao_audio(word,type=2,cache=False):
		src = 'audio='+word+'&type='+str(type)
		dst = 'cache/phonetic/yd_'+str(type)+'_'+word+'.mp3'
		API.YOUDAO_DST = dst
		if not os.path.exists(dst): dst = API.download_file(src,dst)
		if API.YOUDAO_DST!=dst: return
		if not cache: return API.play_sound(dst)

def play(word,type=2,mute=False):
	dst = get_audio(word,type)
	if not mute: media.music(dst)
	return dst
