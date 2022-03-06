import request from '@/utils/request'

export function dataTest(dataPreOutPutPath, arch) {
  return request({
    url: '/api/data/test',
    method: 'post',
    data: {
      dataPreOutPutPath: dataPreOutPutPath,
      arch: arch
    }
  })
}
