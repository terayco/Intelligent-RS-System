<template>
  <div :style="{ backgroundImage: 'url(' + bgImg + ')' }">
    <img :src="require('../../assets/image/intelligent/66.png')" class="bg" />
    <div class="title">基于深度学习的智能解译</div>
    <div class="title-en">Intelligent interpretation based on deep learning</div>
     <div class="title-img">     <img
            :src="require('../../assets/image/decoration/47.png')"
            style="width: 350px"
          /></div>
    <MyHeader class="theheader"></MyHeader>
    <Tabinfor
      style="margin-bottom: 40px; margin-top: 30px"
      class="bigcardinfor"
      id="go-big3"
    >
      <template v-slot:mid>
        <span id="subtitle">智能解译四大功能</span>
        <div class="sub-en">main function</div></template
      >
    </Tabinfor>

    <div class="mainfun">
      <el-row justify="center" :gutter="20" align="middle"
        ><el-col :xs="20" :sm="20" :md="4" :lg="4" :xl="4"
          ><div class="rendr-style">
            <el-divider></el-divider>
            <label>
              <el-row justify="center">
                <el-col id="fade-in2"
                  ><div
                    class="fun"
                    :class="{ 'active-fun': this.ishoverfun == index }"
                    @mouseenter="goThisFun(index)"
                    v-for="(item, index) in fun"
                  >
                    {{ this.fun[index].title }}
                  </div>
                </el-col>
              </el-row>
            </label>
          </div> </el-col
        ><el-col :xs="20" :sm="20" :md="15" :lg="15" :xl="15" id="fade-in3"
          ><el-card
            ><div class="fun-words">
              <div class="words-title">{{ this.fun[funindex].title }}</div>
              <div>{{ this.fun[funindex].words[0] }}</div>
              <div class="words-title">
                {{ this.fun[funindex].subtitle[0] }}：{{
                  this.fun[funindex].words[1]
                }}
              </div>
              <div>
                <el-image
                  :src="`${this.fun[funindex].imgsrc}`"
                  style="height: 400px"
                ></el-image>
              </div>
              <div class="go-fun-site">
                <span
                  class="fun-click"
                  @click="goFunSite(this.fun[funindex].funurlname)"
                  >点此</span
                >去试一试（需先登录）
              </div>
            </div></el-card
          ></el-col
        ></el-row
      >
    </div>

    <Tabinfor
      style="margin-bottom: 10px; margin-top: 40px"
      class="bigcardinfor"
      id="fade-in"
    >
      <template v-slot:mid>
        <span id="subtitle">新闻中心</span>
        <div class="sub-en">news center</div></template
      >
    </Tabinfor>
    <div class="news">
      <el-row align="middle" justify="center" :gutter="50"
        >
        <el-col
          :xs="20"
          :sm="20"
          :md="6"
          :lg="6"
          :xl="6"
          id="fade-in"
          class="news1"
          ><span class="span-title">行业动态</span>
          <span @click="getMoreNews(3)"
            ><i class="iconfont icon-shuaxin"></i
          ></span>
          <div class="industry mynews" style="background-color: white">
            <div
              :class="{ activetri: ishoverindustry == index }"
              class="div-news"
              v-for="(item, index) in this.industry.length"
              @mouseenter="goPreviewIndustry(index)"
            >
              <el-row @click="goVisitSite(3, index)">
                <el-col
                  :xs="6"
                  :sm="6"
                  :md="6"
                  :lg="6"
                  :xl="6"
                  class="big-databox"
                  :class="{ activedata: ishoverindustry == index }"
                >
                  <div
                    class="triangle"
                    :class="{ activetri: ishoverindustry == index }"
                  ></div>
                  <div class="data">
                    <div class="day">{{ this.industry[index].date.day }}</div>
                    <div class="year-month">
                      {{ this.industry[index].date.year }}/{{
                        this.industry[index].date.month
                      }}
                    </div>
                  </div>
                </el-col>
                <el-col :xs="18" :sm="18" :md="18" :lg="18" :xl="18">
                  <div class="news-rough">
                    <div class="rough-title">
                      {{ this.industry[index].title }}
                    </div>
                    <div class="rough-words">
                      {{ this.industry[index].words }}
                    </div>
                  </div>
                </el-col>
              </el-row>
            </div>
          </div></el-col
        >
        <el-col
          :xs="20"
          :sm="20"
          :md="8"
          :lg="8"
          :xl="8"
          id="fade-in2"
          class="news2"
          ><span class="span-title">最新新闻</span>
          <span @click="getMoreNews(1)"
            ><i class="iconfont icon-shuaxin"></i
          ></span>
          <div class="mynews bignews" style="background-color:white">
            <div
              :class="{ activetri: ishovernews == index }"
              class="div-news"
              v-for="(item, index) in this.news.length"
              @mouseenter="goPreviewNews(index)"
            >
              <el-row @click="goVisitSite(1, index)">
                <el-col
                  :xs="6"
                  :sm="6"
                  :md="6"
                  :lg="6"
                  :xl="6"
                  class="big-databox"
                  :class="{ activetri: ishovernews == index }"
                >
                  <div class="triangle"></div>
                  <div class="data">
                    <div class="day">{{ this.news[index].date.day }}</div>
                    <div class="year-month">
                      {{ this.news[index].date.year }}/{{
                        this.news[index].date.month
                      }}
                    </div>
                  </div>
                </el-col>
                <el-col :xs="18" :sm="18" :md="18" :lg="18" :xl="18">
                  <div class="news-rough">
                    <div class="rough-title">
                      {{ this.news[index].title }}
                    </div>
                    <div class="rough-words">
                      {{ this.news[index].words }}
                    </div>
                  </div>
                </el-col>
              </el-row>
            </div>
          </div></el-col
        ><el-col
          :xs="20"
          :sm="20"
          :md="6"
          :lg="6"
          :xl="6"
          id="fade-in3"
          class="news3"
          ><span class="span-title">媒体关注</span
          ><span @click="getMoreNews(2)"
            ><i class="iconfont icon-shuaxin"></i
          ></span>
          <div class="media mynews"  style="background-color:white">
            <div
              :class="{ activetri: ishovermedia == index }"
              class="div-news"
              v-for="(item, index) in this.media.length"
              @mouseenter="goPreviewMedia(index)"
            >
              <el-row @click="goVisitSite(2, index)">
                <el-col
                  :xs="6"
                  :sm="6"
                  :md="6"
                  :lg="6"
                  :xl="6"
                  class="big-databox"
                  :class="{ activedata: ishovermedia == index }"
                >
                  <div
                    class="triangle"
                    :class="{ activetri: ishovermedia == index }"
                  ></div>
                  <div class="data">
                    <div class="day">{{ this.media[index].date.day }}</div>
                    <div class="year-month">
                      {{ this.media[index].date.year }}/{{
                        this.media[index].date.month
                      }}
                    </div>
                  </div>
                </el-col>
                <el-col :xs="18" :sm="18" :md="18" :lg="18" :xl="18">
                  <div class="news-rough">
                    <div class="rough-title">
                      {{ this.media[index].title }}
                    </div>
                    <div class="rough-words">
                      {{ this.media[index].words }}
                    </div>
                  </div>
                </el-col>
              </el-row>
            </div>
          </div></el-col
        ></el-row
      >
    </div>

    <Tabinfor
      style="margin-bottom: 40px; margin-top: 20px"
      class="bigcardinfor"
      id="fade-in"
    >
      <template v-slot:mid>
        <span id="subtitle">遥感智译的优势</span>
        <div class="sub-en">advantage</div></template
      >
    </Tabinfor>
    <div class="bigcard">
      <BigCard
        ><template v-slot:left
          ><div class="card-infor">
            <i class="iconfont icon-kongjianjingdu"></i>
            <div class="feature-words">高精度</div>
            <div class="detail-words">
              利用深度神经网络从计算机视觉角度提取遥感影像信息，能够极大提高高分辨率遥感影像目标检测精度
            </div>
          </div></template
        ><template v-slot:middle
          ><div class="card-infor">
            <i class="iconfont icon-gaoxiao"></i>
            <div class="feature-words">高效率</div>
            <div class="detail-words">
              深度神经网络能够通过大量训练数据及深度学习模型学习高维特征，减少对专家经验的依赖，提高效率
            </div>
          </div></template
        ><template v-slot:right
          ><div class="card-infor">
            <i class="iconfont icon-yingyongzhongxin"></i>
            <div class="feature-words">强应用性</div>
            <div class="detail-words">
              高效获取准确、客观的土地利用情况，监测国土变化情况，可以为国家和地方提供地理国情信息决策支撑
            </div>
          </div></template
        ></BigCard
      >
    </div>
    <MyFooter></MyFooter>
  </div>
