
from RS import task

# 变化检测
task.change_detection(model_path='static_models/ChangeDetection256x256', data_path='data/CD_img', out_dir='out/CD')

# 目标检测
#task.object_detection(model_path='static_models/ObjectDetection608x608', data_path='data/OD_img', out_dir='out/OD')

# 目标提取
#task.segmenter(model_path='static_models/Segmenter1500x1500', data_path='data/Seg_img', out_dir='out/Seg')

# 地物分类
#task.terrain_classification(model_path='static_models/TerrainClassification256x256', data_path='data/TC_img', out_dir='out/TC')

if __name__ == '__main__':
    task.segmenter(model_path='static_models/Segmenter128x128', data_path='data/Seg_img', out_dir='out/Seg')
