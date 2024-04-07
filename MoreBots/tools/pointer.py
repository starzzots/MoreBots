import pyautogui as pg
import keyboard
import time
import sys
import os
from clicks import *


    
while True:
    if keyboard.is_pressed('1'):
        top_left=pg.position()
        time.sleep(1)
    elif keyboard.is_pressed('2'):
        bottom_right=pg.position()
        time.sleep(1)
    elif keyboard.is_pressed('3'):
        print(f"({top_left[0]},{top_left[1]},{bottom_right[0]},{bottom_right[1]})")
        time.sleep(1)
        break
    
    elif keyboard.is_pressed('p'):
        try:
            print(f"Randomize(({top_left[0]},{bottom_right[0]},{top_left[1]},{bottom_right[1]})).randleft()")
            break
        except:
            print("oof try to get coords first with '1' and '2'")
        time.sleep(1)
    elif keyboard.is_pressed('='):
        pg.displayMousePosition()
     

    elif keyboard.is_pressed('delete'):
        break

#120,0,139
#255,3,255