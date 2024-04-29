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


def deposit_check():
    deposit_check_color=(72,62,51)
    deposit_check=pg.pixel(725,555)
    if deposit_check == deposit_check_color:
        return True
    else:
        return False
    
def deposit():
    Randomize((856,867,506,516)).randleft()#last fish slot in deposit box menu
    sleep(1.3)
    Randomize((902,909,325,331)).randleft()#exit button in deposit menu
    sleep(1.3)



def bank():
    bank_color=(255,115,0)
    try:
        bank_click=findobjat(bank_color,coords=screen_size, delta1x=5, delta2x=7,delta1y=2,delta2y=8)
        Randomize(bank_click).randleft()
        sleep(16)
    except:
        print("oh no")


def bag_check(bagfull):
    bagcheck=pg.pixel(1587,980)
    last_slot_color=(255,12,0)
    if bagcheck == last_slot_color:
        bagfull = True
        return bagfull
    else:
        bagfull = False
        return bagfull


def main():
    if bag_check(bagfull) == False:
        fishing_check(fishing)
        return 0
    else:
        bank()
        if deposit_check() == True:
            deposit()
            return 1
        else:
            bank()
            return 0



if __name__ == "__main__":
    count = 0
    while running:
        if count >= 10:
            worldhopper()
            count = 0
        else:
            main()
            count= count+ main()