import wx

class MainUi(wx.Frame):

	def __init__(self,ui_show=None,ui_close=None,search_text_enter=None,search_text=None,result_listbox=None,search_keydown=None,result_keydown=None,result_keyup=None,detail_keyup=None,detail_kill_focus=None):
		super().__init__(None,title='晓英')
		# save event handler
		self.__ui_show = ui_show
		self.__ui_close = ui_close
		self.__search_text_enter = search_text_enter
		self.__search_text = search_text
		self.__result_listbox = result_listbox
		self.__search_keydown = search_keydown
		self.__result_keydown = result_keydown
		self.__result_keyup = result_keyup
		self.__detail_keyup = detail_keyup
		self.__detail_kill_focus = detail_kill_focus
		# init
		self.__init_widgets()
		self.__init_style()
		self.__init_events()

	def __init_widgets(self):
		# Create control widgets
		self.main_panel = wx.Panel(self)
		self.search_editor = wx.TextCtrl(self.main_panel,style=wx.TE_PROCESS_ENTER)
		self.detail_list = wx.ListBox(self.main_panel)
		self.result_list = wx.ListBox(self.main_panel)

	def __init_style(self):
		# Set widget attributes
		self.result_list.Hide()
		self.detail_list.Hide()
		self.search_editor.SetToolTip('搜索')
		self.result_list.SetToolTip('结果')

	def __init_events(self):
		# Bind events for widgets
		self.Bind(wx.EVT_SHOW,self.__ui_show)
		self.Bind(wx.EVT_CLOSE,self.__ui_close)
		self.search_editor.Bind(wx.EVT_TEXT_ENTER,self.__search_text_enter)
		self.search_editor.Bind(wx.EVT_TEXT,self.__search_text)
		self.result_list.Bind(wx.EVT_LISTBOX,self.__result_listbox)
		self.search_editor.Bind(wx.EVT_KEY_DOWN,self.__search_keydown)
		self.result_list.Bind(wx.EVT_KEY_DOWN,self.__result_keydown)
		self.result_list.Bind(wx.EVT_KEY_UP,self.__result_keyup)
		self.detail_list.Bind(wx.EVT_KEY_UP,self.__detail_keyup)
		self.detail_list.Bind(wx.EVT_KILL_FOCUS,self.__detail_kill_focus)
		# Set shortcut keys
		# fuck! Why is it necessary to create the menu item or button before set a shortcut keys?
		self.__focus_menu = wx.Menu()
		self.__focus_menu.Append(wx.ID_ANY,'search')
		self.__focus_menu.Append(wx.ID_ANY,'result')
		self.Bind(wx.EVT_MENU,self.__event_menu_handler)
		self.SetAcceleratorTable(wx.AcceleratorTable([
			(wx.ACCEL_ALT,ord("E"),self.__focus_menu.GetMenuItems()[0].GetId()),
			(wx.ACCEL_ALT,ord("R"),self.__focus_menu.GetMenuItems()[1].GetId()),
		]))

	def __event_menu_handler(self,e):
		if e.GetId()==self.__focus_menu.GetMenuItems()[0].GetId(): self.search_editor.SetFocus()
		elif e.GetId()==self.__focus_menu.GetMenuItems()[1].GetId() and self.result_list.IsShown(): self.result_list.SetFocus()
		else: pass
		e.Skip()
