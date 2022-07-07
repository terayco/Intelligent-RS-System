from os import listdir
import os.path as osp
import paddlers as pdrs
from skimage.io import imsave
import cv2
from operator import itemgetter
from tqdm import tqdm
import numpy as np

from applications.common.path_global import md5_name, generate_url


class WindowGenerator:
    def __init__(self, h, w, ch, cw, si=1, sj=1):
        self.h = h
        self.w = w
        self.ch = ch
        self.cw = cw
        if self.h < self.ch or self.w < self.cw:
            raise NotImplementedError
        self.si = si
        self.sj = sj
        self._i, self._j = 0, 0

    def __next__(self):
        # 列优先移动（C-order）
        if self._i > self.h:
            raise StopIteration

        bottom = min(self._i + self.ch, self.h)
        right = min(self._j + self.cw, self.w)
        top = max(0, bottom - self.ch)
        left = max(0, right - self.cw)

        if self._j >= self.w - self.cw:
            if self._i >= self.h - self.ch:
                # 设置一个非法值，使得迭代可以early stop
                self._i = self.h + 1
            self._goto_next_row()
        else:
            self._j += self.sj
            if self._j > self.w:
                self._goto_next_row()

        return slice(top, bottom, 1), slice(left, right, 1)

    def __iter__(self):
        return self

    def _goto_next_row(self):
        self._i += self.si
        self._j = 0


def crop_patches(dataloader, ori_size, window_size, stride):
    """
    将`dataloader`中的数据裁块。

    Args:
        dataloader: 可迭代对象，返回图片名称和图片矩阵。
        ori_size (tuple): 原始影像的长和宽，表示为二元组形式(h,w)。
        window_size (int): 裁块大小。
        stride (int): 裁块使用的滑窗每次在水平或垂直方向上移动的像素数。

    Returns:
        一个生成器，能够产生iter(`dataloader`)中每一项的裁块结果。一幅图像产生的块在batch维度拼接。例如，当`ori_size`为1024，而
            `window_size`和`stride`均为512时，`crop_patches`返回的每一项的batch_size都将是iter(`dataloader`)中对应项的4倍。
    """

    for name, im in dataloader:
        h, w = ori_size
        win_gen = WindowGenerator(h, w, window_size, window_size, stride, stride)  # (256，256)
        all_patches = []  # 两张图片的全部裁块
        for rows, cols in win_gen:
            # NOTE: 此处不能使用生成器，否则因为lazy evaluation的缘故会导致结果不是预期的
            patches = im[rows, cols]
            all_patches.append(patches)
        yield name, all_patches


def recons_prob_map(patches, ori_size, window_size, stride):
    """从裁块结果重建原始尺寸影像，与`crop_patches`相对应"""
    # NOTE: 目前只能处理batch size为1的情况
    h, w = ori_size
    win_gen = WindowGenerator(h, w, window_size, window_size, stride, stride)
    prob_map = np.zeros((h, w), dtype=np.float)
    cnt = np.zeros((h, w), dtype=np.float)
    # XXX: 需要保证win_gen与patches具有相同长度。此处未做检查
    for (rows, cols), patch in zip(win_gen, patches):
        prob_map[rows, cols] += patch
        cnt[rows, cols] += 1
    prob_map /= cnt
    return prob_map


class data_loader():
    def __init__(self, image_list):
        self.image_list = image_list
        self.idx = 0

    def __next__(self):
        if self.idx >= len(self.image_list):
            raise StopIteration
        name = osp.basename(self.image_list[self.idx])
        im = cv2.imread(self.image_list[self.idx])
        self.idx += 1
        return name, im

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.image_list)


def execute(model_path, data_path, out_dir, names):
    image_list = [osp.join(data_path, name) for name in names]
    test_dataset = data_loader(image_list)
    WINDOW_SIZE = 256
    STRIDE = 128
    ORIGINAL_SIZE = [1500, 1500]
    test_patches = crop_patches(
        test_dataset,
        ORIGINAL_SIZE,
        WINDOW_SIZE,
        STRIDE
    )

    # 构建预测器并执行推理
    predictor = pdrs.deploy.Predictor(model_path, use_gpu=True)

    len_test = len(test_dataset)
    temps = list()
    temps1 = list()
    for name, patches in tqdm(test_patches, total=len_test):
        res = predictor.predict(patches)
        prob_patches = map(itemgetter('label_map'), res)
        prob_map = recons_prob_map(list(prob_patches), ORIGINAL_SIZE, WINDOW_SIZE, STRIDE)
        new_name = md5_name(name)
        imsave(osp.join(out_dir, new_name), prob_map, check_contrast=False)
        temps.append(generate_url + new_name)
        temps1.append(new_name)
    return temps,temps1
