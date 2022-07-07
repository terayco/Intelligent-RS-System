<template>
  <el-container>
    <!-- <MyHeader class="theheader"></MyHeader> -->
    <el-header style="height: 0"></el-header>
    <el-main class="gotop">
      <router-view v-slot="{ Component }">
  
          <transition name="fade" mode="out-in">
            <component :is="Component" />
          </transition>
      
      </router-view>
    
      <el-backtop
        target=".gotop"
        :bottom="40"
        :visibility-height="50"
        :right="27"
      >
      </el-backtop>
    </el-main>
  </el-container>
</template>

<script>
import { reactive, onMounted, onActivated } from "vue";
import MyHeader from "@/components/MyHeader";
import Bottominfor from "@/components/Bottominfor";
import BackTop from "@/components/BackTop";
import scrollReveal from "scrollreveal";
import retScroll from "@/utils/scroll.js";
export default {
  name: "introduce",
  components: {
    Bottominfor,
    BackTop,
    MyHeader,
  },
  data() {
    return {
      scroll: "",
    };
  },
  setup() {
    const data = reactive({
      scrollReveal: scrollReveal(),
    });
    onMounted(() => {
      retScroll(data);
    });
    return {};
  },
  mounted() {
      document.body.style.overflow = "auto";
  },
};
</script>

<style scoped>
.el-main {
  --el-main-padding: 0px;
  overflow: hidden;
  height: auto;
}
.theheader {
  background-color: black;
  top: 0;
}
.el-header {
  height: 150px;
  box-shadow: 0 0;
}
.myvideo {
  width: 100%;
  height: 500px;
}
.overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  opacity: 0.6;
  background: #1c1d21;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.15s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>