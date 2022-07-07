<template>
  <div>
    <img :src="require('../../assets/image/technology/72.jpg')" class="bg" />
    <MyHeader class="theheader"> </MyHeader>
    <div class="title">技术实现</div>
    <div class="title-en">Technical realization</div>
     <div class="title-img">     <img
            :src="require('../../assets/image/decoration/49.png')"
            style="width: 400px"
          /></div>
    <div
      class="divider title-bg"
      :style="{ backgroundImage: 'url(' + Img6 + ')' }"
      style="font-family: Microsoft JhengHei UI, sans-serif; color: white"
    >
      深度学习部分
    </div>
    <div class="bit">
      <el-row justify="center"
        ><el-col :span="6" class="deeplearning-title"
          >变化检测使用模型：BIT</el-col
        ></el-row
      >
      <el-row justify="center" align="middle" :gutter="20"
        ><el-col :xs="20" :sm="20" :md="13" :lg="13" :xl="13"
          ><div class="bit-img">
            <img
              :src="require('../../assets/image/technology/71.jpg')"
              style="width: 600px"
            /></div></el-col
        ><el-col :xs="20" :sm="20" :md="9" :lg="9" :xl="10"
          ><div class="bit-words">
            <p>采用BIT模型，使用Resnet18为backbone</p>
            <p>数据增强：随机裁剪、随机水平翻转、随机垂直翻转、数据归一化</p>
            <p>推理脚本使用固定阈值法从变化概率图获取二值变化图</p>
          </div></el-col
        ></el-row
      >
    </div>

    <div class="bit">
      <el-row justify="center"
        ><el-col :span="8" class="deeplearning-title"
          >变化检测使用模型：DeepLab V3+</el-col
        ></el-row
      >
      <el-row justify="center" align="middle" :gutter="20"
        ><el-col :xs="20" :sm="20" :md="13" :lg="13" :xl="13"
          ><div class="bit-img">
            <img :src="require('../../assets/image/technology/42.png')" /></div></el-col
        ><el-col :xs="20" :sm="20" :md="9" :lg="9" :xl="10"
          ><div class="bit-words">
            <p>DeepLab V3+模型，使用ResNet-50作为backbone</p>
            <p>使用focal loss作为损失函数</p>
            <p>数据变换：影像缩放、随机水平翻转、数据归一化</p>
          </div></el-col
        ></el-row
      >
    </div>

    <div class="bit">
      <el-row justify="center"
        ><el-col :span="6" class="deeplearning-title"
          >变化检测使用模型：PP-YOLO</el-col
        ></el-row
      >
      <el-row justify="center" align="middle" :gutter="20"
        ><el-col :xs="20" :sm="20" :md="13" :lg="13" :xl="13"
          ><div class="bit-img">
            <img
              :src="require('../../assets/image/technology/44.png')"
              style="width: 600px"
            /></div></el-col
        ><el-col :xs="20" :sm="20" :md="9" :lg="9" :xl="10"
          ><div class="bit-words">
            <p>
              数据增强：随机色彩扰动、随机padding、随机裁剪、随机水平翻转、对batch进行随机缩放、影像归一化
            </p>
          </div></el-col
        ></el-row
      >
    </div>

    <div class="bit">
      <el-row justify="center"
        ><el-col :span="6" class="deeplearning-title"
          >变化检测使用模型：DeepLab V3+</el-col
        ></el-row
      >
      <el-row justify="center" align="middle" :gutter="20"
        ><el-col :xs="20" :sm="20" :md="13" :lg="13" :xl="13"
          ><div class="bit-img">
            <img :src="require('../../assets/image/technology/42.png')" /></div></el-col
        ><el-col :xs="20" :sm="20" :md="9" :lg="9" :xl="10"
          ><div class="bit-words">
            <p>DeepLab V3+模型，使用ResNet-50作为backbone</p>
            <p>
              数据增强：随机裁剪、以50%的概率实施随机水平翻转、以50%的概率实施随机垂直翻转、数据归一化
            </p>
          </div></el-col
        ></el-row
      >
    </div>

    <div
      class="divider"
      :style="{ backgroundImage: 'url(' + Img8 + ')' }"
      style="
        color: rgb(65, 184, 131);
        font-family: Microsoft JhengHei UI, sans-serif;
      "
    >
      前端部分
    </div>
    <div class="vue">
      <el-row type="flex" justify="center" align="middle">
        <el-col :span="7" class="hidden-sm-and-down"
          ><img :src="require('../../assets/image/technology/36.png')" class="vue-img"
        /></el-col>
        <el-col :span="14"
          ><div class="vue-words">
            基于<span style="color: #42b983">VUE3</span>的网页设计
          </div>
          <div class="feature">
            <div class="feature-title">易用</div>
            <div class="feature-words">
              已经会了 HTML、CSS、JavaScript？即刻阅读指南开始构建应用！
            </div>
          </div>
          <div class="feature">
            <div class="feature-title">灵活</div>
            <div class="feature-words">
              不断繁荣的生态系统，可以在一个库和一套完整框架之间自如伸缩。
            </div>
          </div>
          <div class="feature">
            <div class="feature-title">高效</div>
            <div class="feature-words">
              20kB min+gzip 运行大小 超快虚拟 DOM 最省心的优化
            </div>
          </div></el-col
        >
      </el-row>
    </div>
    <div class="element">
      <el-row :gutter="20" justify="center" align="middle">
        <el-col :xs="20" :sm="20" :md="10" :lg="10" :xl="10"
          ><div class="element-title">
            <span style="color: rgb(64, 158, 255)">Element Plus</span>
            <div>基于 Vue 3，面向设计师和开发者的组件库</div>
          </div>
          <div></div
        ></el-col>
        <el-col :xs="20" :sm="20" :md="10" :lg="10" :xl="10">
          <img
            :src="require('../../assets/image/technology/37.png')"
            style="width: 700px"
            class="hidden-sm-and-down"
        /></el-col>
      </el-row>
      <el-row :gutter="20" justify="center" align="middle"
        ><el-col :xs="20" :sm="20" :md="7" :lg="7" :xl="7" class="html-box"
          ><div class="element-words">
            合适的网页布局容器<i class="iconfont icon-duigou"></i>
          </div>
          <div class="element-box">
            <el-row type="flex" justify="center" align="middle">
              <el-col :span="7" style="height: 100%"
                ><div class="element-aside">aside导航栏</div></el-col
              >
              <el-col :span="12"
                ><div class="element-header">header头部</div>
                <div class="element-main">main主体内容</div>
              </el-col>
            </el-row>
          </div></el-col
        ><el-col :xs="20" :sm="20" :md="7" :lg="8" :xl="7" class="geid-box"
          ><div class="grid-words">
            通过24分栏组合形成较复杂的混合布局<i
              class="iconfont icon-duigou"
            ></i>
          </div>
          <el-row :gutter="20">
            <el-col :span="16"
              ><div class="grid-content bg-purple"></div
            ></el-col>
            <el-col :span="8"
              ><div class="grid-content bg-purple"></div
            ></el-col>
          </el-row>
          <el-row :gutter="20">
            <el-col :span="8"
              ><div class="grid-content bg-purple"></div
            ></el-col>
            <el-col :span="8"
              ><div class="grid-content bg-purple"></div
            ></el-col>
            <el-col :span="4"
              ><div class="grid-content bg-purple"></div
            ></el-col>
            <el-col :span="4"
              ><div class="grid-content bg-purple"></div
            ></el-col>
          </el-row>
          <el-row :gutter="20">
            <el-col :span="4"
              ><div class="grid-content bg-purple"></div
            ></el-col>
            <el-col :span="16"
              ><div class="grid-content bg-purple"></div
            ></el-col>
            <el-col :span="4"
              ><div class="grid-content bg-purple"></div
            ></el-col> </el-row></el-col
        ><el-col
          :xs="20"
          :sm="20"
          :md="7"
          :lg="7"
          :xl="7"
          style="text-align: center"
        >
          <div class="element-words">
            美观的消息提示<i class="iconfont icon-duigou"></i>
          </div>
          <el-button :plain="true" @click="open2">成功</el-button>
          <el-button :plain="true" @click="open3">警告</el-button>
          <el-button :plain="true" @click="open1">消息</el-button>
          <el-button :plain="true" @click="open4">错误</el-button></el-col
        ></el-row
      >
    </div>
    <div class="axios">
      <el-row :gutter="10" justify="center" align="middle"
        ><el-col :xs="20" :sm="20" :md="10" :lg="10" :xl="10"
          ><img
            :src="require('../../assets/image/technology/39.jpeg')"
            class="hidden-xs-only"
            style="margin-right: 70px" /></el-col
        ><el-col :xs="20" :sm="20" :md="10" :lg="10" :xl="10"
          ><div class="axios-title">
            基于<span style="color: rgb(90, 41, 229)">axios</span>的网络请求
          </div>
          <div class="axios-words">
            是一个基于promise网络请求库，作用于node.js和浏览器中，它是
            isomorphic
            的(即同一套代码可以运行在浏览器和node.js中)。在服务端它使用原生node.js
            http模块, 而在客户端 (浏览端)
            则使用XMLHttpRequests，从而实现前后端的交互。
          </div></el-col
        ></el-row
      >
      <el-row :gutter="10" justify="center" align="middle"
        ><el-col :xs="20" :sm="20" :md="10" :lg="10" :xl="10"
          ><div class="axios-feature">
            <i class="iconfont icon-shan-dian"></i>支持node端和浏览器端
          </div>
          <div class="axios-f-words">
            同样的API，node和浏览器全支持，平台切换无压力
          </div></el-col
        ><el-col :xs="20" :sm="20" :md="10" :lg="10" :xl="10"
          ><div class="axios-feature">
            <i class="iconfont icon-bianji"></i>支持 Promise
          </div>
          <div class="axios-f-words">
            使用Promise管理异步，告别传统callback方式
          </div></el-col
        ><el-col :xs="20" :sm="20" :md="10" :lg="10" :xl="10"
          ><div class="axios-feature">
            <i class="iconfont icon-yunduanshangchuan"></i>丰富的配置项
          </div>
          <div class="axios-f-words">支持拦截器等高级配置</div></el-col
        ><el-col :xs="20" :sm="20" :md="10" :lg="10" :xl="10"
          ><div class="axios-feature">
            <i class="iconfont icon-shezhi"></i>社区支持
          </div>
          <div class="axios-f-words">
            axios相关的npm包数量一直在增长
          </div></el-col
        ></el-row
      >
    </div>
        
    <div
      class="divider"
      :style="{ backgroundImage: 'url(' + Img9 + ')' }"
      style="
        color: rgb(64, 158, 255);
        font-family: Microsoft JhengHei UI, sans-serif;
      "
    >
      后端部分
    </div>
    <div class="vue">
      <!-- <div :style="{ backgroundImage: 'url(' + Img5 + ')' }"  style="height: 100vh"></div> -->
      <el-row type="flex" justify="center" align="middle">
        <el-col :span="7" class="hidden-sm-and-down"
          ><img :src="require('../../assets/image/technology/61.jpeg')" class="vue-img"
        /></el-col>
        <el-col :span="14"
          ><div
            class="vue-words"
            style="font-family: Microsoft JhengHei UI, sans-serif"
          >
            Flask是一个<span class="color-cha">轻量级</span>的<span
              class="color-cha"
              >可定制</span
            >框架，使用<span class="color-cha">Python</span
            >语言编写，较其他同类型框架更为灵活、轻便、安全且容易上手。
          </div>
        </el-col>
      </el-row>
    </div>

    <div
      class="divider title-bg"
      :style="{ backgroundImage: 'url(' + Img7 + ')' }"
      style="color: white; font-family: Microsoft JhengHei UI, sans-serif"
    >
      关于我们
    </div>
    <el-row :gutter="20" justify="space-evenly">
      <el-col :xs="20" :sm="9" :md="7" :lg="5" :xl="5">
        <div class="wesingle" :style="{ backgroundImage: 'url(' + Img1 + ')' }">
          <img
            :src="require('../../assets/image/technology/28.jpg')"
            class="avater"
            @mouseenter="goSee(0)"
          />

          <h2 id="name">yibaikuai</h2>

          <div class="border-style-4">
            <span class="words">破局</span>
          </div>
          <div class="connect">
            <i class="iconfont icon-github" @click="goGitHub('yibaikuai')"></i
            ><i
              class="iconfont icon-QQ"
              @mouseenter="goSeeQQimg(0)"
              @mouseleave="goUnseenQQimg(0)"
            ></i>
            <img :src="require('../../assets/image/technology/52.png')" class="qq-img" />
          </div></div
      ></el-col>
      <el-col :xs="20" :sm="9" :md="7" :lg="5" :xl="5">
        <div class="wesingle" :style="{ backgroundImage: 'url(' + Img2 + ')' }">
          <img
            :src="require('../../assets/image/technology/40.png')"
            class="avater"
            @mouseenter="goSee(1)"
          />
          <h2 id="name2">辣椒酱</h2>
          <div class="border-style-4">
            <span class="words">Every melody is timeless</span>
          </div>
          <div class="connect">
            <i class="iconfont icon-github" @click="goGitHub('terayco')"></i
            ><i
              class="iconfont icon-QQ"
              @mouseenter="goSeeQQimg(1)"
              @mouseleave="goUnseenQQimg(1)"
            ></i>
            <img
              :src="require('../../assets/image/technology/55.png')"
              class="qq-img qq-img2"
            />
          </div></div
      ></el-col>
      <el-col :xs="20" :sm="9" :md="7" :lg="5" :xl="5">
        <div class="wesingle" :style="{ backgroundImage: 'url(' + Img3 + ')' }">
          <img
            :src="require('../../assets/image/technology/41.jpg')"
            class="avater"
            @mouseenter="goSee(2)"
          />
          <h2 id="name2">武虎</h2>
          <div class="border-style-4">
            <span class="words">源头白鹿,水畔青牛</span>
          </div>
          <div class="connect">
            <i class="iconfont icon-github" @click="goGitHub('wu-hu555')"></i
            ><i
              class="iconfont icon-QQ"
              @mouseenter="goSeeQQimg(2)"
              @mouseleave="goUnseenQQimg(2)"
            ></i>
            <img :src="require('../../assets/image/technology/54.png')" class="qq-img" />
          </div></div
      ></el-col>
      <el-col :xs="20" :sm="9" :md="7" :lg="5" :xl="5"
        ><div
          class="wesingle"
          :style="{ backgroundImage: 'url(' + Img4 + ')' }"
        >
          <img
            :src="require('../../assets/image/technology/42.jpg')"
            class="avater"
            @mouseenter="goSee(3)"
          />
          <h2 id="name">Monster</h2>
          <div class="border-style-4">
            <span class="words">We don't stay dead long</span>
          </div>
          <div class="connect">
            <i class="iconfont icon-github"></i
            ><i
              class="iconfont icon-QQ"
              @mouseenter="goSeeQQimg(3)"
              @mouseleave="goUnseenQQimg(3)"
            ></i>
            <img :src="require('../../assets/image/technology/53.png')" class="qq-img" />
          </div></div
      ></el-col>
    </el-row>
    <MyFooter></MyFooter>
  </div>
