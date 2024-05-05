import sys
sys.path.insert(0,'c:\\Users\\Kyle\\Documents\\MoreBots')
from tools.windowcapture import WindowCapture
from tools.clicks import *
from time import time, sleep
from tools.tools import *

#200 zoom
pos1=(0,0,2)
pos2=(0,0,3)
pos3=(0,0,4)
pos4=(0,0,5)
pos5=(0,0,6)
pos6=(0,0,7)
pos7=(0,0,8)

def worldhopper():
    keyboard.press('pageup')# hotkey to switch worlds
    sleep(5)
    keyboard.release('pageup')# release the key presss
    sleep(7.5)
    keyboard.press('x')# bag hotkey ppress
    sleep(1)
    keyboard.release('x')#bag hotkey release
    sleep(2.5)

def logoutcounter():
    center=pg.pixel(816,532)
    if center == pos7:
        return 1
    else:
        return 0

def main():
    center=pg.pixel(822,525)
    if center == pos1:
        Randomize((765,789,609,636)).uniclick()
        sleep(5)
    elif center == pos2:
        Randomize((833,840,680,691)).uniclick()
        sleep(10)
    elif center == pos3:
        Randomize((850,870,485,500)).uniclick()
        sleep(12)
    elif center == pos4:
        Randomize((885,900,502,516)).uniclick()
        sleep(6)
    elif center == pos5:
        Randomize((879,886,433,444)).uniclick()
        sleep(7)
    elif center == pos6:
        Randomize((794,815,425,449)).uniclick()
        sleep(6)
    elif center == pos7:
        Randomize((416,421,518,519)).uniclick()
        sleep(6)
    
    sleep(1)
    return 0

if __name__ == "__main__":
    counter=0
    while True:
        sleep(1.5)
        counter=counter+logoutcounter()
        if counter >= 240:
            worldhopper()
            counter = 0
        else:
            
            main()