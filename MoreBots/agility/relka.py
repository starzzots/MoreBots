import sys
sys.path.insert(0,'c:\\Users\\Kyle\\Documents\\MoreBots2')
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
fail1=(0,0,10)
fail2=(0,0,9)
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
    center=pg.pixel(831,530)
    if center == pos7:
        return 1
    else:
        return 0

def main():
    center=pg.pixel(831,530)
    token1=pg.pixel(785,544)
    token2=pg.pixel(846,545)
    token3=pg.pixel(831,563)#3rd building bottom most token
    token4=pg.pixel(864,563)#4th building right most token 864,563
    token5=pg.pixel(848,578)
    #print(center)
    if center == pos1:
        if token1 == tokenc:
            Randomize((790,794,545,548)).uniclick()
            sleep(3)
            Randomize((808,811,600,607)).uniclick()
            sleep(3)
        else:
            Randomize((765,789,609,636)).uniclick()
            sleep(3)
    elif center == fail1:
        Randomize((838,844,195,200)).uniclick()
        sleep(3)
    elif center == fail2:
        Randomize((693,696,215,218)).uniclick()
        sleep(3)
    elif center == pos2:
        Randomize((833,840,680,691)).uniclick()
        sleep(3)
    elif center == pos3:
        if token2 == tokenc:
            Randomize((851,855,544,547)).uniclick()
            sleep(3.5)
            Randomize((821,828,467,474)).uniclick()
            sleep(4)
        elif token3 == tokenc:
            Randomize((835,841,559,565)).uniclick()
            sleep(3.5)
            Randomize((834,853,460,472)).uniclick()
            sleep(4)
        else:
            Randomize((850,870,485,500)).uniclick()
            sleep(4)
    elif center == pos4:
        if token4 == tokenc or pg.pixel(863,562)== tokenc:
            Randomize((870,873,563,566)).uniclick()
            sleep(3)
            Randomize((834,841,469,477)).uniclick()
            sleep(4)
        elif token5 == tokenc:
            Randomize((852,857,577,582)).uniclick()
            sleep(3)
            Randomize((848,857,458,468)).uniclick()
            sleep(4)
        else:
            Randomize((885,900,502,516)).uniclick()
            sleep(4)
    elif center == pos5:
        Randomize((879,886,433,444)).uniclick()
        sleep(4)
    elif center == pos6:
        Randomize((794,815,425,449)).uniclick()
        sleep(4)
    elif center == pos7:
        Randomize((416,421,518,519)).uniclick()
        sleep(4)
    
    sleep(1)
    return 0

if __name__ == "__main__":
    counter=199
    while True:
        sleep(1.5)
        counter=counter+logoutcounter()
        if counter >= 200:
            worldhopper()
            counter = 0
        else:
            
            main()