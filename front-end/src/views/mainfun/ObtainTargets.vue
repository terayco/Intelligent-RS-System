 <template>
  <div class="bigbox">
    <Tabinfor >
      <template v-slot:left>
        <div id="subtitle" style="font-size: 25px">
          目标提取<i
            class="iconfont icon-dianji"
            style="font-size: 23px; margin-left: 17px; color: blue"
          ></i></div
      ></template>
      <template v-slot:mid> </template>
      <template v-slot:right> </template>
    </Tabinfor>
    <el-divider></el-divider>
    <Tabinfor>
      <template v-slot:left>
        <p >
          请上传包含<span class="goweight">图片的文件夹</span
          ><i class="iconfont icon-wenjianjia" style="color: blue"></i>或者<span
            class="goweight"
            >图片</span
          ><i class="iconfont icon-tupiantianjia" style="color: skyblue"></i>
        </p>
      </template>
    </Tabinfor>
    <el-row type="flex" justify="center">
      <el-col :span="24" >
        <el-card style="border: 4px dashed var(--el-border-color)">
             <div class="clearQ" v-if="this.fileList.length"> <el-button type=primary class="btn-animate2 btn-animate__surround" @click="clearQue">清空图片</el-button></div>
          <el-upload
            class="upload-demo imgcard"
            drag
            action="#"
            multiple
            :auto-upload="false"
            ref="upload"
            id="one "
            :file-list="fileList"
            @change="beforeUpload(this.fileList[this.fileList.length - 1].raw)"
          >
            <i class="iconfont icon-yunduanshangchuan"></i>
            <div class="el-upload__text">
              将文件拖到此处，或<em>点击上传</em>
            </div>
            <div class="el-upload__tip" slot="tip">
              只能上传一张或多张图片，请在下方上传文件夹
            </div>
           
          </el-upload>
                    <el-row justify="center">
            <input
              type="file"
              id="ctrl"
              ref="myfile"
              webkitdirectory
              directory
              multiple
              @change="uploadMore()"
            />
            <i class="iconfont icon-wenjianshangchuan" @click="fileClick"
              >上传文件夹</i
            >
          </el-row>
           
          <el-row justify="center">
            <p>
              <label class="mylabel container">
                <input
                  type="checkbox"
                  class="myinput"
                  ref="cut"
                  @change="select()"
                />
                <span class="checkmark"></span>
                <span class="goweight label-words">上传时编辑图片</span><i class="iconfont icon-crop-full" style="margin-left:10px;color:rgb(64,158,255)"></i>
              </label>
            </p>
          </el-row>
          <el-row justify="center" align="middle">
             <i class="iconfont icon-tuxingtuxiangchuli" style="color:rgb(64,158,255);font-size:20px"></i><p>图像预处理：</p>
            <p>
              <label class="mylabel container">
                <input
                  type="checkbox"
                  class="myinput"
                  ref="clahe"
                  @change="selectClahe(3)"
                />
                <span class="checkmark"></span>
                <span class="goweight label-words">CLAHE</span>
              </label>
            </p>
            <p>
              <label class="mylabel container">
                <input
                  type="checkbox"
                  class="myinput"
                  ref="sharpen"
                  @change="selectSharpen(3)"
                />
                <span class="checkmark"></span>
                <span class="goweight label-words">锐化</span>
              </label>
            </p>
          </el-row>
          <el-row justify="center" align="middle">
              <i class="iconfont icon-agora_AIjiangzao" style="color:rgb(64,158,255);font-size:35px"></i><p>降噪处理：</p>
            <p>
              <label class="mylabel container">
                <input
                  type="checkbox"
                  class="myinput"
                  ref="smooth"
                  @change="selectSmooth()"
                />
                <span class="checkmark"></span>
                <span class="goweight label-words">平滑</span>
              </label>
              <label class="mylabel container">
                <input
                  type="checkbox"
                  class="myinput"
                  @change="selectFilter()"
                  ref="filter"
                />
                <span class="checkmark"></span>
                <span class="goweight label-words">滤波</span>
              </label>
            </p>
          </el-row>

          <div style="text-align: center;margin-top:12px">
            <el-button
              type="primary"
              class="btn-animate btn-animate__shiny"
              style="margin: 0 auto"
              @click="upload('目标提取')"
              >开始处理</el-button
            >
          </div>
            <el-divider v-if="!this.uploadSrc.prehandle"></el-divider>
    <div v-if="this.uploadSrc.prehandle">
        <p  v-if="this.uploadSrc.prehandle==2">
         <div id="subtitle" style="font-size: 25px">
          CLAHE处理结果预览<i
            class="iconfont icon-dianji"
            style="font-size: 23px; margin-left: 17px; color: blue"
          ></i></div
      >   
    </p>
     <p v-else-if="this.uploadSrc.prehandle==4">
         <div id="subtitle" style="font-size: 25px">
          锐化处理结果预览<i
            class="iconfont icon-dianji"
            style="font-size: 23px; margin-left: 17px; color: blue"
          ></i></div
      >   
    </p>
    <el-divider></el-divider>
    <el-row justify="center" :gutter="20">
      <el-col :xs="24" :sm="24" :md="6" :lg="6" :xl="6"><div v-for="(item) in this.before" ><el-image :src="item" :preview-src-list='[item]' :preview-teleported="true"></el-image><div class="his-words">原图</div></div></el-col>
      <el-col  :md="2" :lg="2" :xl="2"></el-col>
      <el-col :xs="24" :sm="24" :md="6" :lg="6" :xl="6" v-if="this.uploadSrc.prehandle==2"><div v-for="(item) in this.claheImg" ><el-image :src="item" :preview-src-list='[item]' :preview-teleported="true"></el-image><div class="his-words">CLAHE处理后     <span
                  @click="
                    downloadimgWithWords(
                      -1,
                      item,
                      `CLAHE处理图`
                    )
                  "
                  ><i class="iconfont icon-xiazai"></i
                ></span></div></div></el-col>
    <el-col :xs="24" :sm="24" :md="6" :lg="6" :xl="6" v-if="this.uploadSrc.prehandle==4"><div v-for="(item) in this.sharpenImg" ><el-image :src="item" :preview-src-list='[item]' :preview-teleported="true"></el-image><div class="his-words">锐化处理后     <span
                  @click="
                    downloadimgWithWords(
                      -1,
                      item,
                      `锐化处理图`
                    )
                  "
                  ><i class="iconfont icon-xiazai"></i
                ></span></div></div></el-col>
    </el-row>
   </div>
        </el-card>
      </el-col>
    </el-row>
    <Tabinfor>
      <template v-slot:left>
        <div id="subtitle" style="font-size: 25px">
          结果图预览<i
            class="iconfont icon-dianji"
            style="font-size: 23px; margin-left: 17px; color: blue"
          ></i></div
      ></template>
    </Tabinfor>
    <el-divider></el-divider>

    <Tabinfor>
      <template v-slot:left>
        <p>
          对输出的结果图进行<span class="goweight">多种渲染</span
          ><i class="iconfont icon-xuanran" style="color: red"></i>
          <span class="goweight">，点击图片</span>即可预览
          <i class="iconfont icon-duigou" style="color: green"></i>
        </p>
      </template>
           <template v-slot:mid>
       <p v-if="this.isUpload"><i class="iconfont icon-dabaoxiazai" @click="goCompress('目标提取')">结果图打包</i>
            </p>
      </template>
      <template v-slot:right>
        <span class="goweight"
          ><i class="iconfont icon-shuaxin" @click="getMore" style="padding-right:24px"><span class="hidden-sm-and-down">点击刷新</span></i></span
        >
      </template>
    </Tabinfor>
    <el-card class="render-box">
      <el-row justify="center" :gutter="20"
        ><el-col :xs="12" :sm="12" :md="12" :lg="10" :xl="10"
          ><div class="render-img render-img1">
                  <p class="render-words">原图</p>
            <el-image
              v-if="this.afterImg.length != 0"
              :preview-src-list="[this.beforeList[this.currentIndex]]"
              :preview-teleported="true"
              :src="this.beforeImg[this.currentIndex].before_img"
              fit="cover"
              style="width: 100%"
            ></el-image>
            <el-image
              v-else
              :preview-src-list="[this.example.first[0]]"
              :preview-teleported="true"
              :src="this.example.first[0]"
              fit="cover"
              style="width: 100%"
            ></el-image>
      
          </div></el-col
        >
        <el-col :xs="12" :sm="12" :md="12" :lg="10" :xl="10"
          ><div class="render-img">
             <p class="render-words">预测图</p>
            <el-image
              v-if="this.afterImg.length != 0"
              :preview-src-list="[this.showingList[this.currentIndex]]"
              :preview-teleported="true"
              :src="this.showingList[this.currentIndex]"
              fit="cover"
              style="width: 100%;"
            ></el-image>
              <div v-else>
            <el-image
              v-if="this.renderstyle=='原图'"
              :preview-src-list="[this.example.outcome[0]]"
              :preview-teleported="true"
              :src="this.example.outcome[0]"
              fit="cover"
              style="width: 100%"
            ></el-image>
                <el-image
              v-else-if="this.renderstyle=='田野'"
              :preview-src-list="[this.example.field[0]]"
              :preview-teleported="true"
              :src="this.example.field[0]"
              fit="cover"
              style="width: 100%"
            ></el-image>    <el-image
              v-else-if="this.renderstyle=='海洋'"
              :preview-src-list="[this.example.ocean[0]]"
              :preview-teleported="true"
              :src="this.example.ocean[0]"
              fit="cover"
              style="width: 100%"
            ></el-image>    <el-image
              v-else-if="this.renderstyle=='熔岩'"
              :preview-src-list="[this.example.lava[0]]"
              :preview-teleported="true"
              :src="this.example.lava[0]"
              fit="cover"
              style="width: 100%"
            ></el-image>    <el-image
              v-else-if="this.renderstyle=='沙漠'"
              :preview-src-list="[this.example.desert[0]]"
              :preview-teleported="true"
              :src="this.example.desert[0]"
              fit="cover"
              style="width: 100%"
            ></el-image>
            </div>
           
          </div></el-col
        ><el-col :xs="24" :sm="24" :md="24" :lg="4" :xl="4"
          ><div class="rendr-style">
               <el-divider style="margin-top:0"></el-divider>
            <div class="style-title">结果图渲染</div>
            <label class="cl-checkbox">
              <el-row justify="center">
                <el-col
                  ><div
                    class="style-words normal"
                    @click="setNormalWay(this.onRender)"
                    :class="{ 'active-normal': this.renderstyle == '原图' }"
                  >
                    原图
                  </div>
                  <div
                    class="style-words field"
                    @click="setField(this.onRender)"
                    :class="{ 'active-field': this.renderstyle == '田野' }"
                  >
                    田野
                  </div>
                  <div
                    class="style-words ocean"
                    @click="setOcean(this.onRender)"
                    :class="{ 'active-ocean': this.renderstyle == '海洋' }"
                  >
                    海洋
                  </div>
                  <div
                    class="style-words lava"
                    @click="setLava(this.onRender)"
                    :class="{ 'active-lava': this.renderstyle == '熔岩' }"
                  >
                    熔岩
                  </div>
                  <div
                    class="style-words desert"
                    @click="setDesert(this.onRender)"
                    :class="{ 'active-desert': this.renderstyle == '沙漠' }"
                  >
                    沙漠
                  </div></el-col
                >
              </el-row>
            </label>
          </div>
             <el-divider style="margin-top:0"></el-divider>
          <div class="style-title">选择图片</div>
       
          <el-empty
            :image-size="100"
            v-if="this.showingList.length == 0"
          ></el-empty>
          <div
            v-for="(item, index) in Math.ceil(this.showingList.length / 5)"
            class="list"
          >
            <div class="list-number" @click="goRenderThese(index)">
              {{ 5 * index + 1 }}-----{{ 5 * (index + 1) }}
            </div>
          </div>
          <p v-show="this.showingList.length != 0">
            下载此图片：<el-button
              type="primary"
              style="width:65px"
                  class="btn-animate btn-animate__shiny"
              @click="
                downloadimgWithWords(
                  ++this.downnumber,
                  this.showingList[this.currentIndex],
                  `目标提取${this.renderstyle}渲染结果图`
                )
              "
              >下载</el-button
            >
         
              <p v-if="this.isUpload"><span class="hidden-sm-and-down">有问题？</span>点此<i
                class="iconfont icon-fankui"
                @click="clickFeedBack(this.currentIndex)"
              ></i
              ><span class="hidden-md-and-down">向我们</span>反馈</p>
          </p>
        </el-col></el-row
      >
      <el-row class="swiper-img">
        <el-button @click="goLeft" class="swiper-lbtn">&lt</el-button>
        <el-button @click="goRight" class="swiper-rbtn">&gt</el-button>

        <div class="img-box" v-for="(item, index) in 5">
          <el-image
            :src="srcs[index]"
            @click="goRenderThis(index)"
            v-if="isExist[index]"
           :class="{'render-border':this.onRender==index}"
          ></el-image>
        </div>
      </el-row>
    </el-card>
    <el-dialog
      v-model="cutVisible"
      :modal="false"
      title="编辑"
      width="75%"
      top="0"
      ><MyVueCropper
        :fileimg="fileimg"
        :funtype="funtype"
        :file="file"
        :length="afterImg.length"
        @cutChanged="notvisible"
        :prehandle='uploadSrc.prehandle'
        :denoise='uploadSrc.denoise'
      ></MyVueCropper
    ></el-dialog>
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
    <Bottominfor></Bottominfor>
  </div>
