import handler.main as main

def search_text_enter(e):
	word = ui.search_editor.GetValue()
	kit.add_items(ui.detail_list,kit.detail(word))
	ui.detail_list.RETURN = ui.search_editor.SetFocus
	kit.show_list(ui.detail_list)
	e.Skip()

def search_text(e):
	ui.search_editor.FULL = False
	ui.result_list.MAX_NO = 0
	kit.hide_list(ui.result_list,clear=True)
	e.Skip()

def result_listbox(e):
	if e.GetInt()+1==ui.result_list.GetCount() and ui.result_list.MAX_NO != ui.result_list.GetCount():
		ui.result_list.MAX_NO = ui.result_list.GetCount()
		word = ui.search_editor.GetValue()
		full=ui.search_editor.FULL
		offset = ui.result_list.GetCount()
		kit.add_items(ui.result_list,kit.search(word,full=full,offset=offset))
	e.Skip()

def search_keydown(e):
	keycode,modifiers = e.GetKeyCode(),e.GetModifiers()
	if (modifiers==0 or modifiers==2) and keycode==317:
		list,editor = ui.result_list,ui.search_editor
		word = editor.GetValue()
		if modifiers==2: editor.FULL = True
		if len(word)>0 and list.GetCount()==0: kit.add_items(list,kit.search(word,full=editor.FULL))
		if list.GetCount()>0: kit.show_list(list)
		list.RETURN = editor.SetFocus
	#if e.GetKeyCode()==27 and e.GetModifiers()==0: editor.SetValue('')
	e.Skip()

def result_keydown(e):
	keycode,modifiers = e.GetKeyCode(),e.GetModifiers()
	if keycode==315 and modifiers==0 and ui.result_list.GetSelection()==0: kit.hide_list(ui.result_list,ret=True)
	e.Skip()

def result_keyup(e):
	keycode,modifiers = e.GetKeyCode(),e.GetModifiers()
	if keycode==13 and modifiers==0:
		word = ui.result_list.GetStringSelection().split('\n')[0]
		kit.add_items(ui.detail_list,kit.detail(word))
		ui.detail_list.RETURN = ui.result_list.SetFocus
		kit.show_list(ui.detail_list)
	e.Skip()

def init():
	global ui, kit
	ui,wx,kit = main.ui,main.wx,main.kit
	ui.search_editor.Bind(wx.EVT_TEXT_ENTER,search_text_enter)
	ui.search_editor.Bind(wx.EVT_TEXT,search_text)
	ui.result_list.Bind(wx.EVT_LISTBOX,result_listbox)
	ui.search_editor.Bind(wx.EVT_KEY_DOWN,search_keydown)
	ui.result_list.Bind(wx.EVT_KEY_DOWN,result_keydown)
	ui.result_list.Bind(wx.EVT_KEY_UP,result_keyup)

main.INITS.append(init)