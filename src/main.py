import handler.main as main

if __name__=='__main__':
	app = main.wx.App()
	ui = main.MainUi(main)
	ui.Show()
	app.MainLoop()