</template>

<script>
import { showFullScreenLoading, hideFullScreenLoading } from "@/utils/loading";
import {
  downloadimgWithWords,
  getImgArrayBuffer,
  atchDownload,
} from "@/utils/download.js";
import { historyGetPage, goFeedBack } from "@/api/history";
import { createSrc, obtainTargetsUpload } from "@/api/upload";
import { getUploadImg, upload, goCompress } from "@/utils/getUploadImg";
import {
  selectSharpen,
  selectFilter,
  selectSmooth,
  selectClahe,
} from "@/utils/preHandle";
import ImgShow from "@/components/ImgShow";
import Tabinfor from "@/components/Tabinfor";
import Bottominfor from "@/components/Bottominfor";
import MyVueCropper from "@/components/MyVueCropper";
import global from '@/global'

export default {
  name: "obtaintargets",
  components: {
    ImgShow,
    Tabinfor,
    Bottominfor,
    MyVueCropper,
  },
  data() {
    return {
      canUpload:true,
      onRender:0,
      onRenderGroup:0,
      claheImg:[],
      sharpenImg:[],
      before:[],
      before1:[],
      before:[],
      before1:[],
       isUpload:true,
      formLabelWidth: "120px",
      value: null,
      iconClasses: ["icon-rate-face-1", "icon-rate-face-2", "icon-rate-face-3"],
      feedBackVisible: false,
      form: {
        content: "",
        type: "目标提取",
        analysis_id: "",
      },
      beforeList: [],
      isExist: [],
      downnumber: 0,
      renderstyle: "原图",
      xminus: 0,
      afterImg: [],
      afterList: [],
      field: [],
      ocean: [],
      lava: [],
      desert: [],
      showingList: [],
      beforeImg: [],
      beforeImg1: [],
      currentQroup: 0,
      src: global.BASEURL+"/_uploads/photos/res/eaf6426f17d1a3d26154018ab0c29492_509e9bf2b066e09601dd14b93c601a7e_img-8.png",
      srcs: [
        global.BASEURL+"/_uploads/photos/res/eaf6426f17d1a3d26154018ab0c29492_509e9bf2b066e09601dd14b93c601a7e_img-8.png",
      ],
      example:{
        outcome:[global.BASEURL+"/_uploads/photos/res/eaf6426f17d1a3d26154018ab0c29492_509e9bf2b066e09601dd14b93c601a7e_img-8.png"],
        first:[global.BASEURL+"/_uploads/photos/509e9bf2b066e09601dd14b93c601a7e_img-8.png"],
        normal:[global.BASEURL+"/_uploads/photos/res/eaf6426f17d1a3d26154018ab0c29492_509e9bf2b066e09601dd14b93c601a7e_img-8.png"],
        field:[global.BASEURL+"/_uploads/photos/res/1fc510840753df86776294b241abe691.png"],
        ocean:[global.BASEURL+"/_uploads/photos/res/64cc9bf627b210d19bdf21d7837ab778.png"],
        lava:[global.BASEURL+"/_uploads/photos/res/423c8e299acf60c6469f748abc6f8d29.png"],
        desert:[global.BASEURL+"/_uploads/photos/res/952e6aec813d354d7a29ee6946ab06e0.png"]
      },
      currentIndex: 0,

      radio: 0,
      fileimg: "",
      file: {},
      isNotCut: true,
      cutVisible: false,
      funtype: "目标提取",
      scrollTop: "",
      scrollContainer: HTMLCollection,
      fit: "fill",
      wrapperElem: null,
      beforeImg: [],
      afterImg: [],
      fileList: [],
      uploadSrc: {
        list: [],
        prehandle: 0,
        denoise: 0,
      },
         prePhoto:{
        list:[],
        prehandle:0,
        type:4
      }
    };
  },
  methods: {
    historyGetPage,
    obtainTargetsUpload,
    getImgArrayBuffer,
    atchDownload,
    createSrc,
    getUploadImg,
    upload,
    goCompress,
    downloadimgWithWords,
    selectSharpen,
    selectFilter,
    selectSmooth,
    selectClahe,
    goFeedBack,
    clearQue(){
      this.fileList = []
      this.$message.success('清除成功')
 
    },
    checkUpload(){
      if(this.afterList.length == 0){
        this.isUpload = false
      }
      else{
        this.isUpload = true
      }
    },
    checkExist(val) {
      this.isExist = val.map((item) => {
        if (typeof item == "undefined") {
          return false;
        } else return true;
      });
    },
    goLeft() {
      let x = document.querySelectorAll(".img-box");
      this.xminus -= 80;
      for (let item of x) {
        item.setAttribute("style", `transform:translateX(${this.xminus}%)`);
      }
    },
    goRight() {
      let x = document.querySelectorAll(".img-box");
      this.xminus += 80;
      for (let item of x) {
        item.setAttribute("style", `transform:translateX(${this.xminus}%)`);
      }
    },
    goRenderThis(index) {
      this.currentIndex = this.currentQroup;
      this.currentIndex += index;
      if (this.showingList.length != 0) {
        this.src = this.showingList[this.currentIndex];
      } else {
        this.src = this.srcs[index];
      }
      this.onRender = index
    },
    goRenderThese(index) {
      this.onRenderGroup = index
      this.xminus = 0;
      let x = document.querySelectorAll(".img-box");
      for (let item of x) {
        item.setAttribute("style", `transform:translateX(0%)`);
      }
      this.currentQroup = 5 * index;
      this.currentIndex = 5 * index;
      this.srcs = [];
      for (let i = 0; i <= 4; i++) {
        this.srcs.push(this.showingList[this.currentIndex++]);
      }
      this.src = this.srcs[0];
     this.goRenderThis(0)
      this.checkExist(this.srcs);
    },
    setNormalWay(render) {
      (render);
      this.renderstyle = "原图";
     
      this.showingList.splice(0, this.showingList.length);
            if(this.afterImg.length == 0){
        this.showingList.push(this.example.normal[0])
      }else{
         this.showingList.push(...this.afterList);
      }
      this.goRenderThese(this.onRenderGroup);
      this.goRenderThis(render);
    
    },
    setField(render) {
      this.renderstyle = "田野";
      this.showingList.splice(0, this.showingList.length);
      if(this.afterImg.length == 0){
    
        this.showingList.push(this.example.field[0])
      }else{
     
      this.showingList.push(...this.field);
      }
      this.goRenderThese(this.onRenderGroup);
      this.goRenderThis(render);
    },
    setOcean(render) {
      this.renderstyle = "海洋";
      this.showingList.splice(0, this.showingList.length);
      if(this.afterImg.length == 0){
        this.showingList.push(this.example.ocean[0])
      }else{
    this.showingList.push(...this.ocean);
      }
       this.goRenderThese(this.onRenderGroup);
      this.goRenderThis(render);
    },
    setLava(render) {
      this.renderstyle = "熔岩";
      this.showingList.splice(0, this.showingList.length);
      if(this.afterImg.length == 0){
        this.showingList.push(this.example.lava[0])
      }else{
  this.showingList.push(...this.lava);
      }
        this.goRenderThese(this.onRenderGroup);
      this.goRenderThis(render);
    },
    setDesert(render) {
      this.renderstyle = "沙漠";
      this.showingList.splice(0, this.showingList.length);
      if(this.afterImg.length == 0){
        this.showingList.push(this.example.desert[0])
      }else{
      this.showingList.push(...this.desert);
      }
        this.goRenderThese(this.onRenderGroup);
      this.goRenderThis(render);
    },
    notvisible() {
      this.cutVisible = false;
      this.fileList = [];
    },
    getMore() {
      this.getUploadImg("目标提取");
    },
    uploadMore() {
             this.beforeUpload(...this.$refs.myfile.files)
        if(this.canUpload){
          this.fileList.push(...this.$refs.myfile.files);
        }else{
          setTimeout(() => {
              this.$message.error('检测到您上传的文件夹内存在不符合规范的图片类型')
          }, 1000);
        
        }
    },
    fileClick() {
      document.querySelector("#ctrl").click();
    },
    beforeUpload(file) {
      if (this.$refs.cut.checked) {
        this.cutVisible = true;
      } else {
        this.cutVisible = false;
      }
              const fileSuffix = file.name.substring(file.name.lastIndexOf(".") + 1)
  const whiteList = ['jpg','jpeg','png','JPG','JPEG']
  if (whiteList.indexOf(fileSuffix) === -1) {
    this.$message.error("上传只能是 jpg,jpeg,png,JPG,JPEG格式,请重新上传");
    this.fileList= []
    this.canUpload = false
     this.cutVisible = false;

  }else{
  let data = window.URL.createObjectURL(new Blob([file]));
      this.fileimg = data;
       this.canUpload = true
  }
    
    },
    select() {
      if (this.$refs.cut.checked) {
        this.isNotCut = true;
      } else {
        this.isNotCut = false;
      }
    },
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
  created() {
    this.getUploadImg("目标提取");
  },
  beforeRouteEnter(to, from, next) {
    next((vm) => {
      document.querySelector(".el-main").scrollTop = 0;
    });
  },
};
</script>
<style lang="less" scoped>
* {
  font-family: SimHei sans-serif;
}
.imgInfor {
  text-align: center;
  margin-bottom: 20px;
}
.imgcard {
  text-align: center;
}
.el-upload-dragger {
  border: 3px dashed var(--el-border-color);
  height: 180px;
  margin-top: 10px;
}
#subtitle:hover:after {
  left: 0%;
  right: 0%;
  width: 220px;
}
#ctrl {
  display: none;
}
.icon-wenjianshangchuan {
  font-size: 20px;
  margin-bottom: 20px;
  margin-top: 20px;
  transition: all 0.5s;
  color: rgb(64,158,255);
}
.icon-wenjianshangchuan:hover {
  color: rgb(64,158,255);
  transform: scale(1.2);
}
.icon-shuaxin {
  transition: all 0.5s;
}
.icon-shuaxin:hover {
  color: rgb(64,158,255);
}
.mylabel {
  margin-right: 10px;
}
.list {
  text-align: center;
  cursor: pointer;
  width: auto;
  height: 20px;
  background-color: rgb(236, 244, 255);
  position: relative;
  margin-bottom: 10px;
}
.list-number:hover::after {
  width: 100%;
  background: rgb(64,158,255);
}
.list-number::after {
  position: absolute;
  content: "";
  width: 0;
  height: 100%;
  top: 0;
  left: 0;
  border-radius: 2px 2px 0 0;
  transition: 0.4s;
  z-index: -1;
}
.list:hover * {
  color: #ecf4ff !important;
}
.list-number {
  z-index: 1;
}
.list-number {
  overflow: hidden;
  margin: 0 auto;
  width: auto;
  height: 20px;
  position: relative !important;
  border-radius: 2px !important;
}
.swiper-img {
  width: 100%;
  overflow: hidden;
  position: relative;
  max-height: 280px;
  min-height: 240px;
  .swiper-lbtn {
    opacity: 0.6;
    left: 0;
    height: 100%;
    z-index: 100;
    position: absolute;
  }
  .swiper-rbtn {
    right: 0;
    opacity: 0.6;
    height: 100%;
    z-index: 100;
    position: absolute;
  }
  .img-box {
    margin-top: 40px;
    flex: 1;
    height: 200px;
    height: 100%;
    overflow: hidden;
    opacity: 0.7;
    margin-right: 10px;
    justify-content: space-between;
  }
}
.render-box {
  .render-img {
    width: 100%;
    // max-height: 800px;
    overflow: hidden;
  }
  .render-style {
    height: auto;
  }
}
.cl-checkbox {
  display: block;
  height: auto;
  text-align: center;
}
.style-words {
  line-height: 30px;
  height: 30px;
  transition: all 0.4s;
  margin-bottom: 10px;
  cursor: pointer;
  font-size: 18px;
}
.style-title {
    text-align: center;
  font-size: 22px;
  font-family: '幼圆', sans-serif;
  font-weight: 600;
  margin-bottom: 20px;
}
.style-words:hover {
  color: white;
}

