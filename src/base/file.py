import os

def exists(path): return os.path.exists(path)

def dirname(path):return os.path.dirname(path)

def save(dst,data):
	if len(dirname(dst))>0 and (not exists(dirname(dst))): os.makedirs(os.path.dirname(dst))
	with open(dst,'wb') as f: f.write(data)

def remove(path): return os.remove(path)
