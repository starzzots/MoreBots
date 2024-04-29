import sys
sys.path.insert(0,'c:\\Users\\Kyle\\Documents\\MoreBots')
from tools.windowcapture import WindowCapture
from tools.clicks import *
from time import time, sleep
from tools.tools import *
#when character is facing north
#20 invos hop
running=True
chiseling=False
bagfull=False
red=(255,0,0)
logoutcounter=0

miningcheckLoc=locate(63,59)

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
def miningcheck(minningpluginLocColor):
    if minningpluginLocColor == red:
        return False
    else:
        sleep(5)
        if minningpluginLocColor == red:
            return False
        return True

def miningspot(rockblockside):
    try:
        rock=findobjat(rockblockside,delta1x=8,delta2x=12,delta1y=5,delta2y=10)
        Randomize(rock).randleft()
    except:
        print('Rock Not Found. Trying again...')
        

def makedarts():
    Randomize(bagslot[1]).randleft()
    sleep(1.2)
    Randomize(bagslot[5]).randleft()
    sleep(1.2)
    keyboard.press_and_release("space")
    sleep(1)

def bagcheck(lastslot):
      if lastslot == ameythst:
          return True
      else:
          return False

def mining():
    miningspot(westblockside)
    sleep(3)

def main():
    lastslot=pg.pixel(bagslot[28][0],bagslot[28][-1])
    miningstatement=miningcheck(pg.pixel(miningcheckLoc[0],miningcheckLoc[-1]))
    if bagcheck(lastslot) == True:
        makedarts()
        sleep(30)
        return 1
    else:
        sleep(5)
        if miningstatement == False:
            mining()
            return 0
    return 0

if __name__ == "__main__":
    makingdarts = False
    while running:
        sleep(.02)
        if keyboard.is_pressed('q'):
            sys.exit()
        logoutcounter=main()+logoutcounter
        if logoutcounter >= 10:
            worldhopper()
            logoutcounter=0
        
        