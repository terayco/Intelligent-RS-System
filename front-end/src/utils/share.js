//https://blog.csdn.net/weixin_43964148/article/details/103450960分享功能参考
import global from '@/global'
function shareToQQ() {
    //此处分享链接内无法携带图片
    const share = {
      share_url: global.HOMEURL+"/remotesense",
    };
    window.open(
      "https://connect.qq.com/widget/shareqq/index.html?url=" +
        encodeURIComponent(share.share_url)
      // "&title=" +
      // share.title +
      // "&desc=" +
      // share.desc
    );
  }
  function shareImgToQQ(imgurl) {
    //此处分享链接内无法携带图片
    const share = {
      share_url: global.HOMEURL+"/remotesense",
      share_img:imgurl,
      share_summary:'来看看这张图片'
    };
    window.open(
      "https://connect.qq.com/widget/shareqq/index.html?url=" +
        encodeURIComponent(share.share_url)+'&pics='+share.share_img+'&summary='+share.share_summary
      // "&title=" +
      // share.title +
      // "&desc=" +
      // share.desc
    );
  }
function  shareToMicroblog() {
    //自定义内容
    const share = {
      title: "我发现了一个不错的网站诶，来看看吧",
      image_url: [
        "https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg",
      ],
      share_url: global.HOMEURL+"/remotesense",
    };
    //跳转地址
    window.open(
      "https://service.weibo.com/share/share.php?url=" +
        encodeURIComponent(share.share_url) +
        "&title=" +
        share.title
      // "&pic=" +
      // share.image_url[0] +
      // "&searchPic=true"
    );
  }
  function  shareImgToMicroblog(imgurl) {
    //自定义内容
    const share = {
      title: "来看看这张图片",
      image_url: imgurl,
      share_url: global.HOMEURL+"/remotesense",
    };
    //跳转地址
    window.open(
      "https://service.weibo.com/share/share.php?url=" +
        encodeURIComponent(share.share_url) +
        "&title=" +
        share.title+'&pics='+share.share_img
      // "&pic=" +
      // share.image_url[0] +
      // "&searchPic=true"
    );
  }
function  shareToTieba() {
    const share = {
      title: "我发现了一个不错的网站诶，来看看吧",
      share_url: global.HOMEURL+"/remotesense",
      image_url: [
        "https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg",
      ],
    };
    let _shareUrl = "http://tieba.baidu.com/f/commit/share/openShareApi?";
    _shareUrl += "title=" + encodeURIComponent(share.title); //分享的标题
    _shareUrl += "&url=" + encodeURIComponent(share.share_url); //分享的链接
    _shareUrl += "&pic=" + encodeURIComponent(share.image_url[0]); //分享的图片
    window.open(
      _shareUrl
      // "_blank",
      // "width=" +
      //   _width +
      //   ",height=" +
      //   _height +
      //   ",left=" +
      //   _left +
      //   ",top=" +
      //   _top +
      //   ",toolbar=no,menubar=no,scrollbars=no,resizable=1,location=no,status=0"
    );
  }
  function    shareToWeChat() {
    //自定义内容
    const share = {
      title: "我发现了一个不错的网站诶，来看看吧",
      image_url: [
        "https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg",
      ],
      share_url: global.HOMEURL+"/remotesense",
    };
    //跳转地址
    window.open(
      "http://zixuephp.net/inc/qrcode_img.php?url=" +
        encodeURIComponent(share.share_url) +
        "&title=" +
        share.title
      // "&pic=" +
      // share.image_url[0] +
      // "&searchPic=true"
    );
  }

  export {shareToQQ,shareToMicroblog,shareToTieba,shareToWeChat,shareImgToQQ,shareImgToMicroblog}