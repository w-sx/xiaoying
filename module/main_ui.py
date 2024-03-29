import wx

class MainUi(wx.Frame):

	def __init__(self,ui_show=None,ui_close=None,search_text_enter=None,search_text=None,result_listbox=None):
		super().__init__(None,title='晓英')
		self.__ui_show = ui_show
		self.__ui_close = ui_close
		self.__search_text_enter = search_text_enter
		self.__search_text = search_text
		self.__result_listbox = result_listbox
		self.__init_widgets()
		self.__init_style()
		self.__init_events()

	def __init_widgets(self):
		# Create control widgets
		self.main_panel = wx.Panel(self)
		self.search_editor = wx.TextCtrl(self.main_panel,style=wx.TE_PROCESS_ENTER)
		self.result_list = wx.ListBox(self.main_panel)
		#self.result_list

	def __init_style(self):
		# Set widget attributes
		self.result_list.Hide()
		self.search_editor.SetToolTip('搜索')
		self.result_list.SetToolTip('结果')

	def __init_events(self):
		# Bind events for widgets
		self.search_editor.Bind(wx.EVT_KEY_DOWN,self.__search_key_down)
		if self.__ui_show: self.Bind(wx.EVT_SHOW,self.__ui_show)
		if self.__ui_close: self.Bind(wx.EVT_CLOSE,self.__ui_close)
		if self.__search_text_enter: self.search_editor.Bind(wx.EVT_TEXT_ENTER,self.__search_text_enter)
		if self.__search_text: self.search_editor.Bind(wx.EVT_TEXT,self.__search_text)
		if self.__result_listbox: self.result_list.Bind(wx.EVT_LISTBOX,self.__result_listbox)
		# Set shortcut keys
		# fuck! Why is it necessary to create the menu item or button before set a shortcut keys?
		# But I can't create menu item because item ids is always -2! fuck I don't know why this is.
		self.BTN_search_focus = wx.Button(self)
		self.BTN_search_focus.Hide()
		self.BTN_search_focus.Bind(wx.EVT_BUTTON,self.__event_focus_handler)
		self.BTN_result_focus = wx.Button(self)
		self.BTN_result_focus.Hide()
		self.BTN_result_focus.Bind(wx.EVT_BUTTON,self.__event_focus_handler)
		self.SetAcceleratorTable(wx.AcceleratorTable([
			(wx.ACCEL_ALT,ord("E"),self.BTN_search_focus.GetId()),
			(wx.ACCEL_ALT,ord("R"),self.BTN_result_focus.GetId()),
		]))

	def __event_focus_handler(self,e):
		print(e)
		if e.GetId()==self.BTN_search_focus.GetId(): self.search_editor.SetFocus()
		elif e.GetId()==self.BTN_result_focus.GetId() and self.result_list.IsShown(): self.result_list.SetFocus()
		else: print(e)

	def __search_key_down(self,e):
		if e.GetModifiers()==0 and e.GetKeyCode()==317:
			if self.result_list.IsShown(): self.result_list.SetFocus()
			return
		e.Skip()


