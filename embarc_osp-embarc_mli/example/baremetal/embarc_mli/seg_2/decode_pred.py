import os
import numpy as np
import scipy.misc as misc
from PIL import Image

pred = []
colors = [  # [  0,   0,   0],
    [128, 64, 128],
    [244, 35, 232],
    [70, 70, 70],
    [102, 102, 156],
    [190, 153, 153],
    [153, 153, 153],
    [250, 170, 30],
    [220, 220, 0],
    [107, 142, 35],
    [152, 251, 152],
    [0, 130, 180],
    [220, 20, 60],
    [255, 0, 0],
    [0, 0, 142],
    [0, 0, 70],
    [0, 60, 100],
    [0, 80, 100],
    [0, 0, 230],
    [119, 11, 32],
]

label_colours = dict(zip(range(19), colors))

def decode_segmap(label_colours, temp):
    r = temp.copy()
    g = temp.copy()
    b = temp.copy()
    for l in range(0, 19):
        r[temp == l] = label_colours[l][0]
        g[temp == l] = label_colours[l][1]
        b[temp == l] = label_colours[l][2]

    rgb = np.zeros((temp.shape[0], temp.shape[1], 3))
    rgb[:, :, 0] = r / 255.0
    rgb[:, :, 1] = g / 255.0
    rgb[:, :, 2] = b / 255.0
    return rgb

out_path = 'result.png'
pred = pred.astype(np.float32)
pred_resize = misc.imresize(pred, orig_size, "nearest", mode="F")

#decoded_resize = loader.decode_segmap(pred_resize)
decoded = decode_segmap(pred)
print("Classes found: ", np.unique(pred))
misc.imsave(out_path, decoded)
print("Segmentation Mask Saved at: {}".format(out_path))