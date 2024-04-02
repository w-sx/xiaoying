import threading

def thread(target,args):
	t = threading.Thread(target=target,args=args)
	t.daemon = True
	t.start()
	return t

