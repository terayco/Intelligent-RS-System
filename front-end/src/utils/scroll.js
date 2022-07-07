//https://zhuanlan.zhihu.com/p/462298873
export default function retScroll (data) {
    data.scrollReveal.reveal('#reveal-top', {
      // 动画的时长
      duration: 600,
      // 延迟时间
      delay: 300,
      // 动画开始的位置，'bottom', 'left', 'top', 'right'
      origin: 'left',
      // 回滚的时候是否再次触发动画
      reset: true,
      // 延时执行方式（always（一直延时执行），once（只延时执行一次），onload（只在加载时延时执行））
      useDelay: 'once',
      // 在移动端是否使用动画
      mobile: true,
      // 滚动的距离，单位可以用%，rem等
      distance: '10px',
      // 其他可用的动画效果
      opacity: 0.01,
      // 执行速度 线性函数啥的
      easing: 'cubic-bezier(0.5, 0, 0, 1)',
      // 执行方式（缩放）
      scale: 0.9,
      // 使用执行之前的回调函数
      beforeReveal: function (ele) {
     
       }
    }),
      data.scrollReveal.reveal('#fade-in',{
        // 动画的时长
        duration: 900,
        // 延迟时间
        delay: 450,
        // 动画开始的位置，'bottom', 'left', 'top', 'right'
        origin: 'bottom',
        // 回滚的时候是否再次触发动画
        reset: false,
        // 延时执行方式（always（一直延时执行），once（只延时执行一次），onload（只在加载时延时执行））
        // // useDelay: 'onload',
        // 滚动的距离，单位可以用%，rem等
        distance: '300px',
        // 其他可用的动画效果
        opacity: 0.6,
        // 执行速度 线性函数啥的
        easing: 'ease-in-out',
        // 执行方式（缩放）
        // scale: 0.9,
        viewportFactor:0.33,
        // 使用执行之前的回调函数
        beforeReveal: function (ele) {
          
         }
      }),
      data.scrollReveal.reveal('#fade-in2',{
        // 动画的时长
        duration: 900,
        // 延迟时间
        delay: 600,
        // 动画开始的位置，'bottom', 'left', 'top', 'right'
        origin: 'bottom',
        // 回滚的时候是否再次触发动画
        reset: false,
        // 延时执行方式（always（一直延时执行），once（只延时执行一次），onload（只在加载时延时执行））
        // // useDelay: 'onload',
        // 滚动的距离，单位可以用%，rem等
        distance: '300px',
        // 其他可用的动画效果
        opacity: 0.6,
        // 执行速度 线性函数啥的
        easing: 'ease-in-out',
        // 执行方式（缩放）
        // scale: 0.9,
        viewportFactor:0.33,
        // 使用执行之前的回调函数
        beforeReveal: function (ele) {
          
         }
      }),
      data.scrollReveal.reveal('#fade-in3',{
        // 动画的时长
        duration: 900,
        // 延迟时间
        delay: 750,
        // 动画开始的位置，'bottom', 'left', 'top', 'right'
        origin: 'bottom',
        // 回滚的时候是否再次触发动画
        reset: false,
        // 延时执行方式（always（一直延时执行），once（只延时执行一次），onload（只在加载时延时执行））
        // // useDelay: 'onload',
        // 滚动的距离，单位可以用%，rem等
        distance: '300px',
        // 其他可用的动画效果
        opacity: 0.6,
        // 执行速度 线性函数啥的
        easing: 'ease-in-out',
        // 执行方式（缩放）
        // scale: 0.9,
        viewportFactor:0.33,
        // 使用执行之前的回调函数
        beforeReveal: function (ele) {
          
         }
      }),
      data.scrollReveal.reveal('#go-big1',{
        // 动画的时长
        duration: 1000,
        // 延迟时间
        delay: 600,
        origin: 'bottom',
        reset: false,
        easing: 'ease-in-out',
        scale: 0.2,
    
      }),
      data.scrollReveal.reveal('#go-big2',{
        // 动画的时长
        duration: 1000,
        // 延迟时间
        delay: 750,
        origin: 'bottom',
        reset: false,
        easing: 'ease-in-out',
        scale: 0.2,
    
      }),
      data.scrollReveal.reveal('#go-big3',{
        // 动画的时长
        duration: 1000,
        // 延迟时间
        delay: 900,
        origin: 'bottom',
        reset: false,
        easing: 'ease-in-out',
        scale: 0.2,
    
      })    
  }