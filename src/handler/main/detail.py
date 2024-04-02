import handler.main as main

def detail_keydown(e):
	keycode,modifiers = e.GetKeyCode(),e.GetModifiers()
	if keycode==32 and modifiers==0: kit.audio(ui.detail_list.GetItems()[0].split('\n')[0])
	e.Skip()

def detail_keyup(e):
	keycode,modifiers = e.GetKeyCode(),e.GetModifiers()
	if keycode==27 and modifiers==0: ui.detail_list.Hide()
	if keycode==13 and modifiers==0: pass
	e.Skip()

def detail_set_focus(e):
	if not 'FIRST' in ui.detail_list.__dir__():
		word = ui.detail_list.GetItems()[0].split('\n')[0]
		kit.audio(word)
	ui.detail_list.FIRST = False
	e.Skip()

def detail_kill_focus(e):
	if not ui.IsActive(): return
	if ui.detail_list.RETURN: ui.detail_list.RETURN()
	ui.detail_list.Hide()
	ui.detail_list.Clear()
	ui.detail_list.RETURN = None
	del(ui.detail_list.FIRST)
	e.Skip()

def init():
	global ui, kit
	ui,wx,kit = main.ui,main.wx,main.kit
	ui.detail_list.Bind(wx.EVT_KEY_DOWN,detail_keydown)
	ui.detail_list.Bind(wx.EVT_KEY_UP,detail_keyup)
	ui.detail_list.Bind(wx.EVT_SET_FOCUS,detail_set_focus)
	ui.detail_list.Bind(wx.EVT_KILL_FOCUS,detail_kill_focus)

main.INITS.append(init)