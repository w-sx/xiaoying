import handler.main as main
import handler.ProcessDb as process
from process.DbPkg import is_has

def ui_show(e):
	dbs = is_has('db')
	if len(dbs)<1:
		process.ProcessDbUi(process)
		ui.Close()
		return
	kit.star.open(dbs[0])
	e.Skip()

def ui_close(e):
	if kit.star.DB: kit.star.DB.close()
	e.Skip()

def init():
	global ui, kit
	ui,wx,kit = main.ui,main.wx,main.kit
	ui.Bind(wx.EVT_SHOW,ui_show)
	ui.Bind(wx.EVT_CLOSE,ui_close)

main.INITS.append(init)