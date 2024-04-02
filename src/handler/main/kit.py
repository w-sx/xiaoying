import wx
import base.utils as utils
import module.star as star
import module.youdao as youdao

def add_items(list:wx.ListBox,items,id=None,clear=False):
	if clear: list.Clear()
	if not items or len(items)<1: return
	if not id: id = list.GetCount()
	list.InsertItems(items,id)

def show_list(list:wx.ListBox,focus=True,audio=True,force=False):
	if list.GetCount()<1 and not force: return
	if list.GetSelection()==-1: list.SetSelection(0)
	list.Show()
	if focus: list.SetFocus()
	if audio: pass

def hide_list(list:wx.ListBox,clear=False,ret=False,audio=True):
	if ret: list.RETURN()
	list.Hide()
	if clear: list.Clear()
	if audio: pass

def search(word,full=False,offset=0,limit=20):
	return star.process_search_result(star.search_result(word,full=full,limit=limit,offset=offset))

def detail(word):
	return star.process_word_detail(star.word_detail(word))

def audio(word,type=2):
	target = youdao.play
	args = (word,type)
	utils.thread(target=target,args=args)