.normal:hover {
  background-color: rgb(64,158,255);
}
.field:hover {
  background-image: linear-gradient(#9be15d, #00e3ae 100%);
}
.ocean:hover {
  background-image: linear-gradient(135deg, #3c8ce7 10%, #00eaff 100%);
}
.lava:hover {
  background-image: linear-gradient(135deg, #fdd819 10%, #e80505 100%);
}
.desert:hover {
  background-image: linear-gradient(135deg, #ffa8a8 10%, #fcff00 100%);
}
.active-normal {
  background-color: rgb(64,158,255);
}
.active-field {
  background-image: linear-gradient(#9be15d, #00e3ae 100%);
}
.active-ocean {
  background-image: linear-gradient(135deg, #3c8ce7 10%, #00eaff 100%);
}
.active-lava {
  background-image: linear-gradient(135deg, #fdd819 10%, #e80505 100%);
}
.active-desert {
  background-image: linear-gradient(135deg, #ffa8a8 10%, #fcff00 100%);
}
.img0 {
  transition: all 0.4s;
}
.img1 {
  transition: all 0.5s;
}
.img2 {
  transition: all 0.6s;
}
.img3 {
  transition: all 0.7s;
}
.img4 {
  transition: all 0.8s;
}
.icon-fankui {
  font-size: 24px;
  color: skyblue;
}
.feed-back {
  border: 3px solid #0f2d2d;
  width: 880px;
  margin-bottom: 30px;
  border-radius: 5px;
  font-size: 18px;
  font-family: Microsoft YaHei;
}
.render-words{
  margin-top: 15px;
  margin-bottom: 10px;
  font-size: 25px;
  text-align: center;
  font-weight: 600;
   font-family: Microsoft JhengHei UI, sans-serif;
}
.clearQ{
  position: absolute;
  left: 5px;
  top: 10%;
  z-index: 100
}
.his-words {
  margin-top: 15px;
  margin-bottom: 10px;
  font-size: 22px;
  text-align: center;
  font-weight: 600;
  font-family: Microsoft JhengHei UI, sans-serif;
}
.render-border{
  border: rgb(64, 158, 255) 15px solid;
}
</style>
