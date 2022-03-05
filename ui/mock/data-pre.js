const dataPreOutPutPath = '/tmp/data_pre_output'

module.exports = [{
    // data pre
    url: '/auto_seg_hippocampus/data/pre',
    type: 'post',
    response: config => {
        const { dataPrePath } = config.body

        return {
            code: 20000,
            data: {
                dataPreOutPutPath: dataPreOutPutPath + "/" + dataPrePath
            }
        }
    }
}]