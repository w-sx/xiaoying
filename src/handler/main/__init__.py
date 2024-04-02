import wx
from gui.MainUi import MainUi

INITS = []

import handler.main.kit as kit
import handler.main.frame as frame
import handler.main.search as search
import handler.main.detail as detail
import handler.main.menu as menu

#import pkgutil,os
#for _, file, _ in pkgutil.iter_modules([os.path.dirname(__file__)]): __import__(__package__+'.'+file)

def init(obj:MainUi):
	global ui
	ui = obj
	for i in INITS: i()
