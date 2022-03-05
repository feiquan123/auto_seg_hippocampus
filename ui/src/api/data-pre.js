import request from '@/utils/request'

export function dataPre(data) {
  return request({
    url: '/auto_seg_hippocampus/data/pre',
    method: 'post',
    data: {
      dataPrePath: data
    }
  })
}
