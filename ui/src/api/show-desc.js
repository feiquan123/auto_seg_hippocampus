import request from '@/utils/request'

export function showDesc(count) {
  return request({
    url: '/api/show_desc',
    method: 'post',
    data: {
      count: count
    }
  })
}
