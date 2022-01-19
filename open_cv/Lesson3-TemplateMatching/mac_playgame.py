import keyboard
import mss
import cv2
import numpy
from time import time, sleep
import pyautogui

pyautogui.PAUSE = 0

print("Press 's' to start playing.")
print("Once started press 'q' to quit.")
keyboard.wait('s')
left = True
x = 240
y = 380
sct = mss.mss()
dimensions_left = {
        'left': 196,
        'top': 270,
        'width': 140,
        'height': 90
    }

dimensions_right = {
        'left': 315,
        'top': 270,
        'width': 115,
        'height': 90
    }

wood_left = cv2.imread('woodleft.jpg')

wood_right = cv2.imread('woodright.jpg')
w = wood_left.shape[1]
h = wood_left.shape[0]

#fps_time = time()
while True:

    if left:
        scr = numpy.array(sct.grab(dimensions_left))
        wood = wood_left
    else:
        scr = numpy.array(sct.grab(dimensions_right))
        wood = wood_right

    # Cut off alpha
    scr_remove = scr[:,:,:3]

    result = cv2.matchTemplate(scr_remove, wood, cv2.TM_CCOEFF_NORMED)
    
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    #print(f"Max Val: {max_val} Max Loc: {max_loc}")
    src = scr.copy()
    if max_val > .85:
        #print('Hallo')
        left = not left
        if left:
            x=240
        else:
            x=380

    pyautogui.click(x=x, y=y)
    sleep(.1)
    if keyboard.is_pressed('q'):
        break

    #print('FPS: {}'.format(1 / (time() - fps_time)))
    #fps_time = time()