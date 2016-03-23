import signal

class AlarmException(Exception):
	pass

def alarmHandler(signum, frame):
	raise AlarmException

def Input(prompt='', timeout=2):
	signal.signal(signal.SIGALRM, alarmHandler)
	signal.alarm(timeout)
	try:
		text = raw_input(prompt)
		return text
		signal.alarm(0)
	except AlarmException:
		print '\nPrompt timeout. Continuing...'
	signal.signal(signal.SIGALRM, signal.SIG_IGN)
	return ''
txt='' 
while txt!='q':
	txt=Input()
	print txt
	print 'stream :',txt
