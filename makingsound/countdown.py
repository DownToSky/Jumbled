import time
import winsound 

freq = 1000
t = 500

for x in range(0,19):
	winsound.Beep(freq, t)
	time.sleep(1-t/1000)
	
winsound.Beep(freq - 100, 1000)