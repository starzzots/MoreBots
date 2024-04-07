from tools.windowcapture import WindowCapture
from tools.clicks import *
from time import time, sleep


def findobjat(objsRGBVal,coords=(0,0,1080,670),stepleftright=1,stepupdown=1,delta1x=0,delta2x=0,delta1y=0,delta2y=0,hwnd="RuneLite"):#topleftx, toplefty, bottomrightx, bottomrighty
    flag=0
    wincap = WindowCapture(hwnd)
    screenshot=pg.screenshot(region=(wincap.coords[0],wincap.coords[1],coords[2],coords[3]))

    
    for y in range(coords[1], coords[3], stepupdown):#1,3
        for x in range(coords[0], coords[2], stepleftright):#0,2
            rgb = screenshot.getpixel((x, y))
            if rgb==objsRGBVal:
                flag = 1
                
                new_x= x+wincap.coords[0]
                new_y= y+wincap.coords[1]
                sleep(0.05)
                break
                            
        if flag == 1:
                return (new_x+delta1x,new_x+delta2x,new_y+delta1y,new_y+delta2y) #new_x,new_y imma reformate for us

def locate(deltax, deltay, hwnd="RuneLite",offsetx1=0,offsetx2=0,offsety1=0,offsety2=0):
    #formats specific location on runelite 800x640 to be ready for Randomize function
    #set runelite to top left then use pointer to locate x,y of location and plug in deltax, delta y
    
    #offsets are for the Randomize class in clicks.py so you can make the clicks random otherwise where you save cords is where itll always click
    wincap = WindowCapture(hwnd)

    locationc = wincap.coords[0]+deltax,wincap.coords[1]+deltay
    locationcords = (locationc[0]+offsetx1,locationc[0]+offsetx2,locationc[1]+offsety1,locationc[1]+offsety2)
    return locationcords





bagslot={1:locate(619,395),2:locate(660,395),3:locate(703,395),4:locate(745,395),
          5:locate(619,431),6:locate(660,431),7:locate(703,431),8:locate(745,431),
          9:locate(619,467),10:locate(660,467),11:locate(703,467),12:locate(745,467),
          13:locate(619,503),14:locate(660,503),15:locate(703,503),16:locate(745,503),
          17:locate(619,539),18:locate(660,539),19:locate(703,539),20:locate(745,539),
          21:locate(619,576),22:locate(660,576),23:locate(703,576),24:locate(745,576),
          25:locate(619,603),26:locate(660,603),27:locate(703,603),28:locate(745,603),
          "magebook":locate(775,342,offsetx2=12,offsety2=12),
          "bagicon":locate(676,343,offsetx2=12,offsety2=12),
          "alch":locate(670,512,offsetx2=12,offsety2=12)}

bagslotclicks={1:locate(619,395,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),2:locate(660,395,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),3:locate(703,395,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),4:locate(745,395,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),
          5:locate(619,431,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),6:locate(660,431,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),7:locate(703,431,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),8:locate(745,431,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),
          9:locate(619,467,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),10:locate(660,467,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),11:locate(703,467,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),12:locate(745,467,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),
          13:locate(619,503,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),14:locate(660,503,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),15:locate(703,503,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),16:locate(745,503,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),
          17:locate(619,539,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),18:locate(660,539,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),19:locate(703,539,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),20:locate(745,539,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),
          21:locate(619,576,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),22:locate(660,576,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),23:locate(703,576,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),24:locate(745,576,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),
          25:locate(619,603,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),26:locate(660,603,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),27:locate(703,603,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),28:locate(745,603,offsetx1=-3,offsetx2=3,offsety1=-3,offsety2=3),}

hwnd="RuneLite"
wincap = WindowCapture(hwnd)
