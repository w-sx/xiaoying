# the file defined some UI events handler
# All functions defined in this file will be passed to the MainUI object
# when the MainUi class is instantiated

from module.utils import *
from module.main_ui import MainUi
import wx

def __ui_show(e):
	MAINUI.DB = open_db('./database/stardict.db')
	e.Skip()

def __ui_close(e):
	MAINUI.DB.close()
	e.Skip()

def __search_text_enter(e):
	print(MAINUI.DB.get_word(MAINUI.search_editor.GetValue()))
	e.Skip()

def __search_text(e):
	MAINUI.result_list.Clear()
	MAINUI.result_list.MAX_NO = 0
	if len(MAINUI.search_editor.GetValue())>0:
		result = search_result(MAINUI.DB,MAINUI.search_editor.GetValue())
		for i in range(len(result)):
			if result[i]['word']==MAINUI.search_editor.GetValue():
				result=[result[i]]+result[:i]+result[i+1:]
				break
		process_search_result(MAINUI.result_list,result)
	if MAINUI.result_list.GetCount()<1: MAINUI.result_list.Hide()
	else:
		MAINUI.result_list.Show()
		MAINUI.result_list.SetSelection(0)
	e.Skip()

def __result_listbox(e):
	if e.GetInt()+1==MAINUI.result_list.GetCount() and MAINUI.result_list.MAX_NO != MAINUI.result_list.GetCount():
		MAINUI.result_list.MAX_NO = MAINUI.result_list.GetCount()
		process_search_result(MAINUI.result_list,search_result(MAINUI.DB,MAINUI.search_editor.GetValue(),offset=MAINUI.result_list.GetCount()))
	e.Skip()

# program entry point
if __name__=='__main__':
	APPLICATION = wx.App()
	MAINUI = MainUi(
		ui_show=__ui_show,
		ui_close=__ui_close,
		search_text_enter=__search_text_enter,
		search_text=__search_text,
		result_listbox=__result_listbox,
		)
	MAINUI.Show()
	APPLICATION.MainLoop()