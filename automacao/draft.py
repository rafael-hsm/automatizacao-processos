import os

import pyautogui
import cv2


img_path = os.getcwd() + os.sep + "automacao" + os.sep + "img" + os.sep + "pitbull.png"
print(img_path)

res = pyautogui.locateOnScreen(image=img_path)

print(res)
