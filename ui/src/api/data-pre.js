import request from '@/utils/request'

export function dataPre(data) {
  return request({
    url: '/api/data/pre',
    method: 'post',
    data: {
      dataPrePath: data
    }
  })
}
