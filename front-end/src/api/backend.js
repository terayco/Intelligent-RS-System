import {request} from  "@/api/request.js"

export function getUserList(page,limit,username){
    return request({
        url:"/api/user/list",
        method:'GET',
        params:{
            page,
            limit,
            username
        }
    })
}

export function changeUser(data){
    return request({
        url:'/api/user/resetPwd',
        method:"POST",
        data
    })
}

export function deleteMore(data){
    return request({
        url:'api/user/batchRemove',
        method:'DELETE',
        data
    })
}