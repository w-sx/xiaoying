import sqlite3, json, re

class DB:

	def __init__(self,filename,fields):
		self.__dbname = filename
		self.FIELDS = fields
		self.__open()

	def __del__(self): self.close()

	def __open(self): self.__dbobj = sqlite3.connect(self.__dbname,isolation_level="IMMEDIATE")

	def close(self):
		if self.__dbobj: self.__dbobj.close()
		self.__dbobj = None

	def exec(self,sql,parameters):
		cursor = self.__dbobj.cursor()
		cursor.execute(sql,parameters)
		return cursor.fetchall()

	def exec_more(self,sql): self.__dbobj.cursor().executescript(sql)

	def query_json(self,text,toText=False):
		query = json.loads(text)
		if not 'sql' in query: return
		tmp = re.findall('select\\s(.+?)\\sfrom',query['sql'])
		if len(tmp)!=1: return
		fields = None
		if tmp[0]!='*': fields = tmp[0].replace(' ','').split(',')
		if not 'data' in query: query['data'] = []
		print(query['sql'],query['data'])
		return self.__result_json(self.exec(query['sql'],query['data']),toText,fields=fields)

	def __result_json(self,datas,toText=False,fields=None):
		result = []
		if not fields: fields = self.FIELDS
		di = 0
		for data in datas:
			ci = 0
			result.append({})
			for column in data:
				result[di][fields[ci]] = column
				ci+=1
			di+=1
		if toText: return json.dumps(result)
		return result

	def query_easy(self,data,toText=False,select='*',table='stardict'):
		if len(data)<1: return
		query = {}
		query['sql'] = 'select '+select+' from '+table+' where ' + data[0]
		query['data'] = data[1:]
		return self.query_json(json.dumps(query),toText=toText,)

class StarDict(DB):

	def __init__(self, filename):
		super().__init__(filename,('id', 'word', 'sw', 'phonetic', 'definition', 'translation', 'pos', 'collins', 'oxford', 'tag', 'bnc', 'frq', 'exchange', 'detail', 'audio'))

	def get_word(self,keyword,select='*'): return self.query_easy(['word = ?',keyword],select=select)

	def match_word(self,keyword,cn=False,prefix='',suffix='',condition=None,order=None,limit=None,offset=None,select='*'):
		if cn: sql = 'translation like ? '
		else: sql = 'sw like ? '
		sql = self.__add_sql(sql,condition=condition,order=order,limit=limit,offset=offset)
		if cn: data = '%'+keyword+'%'
		else: data = prefix+self.strip_word(keyword)+suffix
		return self.query_easy([sql,data],select=select)

	def match_tags(self,tags,connective='and',condition=None,order=None,limit=None,offset=None,select='*'):
		tmp = tags.strip().split(' ')
		data = []
		for i in range(len(tmp)):
			if tmp[i][:-1]=='collins':
				data.append(int(tmp[i][-1]))
				tmp[i]='collins'
			elif tmp[i]=='oxford': data.append(1)
			else:
				data.append('%'+tmp[i]+'%')
				tmp[i]='tag'
			tmp[i]+=' like ? '
		sql = (' '+connective+' ').join(tmp)
		sql = self.__add_sql(sql,condition=condition,order=order,limit=limit,offset=offset)
		return self.query_easy([sql]+data,select=select)





	def __add_sql(self,sql,condition=None,order=None,limit=None,offset=None):
		sql = ' ( '+sql+' ) '
		if condition: sql+=condition
		if order: sql+=' order by '+order+' '
		if limit: sql+='limit '+str(limit)+' '
		if offset: sql+='offset '+str(offset)+' '
		return sql

	def strip_word(self,word):
		#return (''.join([ n for n in word if n.isalnum() ])).lower()
		return ''.join(re.findall('[a-z|A-Z|0-9]+',word))
