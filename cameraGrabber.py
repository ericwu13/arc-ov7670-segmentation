from serial import Serial, EIGHTBITS, PARITY_NONE, STOPBITS_ONE
import time

import sys

# sys.path.append('/usr/local/lib/python3.5/site-packages')

import cv2
import matplotlib.pyplot as plt
import numpy as np

from skimage import exposure

s = Serial(
    port='/dev/serial/by-id/usb-Digilent_Digilent_USB_Device_251642542476-if00-port0',
    # baudrate=921600,
    baudrate=1000000,
    bytesize=EIGHTBITS,
    parity=PARITY_NONE,
    stopbits=STOPBITS_ONE,
    xonxoff=False,
    rtscts=False
)

b1, b2, b3 = b'\x00', b'\x00', b'\x00'

cnt = 0

img = np.zeros((120, 160, 3)).astype(np.uint8)

while True:
    b1, b2, b3 = b2, b3, s.read(1)

    # print(b3)

    if b1 == b'R' and b2 == b'D' and b3 == b'Y':
        start = time.time();
        print("GET")
        cnt = 0
        while True:
            b1 = s.read(1)
            b2 = s.read(1)
            b1i = int.from_bytes(b1, byteorder='little')
            b2i = int.from_bytes(b2, byteorder='little')
            
            R = b1i // 8

            tmp = b1i % 8

        

            G = tmp * 8 + b2i // 32
            B = b2i % 32

            # print(R, G, B)
            # print(b1, b2);

            img[cnt // 160][cnt % 160][2] = np.clip(R * 8, 0, 255)
            img[cnt // 160][cnt % 160][1] = np.clip((R+B)*4, 0, 255)
            img[cnt // 160][cnt % 160][0] = np.clip(B * 8, 0, 255)

            cnt = cnt + 1
            if cnt == 160 * 120:
                break

        # print("PLOT")
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # img2 = img[:, :, 2]

        img2 = exposure.equalize_adapthist(img, clip_limit=0.03)
        img2 = cv2.resize(img2[:,:,:], (640, 480))
        # img3 = cv2.resize(img[:,:,0], (640, 480))
        print("fps = {}".format(1./(time.time()-start)))
        cv2.imshow("", img2)
        # cv2.imshow("R", img3)
        cv2.waitKey(1)
