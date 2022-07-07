//https://blog.csdn.net/HH18700418030/article/details/120976087裁剪参考
import { showFullScreenLoading, hideFullScreenLoading } from "@/utils/loading";
function submitUpload(funtype) {
    this.finish(funtype)
  }
  function   handleRemove(file, fileList) {
    console.log(file, fileList)
  }
  function   handlePreview(file) {
 
    //   let data = window.URL.createObjectURL(new Blob([file]));
    //   this.option.img = data;
  }
  //放大/缩小
  function   changeScale(num) {
 
    num = num || 1
    this.$refs.cropper.changeScale(num)
  }
  //坐旋转
  function  rotateLeft() {
 
    this.$refs.cropper.rotateLeft()
  }
  //右旋转
  function  rotateRight() {

    this.$refs.cropper.rotateRight()
  }
  //上传图片（点击上传按钮）
  function  finish(funtype) {
    funtype = '地物分类'
    // 输出
      this.$refs.cropper.getCropData(data => {
        // this.model = true
        // this.modelSrc = data
        const File = base64toFile(data,this.fileList[this.fileList.length-1].name)
        let formData = new FormData()
        formData.append('files',File);
        formData.append("type", '地物分类');
        this.createSrc(formData).then((res) => {
          this.uploadSrc.list = res.data.data.map((item) => {
            return item.src;
          });
          if (this.afterImg.length >= 20) {
            this.$confirm("上传图片过多，是否压缩?在此期间不能进行其他操作", "提示", {
              confirmButtonText: "确定",
              cancelButtonText: "取消",
              type: "warning",
            })
              .then(() => {
                this.goCompress(type)
              }).catch(()=>{
    
              })
          }
          if (funtype == '目标提取') {
            this.obtainTargetsUpload(this.uploadSrc).then((res) => {
              this.fileList = []
              hideFullScreenLoading("#load")
              this.$message.success("上传成功！");
            });
          }
          else if (funtype == '地物分类') {
            this.classifyUpload(this.uploadSrc).then((res) => {
              this.fileList = []
              hideFullScreenLoading("#load")
              this.$message.success("上传成功！");
            });
          }
          else if (funtype == '目标检测') {
            this.detectTargetsUpload(this.uploadSrc).then((res) => {
              this.fileList = []
              hideFullScreenLoading("#load")
              this.$message.success("上传成功！");
            });
          }
          this.cutVisible = false
        });
      })
    
  }
  // 实时预览函数
  function  realTime(data) {
 
    this.previews = data
  }
  function imgLoad(msg) {
  
  
  }
  function  base64toFile (dataurl, filename) {
    let arr = dataurl.split(',')
    let mime = arr[0].match(/:(.*?);/)[1]
    let suffix = mime.split('/')[1]
    let bstr = atob(arr[1])
    let n = bstr.length
    let u8arr = new Uint8Array(n)
    while (n--) {
        u8arr[n] = bstr.charCodeAt(n)
    }
    return new File([u8arr], `${filename}.${suffix}`, {
        type: mime
    })
}
 
// let file = base64toFile('你需要转成file的base64','filename') //这个file就是base64转成的file文件
  export {submitUpload,handleRemove,handlePreview,changeScale, rotateLeft,rotateRight,finish,realTime,imgLoad}