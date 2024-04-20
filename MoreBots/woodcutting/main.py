import sys
sys.path.insert(0,'c:\\user\\addyourfilepath') # change this to the dir that you saved the project to 
from tools.windowcapture import WindowCapture # actually might not need this need to check when im home should be called when I import tools.tools
from tools.clicks import *
from time import time, sleep
from tools.tools import *



woodcutting=locate(68,59)
woodcuttingcolor=(0,255,0)
white=(255,255,255)
purple=(114,16,160)
tree_color=(255,115,0)
num = 2
logout = 0
def alching():
    num=2
    for _ in range(25):
        Randomize(bagslot["alch"]).randleft()
        sleep(1.3)
        Randomize(bagslotclicks[num]).randleft()
        sleep(1.3)
        num+=1

def findtree():
    try:
        tree=findobjat(tree_color,delta1x=15,delta2x=30,delta1y=15,delta2y=30)
        print(tree)
        Randomize(tree).randleft()
    except:
        print('no trees')

def fletching():
    num=2
    
    for i in range(25):
        sleep(1.8)
        if pg.pixel(bagslot[num][0],bagslot[num][-1]) != white:
            num+=1
        else:
            return num
    num=2
    return num

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

def bagcheckloop(num):
    bagcheck=pg.pixel(bagslot[26][0],bagslot[26][-1])
    if bagcheck == white:
        print('bag is full')
        Randomize(bagslot[1]).randleft()
        sleep(1.2)
        Randomize(bagslot[num]).randleft()
        sleep(1.2)
        keyboard.press_and_release("space")
        sleep(1.2)
        num=fletching()
        sleep(1)
        return num
    return num

def logoutchecker():
    bagcheck=pg.pixel(bagslot[26][0],bagslot[26][-1])
    if bagcheck == purple:
        print('start alching...')
        Randomize(bagslot["magebook"]).randleft()
        sleep(.8)
        alching()
        Randomize(bagslot["bagicon"]).randleft()
        sleep(.5)
        return 1
    return 0

def woodcuttingloop():
    woodcuttingcheck=pg.pixel(woodcutting[0],woodcutting[-1])
    if woodcuttingcheck == woodcuttingcolor:
        sleep(1)
    else:
        print('looking for tree')
        findtree()
        sleep(2)

while True:
    if keyboard.is_pressed('q'):
        sys.exit()
    
    if logout >= 20:
        logout=worldhopper()
        print(logout)
    
    temp=logoutchecker()
    logout=logout+temp
    tempnum=bagcheckloop(num)
    num=tempnum
    woodcuttingloop()

    
