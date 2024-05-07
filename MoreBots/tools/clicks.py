import pyautogui as pg
import time
import random
import numpy
import math
import keyboard
    
     
class Randomize():
    def __init__(self,minMaxs):
        self.minMaxs = [minMaxs] # (min_x, max_x, min_y, max_y)
        self.x_min = minMaxs[0]
        self.x_max = minMaxs[1]
        self.y_min = minMaxs[2]
        self.y_max = minMaxs[3]
        self.random_pix_move_y = random.randrange(25,27,1)
        self.random_pix_move_x = random.randrange(-40,40,1)

        self.random_multi = random.randrange(30,50,1)/100

        self.random_sleep= random.randrange(30,40,1)/100
        self.random_sleep2= random.randrange(10,30,1)/100
        self.random_sleep3= random.randrange(30,50,1)/1000
        self.random_long_sleep = random.randrange(20,50,1)/100
        self.new_x = random.randrange(self.x_min, self.x_max+1)
        self.new_y = random.randrange(self.y_min, self.y_max+1)

    def shiftclick(self):
        keyboard.press('shift')
        pg.moveTo(self.new_x,self.new_y, duration=.08)
        time.sleep(.05)
        pg.mouseDown(self.new_x, self.new_y)
        time.sleep(.05)
        pg.mouseUp(self.new_x, self.new_y)
        time.sleep(.08)
        keyboard.release('shift')

    def move(self):
        pg.moveTo(self.new_x,self.new_y, duration=.02)

    
    def randleftspeed(self):
        pg.moveTo(self.new_x,self.new_y, duration=.02)
        pg.mouseDown(self.new_x, self.new_y)
        time.sleep(.05)
        pg.mouseUp(self.new_x, self.new_y)
        time.sleep(.03)
    
    
    def randleft(self):
        start = pg.position()
        dist = math.dist(start, [self.new_x,self.new_y])
        durByDistance = numpy.random.uniform(0.00125,0.0014) * dist
        lowerBounded = max(durByDistance, numpy.random.normal(0.151,0.015), 0.06)
        dur = min(lowerBounded, numpy.random.normal(0.212,0.06))
        style = numpy.random.choice([pg.easeOutBack, pg.easeOutQuad], p=[0.01, 0.99])

        pg.moveTo(self.new_x,self.new_y, dur, style)
        pg.mouseDown(self.new_x, self.new_y)
        time.sleep(.09)
        pg.mouseUp(self.new_x, self.new_y)
        time.sleep(.03)
    
    
    def dragmove(self,x,y):
        pg.moveTo(self.new_x,self.new_y, duration=.3)
        time.sleep(.1)
        pg.mouseDown(self.new_x, self.new_y)
        pg.moveTo(x, y, duration=.6)
        pg.mouseUp(self.new_x, self.new_y)
        time.sleep(.1)

            