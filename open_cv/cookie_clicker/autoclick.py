from time import sleep
import keyboard
import pyautogui
import mss
import cv2
import numpy
from threading import Thread, current_thread

pyautogui.PAUSE = 0

def buying():
    buy_thread = current_thread()
    buy_thread.alive = True
    while True:
        if not buy_thread.alive:
            break
        
        # scroll up to click 10 times buy
        pyautogui.moveTo(1700, 500)
        pyautogui.scroll(1000)
        sleep(.5)
        #get coords from screenshot in the buying dimension
        scr_buying = numpy.array(sct.grab(dimension_buying))
        #cut off alpha
        scr_buying_remove = scr_buying[:,:,:3]

        #match the color of the screenshot dimension with the buy 10x button
        result = cv2.matchTemplate(scr_buying_remove, buy_button_10_pic, cv2.TM_CCOEFF_NORMED)

        #print max Value with max location
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        # print(f"buying 10x button Max Val: {max_val} Max Loc: {max_loc}")
        scr_buying = scr_buying.copy()

        if max_val> .80:
            pyautogui.click(x=max_loc[0]+.5*buying_width+dimension_buying['left'], y=max_loc[1]+.5*buying_height+dimension_buying['top'])
            # display an image with the match object and draw a yellow rectangle 
            # cv2.rectangle(scr_buying, max_loc, (max_loc[0] + buying_width, max_loc[1] + buying_height), (0,255,255), 2)
            # cv2.imshow('Screen Shot buying button', scr_buying)
            # cv2.waitKey(1)
            sleep(1)
            
            

        # scroll down to the bottom and buy from bottom to top
        pyautogui.moveTo(1700, 500)
        pyautogui.scroll(-1000)
        sleep(.5)
        for y_cord_bottom in range(13):
            pyautogui.click(x=1700, y=1000-y_cord_bottom*70)
            sleep(.1)

        # scroll up tp the top and buy from bottom to top
        pyautogui.moveTo(1700, 500)
        pyautogui.scroll(1000)
        sleep(.5)
        for y_cord_top in range(11):
            pyautogui.click(x=1700, y=1020-y_cord_top*70)
            sleep(.1)
        
        # will buy once per minute
        sleep(60) 
        
def clicking():
    clicking_thread = current_thread()
    clicking_thread.alive = True
    while True:
        if not clicking_thread.alive:
            break

        # around a certain area the script will click 10 times per second onto the big cookie
        x=pyautogui.position()[0]
        y=pyautogui.position()[1]
        if x < 420 and x > 150 and y < 615 and y > 280:
            pyautogui.click(x=x, y=y)
            sleep(0.1)

def golden_cookie():
    golden_thread = current_thread()
    golden_thread.alive = True
    while True:
        if not golden_thread.alive:
            break

        #get coords from screenshot in the cookie dimension
        scr_cookie = numpy.array(sct.grab(dimension_golden_cookie))
        #cut off alpha
        scr_cookie_remove = scr_cookie[:,:,:3]

        #match the color of the screenshot dimension with the cookie
        result = cv2.matchTemplate(scr_cookie_remove, cookie1, cv2.TM_CCOEFF_NORMED)

        #print max Value with max location
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        #print(f"golden cookie Max Val: {max_val} Max Loc: {max_loc}")
        scr_cookie = scr_cookie.copy()

        #if more than 40% match click in the middle of the match object
        if max_val> .40:
            pyautogui.click(x=max_loc[0]+.5*cookie_width+dimension_golden_cookie['left'], y=max_loc[1]+.5*cookie_height+dimension_golden_cookie['top'])
            # cv2.rectangle(scr_cookie, max_loc, (max_loc[0] + cookie_width, max_loc[1] + cookie_height), (0,255,255), 2)
            # cv2.imshow('Screen Shot golden cookie', scr_cookie)
            # cv2.waitKey(1)
            #sleep(1)
            pyautogui.click(x=300, y=400)
            sleep(77)
        else:
            sleep(5)

def mute_button():
    mute_thread = current_thread()
    mute_thread.alive = True
    while True:
        if not mute_thread.alive:
            break

        #get coords from screenshot in the mute button dimension
        scr_mute = numpy.array(sct.grab(dimension_mute_button))
        #cut off alpha
        scr_mute_remove = scr_mute[:,:,:3]

        #match the color of the screenshot dimension with the mute button
        result = cv2.matchTemplate(scr_mute_remove, mute_button_pic, cv2.TM_CCOEFF_NORMED)

        #print max Value with max location
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        #print(f"mute button Max Val: {max_val} Max Loc: {max_loc}")
        scr_mute = scr_mute.copy()

        #if 
        if max_val> .80:
            pyautogui.click(x=max_loc[0]+.5*mute_width+dimension_mute_button['left'], y=max_loc[1]+.5*mute_height+dimension_mute_button['top'])
            # display an image with the match object and draw a yellow rectangle 
            # cv2.rectangle(scr_mute, max_loc, (max_loc[0] + mute_width, max_loc[1] + mute_height), (0,255,255), 2)
            # cv2.imshow('Screen Shot mute button', scr_mute)
            # cv2.waitKey(1)
            #sleep(1)
            pyautogui.click(x=300, y=400)
            sleep(10)
        else:
            sleep(60)

