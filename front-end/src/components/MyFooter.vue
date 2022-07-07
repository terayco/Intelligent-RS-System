<template>
  <div class="bigone">
    <el-row justify="center" :gutter="30"
      ><el-col
        :xs="4"
        :sm="4"
        :md="4"
        :lg="5"
        :xl="5"
        class="hidden-md-and-down"
        ><div class="bottomnav">
          <p>技术支持网站</p>
          <ul>
            <li>    <i class="iconfont icon-jiantou jiantou"></i
              ><span
                class="nav-item"
                @mouseenter="goCanSeen(0)"
                @mouseleave="goUnseen(0)"
                @click="goOtherSite('https://www.paddlepaddle.org.cn/')"
                >百度飞桨官网</span
              ></li>
                  <li>    <i class="iconfont icon-jiantou jiantou"></i
              ><span
                class="nav-item"
                @mouseenter="goCanSeen(1)"
                @mouseleave="goUnseen(1)"
                @click="goOtherSite('https://github.com/PaddleCV-SIG/PaddleRS')"
                >PaddleRS官方文档</span
              ></li>
          </ul>
           <p style="margin-top:0">相关网站</p>
           <ul>
             <li><i class="iconfont icon-jiantou jiantou"></i
              ><span
                class="nav-item"
                @mouseenter="goCanSeen(2)"
                @mouseleave="goUnseen(2)"
                @click="goOtherSite('https://rs.sensetime.com/')"
                >商汤SenseEarth</span
              ></li>
             <li><i class="iconfont icon-jiantou jiantou"></i
              ><span
                class="nav-item"
                @mouseenter="goCanSeen(3)"
                @mouseleave="goUnseen(3)"
                @click="goOtherSite('https://www.piesat.cn/')"
                >航天宏图</span
              ></li>
           </ul>
        </div></el-col
      >
        <el-col :xs="10" :sm="10" :md="10" :lg="5" :xl="5"
        ><div class="bottomnav">
          <p style="margin-top: 44px">
            功能页快速导航<span class="hidden-md-and-down">（需登录）</span>
          </p>
          <ul>
            <li>
              <i class="iconfont icon-jiantou jiantou"></i
              ><span
                @mouseenter="goCanSeen(4)"
                @mouseleave="goUnseen(4)"
                @click="goDetectChanges"
                >变化检测</span
              >
            </li>
            <li>
              <i class="iconfont icon-jiantou jiantou"></i
              ><span
                @mouseenter="goCanSeen(5)"
                @mouseleave="goUnseen(5)"
                @click="goDetectTargets"
                >目标检测</span
              >
            </li>
            <li>
              <i class="iconfont icon-jiantou jiantou"></i
              ><span
                @mouseenter="goCanSeen(6)"
                @mouseleave="goUnseen(6)"
                @click="goObtainTargets"
                >目标提取</span
              >
            </li>
            <li>
              <i class="iconfont icon-jiantou jiantou"></i
              ><span
                @mouseenter="goCanSeen(7)"
                @mouseleave="goUnseen(7)"
                @click="goClassify"
                >地物分类</span
              >
            </li>
            <li>
              <i class="iconfont icon-jiantou jiantou"></i
              ><span
                @mouseenter="goCanSeen(8)"
                @mouseleave="goUnseen(8)"
                @click="goHistory"
                >历史记录</span
              >
            </li>
          </ul>
        </div></el-col
      >
      <el-col :xs="10" :sm="10" :md="10" :lg="4" :xl="4"
        ><div class="bottomnav">
          <p>介绍页快速导航</p>
          <ul>
            <li>
              <i class="iconfont icon-jiantou jiantou"></i
              ><span
                class="nav-item"
                @mouseenter="goCanSeen(9)"
                @mouseleave="goUnseen(9)"
                @click="goRemoteSense"
                >遥感影像微介绍</span
              >
            </li>
            <li>
              <i class="iconfont icon-jiantou jiantou"></i
              ><span
                @mouseenter="goCanSeen(10)"
                @mouseleave="goUnseen(10)"
                @click="goIntelligent"
                >智慧解译</span
              >
            </li>
            <li>
              <i class="iconfont icon-jiantou jiantou"></i
              ><span
                @mouseenter="goCanSeen(11)"
                @mouseleave="goUnseen(11)"
                @click="goTechnology"
                >技术实现</span
              >
            </li>
            <li v-if="!isLogin">
              <i class="iconfont icon-jiantou jiantou"></i
              ><span
                @mouseenter="goCanSeen(12)"
                @mouseleave="goUnseen(12)"
                @click="goLogin"
                >登录/注册</span
              >
            </li>
            <li v-else>
              <i class="iconfont icon-jiantou jiantou"></i
              ><span
                @mouseenter="goCanSeen(12)"
                @mouseleave="goUnseen(12)"
                @click="logOut"
                >登出</span
              >
            </li>
          </ul>
        </div></el-col
      >
    <el-col
        :xs="3"
        :sm="3"
        :md="3"
        :lg="4"
        :xl="4"
        class="hidden-md-and-down"
        ><img
          :src="require('../assets/image/other/23.png')"
          style="height: 200px; margin-top: 60px"
        />
        <p class="qq">我们的交流群</p></el-col
      ></el-row
    >
  </div>
  <div class="smallone">
    <span
      ><span class="hidden-sm-and-down">Copyright © 2022.</span> All rights
      reserved.By 河马海牛队</span
    >
  </div>
