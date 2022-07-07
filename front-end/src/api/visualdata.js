import {request} from  "@/api/request.js"

export function getVisualData(){
    return request({
        url:'/api/report/',
        method:'GET'
    })
}

