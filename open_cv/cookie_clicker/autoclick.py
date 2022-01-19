from time import sleep
import keyboard
import pyautogui
import mss
import cv2
import numpy
from threading import Thread

pyautogui.PAUSE = 0
def buying():
    while True:
        print("buy stuff")
        sleep(10)

buy_thread = Thread(target= buying)
buy_thread.start()

try:
    print("Press 's' to start playing.")
    print("Once started press 'q' to quit.")
    keyboard.wait('s')
    #screenshot 
    sct = mss.mss()
    # dimension where the golden cookie could appear
    dimension = {
            'left': 0,
            'top': 100,
            'width': 1560,
            'height': 940
        }

    #upload picture of golden cookie
    cookie1 = cv2.imread('cookie3.png')
    w = cookie1.shape[1]
    h = cookie1.shape[0]
    while True:

        #get coords from screenshot in the cookie dimension
        scr = numpy.array(sct.grab(dimension))
        #cut off alpha
        scr_remove = scr[:,:,:3]

        #match the color of the screenshot dimension with the cookie
        result = cv2.matchTemplate(scr_remove, cookie1, cv2.TM_CCOEFF_NORMED)

        #print max Value with max location
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        #print(f"Max Val: {max_val} Max Loc: {max_loc}")
        src = scr.copy()

        #if 
        if max_val> .40:
            cv2.rectangle(scr, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)
            pyautogui.click(x=max_loc[0]+.5*w, y=max_loc[1]+1.5*h)
            sleep(1)
            pyautogui.click(x=300, y=400)


        cv2.imshow('Screen Shot', scr)
        cv2.waitKey(1)

        x=pyautogui.position()[0]
        y=pyautogui.position()[1]
        
        if x < 420 and x > 150 and y < 615 and y > 280:
            pyautogui.click(x=x, y=y)
            sleep(.5)
        if keyboard.is_pressed('q'):
            break

except KeyboardInterrupt as e:
    buy_thread.alive = False
    buy_thread.join()
    exit(e)