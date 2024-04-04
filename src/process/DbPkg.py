import base.file as file
import base.network as network
import module.Dict as Dict

proxy = 'https://gh-proxy.com/'
remote_path = 'https://raw.githubusercontent.com/w-sx/xiaoying/main/database/'
local_paths = ['database',file.join('cache','download')]
file_names = ['stardict_full','stardict']

def is_has(suffix='7z'):
	r = []
	for n in file_names:
		for p in local_paths:
			f = file.join(p,n+'.'+suffix)
			if file.exists(f): r.append(f)
	return r

def get_zpkg(type=1,progress_callback=None):
	src = proxy+remote_path+file_names[type]+'.7z'
	dst = file.join(local_paths[1],file_names[type]+'.7z')
	network.get_file(src,dst,progress_callback=progress_callback)
	return dst

def convert(src,progress_callback=None):
	Dict.convert_dict(src[:-3]+'db',src)
	return src[:-3]+'db'

def install(src):
	dst = file.join('database',file.basename(src))
	if src==dst: return True
	file.move(src,dst)
	return True

def clear():
	for i in is_has('7z'): file.remove(i)
	for i in is_has('csv'): file.remove(i)
