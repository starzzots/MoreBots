import sys
sys.path.insert(0,'c:\\Users\\Kyle\\Documents\\MoreBots')
from tools.windowcapture import WindowCapture
from tools.clicks import *
from time import time, sleep
from tools.tools import *
#when character is facing north
#8 invos hop
running=True
chiseling=False
bagfull=False
red=(255,0,0)
green=(0,255,0)
logoutcounter=0


ameythst=(144,184,22)
eastblockrightside=(255,115,0)
eastblockleftside=(255,0,115)
westblockside=(255,255,115)
southblockbottomside=(0,115,255)
#southblocktopside=(0,255,115)

def worldhopper():
    keyboard.press('pageup')# hotkey to switch worlds
    sleep(5)
    keyboard.release('pageup')# release the key presss
    sleep(7.5)
    keyboard.press('x')# bag hotkey ppress
    sleep(1)
    keyboard.release('x')#bag hotkey release
    sleep(2.5)
    return 0


def crafting():
    Randomize(bagslotfullscreen[1]).randleft()
    sleep(1.6)
    Randomize(bagslotfullscreen[5]).randleft()
    sleep(1.6)
    keyboard.press_and_release('space')
    sleep(30)
    

def mining():
    try:
        miningspot=findobjat(westblockside,screen_size,delta1x=4,delta2x=9,delta1y=8,delta2y=10)
        Randomize(miningspot).randleft()
        sleep(4)
    except:
        pass

def main():
    miningcheckLoc=pg.pixel(58,54)
    lastslotcheck=pg.pixel(bagslotfullscreen[28][0],bagslotfullscreen[28][-1])
    #print(miningcheckLoc)
    if lastslotcheck == ameythst:
        #print('bag full')
        crafting()
        return 1
    
    if miningcheckLoc == green:
        #print('mining... sleep 1 second')
        sleep(8)
        if miningcheckLoc == (0,0,0):
            mining()
            return 0
        else:
            sleep(1)
            return 0

    else:
        #print('mining...')
        mining()
        return 0
        

if __name__ == "__main__":
    while True:
        if logoutcounter >= 8:
            worldhopper()
            logoutcounter=0
        count=main()
        logoutcounter=logoutcounter+count
        
        