</template>

<script>
import {
  goRemoteSense,
  goIntelligent,
  goTechnology,
  goLogin,
  goDetectChanges,
  goDetectTargets,
  goObtainTargets,
  goClassify,
  goHistory,
} from "@/utils/gosomewhere.js";
export default {
  name: "myfooter",
  data() {
    return {
      isLogin: localStorage.getItem("token"),
    };
  },
  methods: {
    goRemoteSense,
    goIntelligent,
    goTechnology,
    goLogin,
    goDetectChanges,
    goDetectTargets,
    goObtainTargets,
    goClassify,
    goHistory,
    goCanSeen(index) {
      let a = document.querySelectorAll(".jiantou");
      a[index].classList.add("cansee");
    },
    goUnseen(index) {
      let a = document.querySelectorAll(".jiantou");
      a[index].classList.remove("cansee");
    },
    goOtherSite(site){
      window.open(site)
    }
  },
  mounted() {
    document.body.style.overflow = "auto";
  },
};
</script>
 
<style scoped>
.bigone {
  font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto,
    Helvetica Neue, Arial, Noto Sans, sans-serif, Apple Color Emoji,
    Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;
  width: 100%;
  height: 350px;
  background-color: rgb(26, 26, 26);
  letter-spacing: 2px;
}
.smallone {
  letter-spacing: 2px;
  width: 100%;
  height: 60px;
  background-color: black;
  line-height: 60px;
  color: rgb(192, 192, 192);
  font-family: "Poppins", sans-serif;
  text-align: center;
}
.smallone span {
  margin: 0 auto;
}
.bottomnav p {
  margin-top: 60px;
  font-size: 20px;
  color: white;
  margin-bottom: -10px;
}
.bottomnav span {
  display: inline-block;
  color: rgb(192, 192, 192);
  margin-top: 20px;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.6s;
  margin-left: 10px;
}
.bottomnav span:hover {
  color: rgb(54, 54, 243);
}
.qq {
  margin-left: 80px;
  color: rgb(192, 192, 192);
}
ul {
  padding-left: 0;
}
.icon-jiantou {
  font-size: 20px;
  font-weight: bolder;
  color: red;
  opacity: 0;
}
@keyframes cansee {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
.cansee {
  animation-duration: 0.8s;
  animation-fill-mode: both;
  animation-name: cansee;
}
.see {
  opacity: 1;
}
</style>