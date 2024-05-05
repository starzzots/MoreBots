import sys
sys.path.insert(0,'c:\\Users\\Kyle\\Documents\\MoreBots')
from tools.windowcapture import WindowCapture
from tools.clicks import *
from time import time, sleep
from tools.tools import *


if __name__ == "__main__":
    while True:
        if keyboard.is_pressed('q'):
            sys.exit()
            break
        Randomize((844,854,529,535)).randleft()
        sleep(1.6)
        Randomize(bagslotfullscreen[1]).randleft()
        sleep(1)
        Randomize((762,771,572,578)).randleft()
        sleep(1)
        Randomize((918,927,63,70)).randleft()
        sleep(1)
        for i in range(28):
            Randomize(bagslotfullscreen[i+1]).randleftspeed()
            sleep(.02)
        sleep(1)