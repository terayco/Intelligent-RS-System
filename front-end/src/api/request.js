import axios from "axios"
import router from '../router'
import store from '@/store' 
import global from '@/global'
import { hideFullScreenLoading} from '@/utils/loading'

export function request(config) {
  const instance = axios.create({
    baseURL:global.BASEURL
  })
  instance.interceptors.request.use(
    
    (config) => {
 
      const token = localStorage.getItem('token')
      if (token) config.headers.Authorization = `Bearer ${token}`;
      return config
    },
    (error) => Promise.reject(error),
  )

  instance.interceptors.response.use(
    (response) => {

     
      if (response.data.code == 2) {
        alert('未登录！')
        router.push('login')
      };
      return response
    },
    ({ response }) => {
      hideFullScreenLoading('#load')
      hideFullScreenLoading(".changes-box");
      hideFullScreenLoading(".fb-box")
      alert('网络异常，请稍后重试！')
      return Promise.reject(error)
    },
  )
  return instance(config)
}

