import request from '@/utils/request'

export function dataTest(data) {
  return request({
    url: '/api/data/test',
    method: 'post',
    data: {
      dataPreOutPutPath: data
    }
  })
}
