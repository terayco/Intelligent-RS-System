import {request} from  "@/api/request.js"
export function create(data) {
    return request({
      method: 'POST',
      url: '/api/user/register',
      data,
    })
  }
  
  export function login(data) {
    return request({
      method: 'POST',
      url: '/api/user/login',
      data,
    })
  }

  export function loginOut(){
    return request({
      method:'POST',
      url:'/api/user/logout'
    })
  }

  export function reset(data){
    return request({
      method:'POST',
      url:'/api/user/forget',
      data
    })
  }