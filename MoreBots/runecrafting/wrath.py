import sys
sys.path.insert(0,'c:\\Users\\Kyle\\Documents\\MoreBots2')
from tools.clicks import *
from time import sleep
from tools.tools import *
#200 zoom
#full screen 1920x1080
SCREEN_SIZE=(0,0,1920,1080)

def worldhopper():
    keyboard.press('pageup')# hotkey to switch worlds
    sleep(5)
    keyboard.release('pageup')# release the key presss
    sleep(7.5)
    keyboard.press('x')# bag hotkey ppress
    sleep(1)
    keyboard.release('x')#bag hotkey release
    sleep(2.5)
    
def main():
    color_checks=[(0,1,1)]
    bank_color_check = pg.pixel(764,99)
    center = pg.pixel(823,539)
    bank_chest_color = (255,71,0)
    try:
        click=findobjat(bank_chest_color,SCREEN_SIZE,delta1x=5, delta2x=8,delta1y=5,delta2y=9)
        Randomize(click).randleft()
        sleep(6)
        return 0
    except:
        if bank_color_check == (73,64,52): #banks color(73, 64, 52)
            #start of script should be on bank panel
            Randomize((590,604,95,104)).randleft()
            sleep(1)
            Randomize((565,576,134,144)).randleft()#pure essence
            sleep(1)
            Randomize((1456,1467,760,768)).randleft()#giant pouch
            sleep(1)
            Randomize((565,576,134,144)).randleft()#pure essence
            sleep(1)
            Randomize((1456,1467,760,768)).randleft()#giant pouch
            sleep(1)
            Randomize((565,576,134,144)).randleft()#pure essence
            sleep(1)
            exit_button=Randomize((919,926,61,69)).randleft()
            sleep(1)
            teleport=Randomize((1578,1596,756,773)).randleft()
            sleep(4)
            click=findobjat(color_checks[0], SCREEN_SIZE,delta1x=12,delta2x=25, delta1y=8, delta2y=30)
            Randomize(click).randleft()
            sleep(3)
            return 0
        if center == (0,0,1):
            Randomize((715,734,862,882)).randleft()# middle of dragon room
            sleep(13)
            Randomize((961,985,850,868)).randleft()
            sleep(5)
            return 0
        elif center == (0,0,2):
            Randomize((824,848,390,414)).randleft()# wrath rock
            sleep(5)
            return 0
        elif center == (0,0,3):
            Randomize((814,826,397,412)).randleft() #alter
            sleep(6)
            return 0
        elif center == (0,0,4):
            Randomize((1456,1467,760,768)).shiftclick() #giant pouch shift click
            sleep(.5)
            Randomize((815,826,495,508)).randleft() #alterupclose
            sleep(.5)
            Randomize((1456,1467,760,768)).shiftclick() #giant pouch shift click
            sleep(.5)
            Randomize((815,826,495,508)).randleft() #alterupclose
            sleep(.5)
            Randomize((1542,1551,760,772)).randleft() #house tab 3rd slot
            sleep(5)
            return 0
        elif center == (0,0,5):
            Randomize((779,787,471,479)).randleft()#ornate pool in house
            sleep(4)
            Randomize((773,777,543,547)).randleft()#castlewars in house
            sleep(6)
            return 1
        else:
            return 0
if __name__ == "__main__":
    total = 0
    while True:
        print(total)
        counter = main()
        total = total + counter
        if total == 150:
            worldhopper()
            total = 0