def upgrade():
    upgrade_thread = current_thread()
    upgrade_thread.alive = True
    while True:
        if not upgrade_thread.alive:
            break
        
        #scrollen up the screen to see the upgrade bar
        pyautogui.moveTo(1700, 500)
        pyautogui.scroll(500)
        sleep(.5)
        # clicking on the upgrade
        pyautogui.click(x=1630, y=260)
        sleep(1)
        # back to big cooke
        pyautogui.click(x=300, y=400)
        sleep(60*5) # will buy 1 upgrade every 5 minutes

def close_achievement():
    close_thread = current_thread()
    close_thread.alive = True
    while True:
        if not close_thread.alive:
            break
        
        #get coords from screenshot in the close button dimension
        scr_close = numpy.array(sct.grab(dimension_close_button))
        #cut off alpha
        scr_close_remove = scr_close[:,:,:3]

        #match the color of the screenshot dimension with the close button
        result = cv2.matchTemplate(scr_close_remove, close_button_pic, cv2.TM_CCOEFF_NORMED)

        #print max Value with max location
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        print(f"close button Max Val: {max_val} Max Loc: {max_loc}")
        scr_close = scr_close.copy()

        #if 
        if max_val> .80:
            pyautogui.click(x=max_loc[0]+.5*close_width+dimension_close_button['left'], y=max_loc[1]+.5*close_height+dimension_close_button['top'])
            # display an image with the match object and draw a yellow rectangle 
            # cv2.rectangle(scr_close, max_loc, (max_loc[0] + close_width, max_loc[1] + close_height), (0,255,255), 2)
            # cv2.imshow('Screen Shot close achievement', scr_close)
            # cv2.waitKey(1)
            #sleep(1)
            pyautogui.click(x=300, y=400)
        sleep(60)



print("Press 's' to start playing.")
print("Once started press 'ctrl+c' into the console to quit.\nIt may take some time to close all Thread, because they have to finished before closing.")
keyboard.wait('s')

#screenshot your main display
sct = mss.mss()
# dimension where the golden cookie could appear
dimension_golden_cookie = {
        'left': 0,
        'top': 100,
        'width': 1560,
        'height': 940
    }
# dimension for the mute button appearance 
dimension_mute_button = {
        'left': 1300,
        'top': 350,
        'width': 270,
        'height': 80
}

# dimension for the close button appearance
dimension_close_button = {
        'left': 1070,
        'top': 990,
        'width': 80,
        'height': 60
}

# dimension for 10x buying button
dimension_buying = {
        'left': 1700,
        'top': 250,
        'width': 60,
        'height': 60
}

#upload picture 
#notice [pic].shape returns (height,width)
cookie1 = cv2.imread('cookie4.png')
cookie_width = cookie1.shape[1]
cookie_height = cookie1.shape[0]

mute_button_pic = cv2.imread('mute_button.png')
mute_width = mute_button_pic.shape[1]
mute_height = mute_button_pic.shape[0]

close_button_pic = cv2.imread('x_button_big2.png')
close_width = close_button_pic.shape[1]
close_height = close_button_pic.shape[0]

big_cookie = cv2.imread('big_cookie4.png')
big_cookie_width = big_cookie.shape[1]
big_cookie_height = big_cookie.shape[0]

buy_button_10_pic = cv2.imread('10_buy_button.png')
buying_width = buy_button_10_pic.shape[1]
buying_height = buy_button_10_pic.shape[0]

# starting the threads
buy_thread = Thread(target= buying)
buy_thread.start()
clicking_thread = Thread(target= clicking)
clicking_thread.start()
golden_thread = Thread(target= golden_cookie)
golden_thread.start()
mute_thread = Thread(target= mute_button)
mute_thread.start()
upgrade_thread = Thread(target= upgrade)
upgrade_thread.start()
close_thread = Thread(target= close_achievement)
close_thread.start()

try:
    while True:
        #this prints out x and y Coordinates from your mouse every 5 seconds for adjusting the programm
        a=pyautogui.position()[0]
        b=pyautogui.position()[1]
        print("x={}, y={}".format(a, b))   
        sleep(5)

except KeyboardInterrupt as e:
    # closing the threads 
    buy_thread.alive = False
    buy_thread.join()
    clicking_thread.alive = False
    clicking_thread.join()
    mute_thread.alive = False
    mute_thread.join()
    close_thread.alive = False
    close_thread.join()
    golden_thread.alive = False
    golden_thread.join()
    upgrade_thread.alive = False
    upgrade_thread.join()
    print("You closed the script.")
    exit(e)