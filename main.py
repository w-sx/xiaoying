# the file defined some UI events handler
# All functions defined in this file will be passed to the MainUI object
# when the MainUi class is instantiated

from module.utils import *
from module.main_ui import MainUi
from wx import App as Application

def __ui_show(e):
	MAINUI.DB = open_db('./database/stardict.db')
	e.Skip()

def __ui_close(e):
	MAINUI.DB.close()
	e.Skip()

def __search_text_enter(e):
	add_items(MAINUI.detail_list,process_word_detail(word_detail(MAINUI.DB,MAINUI.search_editor.GetValue())))
	MAINUI.detail_list.RETURN = MAINUI.search_editor.SetFocus
	if MAINUI.detail_list.GetCount()>0: show_list(MAINUI.detail_list)
	e.Skip()

def __search_text(e):
	MAINUI.search_editor.CN = False
	MAINUI.result_list.Hide()
	MAINUI.result_list.Clear()
	MAINUI.result_list.MAX_NO = 0
	e.Skip()

def __result_listbox(e):
	if e.GetInt()+1==MAINUI.result_list.GetCount() and MAINUI.result_list.MAX_NO != MAINUI.result_list.GetCount():
		MAINUI.result_list.MAX_NO = MAINUI.result_list.GetCount()
		add_items(MAINUI.result_list,process_search_result(search_result(MAINUI.DB,MAINUI.search_editor.GetValue(),cn=MAINUI.search_editor.CN,offset=MAINUI.result_list.GetCount())))
	e.Skip()

def __search_keydown(e):
	if (e.GetModifiers()==0 or e.GetModifiers()==2) and e.GetKeyCode()==317:
		if e.GetModifiers()==2: MAINUI.search_editor.CN = True
		if len(MAINUI.search_editor.GetValue())>0:
			if MAINUI.result_list.GetCount()==0: add_items(MAINUI.result_list,process_search_result(search_result(MAINUI.DB,MAINUI.search_editor.GetValue(),cn=MAINUI.search_editor.CN)))
		if MAINUI.result_list.GetCount()>0: show_list(MAINUI.result_list)
	#if e.GetKeyCode()==27 and e.GetModifiers()==0: MAINUI.search_editor.SetValue('')
	e.Skip()

def __result_keydown(e):
	if e.GetKeyCode()==315 and e.GetModifiers()==0:
		if MAINUI.result_list.GetSelection()==0: MAINUI.search_editor.SetFocus()
	e.Skip()

def __result_keyup(e):
	if e.GetKeyCode()==13 and e.GetModifiers()==0:
		add_items(MAINUI.detail_list,process_word_detail(word_detail(MAINUI.DB,MAINUI.result_list.GetStringSelection().split('\n')[0])))
		MAINUI.detail_list.RETURN = MAINUI.result_list.SetFocus
		if MAINUI.detail_list.GetCount()>0: show_list(MAINUI.detail_list)
	e.Skip()

def __detail_keyup(e):
	if e.GetKeyCode()==27 and e.GetModifiers()==0: MAINUI.detail_list.Hide()
	e.Skip()

def __detail_kill_focus(e):
	if not MAINUI.IsActive(): return
	if MAINUI.detail_list.RETURN: MAINUI.detail_list.RETURN()
	MAINUI.detail_list.Hide()
	MAINUI.detail_list.Clear()
	MAINUI.detail_list.RETURN = None
	e.Skip()

# program entry point
if __name__=='__main__':
	APPLICATION = Application()
	MAINUI = MainUi(
		ui_show=__ui_show,
		ui_close=__ui_close,
		search_text_enter=__search_text_enter,
		search_text=__search_text,
		result_listbox=__result_listbox,
		search_keydown=__search_keydown,
		result_keydown=__result_keydown,
		result_keyup=__result_keyup,
		detail_keyup=__detail_keyup,
		detail_kill_focus=__detail_kill_focus,
	)
	MAINUI.Show()
	APPLICATION.MainLoop()