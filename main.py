import time
import numpy as np
import pyautogui

pyautogui.moveTo(1520, 800)
pyautogui.click()


def capture():
    position = pyautogui.position()
    screenshot = pyautogui.screenshot(region=(position[0] - 1, position[1] - 1, 1, 1))
    screenshot = np.array(screenshot)
    return screenshot[0, 0]


click_counter = 0
max_click = 100
is_cast = True
while True:
    color_code = capture()
    print(color_code, click_counter)
    if is_cast and color_code[0] > 100 and color_code[1] > 110 and color_code[2] > 110:
        time.sleep(0.5)
        pyautogui.moveTo(1520, 800)
        pyautogui.click()
        click_counter += 1
        is_cast = False
    if color_code[0] > 130 and color_code[1] > 175 and color_code[2] > 110:
        pyautogui.moveTo(1520, 800)
        pyautogui.click()
        click_counter += 1
        is_cast = True
        time.sleep(3)
    if click_counter >= max_click:
        break
