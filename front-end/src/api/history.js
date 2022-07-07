import {request} from  "@/api/request.js"

export function historyGetPage(page,limit,type){
    return request({
        method:'GET',
        url:'/api/history/list',
        params:{
            page:page,
            limit:limit,
            type:type
        }
    })
}

export function historyDelete(data){
    return request({
        method:'DELETE',
        url:'api/history/batchRemove',
        data
    })
}

export function fbGetPage(page,limit){
    return request({
        method:'GET',
        url:'/api/analysis/feedback/list',
        params:{
            page:page,
            limit:limit
        }
    })
}

export function goFeedBack(data){
    return request({
        method:'POST',
        url:'/api/analysis/feedback',
        data
    })
}