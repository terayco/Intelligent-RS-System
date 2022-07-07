<template>
  <el-row>
    <el-col >
      <el-card  style="margin-bottom: 10px">
        <el-empty
          :image-size="200"
          v-if="this.beforeImg.length == 0"
        ></el-empty>
        <el-row :gutter="10">
          <el-col  :lg="5" :xl="5"
            ><div
              v-for="index in beforeList.length"
              class="img-index hidden-sm-and-down"  :style="{ height:  this.indexHeight + 'px' }"
            >
              第<span class="index-number">{{ index }}</span
              >组
            </div></el-col
          >
          <el-col :xs="20" :sm="10" :md="6" :lg="6" :xl="6" >
            <div v-for="(item, index) in beforeList" style="position: relative;">
              <el-image
                :src="beforeList[index]"
                :fit="fit"
                :lazy="true"
                ref="tableTab"
                class="gobig"
                :preview-src-list="[beforeList[index]]"
                :preview-teleported="true"
              ></el-image>
              <div class="img-infor">
                <span
                  >原图</span
                >
  
              </div>
            </div>
          </el-col>
          <el-col :xs="1" :sm="1" :md="2" :lg="2" :xl="2"></el-col>
          <el-col :xs="20" :sm="10" :md="6" :lg="6" :xl="6" >
            <div v-for="(item, index) in afterList" style="position: relative">
              <el-image
                :src="afterList[index]"
                :fit="fit"
                lazy
                ref="tableTab"
                class="gobig"
                :preview-src-list="[afterList[index]]"
                :preview-teleported="true"
           
              ></el-image>
              <div class="img-infor">
                <span
                  >预测结果</span
                >
                <span
                  @click="
                    downloadimgWithWords(
                      index + 1,
                      afterList[index],
                      `${this.funtype}结果图`
                    )
                  "
                  ><i class="iconfont icon-xiazai"></i
                ></span>
                <span style="margin-left: 15px"
                  ><span class="hidden-md-and-down">有问题？点此</span><i
                    class="iconfont icon-fankui"
                    @click="clickFeedBack(index)"
                  ></i
                  >反馈</span
                >
              </div>
            </div>
          </el-col>
        </el-row>
      </el-card>
    </el-col>
  </el-row>
  <el-dialog title="您的反馈" v-model="feedBackVisible" center fullscreen>
    <el-row justify="center">
      <el-rate
        class="rate"
        v-model="value"
        :icon-classes="iconClasses"
        void-icon-class="iconfont"
      >
      </el-rate>
    </el-row>
    <el-row justify="center">
      <el-form :model="form">
        <el-input
          v-model="form.content"
          autocomplete="off"
          :rows="10"
          type="textarea"
          class="feed-back"
        ></el-input>
      </el-form>
    </el-row>
    <el-row justify="center">
      <div slot="footer" class="dialog-footer">
        <el-button @click="notFeedBack">取 消</el-button>
        <el-button type="primary" @click="realFeedBack()">确定</el-button>
      </div>
    </el-row>
  </el-dialog>
</template>

<script>
import { downloadimgWithWords } from "@/utils/download.js";
import { goFeedBack } from "@/api/history";
export default {
  name: "imgshow",
  props: {
    beforeImg: {},
    afterImg: {},
    funtype: "",
  },
  data() {
    return {
      indexHeight:'',
      beforeList: [],
      afterList: [],
      feedBackVisible: false,
      previewPic1: "",
      dialogVisible: false,
      fit: "fill",
      form: {
        content: "",
        type: this.funtype,
        analysis_id: "",
      },
      formLabelWidth: "120px",
      value: null,
      iconClasses: ["icon-rate-face-1", "icon-rate-face-2", "icon-rate-face-3"],
    };
  },
  watch:{
    data() {
      return {
        
      }
    },
  },
  created() {
        if(this.funtype == '地物分类'){
      this.indexHeight = 290
    }
    if(this.funtype == '目标提取'){
      this.indexHeight = 335
    }
  },
  // mounted() {
  //   setTimeout(() => {
  //     this.beforeList = this.beforeImg.map((item) => {
  //       return item.before_img;
  //     });
  //     this.afterList = this.afterImg.map((item) => {
  //       return item.after_img;
  //     });
  //   }, 500);
  // },
  updated() {
    setTimeout(() => {
      this.beforeList = this.beforeImg.map((item) => {
        return item.before_img;
      });
      this.afterList = this.afterImg.map((item) => {
        return item.after_img;
      });
    }, 500);
  },
  methods: {
    downloadimgWithWords,
    goFeedBack,
    clickFeedBack(index) {
      this.form.analysis_id = this.afterImg[index].id;
      this.feedBackVisible = true;
    },
    notFeedBack() {
      this.feedBackVisible = false;
      this.$message("取消反馈");
      this.form.content = "";
    },
    realFeedBack() {
      if (this.form.content.split(" ").join("").length == 0) {
        this.$message.warning("请输入信息哦");
      } else {
        this.goFeedBack(this.form).then((res) => {
          this.feedBackVisible = false;
  
          this.form.content = "";
          this.$message.success("反馈成功！");
        });
      }
    },
  },
};
</script>

<style scoped lang="less">
* {
  font-family: SimHei sans-serif;
}

.feed-back {
  border: 3px solid #0f2d2d;
  width: 880px;
  margin-bottom: 30px;
  border-radius: 5px;
  font-size: 18px;
  font-family: Microsoft YaHei;
}
.img-index {
  text-align: center;
  height: 335px;
  align-content: center;
  line-height: 335px;
}
.index-number {
  font-family: Yu Gothic Medium;
  font-style: oblique;
  font-size: 30px;
  margin-left: 5px;
  margin-right: 10px;
}
.img-infor {
  text-align: center;
  font-size: 18px;
  margin-top: 5px;
  margin-bottom: 10px;
  height: 30px;
  font-weight: 500;
  font-family: Microsoft JhengHei UI, sans-serif;
}
.icon-xiazai {
  margin-left: 5px;
  font-size: 24px;
}
.icon-fankui {
  font-size: 24px;
  color: skyblue;
}
</style>