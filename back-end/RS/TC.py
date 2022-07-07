from os import listdir
import os.path as osp
import paddlers as pdrs
from skimage.io import imsave
import numpy as np
import cv2


def get_lut():
    lut = np.zeros((256, 3), dtype=np.uint8)
    lut[0] = [255, 0, 0]  # 红
    lut[1] = [30, 255, 142]  # 浅绿
    lut[2] = [60, 0, 255]  # 蓝
    lut[3] = [255, 222, 0]  # 橙黄
    lut[4] = [0, 0, 0]  # 黑
    return lut


def execute(model_path, data_path, out_dir):
    test_names = listdir(data_path)
    test_names = list(filter(lambda n: n.endswith('.jpg'), test_names))[0:10]
    test_names.sort()
    image_list = [osp.join(data_path, name) for name in test_names]
    predictor = pdrs.deploy.Predictor(model_path, use_gpu=True)
    pred = predictor.predict(image_list)
    ims = [i['label_map'] for i in pred]
    lut = get_lut()
    for idx, im in zip(range(len(image_list)), ims):
        if im.ndim == 3:
            im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        im = lut[im]
        imsave(osp.join(out_dir, test_names[idx]), im)