</template>

<script>
import Img1 from "@/assets/image/technology/29.jpeg";
import Img2 from "@/assets/image/technology/31.jpg";
import Img3 from "@/assets/image/technology/32.jpg";
import Img4 from "@/assets/image/technology/33.jpg";
import Img5 from "@/assets/image/technology/36.png";
import Img6 from "@/assets/image/technology/70.jpg";
import Img7 from "@/assets/image/technology/74.jpg";
import Img8 from "@/assets/image/technology/78.jpg";
import Img9 from "@/assets/image/technology/79.jpg";

import MyHeader from "@/components/MyHeader";
import MyFooter from "@/components/MyFooter";
export default {
  name: "technology",
  components: {
    MyHeader,
    MyFooter,
  },
  data() {
    return {
      Img1,
      Img2,
      Img3,
      Img4,
      Img5,
      Img6,
      Img7,
      Img8,
      Img9,
    };
  },
  mounted() {
        document.body.style.overflow = "auto";
  },
  methods: {
    open1() {
      this.$message("这是一条消息提示");
    },
    open2() {
      this.$message({
        message: "恭喜你，这是一条成功消息",
        type: "success",
      });
    },
    open3() {
      this.$message({
        message: "警告哦，这是一条警告消息",
        type: "warning",
      });
    },
    open4() {
      this.$message.error("错了哦，这是一条错误消息");
    },
    goSee(index) {
      let x = document.querySelectorAll(".connect");
      x[index].classList.add("cansee");
    },
    goGitHub(string) {
      window.open(`https://github.com/${string}`);
    },
    goSeeQQimg(index) {
      let x = document.querySelectorAll(".qq-img");
      x[index].classList.add("active-qqimg");
    },
    goUnseenQQimg(index) {
      let x = document.querySelectorAll(".qq-img");
      x[index].classList.remove("active-qqimg");
    },
  },
    beforeRouteEnter(to, from, next) {
    next((vm) => {
      document.querySelector(".el-main").scrollTop = 0;
    });
  },
};
</script>

