import {request} from  "@/api/request.js"

export function getNews(page,limit,type){
    return request({
        url:'/api/home/news',
        method:'GET',
        params:{
            page,
            limit,
            type
        }
    })
}
