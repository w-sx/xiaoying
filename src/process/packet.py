from py7zr import SevenZipFile
import base.file as file

def unzip(name):
	if not file.exists(name): return
	with SevenZipFile(name,mode='r') as z:
		z.extractall(path=file.dirname(name))
	return True
