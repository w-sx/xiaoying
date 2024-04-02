import handler.main as main

def event_menu_handler(e):
	if e.GetId()==ui.focus_menu.GetMenuItems()[0].GetId(): ui.search_editor.SetFocus()
	elif e.GetId()==ui.focus_menu.GetMenuItems()[1].GetId() and ui.result_list.IsShown(): ui.result_list.SetFocus()
	else: pass
	print('press')
	e.Skip()

def init():
	global ui
	ui,wx = main.ui,main.wx
	ui.Bind(wx.EVT_MENU,event_menu_handler,ui.focus_menu.GetMenuItems()[0])
	ui.Bind(wx.EVT_MENU,event_menu_handler,ui.focus_menu.GetMenuItems()[1])
	ui.SetAcceleratorTable(wx.AcceleratorTable([
		(wx.ACCEL_ALT,ord("E"),ui.focus_menu.GetMenuItems()[0].GetId()),
		(wx.ACCEL_ALT,ord("R"),ui.focus_menu.GetMenuItems()[1].GetId()),
	]))

main.INITS.append(init)