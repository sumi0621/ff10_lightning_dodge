import cv2
import pydirectinput as direct
from PIL import ImageGrab
import numpy as np

def main():
    counter = 0

    while True:
        # Keep advancing to the wall and do not go outside the lightning strike area.
        direct.keyDown('up')
        
        # Capture screen and convert to unified size
        img = ImageGrab.grab()
        cv_img = np.array(img, dtype=np.uint8)
        cv_img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)
        frame = cv2.resize(cv_img,(100,100))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        retu, binal = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
        screen_white_ave = np.sum(binal) // 10000

        # When the screen goes white, press enter to dodge lightning.
        # Count the number of times you avoided lightning.
        if screen_white_ave > 200:
            direct.press('enter')
            print(counter)
            counter+=1

if __name__ == '__main__':
    main()
