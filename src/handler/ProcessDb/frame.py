import handler.ProcessDb as process
import handler.main as main
from process.DbPkg import is_has

def ui_show(e):
	kit.btn_get(ui.msg_list,ui.info_list)
	e.Skip()

def ui_close(e):
	dbs = is_has('db')
	if len(dbs)>0: main.MainUi(main)
	e.Skip()

def init():
	global ui,kit
	ui,wx,kit = process.ui,process.wx,process.kit
	ui.Bind(wx.EVT_SHOW,ui_show)
	ui.Bind(wx.EVT_CLOSE,ui_close)

process.INITS.append(init)