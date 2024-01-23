import time
import threading
from pynput.mouse import Controller

mouse = Controller()

time_remaining = 0
minutes = 0
seconds=time_remaining/6

#tugging_key = (char"s")

def timing (time_remaining):
    while time_remaining!= 0:
        time.sleep(2)
        time_remaining=time_remaining-2
        minutes = time_remaining/60
        seconds=time_remaining
        print (f"faltan {(minutes):.0f} minutos y {(seconds):.0f} segundos")
    if time_remaining ==0:
        print("Time´s Up!")
        return False
    
def mooving_mouse ():
    mouse.move(50,-50)
        
while timing(time_remaining=20) is True:
    mooving_mouse()
