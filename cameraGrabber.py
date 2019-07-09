import time
import sys
import cv2
import matplotlib.pyplot as plt
import numpy as np
import torch.nn.functional as F
import torch

from skimage import exposure
from serial import Serial, EIGHTBITS, PARITY_NONE, STOPBITS_ONE
s = Serial(
        port='/dev/serial/by-id/usb-Digilent_Digilent_USB_Device_251642542476-if00-port0',
        baudrate=1000000,
        bytesize=EIGHTBITS,
        parity=PARITY_NONE,
        stopbits=STOPBITS_ONE,
        xonxoff=False,
        rtscts=False
    )

def predDecoder():
    cnt = 0;
    # print(s.readline())
    while True:
        b = s.read(1)
        f = int.from_bytes(b, byteorder='little')
        if f != 0:
            print((f))
        cnt = cnt + 1
        if cnt == 512:
            break;


def main():

    b1, b2, b3 = b'\x00', b'\x00', b'\x00'

    cnt = 0
    RGB = True;

    img = np.zeros((64, 64, 3)).astype(np.uint8)

    while True:
        b1, b2, b3 = b2, b3, s.read(1)

        if b1 == b'R' and b2 == b'D' and b3 == b'Y':
            start = time.time();
            print("GET")
            cnt = 0
            while True:
                if(not RGB):
                    b1 = s.read(1)
                    b2 = s.read(1)
                    b1i = int.from_bytes(b1, byteorder='little')
                    b2i = int.from_bytes(b2, byteorder='little')
                    R = b1i // 8
                    tmp = b1i % 8
                    G = tmp * 8 + b2i // 32
                    B = b2i % 32
                else:
                    b1 = s.read(1)
                    b2 = s.read(1)
                    b3 = s.read(1)
                    R = int.from_bytes(b1, byteorder='little')
                    G = int.from_bytes(b2, byteorder='little')
                    B = int.from_bytes(b3, byteorder='little')


                # print(R, G, B)
                # print(b1, b2);

                img[cnt // 64][cnt % 64][2] = np.clip(R * 8, 0, 255)
                img[cnt // 64][cnt % 64][1] = np.clip((R+B)*4, 0, 255)
                img[cnt // 64][cnt % 64][0] = np.clip(B * 8, 0, 255)

                cnt = cnt + 1
                if cnt == 64 * 64:
                    predDecoder()
                    break

            img2 = exposure.equalize_adapthist(img, clip_limit=0.03)
            img2 = cv2.resize(img2[:,:,:], (640, 640))

            print("fps = {}".format(1./(time.time()-start)))

            cv2.imshow("", img2)
            cv2.waitKey(1)

if __name__ == "__main__":
    main()