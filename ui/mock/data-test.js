const dataTestOutputPath = '/tmp/data_test_output'

const chartData = {
    title: "模型测试结果 DICE",
    legendNames: ["Unet", "ResUnet", "MMIgan"],
    xData: ['13:00', '13:05', '13:10', '13:15', '13:20', '13:25', '13:30', '13:35', '13:40', '13:45', '13:50', '13:55'],
    Unet: {
        name: "Unet",
        path: dataTestOutputPath + "/Unet",
        data: [220, 182, 191, 134, 150, 120, 110, 125, 145, 122, 165, 122]
    },
    ResUnet: {
        name: "ResUnet",
        path: dataTestOutputPath + "/ResUnet",
        data: [120, 110, 125, 145, 122, 165, 122, 220, 182, 191, 134, 150]
    },
    MMIgan: {
        name: "MMIgan",
        path: dataTestOutputPath + "/MMIgan",
        data: [220, 182, 125, 145, 122, 191, 134, 150, 120, 110, 165, 122]
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
            data: chartData
        }
    }
}]