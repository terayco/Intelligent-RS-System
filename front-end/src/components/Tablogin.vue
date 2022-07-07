<template>
  <span class="date hidden-sm-and-down"
    ><i class="iconfont icon-shijian" style="font-size:20px"></i>：<span class="hms"
      >{{ this.currenthour }}:{{ this.currentminute }}:{{
        this.currentsecond
      }}</span
    ><span class="ymd"
      >[{{ this.currentyear }}-{{ this.currentmonth }}-{{
        this.currentday
      }}]</span
    ></span
  >

  <div style="position: absolute; right: 8vw">
    <div class="share-button">
      <span
        ><i class="iconfont icon-fenxiang" style="font-size: 18px"></i>
        分享</span
      >
      <a href="#"><i class="iconfont icon-social-tieba" style="font-size: 22px" @click="shareToTieba"></i></a>
      <a href="#"><i class="iconfont icon-QQ" @click="shareToQQ"></i></a>
      <a href="#"
        ><i class="iconfont icon-xinlangweibo" @click="shareToMicroblog()"></i
      ></a>
    </div>
  </div>
  <div style="margin-left:15px"><i class="iconfont icon-github" style="font-size:28px" @click="goGithub"></i></div>
  <el-dropdown>
    <span class="el-dropdown-link">
      <i class="iconfont icon-yonghu" style="font-size: 27px"></i>
    </span>
    <template #dropdown>
      <el-dropdown-menu>
        <el-dropdown-item @click="logOut">登出</el-dropdown-item>
      </el-dropdown-menu>
    </template>
  </el-dropdown>
</template>

<script >
import {shareToQQ,shareToMicroblog,shareToTieba,shareToWeChat} from "@/utils/share.js"
import {getCurrentTime} from "@/utils/gettime.js"
import {loginOut} from "@/api/login"
export default {
  data() {
    return {
      currentyear: "",
      currentday: "",
      currentmonth: "",
      currenthour: "",
      currentminute: "",
      currentsecond: "",
      getDate: "",
      imgurl: "https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg"
    };
  },
  methods: {
    shareToQQ,shareToMicroblog,shareToTieba,shareToWeChat,getCurrentTime,loginOut,
    goGithub(){
      window.open();
    },
     logOut() {
      this.$confirm("是否确定登出?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          this.loginOut().then((res) => {
            localStorage.setItem("token", "");
            this.$message.success("登出成功！");
            this.$router.push("login");
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消操作",
          });
        });
    },
   shareImgToMicroblog(imgurl) {
    //自定义内容
    const share = {
      title: "来看看这张图片呗",
      image_url: imgurl,
    };
    //跳转地址
    window.open(
      "https://service.weibo.com/share/share.php?url=" +
        "&title=" +
        share.title+'&pic='+share.image_url+"&searchPic=true"
      // "&pic=" +
      // share.image_url[0] +
      // "&searchPic=true"
    );
  }

  },
  mounted() {
    this.getCurrentTime();
  },
  destroyed() {
    clearTimeout(this.getDate);
  },
};
</script>
<style scoped>
* {
    font-family: Microsoft JhengHei UI, sans-serif;
}
.date {
  font-family: Microsoft YaHei;
  font-weight: 400;
}
.hms {
  color: rgb(64,158,255);
  font-size: 18px;
}
.ymd {
  color: rgb(58, 99, 134);
  font-size: 13px;
}
.example-showcase .el-dropdown-link {
  cursor: pointer;
  color: var(--el-color-primary);
  display: flex;
  align-items: center;
}
.iconfont icon-yonghu {
  line-height: 70px;
  padding-top: 10px;
}
.iconfont icon-yonghu:hover {
  color: skyblue;
}
.el-dropdown-item {
  z-index: 10000;
}
.share-button {
  width: 120px;
  height: 30px;
  margin-bottom: 3px;
  background: #dfe6e9;
  border-radius: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  position: relative;
  cursor: pointer;
  transition: 0.3s linear;
}

.share-button:hover {
  transform: scale(1.1);
}
.share-button i {
  font-size: 25px;
}
.share-button span {
  position: absolute;
  width: 100%;
  height: 100%;
  background: rgb(64,158,255);
  color: #f1f1f1;
  text-align: center;
  line-height: 30px;
  z-index: 999;
  transition: 0.4s linear;
  border-radius: 40px;
}

.share-button:hover span {
  transform: translateX(-100%);
  transition-delay: 0.4s;
 
}

.share-button a {
  flex: 1;
  font-size: 26px;
  color: #2d3436;
  text-align: center;
  transform: translateX(-100%);
  opacity: 0;
  transition: 0.3s linear;
}

.share-button:hover a {
  opacity: 1;
  transform: translateX(0);

}
.share-button a:nth-of-type(1) {
  transition-delay: 1s;
}

.share-button a:nth-of-type(2) {
  transition-delay: 0.8s;
}

.share-button a:nth-of-type(3) {
  transition-delay: 0.6s;
}
</style>
