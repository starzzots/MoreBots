import sys
sys.path.insert(0,'c:\\Users\\Kyle\\Documents\\MoreBots')
from tools.windowcapture import WindowCapture
from tools.clicks import *
from time import time, sleep
from tools.tools import *


while True:
    Randomize(bagslotfullscreen[1]).randleft()
    sleep(1)
    Randomize(bagslotfullscreen[5]).randleft()
    sleep(1)
    keyboard.press_and_release("space")
    sleep(15)