<style scoped>
* {
  letter-spacing: 2px;
  margin-bottom: 10px;
}
#name2 {
  display: inline-block;

  text-align: center;
  font-family: Microsoft JhengHei UI, sans-serif;
  font-size: 40px;
}
.bit-feature {
  margin-top: 40px;
  text-align: center;
  font-size: 20px;
  font-family: Open Sans, Inter, Roboto, Oxygen, Fira Sans, Helvetica Neue,
    sans-serif;
  height: 200px;
}
.bit-img {
  text-align: center;
  width: auto;
  background: rgb(255, 255, 255);
  border-radius: 5px;
  border: 1px solid rgba(0, 0, 255, 0.2);
  transition: all 0.2s;
  box-shadow: 12px 12px 2px 1px rgba(0, 0, 255, 0.2);
}
.bit-img:hover {
  box-shadow: -12px 12px 2px -1px rgba(0, 0, 255, 0.2);
}
.bit-words {
  margin-top: 40px;
  text-align: center;
  font-size: 20px;
  font-family: Open Sans, Inter, Roboto, Oxygen, Fira Sans, Helvetica Neue,
    sans-serif;
}
.deeplearning-title {
  text-align: center;
  font-weight: 600;
  font-size: 22px;
  font-family: Helvetica Neue, Helvetica, PingFang SC, Hiragino Sans GB,
    Microsoft YaHei, 微软雅黑, Arial, sans-serif;
  background-color: rgba(255, 255, 255, 0.15);
  border: 0.8px solid rgba(255, 255, 255, 0.18);
  box-shadow: rgba(142, 142, 142, 0.19) 0px 6px 15px 0px;
  -webkit-box-shadow: rgba(142, 142, 142, 0.19) 0px 6px 15px 0px;
  border-radius: 11px;
  -webkit-border-radius: 11px;
  color: black;
}
.connect {
  margin-top: 30px;
  transition: all 0.5s;
  font-size: 20px;
  opacity: 0;
  position: relative;
  z-index: -1;
}
.qq-img {
  z-index: 100;
  width: 150px;
  position: absolute;
  border-radius: 5px;
  border: 1px solid skyblue;
  transition: all 0.5s;
  opacity: 0;
  top: -50px;
}
.active-qqimg {
  opacity: 1;
}
.cansee {
  opacity: 1;
  z-index: 10;
}
.icon-github,
.icon-QQ {
  font-size: 40px !important;
}
.icon-duigou {
  color: green;
  display: inline-block;
  font-size: 23px;
}
.iconfont {
  margin-right: 10px;
  font-size: 30px;
  transition: all 0.6s;
}
.el-col-7 {
  flex: 0;
}
.divider {
  margin: 0 auto;
  border-radius: 5px;
  text-align: center;
  letter-spacing: 30px;
  line-height: 200px;
  margin-bottom: 20px;
  width: 96%;
  height: 200px;
  font-weight: 600;
  font-size: 34px;
  font-family: Helvetica Neue, Helvetica, PingFang SC, Hiragino Sans GB,
    Microsoft YaHei, 微软雅黑, Arial, sans-serif;
  border: 1px solid rgba(0, 0, 255, 0.2);
  transition: all 0.2s;
  box-shadow: 12px 12px 2px 1px rgba(0, 0, 255, 0.2);
}
.divider:hover {
  box-shadow: -12px 12px 2px -1px rgba(0, 0, 255, 0.2);
}
.axios {
  text-align: center;
  border-radius: 2px;
  font-family: Open Sans, Inter, Roboto, Oxygen, Fira Sans, Helvetica Neue,
    sans-serif;
}
.iconfont:hover {
  transform: rotateY(360deg);
}
.axios-title {
  text-align: center;
  font-weight: 600;
  font-size: 34px;
  font-family: Helvetica Neue, Helvetica, PingFang SC, Hiragino Sans GB,
    Microsoft YaHei, 微软雅黑, Arial, sans-serif;
}
.axios-feature {
  text-align: center;
  margin-top: 45px;
  margin-bottom: 15px;
  color: #009688;
  font-family: Lato, "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 24px;
}
.axios-f-words {
  text-align: center;
  margin-bottom: 20px;
}
.element {
  border-radius: 2px;
  font-family: Open Sans, Inter, Roboto, Oxygen, Fira Sans, Helvetica Neue,
    sans-serif;
}
.element-words {
  margin-bottom: 20px;
  font-size: 20px;
  text-align: center;
}
.element-header {
  text-align: center;
  background-color: rgb(198, 226, 255);
  height: 50px;
  transition: all 0.5s;
  display: grid;
  align-content: center;
  width: 100%;
  margin-bottom: 0;
}
.element-main {
  text-align: center;
  background-color: rgb(236, 245, 255);
  height: 400px;
  width: 100%;
  transition: all 0.5s;
  display: grid;
  align-content: center;
  margin-bottom: 0;
}
.element-aside {
  width: 100px;
  text-align: center;
  background-color: rgb(217, 236, 255);
  margin-bottom: 0;
  height: 450px;
  transition: all 0.5s;
  display: grid;
  align-content: center;
}
.element-header:hover {
  -webkit-box-shadow: #ccc 0px 10px 10px;

  -moz-box-shadow: #ccc 0px 10px 10px;

  box-shadow: #ccc 0px 10px 10px;
  transform: scale(1.1);
}
.element-main:hover {
  -webkit-box-shadow: #ccc 0px 10px 10px;

  -moz-box-shadow: #ccc 0px 10px 10px;

  box-shadow: #ccc 0px 10px 10px;
  transform: scale(1.05);
}
.element-aside:hover {
  -webkit-box-shadow: #ccc 0px 10px 10px;

  -moz-box-shadow: #ccc 0px 10px 10px;

  box-shadow: #ccc 0px 10px 10px;
  transform: scale(1.05);
}
.grid-content:hover {
  -webkit-box-shadow: #ccc 0px 10px 10px;

  -moz-box-shadow: #ccc 0px 10px 10px;

  box-shadow: #ccc 0px 10px 10px;
  transform: scale(1.05);
}
.grid-words {
  text-align: center;
  margin-bottom: 20px;
  font-size: 20px;
}
.theheader {
  height: 0;
  z-index: 200;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  color: white;
}
li {
  height: 200px;
}
.wesingle {
  padding-top: 30px;
  text-align: center;
  margin-top: 20px;
  height: 400px;
  border-color: skyblue;
  border-top: none;
}
.avater {
  width: 70px;
  height: 70px;
  transition: all 0.5s;
  color: #000;
  border-radius: 50%;
}
.avater:hover {
  /* border-radius: 25%; */
  transform: scale(1.5);
}
#name {
  display: inline-block;

  text-align: center;
  font-family: Freestyle Script;
  font-size: 40px;
}
.words {
  letter-spacing: 2px;
  font-family: "Montserrat", sans-serif;
  top: 46px;
  left: 0;
  right: 0;
  position: absolute;
}
.border-style-4 {
  opacity: 0.7;
  margin: 0 auto;
  position: relative;
  width: 220px;
  height: 130px;
  background: linear-gradient(-150deg, transparent 1.5em, #d1fdff 0);
  border-radius: 0.5em;
}
.border-style-4::before {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  background: linear-gradient(
      to left bottom,
      transparent 50%,
      rgba(0, 0, 0, 0.2) 0,
      rgba(0, 0, 0, 0.4)
    )
    100% 0 no-repeat;
  width: 1.73em;
  height: 3em;
  transform: translateY(-1.3em) rotate(-30deg);
  transform-origin: bottom right;
  border-bottom-left-radius: inherit;
  box-shadow: -0.2em 0.2em 0.3em -0.1em rgba(0, 0, 0, 0.15);
}
.vue {
  position: relative;
  width: 100%;

  align-items: center;
  text-align: center;
}
.vue-img {
  width: 400px;
}
@keyframes border-style-2 {
  to {
    background-position: 100%;
  }
}
.vue-words {
  font-size: 40px;
  font-weight: 600;
  font-size: 34px;
  font-family: Helvetica Neue, Helvetica, PingFang SC, Hiragino Sans GB,
    Microsoft YaHei, 微软雅黑, Arial, sans-serif;
  width: auto;
  height: auto;
  border: 3px solid transparent;
  background: linear-gradient(white, white) padding-box,
    repeating-linear-gradient(
        -45deg,
        #42b983 0,
        #42b983 25%,
        white 0,
        white 50%
      )
      0/0.6em 0.6em;
  animation: border-style-2 12s linear infinite;
}
.feature-title {
  margin-top: 20px;
  margin-bottom: 10px;
  font-size: 25px;
  color: #42b983;
  font-weight: 400;
  text-align: center;
}
.feature {
  text-align: center;
  font-family: Open Sans, Inter, Roboto, Oxygen, Fira Sans, Helvetica Neue,
    sans-serif;
}
.element {
  height: auto;
}
.element-title {
  text-align: center;
  font-weight: 600;
  font-size: 34px;
  font-family: Helvetica Neue, Helvetica, PingFang SC, Hiragino Sans GB,
    Microsoft YaHei, 微软雅黑, Arial, sans-serif;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
  margin-bottom: 25px;
  transition: all 0.4s;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
.bg {
  z-index: -1;
  background-size: 100%;
  left: 0;
  top: 0;
  width: 100%;
  height: 700px;
  background-size: cover;
}
.title-bg {
  z-index: -1;
  background-size: 100%;
  left: 0;
  top: 0;
  width: 100%;
  background-size: cover;
}
.color-cha {
  color: rgb(64, 158, 255);
}
.title {
  font-family: PingfangSC-Light, NotoSansHans-Light, Microsoft Yahei, sans-serif;
  font-weight: 800;
  position: absolute;
  top: 35%;
  left: 25%;
  color: white;
  font-size:30px;
  letter-spacing: 15px;
}
.title-en{
  font-family: Microsoft JhengHei UI, sans-serif;
  font-weight: 800;
  position: absolute;
  top: 45%;
  left: 25%;
  color: white;
  font-size:30px;
}
.title-en::after{
  position: absolute;
  left: -20%;
  top: 50%;
  content: "";
  height: 2px;
  width: 50px;
  background: #ffffff;
}
.title-img{
    position: absolute;
  top: 20%;
  left: 30%;
  opacity: .6;
}
</style>