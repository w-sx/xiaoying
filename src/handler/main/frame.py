import handler.main as main

def ui_show(e):
	kit.star.open('./database/stardict.db')
	e.Skip()

def ui_close(e):
	kit.star.DB.close()
	e.Skip()

def init():
	global kit
	ui,wx,kit = main.ui,main.wx,main.kit
	ui.Bind(wx.EVT_SHOW,ui_show)
	ui.Bind(wx.EVT_CLOSE,ui_close)

main.INITS.append(init)