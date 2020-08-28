import time
from PIL import ImageGrab

time.sleep(5) #사용자가 5초 대기

for i in range(1,11):
    img= ImageGrab.grab()
    img.save("image{}.png".format(i)) #파일로 저장( image1.png~image10.png)
    time.sleep(2)
