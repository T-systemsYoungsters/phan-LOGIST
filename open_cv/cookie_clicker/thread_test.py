from threading import Thread, current_thread
from time import sleep

def child():
    child_thread = current_thread()
    child_thread.alive = True
    while True:
        if not child_thread.alive:
            break
        
        print("child")
        sleep(2)

def child2():
    child_thread2 = current_thread()
    child_thread2.alive = True
    while True:
        if not child_thread2.alive:
            break
        
        sleep(1)

dimension_golden_cookie = {
        'left': 0,
        'top': 100,
        'width': 1560,
        'height': 940
    }

child_thread = Thread(target= child)
child_thread.start()

child_thread2 = Thread(target= child2)
child_thread2.start()

try:
    while True:
        print(dimension_golden_cookie['top'])
        sleep(1)

except KeyboardInterrupt as e:
    child_thread.alive = False
    child_thread.join()
    child_thread2.alive = False
    child_thread2.join()
    exit(e)