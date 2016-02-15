from time import sleep
from seriaLED import seriaLED
from colour import Color
from multiprocessing import Process, Queue, Pipe
import snippets

def setup(q):
	ledString = seriaLED(30)

	response = q.recv()

	if response == 1:
		snippets.breathe(ledString, Color('blue'))
	elif response == 2:
		while True:
			snippets.rainbowRotate(ledString, 0.1)
	elif response == 3:
		while True:
			snippets.colorFade(ledString, Color('violet'), Color('red'), 50, .1)
	elif response == 4:
		while True:
			snippets.rgbFill(ledString, 1)
	else:
		quit()

if __name__ == '__main__':
	q = Queue()
	parent_conn, child_conn = Pipe(False)
	p = Process(target=setup, args=(parent_conn,))
	p.start()

	print("\
	#########################\n\
	# Watasenia version 0.1 #\n\
	#     by  Aucuparia     #\n\
	#########################\n\
	")
	print("Options:\n\
	1: Gentle Breathing\n\
	2: Swirling Rainbow\n\
	3: Fading Rainbow\n\
	4: Rotating Pattern")
	response = int(input("> "))
	child_conn.send(response)