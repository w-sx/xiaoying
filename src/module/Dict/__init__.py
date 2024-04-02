import sqlite3,csv,os,json,sys,io

if sys.version_info[0] >= 3:
	unicode = str
	long = int
	xrange = range

def stripword(word):
	return (''.join([ n for n in word if n.isalnum() ])).lower()

# 根据文件名自动判断数据库类型并打开
def open_dict(filename):
	#if isinstance(filename, dict):
		#return DictMySQL(filename)
	#if filename[:8] == 'mysql://':
		#return DictMySQL(filename)
	if os.path.splitext(filename)[-1].lower() in ('.csv', '.txt'):
		return DictCsv(filename)
	return DictDb(filename)


# 字典转化，csv sqlite之间互转
def convert_dict(dstname, srcname):
	dst = open_dict(dstname)
	src = open_dict(srcname)
	keywords = ['oxford','collins','frq','bnc']
	dst.delete_all()
	for word in src.dumps():
		data = src[word]
		for keyword in keywords:
			x = data[keyword]
			if isinstance(x, int) or isinstance(x, long):
				if x <= 0:
					data[keyword] = None
			elif isinstance(x, str) or isinstance(x, unicode):
				if x == '' or x == '0':
					data[keyword] = None
		dst.register(word, data, False)
	dst.commit()
	return True


from module.Dict.DictDb import DictDb
from module.Dict.DictCsv import DictCsv