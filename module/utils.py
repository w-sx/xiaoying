from module.db_process import StarDict
import os

SEARCH_ORDER = 'oxford desc, collins desc, word, frq, bnc'
TAG_NAME = {
	'ielts':'雅思',
	'toefl':'托福',
	'gre':'GRE',
	'ky':'考研',
	'cet6':'六级',
	'cet4':'四级',
	'gk':'高考',
	'zk':'中考',
}
POS_NAME = {
	'n':'名词',
	'v':'动词',
	'i':'介词',
	'j':'形容词',
	'a':'形容词',
	'r':'副词',
	'p':'代词',
	'u':'感叹词',
}
EXCHANGE_NAME = {
	'0':'原型',
	'1':'原自',
	's':'复数',
	'r':'比较级',
	't':'最高级',
	'3':'第三人称单数',
	'i':'现在分词',
	'd':'过去分词',
	'p':'过去式',
}

def open_db(db_name:str) -> StarDict:
	if not os.path.exists(db_name): return
	return StarDict(db_name)

def search_result(db,keyword,cn=False,limit=20,offset=0):
	if len(keyword)<1: return []
	if len(db.strip_word(keyword))<1: cn = True
	print(db.strip_word(keyword))
	result = db.match_word(keyword,cn=cn,suffix='%',limit=limit,offset=offset,order=SEARCH_ORDER,select='word,translation')
	if offset==0:
		for i in range(len(result)):
			if result[i]['word']==keyword:
				result=[result[i]]+result[:i]+result[i+1:]
				break
	return result

def process_search_result(result):
	data = []
	for i in range(len(result)): data.append(result[i]['word']+'\n'+result[i]['translation'])
	return data

def word_detail(db,keyword):
	word = db.get_word(keyword)
	if len(word)!=1: return
	return word[0]

def process_word_detail(word):
	if not word: return []
	print(word)
	data = []
	m = word['word']
	if len(word['phonetic'])>0: m+='\n('+word['phonetic']+')'
	data.append(m)
	m = ''
	if word['collins']: m+='科林斯'+str(word['collins'])+'星 '
	if word['oxford']: m+='牛津核心 '
	for i in word['tag'].strip().split(' '):
		if len(i)>0: m+=TAG_NAME[i]+' '
	if len(m)>0: data.append(m)
	if len(word['definition'])>0: data.append('英义:\n'+word['definition'])
	if len(word['translation'])>0: data.append('中义:\n'+word['translation'])
	if len(word['pos'])>0:
		tmp = word['pos'].split('/')
		m = '位置:\n'
		for i in tmp:
			j = i.split(':')
			if len(j)!=2 or len(j[0])<1 or len(j[1])<1: continue
			if j[0] in POS_NAME: m+=POS_NAME[j[0]]+' '+j[1]+'%; '
			else: data.append(j[0]+' '+j[1])
		data.append(m)
	m = ''
	if word['frq']>0: m+='FRQ '+str(word['frq'])+'; '
	if word['bnc']>0: m+='BNC '+str(word['bnc'])+'; '
	if len(m)>0: data.append('词频:\n'+m)
	if len(word['exchange'])>0:
		tmp = word['exchange'].split('/')
		m = '变形:\n'
		for i in tmp:
			j = i.split(':')
			if len(j)!=2 or len(j[0])<1 or len(j[1])<1: continue
			if j[0] in EXCHANGE_NAME:
				if j[0]=='1': j[1] = '['+(','.join([ EXCHANGE_NAME[k] for k in j[1] ]))+']'
				m+=EXCHANGE_NAME[j[0]]+' '+j[1]+'; '
			else: data.append(j[0]+' '+j[1])
		data.append(m)
	return data


def add_items(list,items,id=None):
	if len(items)<1: return
	if not id: id = list.GetCount()
	list.InsertItems(items,id)

def show_list(list,focus=True,audio=True):
	if list.GetSelection()==-1: list.SetSelection(0)
	list.Show()
	if focus: list.SetFocus()
	if audio: pass