</template>

<script>
import { showFullScreenLoading, hideFullScreenLoading } from "@/utils/loading";
import { getNews } from "@/api/news";
import MyHeader from "@/components/MyHeader";
import Tabinfor from "@/components/Tabinfor";
import BigCard from "@/components/BigCard";
import MyFooter from "@/components/MyFooter";
import funImg1 from "@/assets/image/intelligent/61.png";
import funImg2 from "@/assets/image/intelligent/62.png";
import funImg3 from "@/assets/image/intelligent/63.png";
import funImg4 from "@/assets/image/intelligent/64.png";
import bgImg from "@/assets/image/intelligent/75.jpg";
export default {
  name: "intelligent",
  components: {
    MyHeader,
    BigCard,
    Tabinfor,
    MyFooter,
  },
  data() {
    return {
      bgImg,
      page: {
        newsPage: 1,
        industryPage: 1,
        mediaPage: 1,
      },
      ishovermedia: 0,
      ishovernews: 0,
      ishoverfun: 0,
      ishoverindustry: 0,
      funindex: 0,
      fun: [
        {
          title: "变化检测",
          words: [
            "通过对同一地区不同时间重复观测来分析区域内地物的状态变化",
            "BIT",
          ],
          imgsrc: funImg1,
          subtitle: ["使用模型"],
          githubsrc: "",
          funurlname: "detectchanges",
        },
        {
          title: "目标检测",
          words: [
            "关注图像中特定的物体目标，要求同时获得这一目标的类别信息和位置信息",
            "DeepLab V3+",
          ],
          imgsrc: funImg2,
          subtitle: ["使用模型"],
          githubsrc: "",
          funurlname: "detecttargets",
        },
        {
          title: "目标提取",
          words: [
            "对地物分类，地物是指的是地表面的固定性物体，包括自然形成和人工建造的",
            "PP-YOLO",
          ],
          imgsrc: funImg4,
          subtitle: ["使用模型"],
          githubsrc: "",
          funurlname: "obtaintargets",
        },
        {
          title: "地物分类",
          words: [
            "单幅图像或序列图像中将感兴趣的目标与背景分割开来，从图像中识别和解译有意义的物体实体而提取不同的图像特征的操作",
            "DeepLab V3+",
          ],
          imgsrc: funImg3,
          subtitle: ["使用模型"],
          githubsrc: "",
          funurlname: "classify",
        },
      ],
      news: [],
      industry: [],
      media: [],
    };
  },
  created() {
    showFullScreenLoading("#load");
    this.getNews(1, 4, 1).then((res) => {
  
      this.news.push(...res.data.data);

      this.ishovernews = 0;
      this.newsGet = true;
      hideFullScreenLoading("#load");
    });
    this.getNews(1, 4, 3).then((res) => {
      this.industry = res.data.data;
   
      this.industryGet = true;
    });
    this.getNews(1, 4, 2).then((res) => {
      this.media = res.data.data;
     
      this.mediaGet = true;
    });
  },
  methods: {
    getNews,
    getMoreNews(type) {
      if (type == 1) {
        showFullScreenLoading(".bignews");
        this.page.newsPage++;
        if (this.page.newsPage == 6) {
          this.page.newsPage = 2;
        }
      
        this.getNews(this.page.newsPage, 4, 1).then((res) => {
          // this.news.splice(0,this.news.length)
       
          this.news = res.data.data;
          hideFullScreenLoading(".bignews");
        });
      } else if (type == 2) {
        showFullScreenLoading(".media");
        this.page.mediaPage++;
        if (this.page.mediaPage == 6) {
          this.page.mediaPage = 2;
        }
        this.getNews(this.page.mediaPage, 4, 2).then((res) => {
          this.media = res.data.data;
          hideFullScreenLoading(".media");
        });
      } else if (type == 3) {
        showFullScreenLoading(".industry");
        this.page.industryPage++;
        if (this.page.industryPage == 6) {
          this.page.industryPage = 2;
        }
        this.getNews(this.page.industryPage, 4, 3).then((res) => {
          this.industry = res.data.data;
          hideFullScreenLoading(".industry");
        });
      }
    },
    goPreviewNews(index) {
      this.ishovernews = index;
    },
    goPreviewIndustry(index) {
      this.ishoverindustry = index;
    },
    goPreviewMedia(index) {
      this.ishovermedia = index;
    },

    goThisFun(index) {
      let x = document.querySelectorAll(".fun");
      this.funindex = index;
      x[index].classList.add("active-fun");
      this.ishoverfun = index;
    },
    goFunSite(urlname) {
      this.$router.push(urlname);
    },
    goVisitSite(type, index) {
      if (type == 1) {
        var a = document.createElement("a");
        a.href = this.news[index].url;
        a.target = "_blank";
        a.rel = "noreferrer";
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
      } else if (type == 2) {
        window.open(this.media[index].url, "_blank");
      } else if (type == 3) {
        window.open(this.industry[index].url, "_blank");
      }
    },
  },
      beforeRouteEnter(to, from, next) {
    next((vm) => {
      document.querySelector(".el-main").scrollTop = 0;
    });
  },
};
</script>

