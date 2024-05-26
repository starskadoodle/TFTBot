import cv2
import numpy as np
import pyautogui

def capture_screenshot(file_path):
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    cv2.imwrite(file_path, screenshot)