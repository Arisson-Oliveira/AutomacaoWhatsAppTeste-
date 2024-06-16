import pyautogui
from time import sleep


pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')
sleep(2)
pyautogui.write('https://web.whatsapp.com/')
pyautogui.press('enter')
sleep(6)
pyautogui.click(x=201, y=233)
sleep(2)
pyautogui.write('Maria')
sleep(2)
pyautogui.click(x=274, y=457)
sleep(2)
pyautogui.click(x=709, y=962) #figurinha botao
sleep(2)
while True:
    pyautogui.click(x=981, y=712)
    sleep(2)

#pyautogui.write('OI')
#pyautogui.press('enter')
#pyautogui.press('enter')
