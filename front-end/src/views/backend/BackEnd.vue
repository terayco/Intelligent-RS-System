<template>
  <el-header height="100px" class="be-title">遥感图像智能解译后台管理系统</el-header>
  <el-main>
    <div class="backend-box">
      <el-row justify="start" align="middle"
        ><el-col :xs="20" :sm="20" :md="3" :lg="3" :xl="3"
          ><div
            id="subtitle"
            @click="goUserList"
           :class="{ 'active': this.$route.path == '/userlist' }"
          >
            用户列表
          </div></el-col
        ><el-col :xs="20" :sm="20" :md="3" :lg="3" :xl="3"
          ><div id="subtitle" @click="goFeedBackList" :class="{ 'active': this.$route.path == '/feedbacklist' }">反馈信息列表</div></el-col
        ></el-row
      >
      <router-view v-slot="{ Component }">
        <keep-alive include="userlist,feedbacklist">
          <transition name="fade" mode="out-in">
            <component :is="Component" />
          </transition>
        </keep-alive>
      </router-view>
    </div>
  </el-main>
</template>

<script>
export default {
  name: "backend",
  mounted(){
      document.body.style.overflow = "auto";
  },
  methods: {
    goUserList() {
      if (this.$route.path == "/userlist") {
        this.$message.success("已在当前界面");
      } else {
        this.$router.push("userlist");
        this.site = "用户列表";
      }
    },
    goFeedBackList() {
      if (this.$route.path == "/feedbacklist") {
        this.$message.success("已在当前界面");
      } else {
        this.site = " 反馈信息列表";
        this.$router.push("feedbacklist");
      }
    },
  },
  beforeRouteEnter(to, from, next){
      const superAdmin = localStorage.getItem('superAdmin')
    if (superAdmin == '') {
      next({ path: '/remotesense' })
    }
    else {next()}
  
  }
};
</script>

<style scoped>
* {
  font-family: SimHei sans-serif;
}
.el-header {
  text-align: center;
  font-size: 30px;
  line-height: 100px;
}
.backend-box {
  padding-right: 50px;
  padding-left: 50px;
}
.user-list {
  margin-bottom: 20px;
  font-size: 20px;
  text-align: center;
}
#subtitle {
  transition: all 0.4s;
  text-align: center;
  font-family: Microsoft JhengHei UI, sans-serif;
  font-size: 20px;
}
#subtitle:hover:after {
  left: 0%;
  right: 0%;
  width: 100%;
}
.active {
  color: rgb(64, 158, 255);
}
#subtitle:hover{
  color: rgb(64, 158, 255);
}
.be-title{
  letter-spacing: 20px;
}
</style>