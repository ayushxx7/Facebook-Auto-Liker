import time
import pyautogui
'''
pyautogui.hotkey('alt','tab')
time.sleep(2)
x1 = 224
y1 = 499
m =258
cnt = 0
for l in range(0,20):
    for z in range(0,4):
        pyautogui.moveTo(x1,y1)
        time.sleep(0.5)
        x1 += 210
    x1 = 224
    pyautogui.moveTo(x1,y1)
    time.sleep(0.8)
    pyautogui.scroll(-m)
    cnt += 1
    if cnt == 2:
        m -= 4
        cnt = 0


#pyautogui.scroll(-760)

# 760 scroll difference b/w 1st and 4th image line distance
'''

pyautogui.hotkey('alt', 'tab')
for z in range(0,100):
    time.sleep(0.2)
    if (pyautogui.locateOnScreen('newlikeButton.png')) != None:
        pyautogui.press('l')
    pyautogui.press('right')
    time.sleep(0.2)

'''
<a aria-pressed="false" class="UFILikeLink _4x9- _4x9_ _48-k" data-testid="fb-ufi-likelink" href="#" role="button" tabindex="-1"><!-- react-text: 8 -->Like<!-- /react-text --></a>
'''