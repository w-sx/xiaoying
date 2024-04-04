import handler.main as main

if __name__=='__main__':
	app = main.wx.App()
	main.MainUi(main)
	app.MainLoop()
