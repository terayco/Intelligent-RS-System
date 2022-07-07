<template>
  <div class="data-box">
    <Tabinfor>
      <template v-slot:left> <h2>数据面板</h2> </template>
    </Tabinfor>
    <el-row :gutter="20" justify="center" align="middle"
      ><el-col :xs="24" :sm="12" :md="10" :lg="6" :xl="6"
        ><el-card class="data-cards"
          ><img :src="require('../assets/image/visualdata/39.png')" class="card-image" />
          <div class="card-words">欢迎您，<span class="username">{{this.username}}</span></div></el-card
        ></el-col
      ><el-col :xs="24" :sm="12" :md="10" :lg="6" :xl="6"
        ><el-card class="data-cards"
          ><img :src="require('../assets/image/visualdata/56.png')" class="card-image" />
          <div class="card-words">
            总访问量<span class="number" style="color: red">{{
              this.visit.visitCount
            }}</span>
          </div></el-card
        ></el-col
      ><el-col :xs="24" :sm="12" :md="10" :lg="6" :xl="6"
        ><el-card class="data-cards"
          ><img :src="require('../assets/image/visualdata/57.png')" class="card-image" />
          <div class="card-words">
            总上传图片数<span class="number" style="color: orange">{{
              this.photoCount
            }}</span>
          </div></el-card
        ></el-col
      ><el-col :xs="24" :sm="12" :md="10" :lg="6" :xl="6"
        ><el-card class="data-cards"
          ><img :src="require('../assets/image/visualdata/58.png')" class="card-image" />
          <div class="card-words">
            总注册用户数<span class="number" style="color: skyblue">{{
              this.userCount
            }}</span>
          </div></el-card
        ></el-col
      ></el-row
    >
    <el-row align="middle" justify="center"
      ><el-col :xs="17" :sm="17" :md="9" :lg="12" :xl="12">
        <div id="visit-chart"></div
      ></el-col>
      <el-col
        :xs="3"
        :sm="4"
        class="hidden-md-and-up hidden-xs-only"
        :offset="2"
        ><div class="visitchart-words">
          共计已有<span class="number">{{ this.visit.visitCount }}</span
          >访问量
        </div></el-col
      >
      <el-col
        :xs="24"
        :sm="20"
        :md="12"
        :lg="11"
        :xl="12"
        style="text-align: right"
      >
        <div id="fun-chart"></div></el-col
    ></el-row>
    <el-row align="middle" justify="center"
      ><el-col :xs="24" :sm="20" :md="10" :lg="10" :xl="10"
        ><div id="pic-chart"></div></el-col
      ><el-col :xs="24" :sm="20" :md="10" :lg="10" :xl="10"
        ><div id="feedback-chart"></div></el-col
    ></el-row>
  </div>
</template>

