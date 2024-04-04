import handler.ProcessDb as process

def button(e):
	id = e.GetId()
	if id==ui.get_btn.GetId(): kit.btn_get(ui.msg_list,ui.info_list,v=False)
	elif id==ui.install_btn.GetId(): kit.btn_install(ui.msg_list,ui.info_list,progress)
	elif id==ui.remove_btn.GetId(): kit.btn_remove(ui.msg_list,ui.info_list)
	e.Skip()

def progress(c,s):
	ui.progress.SetRange(s)
	ui.progress.SetValue(c)

def info_listbox(e):
	key = e.GetString()
	ui.install_btn.Hide()
	ui.remove_btn.Hide()
	k = key[-2:]
	if k=='sv' or k=='7z': ui.install_btn.Show()
	if (k=='7z' or k=='sv' or k=='db') and not 'https:' in key: ui.remove_btn.Show()
	e.Skip()

def init():
	global ui,kit
	ui,wx,kit = process.ui,process.wx,process.kit
	ui.info_list.Bind(wx.EVT_LISTBOX,info_listbox)
	ui.Bind(wx.EVT_BUTTON,button)

process.INITS.append(init)