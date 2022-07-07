<template>
  <div>
    <div class="shell">
      <MyHeader class="theheader"></MyHeader>
      <div
        class="image"
        :style="{ backgroundImage: 'url(' + Img1 + ')' }"
        style="height: 130vh"
        id="go-big"
      ></div>

          <div class="wel">  欢迎来到遥感智能解译平台</div>
          <div class="wel-en"> Welcome to the remote sensing intelligent interpretation platform</div>
         <div class="gofun">
           <el-row><el-button  class="gofun-btn btn-animate btn-animate__shiny" @click="goDetectchanges" style="font-size:13px">前往体验</el-button></el-row>
           </div>
      <div class="heading">
        
        <div class="dec-words">
          <h4 class="h4-words hidden-sm-and-down">
            Application of remote sensing images
          </h4>
        </div>
        <div class="header-dec">
          <img
            :src="require('../../assets/image/decoration/47.png')"
            style="width: 350px"
          />
        </div>
        <h2 class="subtitle">
          <span class="hidden-md-and-down">遥感图像</span>微介绍
        </h2>
      </div>
      <div class="text color">
        <img
          :src="require('../../assets/image/remotesense/08.jpg')"
          class="litimg img1 hidden-md-and-down"
        />
        <img
          :src="require('../../assets/image/remotesense/09.jpeg')"
          class="litimg img2 hidden-md-and-down"
        />
        <img
          :src="require('../../assets/image/remotesense/10.jpeg')"
          class="litimg img3 hidden-md-and-down"
        />
        <el-row justify="center">
          <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
            <h2 class="animated" style="color:white">
              <i
                class="iconfont icon-wenhao"
                style="font-size: 90px; color: orange"
              ></i
              >何为<span style="color:skyblue">遥感图像</span>
            </h2>
          </el-col>
        </el-row>
        <el-row justify="center">
          <el-col :xs="20" :sm="20" :md="20" :lg="20" :xl="20">
            <h4 style="color: white" class="nor-words">
              凡是只纪录各种地物<span class="color-cha">电磁波大小的胶片（或相片）</span>，都称为遥感影像，在遥感影像图中，图面内容要素主要由影像构成，辅助以一定地图符号来表现或说明制图对象，与普通地图相比，影像地图具有<span class="color-cha">丰富的地面信息</span>，内容层次分明，图面清晰易读，充分表现出影像与地图的双重优势。
            </h4>
          </el-col>
        </el-row>
      </div>
      <div
        class="image"
        :style="{ backgroundImage: 'url(' + Img2 + ')' }"
        style="height: 140vh; margin-top: 20vh"
      ></div>
      <div class="heading des">
        <h5>下图为内蒙古某地,绿色代表植被覆盖程度</h5>
      </div>
      <div class="heading">
        <div class="dec-words">
          <h4 class="h4-words hidden-sm-and-down">
            History of remote sensing image
          </h4>
        </div>
        <div class="header-dec">
          <img
            :src="require('../../assets/image/decoration/60.png')"
            style="width: 350px"
          />
        </div>
        <h1 style="letter-spacing: 25px">
          <span class="hidden-md-and-down">遥感</span>发展史
        </h1>
      </div>
      <div class="text color2" style="height: 45vh" >
        <el-row justify="center">
          <el-col :xs="20" :sm="20" :md="20" :lg="20" :xl="20" >
            <p class="remote-hiswords">
        现代遥感技术历史悠久，可以追溯到 <span class="color-cha">19 世纪末照相机</span>的发明。
        最初，相机被用来在地面上拍照，这提供了（现在仍然）
        一种迷人而令人兴奋的方式来及时捕捉瞬间并记录所发生的事情，这看起来比图画或油画更逼真，并且可以比通过绘画或绘画更快地捕获，如今，遥感是使用<span class="color-cha">机载和卫星技术</span>进行的，不仅利用胶片摄影，还利用数码相机、扫描仪和视频，以及雷达和热传感器。</p></el-col></el-row>
      </div>
      <div
        class="image"
        :style="{ backgroundImage: 'url(' + Img4 + ')' }"
        style="margin-top: 10vh; opacity: 0.8"
      >
        <div class="remote-history">
          <img
            :src="require('../../assets/image/remotesense/51.png')"
            style="width: 100vw"
          />
  
          <span class="remote-topwords words1"
            ><span class="hidden-md-and-down">1608年制造了世界</span
            >第一架望远镜</span
          >
          <span class="remote-downwords words2"
            ><span class="hidden-md-and-down">1839年</span>第一张摄影像片</span
          >
          <span class="remote-topwords words3"
            ><span ><span class="hidden-md-and-down">1858年用气球拍摄了</span>鸟瞰像片</span
            ></span
          >
          <span class="remote-downwords words4"
            ><span ><span class="hidden-md-and-down">1909年</span>第一张航空像片制</span
            ></span
          >
          <span class="remote-topwords words5"
            ><span><span class="hidden-md-and-down">1957年前苏联发射了</span>第一颗人造地球卫星</span
            ></span
          >
          <span class="remote-downwords words6"
            ><span ><span class="hidden-md-and-down">至今遥感信息处理</span>技术发展成熟</span
            ></span
          >
        </div>
      </div>
      <div class="heading">
        <div class="dec-words">
          <h4 class="h4-words hidden-sm-and-down">
            Brief introduction of remote sensing image
          </h4>
        </div>
        <div class="header-dec">
          <img
            :src="require('../../assets/image/decoration/49.png')"
            style="width: 300px"
          />
        </div>
        <h1 style="letter-spacing: 25px">
          <span class="hidden-md-and-down">遥感影像的</span>应用
        </h1>
      </div>
      <div class="text color2" style="height: auto">
        <el-row justify="center">
          <el-col :xs="20" :sm="20" :md="20" :lg="20" :xl="20">
            <h4>
              掌握<span class="color-cha">国土资源利用</span>和<span class="color-cha">土地覆盖类型</span>，是地理国情普查与监测的重要内容。高效获取准确、客观的<span class="color-cha">土地利用情况</span>，监测<span class="color-cha">国土变化情况</span>，可以为国家和地方提供地理国情信息决策支撑,以下是两大遥感应用示例
            </h4>
          </el-col>
        </el-row>
        <el-row justify="center" :gutter="40" style="margin-bottom: 20px">
          <el-col :xs="22" :sm="20" :md="10" :lg="10" :xl="10">
            <div class="animate-card animate-card-32">
              <div class="animate-card__layer">
                <img :src="require('../../assets/image/remotesense/13.jpg')" />
                <div class="words">地质测绘</div>
              </div>

              <div class="animate-card__sublayer">
                <h3>地质测绘</h3>
                <div>
                  基于地物光谱的特性，并通过遥感图像判读，可将具体地貌、波谱特征、地表情况及位置分布等充分反映出来，从而为地质测绘提供可靠的信息基础。
                </div>
              </div>
            </div>
          </el-col>
          <el-col :xs="22" :sm="20" :md="10" :lg="10" :xl="10">
            <div class="animate-card animate-card-32">
              <div class="animate-card__layer">
                <img :src="require('../../assets/image/remotesense/15.jpg')" />
                <div class="words">土地勘测</div>
              </div>

              <div class="animate-card__sublayer">
                <h3>土地勘测</h3>
                <span
                  >利用遥感图像处理技术可大量瞬间静态图像信息，这些图像信息既可用于监测动态变化，也可用于规模性的重复用观测活动。</span
                >
              </div>
            </div>
          </el-col>
        </el-row>
      </div>

      <div
        class="image"
        :style="{ backgroundImage: 'url(' + Img3 + ')' }"
        style="margin-top: 10vh"
      ></div>
      <div class="heading">
        <div class="dec-words">
          <h4 class="h4-words hidden-sm-and-down">
            Processing of remote sensing image
          </h4>
        </div>
        <div class="header-dec">
          <img
            :src="require('../../assets/image/decoration/50.png')"
            style="width: 300px"
          />
        </div>
        <h1 style="letter-spacing: 25px">
          <span class="hidden-md-and-down">遥感</span>图像处理
        </h1>
      </div>
      <div class="text color3" style="height: 45vh">
        <h1>传统解译与基于深度学习的智能解译</h1>
      </div>
      <el-row style="margin-top: 50px" justify="center">
        <el-col :xs="20" :sm="20" :md="10" :lg="10" :xl="10"
          ><h3 class="nor-words">
            高分辨率卫星遥感图像的对<span class="color-cha">特征刻画能力差</span>且依赖<span class="color-cha">人工经验,</span><span class="color-cha">工作量巨大</span>
          </h3></el-col
        >
        <el-col :xs="20" :sm="20" :md="10" :lg="10" :xl="10"
          ><img :src="require('../../assets/image/remotesense/22.png')"
        /></el-col>
      </el-row>
      <el-row style="margin-top: 50px" justify="center">
        <el-col :xs="20" :sm="20" :md="10" :lg="10" :xl="10"
          ><img :src="require('../../assets/image/remotesense/20.png')"
        /></el-col>
        <el-col :xs="20" :sm="20" :md="10" :lg="10" :xl="10"
          ><h3 class="nor-words">
            随着人工智能技术的兴起，特别是<span class="color-cha">基于深度学习的图像识别方法</span>获得了极大的发展，相关技术也推动了遥感领域的变革。相对于传统基于人海战术的目视解译方法，基于深度学习的遥感图像识别技术可以<span class="color-cha"> 自动分析</span>图像中的地物类型，在<span class="color-cha">准确率和效率</span>方面展现出极大的潜力。
            <h4>
              <span @click="goIntelligent" class="gointelligent">点我</span
              >前往下一界面了解更多关于基于深度学习的图像识别技术
            </h4>
          </h3>
          <br />
        </el-col>
      </el-row>

      <MyFooter></MyFooter>
    </div>
  </div>
