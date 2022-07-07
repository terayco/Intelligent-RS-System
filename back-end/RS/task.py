from RS import Seg
from RS import TC
from RS import CD
from RS import OD


def change_detection(model_path, data_path, out_dir):
    """
    变化检测
    :param modir_path: 静态图模型路径
    :param data_path: 图片数据路径，路径中有名称为A和B的两个文件夹分别存储不同时相的图片（1024，1024），且相应图片名称相同
    :param out_dir:图片保存路径
    :return:
    """
    CD.execute(model_path, data_path, out_dir)


def object_detection(model_path, data_path, out_dir):
    """
    目标检测
    :param model_path:
    :param data_path:
    :param out_dir:
    :return:
    """
    OD.execute(model_path, data_path, out_dir)


def segmenter(model_path, data_path, out_dir):
    """
    目标提取
    :param model_path:
    :param data_path:
    :param out_dir:
    :return:
    """
    Seg.execute(model_path, data_path, out_dir)


def terrain_classification(model_path, data_path, out_dir):
    """
    地物分类
    :param model_path:
    :param data_path:
    :param out_dir:
    :return:
    """
    TC.execute(model_path, data_path, out_dir)
