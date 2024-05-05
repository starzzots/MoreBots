import sys
sys.path.insert(0,'c:\\Users\\Kyle\\Documents\\MoreBots')
from tools.windowcapture import WindowCapture
from tools.clicks import *
from time import time, sleep
from tools.tools import *

def bank():
    Randomize((844,854,529,535)).randleft()
    sleep(1.6)
    Randomize(bagslotfullscreen[1]).randleft()
    sleep(1)
    Randomize((712,722,496,506)).randleft()
    sleep(1)
    Randomize((715,722,534,543)).randleft()
    sleep(1)
    Randomize((918,927,63,70)).randleft()#exit
    sleep(1)

def makepotion():
    Randomize(bagslotfullscreen[14]).randleft()
    sleep(.2)
    Randomize(bagslotfullscreen[15]).randleft()
    sleep(1.6)
    keyboard.press_and_release('space')
    sleep(1)



if __name__ == "__main__":
    while True:
        if keyboard.is_pressed('q'):
            sys.exit()
        bank()
        makepotion()
        sleep(10)
