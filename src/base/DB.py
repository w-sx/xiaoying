import sqlite3, json, re

class DB:

	def __init__(self,filename,table=None,fields=None):
		self.__dbname = filename
		self.TABLE = table
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
		#print(query['sql'],query['data'])
		return self.__result_json(self.exec(query['sql'],query['data']),toText,fields=fields)

	def __result_json(self,datas,toText=False,fields=None):
		result = []
		if not fields: fields = self.FIELDS
		if not fields:
			if toText: return json.dumps(datas)
			else: return datas
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

	def query_easy(self,data,toText=False,select='*',table=None,condition=None,order=None,limit=None,offset=None):
		if len(data)<1: return
		if not table: table = self.TABLE
		if not table: return
		data[0] = ' ( '+data[0]+' ) '
		if condition: data[0]+=condition
		if order: data[0]+=' order by '+order+' '
		if limit: data[0]+='limit '+str(limit)+' '
		if offset: data[0]+='offset '+str(offset)+' '
		query = {}
		query['sql'] = 'select '+select+' from '+table+' where ' + data[0]
		query['data'] = data[1:]
		return self.query_json(json.dumps(query),toText=toText,)



