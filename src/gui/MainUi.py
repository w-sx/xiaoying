import wx

class MainUi(wx.Frame):

	def __init__(self,handler):
		super().__init__(None,title='晓英')
		# save event handler
		self.HANDLER = handler
		# init
		self.__init_widgets()
		self.__init_style()
		self.HANDLER.init(self)

	def __init_widgets(self):
		# Create control widgets
		self.main_panel = wx.Panel(self)
		self.search_editor = wx.TextCtrl(self.main_panel,style=wx.TE_PROCESS_ENTER)
		self.detail_list = wx.ListBox(self)
		self.result_list = wx.ListBox(self.main_panel)
		#wx.MenuBar()
		# fuck! Why is it necessary to create the menu item or button before set a shortcut keys?
		self.focus_menu = wx.Menu()
		self.focus_menu.Append(wx.ID_ANY,'search')
		self.focus_menu.Append(wx.ID_ANY,'result')

	def __init_style(self):
		# Set widget attributes
		self.result_list.Hide()
		self.detail_list.Hide()
		self.search_editor.SetToolTip('搜索')
		self.result_list.SetToolTip('结果')
