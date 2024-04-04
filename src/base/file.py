import os
from py7zr import SevenZipFile
from functools import partial

def join(*args):
	return os.path.join(*args)

def exists(path,type=0):
	""" Type: 0 is exists, 1 is file, 2 is dir."""
	if type==0: return os.path.exists(path)
	if type==1: return os.path.isfile(path)
	if type==2: return os.path.isdir(path)

def get_size(path):
	return os.path.getsize(path)

def convert_size(size):
	d = ['B','K','M','G','T']
	i = 0
	while size/(1024**i)>1024: i+=1
	return str(round(size/(1024**i),2))+d[i]


def dirname(path):
	return os.path.dirname(path)

def basename(path):
	return os.path.basename(path)

def get(path):
	if not exists(path): return
	with open(path,'rb') as f: return f.read()

def put(path,data):
	mkdir(dirname(path))
	with open(path,'wb') as f: f.write(data)

def remove(path):
	return os.remove(path)

def mkdir(path):
	if len(path)>0 and not exists(path,2): return os.makedirs(path)

def move(src,dst):
	return os.rename(src,dst)

def copy(src,dst):
	if not exists(src,1): return False
	if dst[-1]=='\\' or dst[-1]=='/': dst+=basename(src)
	mkdir(dirname(dst))
	with open(src,'rb') as s, open(dst,'wb') as d:
		for i in __chunked_reader(s): d.write(i)
	return True

def un7z(src,dst=None):
	if not exists(src,1): return
	if not dst: dst = dirname(src)
	mkdir(dst)
	with SevenZipFile(src,mode='r') as z: z.extractall(path=dst)

def __chunked_reader(file, block_size=1024*8):
	for chunk in iter(partial(file.read, block_size), b''):
		yield chunk