</template>

<script>
import MyHeader from "@/components/MyHeader";
import BigCard from "@/components/BigCard";
import BackTop from "@/components/BackTop";
import MyFooter from "@/components/MyFooter";
import Img1 from "@/assets/image/remotesense/16.jpg";
import Img2 from "@/assets/image/remotesense/11.jpeg";
import Img3 from "@/assets/image/remotesense/12.jpg";
import Img4 from "@/assets/image/remotesense/59.jpg";
export default {
  name: "remotesenseense",
  components: {
    MyHeader,
    BigCard,
    BackTop,
    MyFooter,
  },
  data() {
    return {
      Img1: Img1,
      Img2: Img2,
      Img3: Img3,
      Img4: Img4,
    };
  },
  mounted() {
    document.body.style.overflow = "auto";
  },
  methods: {
    goIntelligent() {
      this.$router.push("intelligent");
    },
    goDetectchanges(){
 
      if(!localStorage.getItem('token')){
        this.$message('请先注册登录')
      }
      this.$router.push('detectchanges')
    }
  },
};
</script>

<style scoped>
.color-cha{
  color: rgb(64,158,255);
}
.nor-words{
  font-family: SimHei sans-serif;
  line-height: 35px;
}
.remote-history {
  position: relative;
  font-family: SimHei sans-serif;
  line-height: 35px;
}
.remote-topwords,
.remote-downwords {
  line-height: 20vh;
  height: 20vh;
  border-left: 3px solid;
  color: black;
  position: absolute;
}
.words1 {
  top:-1.5vh;
  left: 12vw;
}
.words2 {
  top: 10vh;
  left: 24vw;
}
.words3 {
  top: 2vh;
  left: 37vw;
}
.words4 {
  top: 21.5vh;
  left: 48vw;
}
.words5 {
  top:0.5vh;
  left: 60vw;
}
.words6 {
  top:18.5vh;
  left: 72vw;
}
.remote-hiswords{
  font-size: 22px;
   font-family: SimHei sans-serif;
   font-weight: 700;
   line-height: 40px;
}
.remote-topwords::after {
  width: 15px;
  height: 15px;
  background-color: black;
  display: block;
  content: "";
  border-radius: 50%;
  text-align: center;
  position: absolute;
  bottom: 0;
  left: -9px;
}
.remote-downwords::after {
  width: 15px;
  height: 15px;
  background-color: black;
  display: block;
  content: "";
  border-radius: 50%;
  text-align: center;
  position: absolute;
  top: 0;
  left: -9px;
}
.dec-words {
  font-size: 14px;
  position: absolute !important;
  left: 40%;
  top: -20%;
}
.h4-words::after {
  position: absolute;
  left: -20%;
  top: 50%;
  content: "";
  height: 2px;
  width: 50px;
  background: #ffffff;
}
.header-dec {
  left: 30%;
  top: -70%;
  position: absolute !important;
  width: 200px;
  height: 200px;
  opacity: 0.5;

  box-shadow: #000 12px solid;
}
.gointelligent {
  cursor: pointer;
  color: rgb(64,158,255);
  transition: all 0.6s;
}
.gointelligent:hover {
  color: red;
}
.el-main {
  --el-main-padding: 0px;
}
.shell {
  height: 100vh;
  overflow-x: hidden;
  perspective: 3px;
}
.shell div {
  position: relative;
  display: flex;

  align-items: center;
  font-style: 30px;
  letter-spacing: 2px;
}
.image {
  transform: translateZ(-1px) scale(1.65);
  background-size: cover;
  height: 100vh;
  z-index: -1;
}
.text {
  font-family: SimHei sans-serif;
  font-size: 20px;
  flex-direction: column;
  justify-content: center;
  height: 53vh;
}
.text h1 {
  justify-content: center;
  color: #000;
}
.heading {
  position: relative;
  justify-content: center;
  z-index: -1;
  transform: translateY(-30vh) translateZ(1px);
  color: #fff;
  font-size: 30px;
  font-family: SimHei sans-serif;
}
.cards {
  margin: 0 auto;
  justify-content: space-evenly;
  opacity: 1 !important;
  flex: auto;
}
.theheader {
  height: 90px;
  color: skyblue;
}
.subtitle {
  margin-left: 25px;
  letter-spacing: 25px;
  font-family: SimHei sans-serif;
}
.color {
  background-image: linear-gradient(135deg, #130cb7 15%, #43e97b 100%);
}
.color2 {
  background-image: linear-gradient(135deg, #70f570 10%, #fffeff 100%);
}
.color3 {
  background-image: linear-gradient(135deg, #feb692 10%, #ea5455 100%);
}
.litimg {
  position: absolute;
  border: 10px solid;
  border-image: linear-gradient(45deg, #90cf5b, #00afee) 1;
  clip-path: inset(0 round 10px);
  transition: all 0.5s;
  transform: rotate(30deg);
  -moz-transform: rotate(10deg);
  -webkit-transform: rotate(10deg);
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3);
}
.img1 {
  left: 80px;
  top: 40px;
  width: 150px;
}
.img2 {
  left: 200px;
  top: 40px;
  width: 200px;
}
.img3 {
  left: 380px;
  top: 40px;
  width: 200px;
}
.img1:hover,
.img2:hover,
.img3:hover {
  z-index: 100;
}
.litimg:hover {
  transform: scale(1.8);
}
.animated:hover {
  animation-duration: 1s;
  animation-fill-mode: both;
  animation-name: shakeX;
}

@keyframes shakeX {
  from,
  to {
    transform: translate3d(0, 0, 0);
  }

  10%,
  30%,
  50%,
  70%,
  90% {
    transform: translate3d(-10px, 0, 0);
  }

  20%,
  40%,
  60%,
  80% {
    transform: translate3d(10px, 0, 0);
  }
}

.shakeX {
  animation-name: shakeX;
}
.des {
  position: absolute;
  top: -120%;
}
.animate-card {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
}
.animate-card-32 {
  z-index: 10;
}
.animate-card-32 .animate-card__layer {
  width: 50%;
  height: 100%;
  transition: 0.5s;
  transform: rotate(360deg) scale(1, 1);
  position: relative;
}
.animate-card-32 .animate-card__layer > img {
  border: 10px solid;
  border-image: linear-gradient(45deg, #90cf5b, #00afee) 1;
  clip-path: inset(0 round 10px);
  width: 120%;
  height: 120%;
}
.animate-card-32 .animate-card__sublayer {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  transform: rotate(0deg) scale(0, 0);
  text-align: center;
  background-color: #fff;
  color: #000;
  opacity: 0;
  transition: 0.5s;
  border-radius: 5px;
  opacity: 0.8 !important;
  background-image: linear-gradient(90deg, #92fe9d, #00c9ff 100%);
}
.animate-card-32:hover .animate-card__layer {
  transform: rotate(0deg) scale(0, 0);
}
.animate-card-32:hover .animate-card__sublayer {
  transform: rotate(360deg) scale(1, 1);
  opacity: 1;
}

.words {
  font-size: 30px;
  right: -120px;
  position: absolute;
}
.gofun{
   position: relative;
  justify-content: center;
  z-index: -1;
  transform: translateY(-95vh) translateZ(1px) translateX(-11vw);
}
.wel{
  position: relative;
  justify-content: center;
  z-index: -1;
  transform: translateY(-100vh) translateZ(1px) translateX(-10vw);
  letter-spacing: 10px!important;
  font-size:20px!important;
  font-family:   PingfangSC-Light,NotoSansHans-Light,Microsoft Yahei,sans-serif;
  font-weight: 800;
  color: white
}
.wel-en{
    position: relative;
  justify-content: center;
  z-index: -1;
  transform: translateY(-98vh) translateZ(1px) translateX(-10vw);
  font-size:12px!important;
   font-family: Microsoft JhengHei UI, sans-serif;
  font-weight: 800;
  color: white;
}

.gofun-btn{
  font-family: PingfangSC-Light,NotoSansHans-Light,Microsoft Yahei,sans-serif;
  width:100px;
  height: 30px;
  transition: all .5s;
  color: black;
  background-color: rgb(76, 192, 238);
  border-color: rgb(76, 192, 238);
  letter-spacing: 3px;
  font-weight: 500;
}
.gofun-btn:hover{
  background-color: rgb(135,206,235,.5);
  color: white;
  border-color: transparent
}
</style>