import request from '@/utils/request'

export function getRoutes() {
  return request({
    url: '/auto_seg_hippocampus/routes',
    method: 'get'
  })
}

export function getRoles() {
  return request({
    url: '/auto_seg_hippocampus/roles',
    method: 'get'
  })
}

export function addRole(data) {
  return request({
    url: '/auto_seg_hippocampus/role',
    method: 'post',
    data
  })
}

export function updateRole(id, data) {
  return request({
    url: `/auto_seg_hippocampus/role/${id}`,
    method: 'put',
    data
  })
}

export function deleteRole(id) {
  return request({
    url: `/auto_seg_hippocampus/role/${id}`,
    method: 'delete'
  })
}
