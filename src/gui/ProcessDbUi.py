import wx

class ProcessDbUi(wx.Frame):

	def __init__(self,handler):
		super().__init__(None,title='晓英 - 数据库管理')
		self.__init_widgets()
		handler.init(self)

	def __init_widgets(self):
		self.main_panel = wx.Panel(self)
		self.progress = wx.Gauge(self.main_panel,)
		self.msg_list = wx.ListBox(self.main_panel)
		self.info_list = wx.ListBox(self.main_panel)
		self.install_btn = wx.Button(self.main_panel,label='安装')
		self.install_btn.Hide()
		self.remove_btn = wx.Button(self.main_panel,label='删除')
		self.remove_btn.Hide()
		self.get_btn = wx.Button(self.main_panel,label='刷新')
