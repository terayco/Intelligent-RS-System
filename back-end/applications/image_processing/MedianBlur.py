import cv2
import os.path as osp
from glob import glob

from applications.common.path_global import md5_name


def Median_Blur(src_dir, save_dir, names):
    temps = list()
    for name in names:
        Gn = cv2.imread(osp.join(src_dir, name))
        Gf = cv2.medianBlur(Gn, 3)
        new_name = md5_name(name)
        cv2.imwrite(osp.join(save_dir, new_name), Gf)
        temps.append(new_name)
    return temps
