from time import sleep
import keyboard
import pyautogui
import mss
import cv2
import numpy

pyautogui.PAUSE = 0


print("Press 's' to start playing.")
print("Once started press 'q' to quit.")
keyboard.wait('s')
#screenshot 
sct = mss.mss()
# dimension where the golden cookie could appear
dimension = {
        'left': 0,
        'top': 110,
        'width': 1110,
        'height': 800
    }

#upload picture of golden cookie
cookie1 = cv2.imread('mac_cookie.png')
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
    

    #if 
    if max_val> .40:
        pyautogui.click(x=max_loc[0]+.5*w, y=max_loc[1]+1.5*h)
        sleep(1)
        pyautogui.click(x=300, y=400)


    x=pyautogui.position()[0]
    y=pyautogui.position()[1]
    
    if x < 330 and x > 100 and y < 530 and y > 300:
        pyautogui.click(x=x, y=y)
        sleep(.5)
    if keyboard.is_pressed('q'):
        break