import time
import keyboard
from PIL import ImageGrab

def screenshot():
    #2020년 8월 28일 17시 30분 30초 -> 20200828_173030
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("imgae{}.png".format(curr_time)) #image_20200828_173030.pnh

keyboard.add_hotkey("F9",screenshot) # 사용자가 F9 키를 누르면 스크린 샷 저장

keyboard.wait("esc") # 사용자가 esc를 누를 때까지 프로그램 수행