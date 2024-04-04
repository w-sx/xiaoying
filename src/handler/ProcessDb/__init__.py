import wx
from gui.ProcessDbUi import ProcessDbUi

INITS = []

import handler.ProcessDb.kit as kit
import handler.ProcessDb.frame as frame
import handler.ProcessDb.processor

#import pkgutil,os
#for _, file, _ in pkgutil.iter_modules([os.path.dirname(__file__)]): __import__(__package__+'.'+file)

def init(obj:ProcessDbUi):
	global ui
	ui = obj
	for i in INITS: i()
	ui.Show()
