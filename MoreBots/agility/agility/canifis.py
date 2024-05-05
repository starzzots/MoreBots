import sys
sys.path.insert(0,'c:\\Users\\Kyle\\Documents\\MoreBots')
from tools.windowcapture import WindowCapture
from tools.clicks import *
from time import time, sleep
from tools.tools import *




pos1=(0,0,1)
pos2=(0,0,2)
pos3=(0,0,3)
pos4=(0,0,4)
pos5=(0,0,5)
pos6=(0,0,6)
pos7=(0,0,7)
pos8=(0,0,8)
glitched=(15,0,15)
glitched2=(0,0,15)
fail1=(0,0,9)
fail2=(0,0,10)
tokenc=(205,0,0)

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
    center=pg.pixel(822,525)
    if center == pos8:
        return 1
    else:
        return 0

def main(): 
    center=pg.pixel(822,525)
    token1=pg.pixel(822,478)
    token2=pg.pixel(786,583)
    token3=pg.pixel(826,554)
    token4=pg.pixel(816,578)
    token5=pg.pixel(801,516)
    if center == pos1:
        sleep(2)
        if token1 == tokenc:
            Randomize((821,825,482,487)).randleft()
            sleep(4)
            Randomize((804,819,476,493)).randleft()
            sleep(1)
        else:
            Randomize((805,820,428,447)).randleft()
            sleep(2)
    elif center == glitched:
        Randomize((1063,1073,523,539)).randleft()
        sleep(5)
    
    elif center == glitched2:
        Randomize((1231,1241,695,702)).randleft()
        sleep(5)

    elif center == fail1:
        sleep(1)
        Randomize((1241,1249,688,700)).randleft()
        sleep(2)
    elif center == fail2:
        sleep(1)
        Randomize((847,856,343,354)).randleft()
        sleep(2)
    elif center == pos2:
        if token5 == tokenc:
            Randomize((806,810,514,520)).randleft()
            sleep(2)
            Randomize((749,756,540,552)).randleft()
            sleep(8)
        else:
            Randomize((732,742,526,535)).randleft()
            sleep(8)
    elif center == pos3:
        if token2 == tokenc:
            Randomize((790,795,575,580)).randleft()
            sleep(4)
            Randomize((750,757,549,561)).randleft()
            sleep(6)
        else:
            Randomize((717,728,600,612)).randleft()
            sleep(6)
    elif center == pos4:
        sleep(2)
        if token4 == (255,0,0):
            Randomize((805,809,575,579)).randleft()
            sleep(4)
            Randomize((819,826,590,607)).randleft()
            sleep(1)
        else:
            Randomize((804,812,635,653)).randleft()
            sleep(2)
    elif center == pos5:
        sleep(2)
        if token3 == tokenc:
            Randomize((820,824,558,563)).randleft()
            sleep(2)
            Randomize((847,856,539,549)).randleft()
            sleep(8)
        else:
            Randomize((848,858,572,579)).randleft()
            sleep(8)
    elif center == pos6:
        sleep(1)
        Randomize((1038,1051,522,538)).randleft()
        sleep(2)
    elif center == pos7:
        sleep(1)
        Randomize((818,825,412,423)).randleft()
        sleep(2)
    elif center == pos8:
        sleep(1)
        Randomize((735,750,451,460)).randleft()
        sleep(2)
    pass

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