<style scoped lang="less">
.active-fun {
  background-color: rgb(41, 50, 225) !important;
  color: white !important;
}
.mainfun {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji",
    "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  .fun {
    margin-bottom: 20px;
    line-height: 70px;
    color: rgb(114, 114, 115);
    width: 100%;
    height: 70px;
    cursor: pointer;
    background-color: rgb(245, 246, 249);
    transition: all 0.2s;
    text-align: center;
    font-size: 20px;
  }
  .fun-words {
    padding: 30px;
    height: 550px;
    transition: all 0.6s;
    text-align: center;
    .words-title {
      margin-top: 10px;
      margin-bottom: 10px;
      font-size: 20px;
    }
    .go-fun-site {
      .fun-click {
        cursor: pointer;
        color: skyblue;
        transition: all 0.3s;
      }
      .fun-click:hover {
        color: red;
      }
    }
  }
}
el-col {
  text-align: center;
}
.icon-shuaxin {
  cursor: pointer;
  transition: all 1s;
  color: rgb(30, 152, 249);
  // transform: rotate(360deg);
}
@keyframes turnZ {
  0% {
    transform: rotateZ(0deg);
  }
  100% {
    transform: rotateZ(360deg);
  }
}
.icon-shuaxin:hover {
  animation-name: turnZ;
  animation-duration: 1s;
  animation-iteration-count: 1;
  color: white;
}
.news-rough {
  letter-spacing: 0px;
  margin-left: 20px;
  width: 100%;
  height: 110px;
  font-weight: 400;
  .rough-title {
    margin-top: 10px;
    line-height: 40px;
    font-size: 16px;
    color: #333333;
  }
  .rough-words {
    padding-right: 40px;
    font-size: 14px;
    color: #888888;
    margin-top: 10px;
  }
}
.big-databox {
  height: 110px;
  position: relative;
  .triangle {
    width: 0;
    height: 0;
    position: absolute;
    right: 0;
    top: 45px;
  }
}
.activetri {
  border-right: 8px solid rgb(237, 243, 249);
  border-top: 8px solid rgb(55, 163, 250);
  border-left: 8px solid rgb(55, 163, 250);
  border-bottom: 8px solid rgb(55, 163, 250);
  color: white;
}
.activedata {
  background-color: rgb(55, 163, 250);
}
.data {
  display: inline;
  text-align: center;
  width: 100px;
  height: 110px;
}
.day {
  padding-top: 10px;
  letter-spacing: 0px;
  line-height: 60px;
  width: 100%;
  height: 50px;
  font-size: 30px;
  font-family: Bahnschrift;
  font-weight: normal;
  color: #333333;
}
.year-month {
  letter-spacing: 0px;
  width: 100%;
  height: 40px;
  line-height: 40px;
  font-size: 16px;
  font-family: Microsoft YaHei;
  font-weight: 400;
  color: #666666;
}
.news {
  font-family: Microsoft YaHei;
  letter-spacing: 2px;
}
.div-news {
  height: 110px;
}
.div-news:hover {
  background-color: rgb(237, 243, 249);
  cursor: pointer;
}
.span-title {
  font-size: 20px;
  font-weight: 400;
  color: rgb(30, 152, 249);
  letter-spacing: 1px;
}
.mynews {
  padding-bottom: 10px;
  padding-top: 10px;
  margin-top: 15px;
  width: auto;
  height: 440px;
  box-shadow: 0px 1px 16px 0px rgba(47, 47, 47, 0.14);
  border-radius: 8px;
  margin-bottom: 20px;
}
.sub-en {
  margin-top: 10px;
  color: white;
  font-family: Microsoft YaHei;
  letter-spacing: 2px;
}
.bigcardinfor {
  text-align: center;
}
.card-infor {
  font-family: Open Sans, Inter, Roboto, Oxygen, Fira Sans, Helvetica Neue,
    sans-serif;
  padding: 40px;
  .iconfont {
    font-size: 80px;
    color: rgb(241, 77, 93);
  }
  .feature-words {
    font-size: 30px;
  }
  .detail-words {
    line-height: 40px;
    color: rgb(130, 130, 141);
    letter-spacing: 2px;
    margin-top: 20px;
    font-size: 18px;
  }
  .more {
    cursor: pointer;
    margin-top: 33px;
    .iconfont {
      font-size: 15px;
    }
  }
}
#subtitle {
  color: rgb(30, 152, 249);
  font-size: 30px;
  font-family: sans-serif;
}
#subtitle:hover:after {
  left: 0%;
  right: 0%;
  width: 100%;
}
.bg {
  z-index: -1;
  height: 300px;
  background-size: 100%;
  left: 0;
  top: 0;
  width: 100%;
  height: 700px;
  background-size: cover;
}
.bg1 {
  position: absolute;
  z-index: -1;
  background-size: 100%;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
}
.theheader {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  color: white;
}
.title {
  font-family: PingfangSC-Light, NotoSansHans-Light, Microsoft Yahei, sans-serif;
  font-weight: 800;
  position: absolute;
  top: 45%;
  left: 60%;
  color: white;
  font-size:30px;
  letter-spacing: 15px;
  
}
.title-en{
  font-family: Microsoft JhengHei UI, sans-serif;
  font-weight: 800;
  position: absolute;
  top: 55%;
  left: 55%;
  color: white;
  font-size:30px;
}
.title-en::after{
  position: absolute;
  left: -8%;
  top: 23%;
  content: "";
  height: 2px;
  width: 50px;
  background: #ffffff;
}
.title-img{
    position: absolute;
  top: 30%;
  left: 60%;
  opacity: .6;
}
</style>