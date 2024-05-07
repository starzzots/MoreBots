
import sys
sys.path.insert(0,'c:\\Users\\ohgre\\OneDrive\\Documents\\MoreBots')
from tools.windowcapture import WindowCapture
from tools.clicks import *
from time import time, sleep
from tools.tools import *
#200 zoom

pos1=(0,0,1)
pos2=(0,1,2)
pos3=(0,0,3)
pos4=(0,0,4)
pos5=(0,0,5)
pos6=(0,0,6)
fail=(0,0,16)
fail2=(0,0,32)
colort=(205,0,0)
sleeps=2
laps=0

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
    if center == pos6:
        return 1
    else:
        return 0

def main():
    center=pg.pixel(822,525)
    token1=pg.pixel(755,545)
    token2=pg.pixel(846,516)
    token3=pg.pixel(786,501)
    token4=pg.pixel(755,537)
    token5=pg.pixel(710,548)
    if center == pos1:
        if token3 == colort:
            Randomize((791,795,497,503)).randleft()
            sleep(3)
            Randomize((707,719,508,526)).randleft()
            sleep(6)
        else:
            Randomize((677,689,465,498)).randleft()
            sleep(6)
    elif center == fail:
        Randomize((1031,1044,604,609)).randleft()
        sleep(7)
    elif center == fail2:
        Randomize((1115,1120,448,450)).randleft()
        sleep(7)
    
    elif center == pos2:
        if token1 == colort:
            Randomize((760,764,542,547)).randleft()
            sleep(4)
            Randomize((835,840,588,594)).randleft()
            sleep(8)
        elif token5 == colort:
            Randomize((714,720,544,549)).randleft()
            sleep(4)
            Randomize((879,884,587,592)).randleft()
            sleep(8)
        else:
            Randomize((773,778,604,609)).randleft()
            sleep(8)
    elif center == pos3:
        if token2 == colort:
            Randomize((850,858,512,518)).randleft()
            sleep(3)
            Randomize((805,820,603,614)).randleft()
            sleep(5)
        else:
            Randomize((817,850,588,597)).randleft()
            sleep(6)
    elif center == pos4:
        Randomize((669,685,573,582)).randleft()
        sleep(6)
    elif center == pos5:
        if token4 == colort:
            Randomize((759,763,527,536)).randleft()
            sleep(3)
            Randomize((895,905,541,557)).randleft()
            sleep(5)
        else:
            Randomize((830,844,541,552)).randleft()
            sleep(4)
    elif center == pos6:
        Randomize((1212,1212,132,141)).randleft()
        sleep(12)

if __name__ =='__main__':
    counter=119
    while True: 
        counter=counter+logoutcounter()
        if counter >= 120:
            worldhopper()
            counter = 0
        else:
            sleep(1)
            main()