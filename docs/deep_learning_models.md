# 深度学习模型介绍
## 变化检测
- 使用模型：BIT<br>
BIT有三个主要组件：  
*1.Semantic Tokenizer* 连体语义标记器，它将像素分组为概念，为两个不同时间输入图像生成一组紧凑的语义标记；<br>
*2.Transformer Encoder* 转换器编码器，它在基于标签的时空中对语义概念的全局信息建模；<br>
*3.Siamese Transformer Decoder* 连体转换器解码器，它将对应的语义标签投射回像素空间，以获得两个不同时间图像的细化特征图。
<p align="center">
    <img src="../images/zhuyemian.png" align="middle" width = "800" />
</p><p align="center">BIT模型的工作流程</p>
将BIT合并到基于深度特征差分的CD框架中。流程如下：
1.首先，利用CNN主干网（ResNet）用于从输入图像对中提取高级语义特征。
2.利用空间注意将两个不同时间特征图转换为一组紧凑的语义标签。
3.再使用transformer编码器在两个标签集中对全局信息进行建模。
4.生成的含有全局信息丰富的标签由连体transformer解码器重新投影到像素空间，以增强原始像素级特征。
5.最后，从两个细化的特征图中计算特征差异图像（Feature Difference Images，FDI），然后将它们输入到浅层CNN中，以生成像素级的变化预测。 
## 目标检测
