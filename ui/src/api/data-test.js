import request from '@/utils/request'

export function dataTest(data) {
  return request({
    url: '/auto_seg_hippocampus/data/test',
    method: 'post',
    data: {
      dataPreOutPutPath: data
    }
  })
}
