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
pos9=(0,0,9)
fail1=(0,0,10)
fail2=(0,0,11)
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
    if center == pos9:
        return 1
    else:
        return 0

def main():
    center=pg.pixel(822,525)
    token1=pg.pixel(708,571)
    token2=pg.pixel(786,528)
    token3=pg.pixel(847,458)
    token4=pg.pixel(787,585)
    token5=pg.pixel(847,479)
    
    if center == pos1:
        Randomize((727,735,529,535)).randleft()
        sleep(2)
    elif center == fail1:
        Randomize((959,965,529,533)).randleft()
        sleep(2)
    elif center == fail2:
        Randomize((1315,1324,465,469)).randleft()
        sleep(2)
    elif center == pos2:
        Randomize((686,702,479,496)).randleft()
        sleep(2)

    elif center == pos3:
        if token2 == tokenc:
            Randomize((791,794,529,533)).randleft()
            sleep(2)
            Randomize((764,777,533,547)).randleft()
            sleep(2)
        else:
            Randomize((732,747,532,544)).randleft()
            sleep(2)

    elif center == pos4:
        Randomize((827,848,604,613)).randleft()
        sleep(2)

    elif center == pos5:
        if token1 == tokenc:
            Randomize((714,717,575,580)).randleft()
            sleep(5)
            Randomize((1156,1162,454,481)).randleft()
            sleep(2)
        elif token4 == tokenc:
            Randomize((790,794,590,595)).randleft()
            sleep(6)
            Randomize((1085,1093,439,458)).randleft()
            sleep(2)
        else:
            Randomize((1062,1070,498,533)).randleft()
            sleep(2)

    elif center == pos6:
        if token5 == tokenc:
            Randomize((851,854,484,487)).randleft()
            sleep(5)
            Randomize((1005,1015,518,533)).randleft()
            sleep(2) 
        else:
            Randomize((1041,1064,469,487)).randleft()
            sleep(2)

    elif center == pos7:
        if token3 == tokenc:
            Randomize((853,855,451,455)).randleft()
            sleep(4)
            Randomize((806,831,512,519)).randleft()
            sleep(1)
        else:
            Randomize((820,839,428,437)).randleft()
            sleep(2)
    elif center == pos8:
        Randomize((819,837,437,446)).randleft()
        sleep(2)
    elif center == pos9:
        Randomize((577,583,577,581)).randleft()
        sleep(2)
    else:
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
        
