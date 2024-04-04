import requests
import base.file as file

def get_file(src,dst,data=None,progress_callback=None):
	file.mkdir(file.dirname(dst))
	with get_responding(src,data,stream=True) as r, open(dst,'wb') as f:
		if 'Content-Length' in r.headers: size = int(r.headers['Content-Length'])
		else: size = -1	
		cursor=0
		for d in r.iter_content(chunk_size=1024):
			cursor+=len(d)
			if progress_callback: progress_callback(cursor,size)
			f.write(d)

def get_text(src,data=None,encoding='utf-8'):
	content = get_content(src,data)
	if not content or len(content)<1: return
	return content.decode(encoding=encoding)

def get_content(src,data=None):
	r = get_responding(src,data)
	content = r.content
	r.close()
	return content

def get_size(src,data=None):
	r = get_responding(src,data,True)
	if 'Content-Length' in r.headers: size = int(r.headers['Content-Length'])
	else: size = 0
	r.close()
	return size


def get_responding(src,data=None,stream=False):
	if data: r = requests.post(src,data=data,stream=stream)# post method
	else: r = requests.get(src,stream=stream) # get method
	return r
