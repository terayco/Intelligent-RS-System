<template>
  <div class="fb-box">
    <el-table
      :data="tableData"
      style="width: 100%"
      ref="multipleTable"
      @selection-change="handleSelectionChange"
    >
      <el-table-column type="selection" width="55"> </el-table-column>
      <el-table-column label="反馈时间">
        <template v-slot="scope">
          <i class="el-icon-time"></i>
          <span>{{ scope.row.create_time }}</span>
        </template>
      </el-table-column>
      <el-table-column label="功能区" width="180">
        <template v-slot="scope">
          <span id="bigtitle"
            ><i
              style="font-size: 18px; margin-right: 6px"
              :class="{
                'iconfont icon-bianhuajiance': scope.row.type == '变化检测',
                'iconfont icon-mubiaojiance': scope.row.type == '目标检测',
                'iconfont icon-tiqu': scope.row.type == '目标提取',
                'iconfont icon-erfenleibianhuajiance16px':
                  scope.row.type == '地物分类',
              }"
            ></i
            >{{ scope.row.type }}</span
          >
        </template>
      </el-table-column>
      <el-table-column label="原图">
        <template v-slot="scope">
          <img
            :src="global.BASEURL+scope.row.before_img"
            min-width="70"
            height="70"
            @click="previewOnePic(scope.row.before_img)"
            class="goup"
          />
          <img
            v-if="scope.row.type == '变化检测'"
            :src="global.BASEURL+scope.row.before_img1"
            min-width="70"
            height="70"
            @click="previewOnePic(scope.row.before_img1)"
            class="goup"
            style="margin-left: 20px"
          />
        </template>
      </el-table-column>
      <el-table-column label="结果图">
        <template v-slot="scope">
          <img
            :src="global.BASEURL+scope.row.after_img"
            min-width="70"
            height="70"
            @click="previewOnePic(scope.row.after_img)"
            class="goup"
          />
        </template>
      </el-table-column>

      <el-table-column label="操作">
        <template v-slot="scope">
          <!-- <el-button size="default" @click="handleEdit(scope.$index, scope.row)"
          >编辑</el-button
        > -->
          <el-button
            v-if="scope.row.type != '变化检测'"
            size="default"
            type="primary"
            @click="previewTwoPic(scope.row.before_img, scope.row.after_img)"
          >
            预览
          </el-button>
          <el-button
            v-else
            size="default"
            type="primary"
            @click="
              previewThreePic(
                scope.row.before_img,
                scope.row.before_img1,
                scope.row.after_img
              )
            "
          >
            预览
          </el-button>
          <el-button
            size="default"
            type="primary"
            @click="
              downloadimgWithWords(
                scope.row.id,
                global.BASEURL+scope.row.after_img,
                `${scope.row.type}结果图`
              )
            "
          >
            下载
          </el-button>
        </template>
      </el-table-column>
      <el-table-column label="反馈信息">
        <template v-slot="scope">
          <span class="feed-back">{{ scope.row.content }}</span>
        </template>
      </el-table-column>
    </el-table>
    <div style="margin-top: 20px" v-show="this.tableData.length != 0">
      <el-button @click="toggleSelection(tableData)">全选</el-button>
      <el-button @click="toggleSelection()">取消选择</el-button>
      <el-button @click="downLoadAll()" type="primary">下载</el-button>
    </div>
    <el-row justify="center" v-show="this.tableData.length != 0">
      <el-col
        :xs="24"
        :sm="24"
        :md="10"
        :lg="11"
        :xl="10"
        style="margin-right: 40px"
      >
        <el-pagination
          background
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :page-size="fbpageSize"
          layout="prev, pager, next, jumper"
          :total="fbtotal"
          :current-page="fbcurrentPage"
          @next-click="goNextPage"
          @prev-click="goPrePage"
        >
        </el-pagination>
      </el-col>
    </el-row>

    <el-dialog
      v-model="dialogVisible"
      :modal="false"
      title="图片预览"
      width="75%"
      fullscreen
      center
    >
      <div v-if="flag == 2">
        <el-row justify="center">
          <el-col :xs="20" :sm="20" :md="10" :lg="10" :xl="10">
            <img :src="previewPic1" id="pre-img" />
          </el-col>
          <el-col :xs="20" :sm="20" :md="10" :lg="10" :xl="10">
            <img :src="previewPic2" id="pre-img" />
          </el-col>
        </el-row>
      </div>
      <div v-else-if="flag == 1">
        <el-row justify="center">
          <el-col :xs="10" :sm="10" :md="10" :lg="10" :xl="10">
            <img :src="previewPic1" id="pre-img" />
          </el-col>
        </el-row>
      </div>
      <div v-else-if="flag == 3">
        <el-row justify="center">
          <el-col :xs="20" :sm="20" :md="7" :lg="7" :xl="7">
            <img :src="previewPic1" id="pre-img" />
          </el-col>
          <el-col :xs="20" :sm="20" :md="10" :lg="7" :xl="7">
            <img :src="previewPic3" id="pre-img" />
          </el-col>
          <el-col :xs="20" :sm="20" :md="7" :lg="7" :xl="7">
            <img :src="previewPic2" id="pre-img" />
          </el-col>
        </el-row>
        <el-row> </el-row>
      </div>
      <el-row type="flex" justify="center">
        <el-col :span="1">
          <el-button type="primary" @click="dialogVisible = false"
            >OK</el-button
          >
        </el-col>
      </el-row>
    </el-dialog>
  </div>
