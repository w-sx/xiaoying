from module.db_process import StarDict
import os

SEARCH_ORDER = 'oxford desc, collins desc, word, frq, bnc'

def open_db(db_name:str) -> StarDict:
	if not os.path.exists(db_name): return
	return StarDict(db_name)

def search_result(db,keyword,limit=20,offset=0):
	return db.match_word(keyword,suffix='%',limit=limit,offset=offset,order=SEARCH_ORDER,select='word,translation')

def add_item(obj,txt,id=None):
	if not id: id = obj.GetCount()
	obj.InsertItems([txt],id)

def process_search_result(obj,result):
	for i in range(len(result)): add_item(obj,result[i]['word']+'\n'+result[i]['translation'])