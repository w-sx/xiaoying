import process.DbPkg as pkg
from module.Dict import convert_dict
import info
import base.utils as utils
import base.network as network
import base.file as file
import wx

INSTALL_LOCKED = False

def btn_install(list1,list2,callback):
	if INSTALL_LOCKED: return
	src = list2.GetItems()[list2.GetSelection()].split('\n')[2]
	dst = file.basename(src)
	if alert('询问','确定安装 '+dst+'?\n来源: '+src)!=wx.ID_YES: return
	utils.thread(install,(list1,list2,src,callback))

def install(list1,list2,src,callback):
	global INSTALL_LOCKED
	INSTALL_LOCKED = True
	if 'https:' in src:
		add_items(list1,['准备下载 '+src,'使用代理 '+pkg.proxy],clear=False,jump=True)
		dst = file.join('cache','download',file.basename(src))
		network.get_file(pkg.proxy+src,dst,progress_callback=callback)
		add_items(list1,['下载完成 '+dst],clear=False,jump=True)
		btn_get(list1,list2,ve=False,re=False)
		return install(list1,list2,dst,callback)
	elif src[-2:]=='7z':
		add_items(list1,['准备解压 '+src],clear=False,jump=True)
		dst = src[:-2]+'csv'
		file.un7z(src)
		btn_get(list1,list2,ve=False,re=False)
		if file.exists(dst):
			add_items(list1,['解压完成 '+dst],clear=False,jump=True)
			return install(list1,list2,dst,callback)
		else:
			add_items(list1,['解压失败 '+dst],clear=False,jump=True)
			return
	elif src[-3:]=='csv':
		add_items(list1,['转换数据 '+src],clear=False,jump=True)
		dst = file.join('database',file.basename(src)[:-3]+'db')
		convert_dict(dst,src,callback)
		btn_get(list1,list2,ve=False,re=False)
		if file.exists(dst):
			add_items(list1,['成功生成 '+dst],clear=False,jump=True)
			return install(list1,list2,dst,callback)
		else:
			add_items(list1,['生成失败 '+dst],clear=False,jump=True)
			return
	else:
		add_items(list1,['完成'],clear=False,jump=True)
		INSTALL_LOCKED = False
		btn_get(list1,list2,ve=False,re=False)

def btn_remove(list1,list2):
	src = list2.GetItems()[list2.GetSelection()].split('\n')[2]
	if alert('询问','确认删除 '+src+'？')!=wx.ID_YES: return
	file.remove(src)
	btn_get(list1,list2,ve=False)
	add_items(list1,['删除 '+src],jump=True,clear=False)

def btn_get(list1,list2,lo=True,re=True,ve=True):
	utils.thread(get_info,(list1,list2,lo,re,ve))

def get_info(list1,list2,lo,re,ve):
	if ve:
		r = []
		r.append(info.NAME+' Version '+info.VERSION)
		r.append('By '+info.AUTHOR+' '+info.EMAIL)
		add_items(list1,r)
	if lo:
		r = []
		r+=is_has('db')
		r+=is_has('csv')
		r+=is_has('7z')
		add_items(list2,r)
	if re: add_items(list2,get_network_db(),clear=False,jump=True)

def is_has(k):
	d = {'db':'数据库','csv':'数据表','7z':'数据包'}
	if not k in d: return []
	t = pkg.is_has(k)
	r = [d[k]+' '+str(len(t))]
	for i in t: r.append(file.basename(i)+'\n'+'大小 '+file.convert_size(file.get_size(i))+'\n'+i)
	return r

def get_network_db():
	r = ['可下载 '+str(len(pkg.file_names))]
	for i in pkg.file_names: r.append(i+'.7z\n'+'大小 '+file.convert_size(network.get_size(pkg.proxy+pkg.remote_path+i+'.7z'))+'\n'+pkg.remote_path+i+'.7z')
	return r

def add_items(list,data,id=None,clear=True,jump=False):
	if clear: list.Clear()
	if not id: id = list.GetCount()
	list.InsertItems(data,id)
	if list.GetSelection()<0: list.SetSelection(0)
	if jump: list.SetSelection(list.GetCount()-len(data))

def alert(title,message,btn=wx.YES_NO|wx.CANCEL):
	dlg = wx.MessageDialog(None,message,title,btn)
	r = dlg.ShowModal()
	dlg.Destroy()
	return r
