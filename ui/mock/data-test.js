const dataTestOutputPath = '/tmp/data_test_output'

const data = {
    Unet: {
        name: "Unet",
        path: dataTestOutputPath + "/Unet",
    },
    ResUnet: {
        name: "ResUnet",
        path: dataTestOutputPath + "/ResUnet",
    },
    MMIgan: {
        name: "MMIgan",
        path: dataTestOutputPath + "/MMIgan",
    }
}

module.exports = [{
    // data test
    url: '/auto_seg_hippocampus/data/test',
    type: 'post',
    response: config => {
        const { dataPreOutPutPath } = config.body

        return {
            code: 20000,
            data: data
        }
    }
}]