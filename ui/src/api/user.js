import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/auto_seg_hippocampus/user/login',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    url: '/auto_seg_hippocampus/user/info',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/auto_seg_hippocampus/user/logout',
    method: 'post'
  })
}
