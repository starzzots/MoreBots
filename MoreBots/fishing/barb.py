import sys
sys.path.insert(0,'c:\\Users\\Kyle\\Documents\\MoreBots')
from tools.clicks import *
from time import sleep
from tools.tools import *

#full screen 1920x1080
#67x56
screen_size=(0,0,1920,1080)

running=True
fishing=False
bagfull=False



def worldhopper():
    keyboard.press('pageup')# hotkey to switch worlds
    sleep(5)
    keyboard.release('pageup')# release the key presss
    sleep(7.5)
    keyboard.press('x')# bag hotkey ppress
    sleep(1)
    keyboard.release('x')#bag hotkey release
    sleep(2.5)

def find_finshing_spot():
    fishing_spot_color=(235,20,255)
    try:
        sleep(1.5)
        fishing_click=findobjat(fishing_spot_color,coords=screen_size,delta1x=8,delta2x=12,delta1y=8,delta2y=12)
        Randomize(fishing_click).randleft()
        sleep(16)
    except:
        print("oops")


def fishing_check(fishing):
    green=(0,255,0) 
    fishing_color_check = pg.pixel(67,56)
    if fishing_color_check == green:
        fishing = True
        return fishing
    else:
        find_finshing_spot()


def bag_check(bagfull):
    bagcheck=pg.pixel(1587,980)
    last_slot_color=(255,0,0)
    if bagcheck == last_slot_color:
        bagfull = True
        return bagfull
    else:
        bagfull = False
        return bagfull

def dropfish():
    for i in range(26):
        Randomize(bagslotfullscreen[i+3]).shiftclick()
        sleep(.8)


def main():
    if bag_check(bagfull) == False:
        fishing_check(fishing)
        return 0
    else:
        dropfish()
        return 1



if __name__ == "__main__":
    count = 50
    while running:
        if count >= 100:
            worldhopper()
            count = 0
        else:
            main()
            count= count+ main()