</template>

<script>
import {
  previewOnePic,
  previewTwoPic,
  previewThreePic,
} from "@/utils/preview.js";
import { showFullScreenLoading, hideFullScreenLoading } from "@/utils/loading";
import { downloadimgWithWords } from "@/utils/download.js";
import { fbGetPage } from "@/api/history.js";
import store from '@/store'
import global from '@/global.vue'
export default {
  name: "feedbackhistory",
  components: {},
  data() {
    return {
          global:{
        BASEURL:global.BASEURL
      },
      direction: "rtl",
      size: "15%",
      fbpageSize: 10,
      fbtotal: 0,
      flag: "",
      fbcurrentPage: 1,
      multipleSelection: [],
      dialogVisible: false,
      previewPic1: "",
      previewPic2: "",
      previewPic3: "",
      tableData: [],
      initialTableData: [
      ],
   
    };
  },
  mounted() {
    this.getTabelInfo();
  },
  methods: {
    previewOnePic,
    downloadimgWithWords,
    previewTwoPic,
    previewThreePic,
    fbGetPage,
    handleEdit(index, row) {
     
    },
    downLoadAll() {
      if (this.multipleSelection.length == 0) {
        this.$message.warning("请选择要下载的历史记录的图片哦");
      } else {
        for (let item of this.multipleSelection) {
          this.downloadimgWithWords(
            item.id,
            global.BASEURL+item.after_img,
            `${item.type}结果图`
          );
        }
      }
    },
    toggleSelection(rows) {
      if (rows) {
        rows.forEach((row) => {
          this.$refs.multipleTable.toggleRowSelection(row);
        });
      } else {
        this.$refs.multipleTable.clearSelection();
      }
    },
    handleSelectionChange(val) {
      this.multipleSelection = val;
    },
    handleSizeChange(val) {
      this.pageSize = val;
      this.getTabelInfo();
  
    },
    handleCurrentChange(val) {
      //当前为第几页时调用getTabelInfo()显示第几页数据
      this.fbpage = val;
      this.fbcurrentPage = val;
      this.getTabelInfo();
    
    },
    getTabelInfo() {
     showFullScreenLoading(".fb-box");
      this.fbGetPage(this.fbcurrentPage,10).then((res) => {
  
        hideFullScreenLoading(".fb-box")
        this.fbtotal = res.data.count;
        this.tableData = res.data.data;
      });
    },
    goNextPage() {
      this.getTabelInfo();
    },
    goPrePage() {
      this.getTabelInfo();
    },
  },
    beforeRouteEnter(to, from, next) {
    next((vm) => {
      document.querySelector(".el-main").scrollTop = 0;
    });
  },
};
</script>

<style lang="less" scoped>
.hint {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji",
    "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  font-size: 18px;
  margin-bottom: 10px;
  margin-top: 10px;
}
.feed-back {
  font-family: SimHei sans-serif;
}
.block {
  text-align: center;
  margin: 0 auto;
  // margin-top: 1rem;
  // padding-left: 19rem;
}
.el-pagination {
  text-align: center;
  margin: 20px 0 10px 0;
}
.dis {
  display: none;
}
#bigtitle {
  font-size: 16px;
}
#bigtitle:hover:after {
  left: 0%;
  right: 0%;
  width: 100%;
}
</style>