<script>
//https://www.jianshu.com/p/56a7847338ad使用escharts
let echarts = require("echarts/lib/echarts");
require("echarts/lib/chart/bar"); //柱状图
require("echarts/lib/chart/pie"); //饼图
//下面的是需要的提示框
require("echarts/lib/component/tooltip");
require("echarts/lib/component/title");
require("echarts/lib/component/legend");
require("echarts/lib/component/grid");
require("echarts/lib/component/toolbox");
require("echarts/renderers");
import Tabinfor from "@/components/Tabinfor.vue";
import { getVisualData } from "@/api/visualdata";
import { showFullScreenLoading, hideFullScreenLoading } from "@/utils/loading";
import Img1 from "@/assets/image/visualdata/39.png";
import { nextTick } from "vue";
export default {
  name: "visualdata",
  components: {
    Tabinfor,
  },
  data() {
    return {
      Img1,
      isShow: true,
      username:'',
      userCount: "",
      photoCount: "",
      visit: {
        visitCount: "",
        visitDates: [],
        visitNum: [],
      },
      visit: {},
      photo: [],
      feedBack: [],
      siteVisit: [],
    };
  },
  created() {
    showFullScreenLoading(".data-box");
    this.getVisualData().then((res) => {
    
      this.username = res.data.data.user_name
      this.visit.visitCount = res.data.data.visit_count;
      this.userCount = res.data.data.user_count;
      this.photoCount = res.data.data.photo_count;

      const visits = res.data.data.seven_days_items;
      this.visit.visitDates = visits.map((item) => {
        return item.dates;
      });
      this.visit.visitNum = visits.map((item) => {
        return item.num;
      });

      this.photo = res.data.data.photo_items;

      this.feedBack = res.data.data.feedback_items;

      this.siteVisit = res.data.data.function_items;
    
           hideFullScreenLoading(".data-box")
      this.drawVisit("visit-chart");
      this.drawFunVisit("fun-chart");
      this.drawPic("pic-chart");
      this.drawFeedBack("feedback-chart");
    });
      nextTick(() => {
        // this.drawVisit("visit-chart");
        // this.drawFunVisit("fun-chart");
        // this.drawPic("pic-chart");
        // this.drawFeedBack("feedback-chart");
      });
  },
  methods: {
    getVisualData,
    drawVisit(id) {
      let visitChart = echarts.init(document.getElementById(id));
      visitChart.setOption({
        title: {
          text: "近7天访客量",
          show: true,
          textAlign: "auto",
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow",
          },
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        xAxis: [
          {
            type: "category",
            data: this.visit.visitDates,
            axisTick: {
              alignWithLabel: true,
            },
          },
        ],
        yAxis: [
          {
            type: "value",
          },
        ],
        series: [
          {
            name: "访客量",
            type: "bar",
            barWidth: "60%",
            data: this.visit.visitNum,
          },
        ],
      });
    },
    drawFunVisit(id) {
      let funVisitChart = echarts.init(document.getElementById(id));
      funVisitChart.setOption({
        title: {
          text: "各界面访问量",
        },
        legend: {
          top: "bottom",
        },
        toolbox: {
          show: true,
          feature: {
            mark: { show: true },
            dataView: { show: true, readOnly: false },
            restore: { show: true },
            saveAsImage: { show: true },
          },
        },
        series: [
          {
            name: "",
            type: "pie",
            radius: [50, 250],
            center: ["50%", "50%"],
            roseType: "area",
            itemStyle: {
              borderRadius: 8,
            },
            data: [
              { value: 400, name: this.siteVisit[0].name },
              { value: 500, name: this.siteVisit[1].name },
              { value: 600, name: this.siteVisit[2].name },
              { value: 700, name: this.siteVisit[3].name },
              { value: 600, name: this.siteVisit[4].name },
              { value: 1200, name: this.siteVisit[5].name },
              { value: 100, name: this.siteVisit[6].name },
              //    { value: this.siteVisit[7].num, name: this.siteVisit[7].name },
              //       { value: this.siteVisit[8].num, name: this.siteVisit[8].name },
              //  { value: this.siteVisit[9].num, name: this.siteVisit[9].name },
              //     { value: this.siteVisit[10].num, name: this.siteVisit[10].name },
            ],
          },
        ],
      });
    },
    drawPic(id) {
      let picChart = echarts.init(document.getElementById(id));
      picChart.setOption({
        title: {
          text: "各功能区上传图片数",
        },
        tooltip: {
          trigger: "item",
        },
        legend: {
          top: "5%",
          left: "center",
        },
        series: [
          {
            name: "上传图片数",
            type: "pie",
            radius: ["40%", "70%"],
            avoidLabelOverlap: false,
            label: {
              show: false,
              position: "center",
            },
            emphasis: {
              label: {
                show: true,
                fontSize: "40",
                fontWeight: "bold",
              },
            },
            labelLine: {
              show: false,
            },
            data: [
              {
                value: 2130,
                name: '目标提取',
              },
              {
                value: 1800,
                name: '地物分类',
              },
              {
                value: this.photo[2].num,
                name: this.photo[2].type,
              },
              {
              value: 1600,
                name: '目标检测',
              },
            ],
          },
        ],
      });
    },
    drawFeedBack(id) {
      let feedBackChart = echarts.init(document.getElementById(id));
      feedBackChart.setOption({
        title: {
          text: "各功能区反馈信息数",
        },
        tooltip: {
          trigger: "item",
        },
        legend: {
          top: "5%",
          left: "center",
        },
        series: [
          {
            name: "反馈信息数",
            type: "pie",
            radius: ["40%", "70%"],
            avoidLabelOverlap: false,
            label: {
              show: false,
              position: "center",
            },
            emphasis: {
              label: {
                show: true,
                fontSize: "40",
                fontWeight: "bold",
              },
            },
            labelLine: {
              show: false,
            },
            data: [
              { value: 40, name: '目标提取' },
              { value: 68, name: '地物分类' },
              { value: 36, name: '目标检测'},
              { value: 90, name: '变化检测' },
            ],
          },
        ],
      });
    },
  },
};
</script>

<style scoped>
* {
  margin-bottom: 10px;
  font-family: SimHei sans-serif;
}
.data-cards {
  position: relative;
  height: 150px;
  align-content: center;
  overflow: hidden;
}
.card-image {
  width: 100%;
}
.card-words {
  padding-left: 10px;
  margin-top: 40px;
  display: inline-block;
  font-size: 20px;
  position: absolute;
  left: 0;
  right: 0;
  font-family: Open Sans, Inter, Roboto, Oxygen, Fira Sans, Helvetica Neue,
    sans-serif;
}
#visit-chart {
  height: 700px;
  width: 540px;
  box-shadow: 0 0 2rem 0 rgba(41, 48, 66, 0.1);
}
#fun-chart {
  position: relative;
  right: 0;
  height: 700px;
  width: 665px;
  box-shadow: 0 0 2rem 0 rgba(41, 48, 66, 0.1);
}
#pic-chart {
  width: 450px;
  height: 400px;
  box-shadow: 0 0 2rem 0 rgba(41, 48, 66, 0.1);
}
#feedback-chart {
  width: 450px;
  height: 400px;
  box-shadow: 0 0 2rem 0 rgba(41, 48, 66, 0.1);
}
.number {
  font-family: Yu Gothic Medium;
  font-style: oblique;
  font-size: 60px;
}
.visitchart-words {
  margin-top: 150px;
  font-size: 25px;
}
.username{
  font-size: 60px;
   font-family: Yu Gothic Medium;
}
</style>