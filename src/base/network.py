import requests
import base.file as file

def get_file(src,dst,data=None):
	content = get_content(src,data)
	if not content: return
	file.save(dst,content)
	return dst

def get_text(src,data=None,encoding='utf-8'):
	content = get_content(src,data)
	if not content: return
	return content.decode(encoding=encoding)

def get_content(src,data=None,timeout=5):
	if data: r = requests.post(src,data=data,timeout=timeout)# post method
	else: r = requests.get(src,timeout=timeout) # get method
	if r.status_code!=200: return
	return r.content
