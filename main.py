import cv2
import time
import mediapipe as mp
from hands import Hands
import pyautogui
import threading


def move_mouse(x,y) -> None:
    pyautogui.moveRel(x,y)


def loop(camera, ptime) -> None:
    while True:
        success, img = camera.read()
        img = cv2.flip(img, 1)
        img = hands.find_hands(img)
        li = hands.find_location(img)
        init = False
        if len(li) == 21:
            li[17][0] >= li[5][0]
            print("OK")
            if init:
                index_tip_val_prev[0] = li[8][1]
                init = False
                continue
            # print("================================") 
            dif[0] = li[8][1] - index_tip_val_prev[0]
            dif[1] = li[8][2] - index_tip_val_prev[1]
            x = dif[0]
            y = dif[1]
            print(x, y)
            hands.hand_type()
            index_tip_val_prev[0] = li[8][1]
            index_tip_val_prev[1] = li[8][2]
            # print("================================")
        ctime = time.time()
        fps = 1/(ctime-ptime)
        ptime = ctime
        print("ctime", ctime, "ptime", ptime)
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('q'):
            break



# Camera Setup
print("PKKK")
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
hands = Hands()
sensitivity = 2.87
ptime = 0

index_tip_val_prev = [0,0]
dif = [0,0]

sw = pyautogui.size()[0]
sh = pyautogui.size()[1]

pyautogui.FAILSAFE = False

pyautogui.moveTo(sw/2,sh/2)

loop(camera, ptime)

