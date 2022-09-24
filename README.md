![](images/paddleRS.png)
# 基于百度飞桨paddlepaddle的遥感图像智能解译平台
 [![License](https://img.shields.io/badge/license-MIT%20-blue.svg)](LICENSE)
  ![python version](https://img.shields.io/badge/python-3.8+-orange.svg)
  ![support os](https://img.shields.io/badge/os-linux%2C%20win%2C%20mac-yellow.svg)
## 演示视频
网址：https://www.bilibili.com/video/BV1eY4y1u7Eq/?vd_source=75a73fc15a4e8b25195728ee93a5b322
## 介绍
本项目为第十一届中国软件杯一等奖作品，基于[百度飞桨Paddle](https://www.paddlepaddle.org.cn/)框架和[PaddleRS](https://github.com/PaddleCV-SIG/PaddleRS)库开发，以web形式为用户提供遥感图像智能解译服务。
## Overview
* 系统组成
  * [平台主页](docs/system_component_main.md)
  * [功能区](docs/system_component_function.md)
* [系统架构设计](docs/system_design.md)
* [深度学习模型介绍](docs/deep_learning_models.md)
## 平台特点
- 用户不仅可以使用基本功能，还可以通过本平台了解遥感相关讯息
- 适应性强，对图片大小、分辨率无要求限制
- 界面美观，使用体验良好
## 功能实现
本平台的主要功能如下：
###### 基本功能
- 1.变化检测
- 2.目标检测
- 3.目标提取
- 4.地物分类
- 5.在线地图
###### 扩展功能
- 1.直方图匹配（针对变化检测使用，使两个时期图片风格保持一致）
- 2.连通域滤波及孔洞填充（有效提高变化检测结果图准确率）
- 3.CLAHE（限制对比度自适应直方图均衡化，用于增强图像对比图）
- 4.锐化处理（突出地物边缘，轮廓或某些线性目标要素的特征）
- 5.中值滤波（对应本平台“平滑”功能）
- 6.高斯滤波（对应本平台“滤波”功能）
- 7.渲染（对于变化检测/目标提取功能用户可选择不同的渲染风格进行结果展示）
- 8.问题反馈（若用户对于处理结果不满意可以进行反馈，促使我们可以更好地改进平台）
- 9.图片压缩打包下载（用户可以对多张图片进行压缩打包下载）
- 10.图片编辑（用户可以对除变化检测外的三个功能的待处理图片进行预先编辑后再上传）
## Contributing
如果你有好的意见或建议，欢迎给我们提 Issues 或 Pull Requests。
## 技术交流
技术交流QQ群（873208513）扫码进群戳[这里](images/erweima.jpg)
## License
项目基于 MIT 协议，详细请参考 [LICENSE](LICENSE)。
## 作者
**HHU-河马海牛队**<p align="r">
    <img src="images/logo.png" align="middle" width = "100" />
</p>


