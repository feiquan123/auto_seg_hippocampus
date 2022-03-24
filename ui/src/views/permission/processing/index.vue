<template>
  <div class="data-preprocessing-container">
    <el-tabs type="border-card" style="width:100%;">
      <el-tab-pane label="数据预处理说明">
        <el-row>
          <p>
            <pre>注：测试数据中的文件夹结构如下【2个HGG病例，1个LGG病例】，其中 HGG、LGG 文件夹下最多只允许放 5 个病例
        .
      ├── HGG
      │   ├── BraTS19_CBICA_AAB_1
      │   │   ├── BraTS19_CBICA_AAB_1_flair.nii.gz
      │   │   ├── BraTS19_CBICA_AAB_1_seg.nii.gz
      │   │   ├── BraTS19_CBICA_AAB_1_t1.nii.gz
      │   │   ├── BraTS19_CBICA_AAB_1_t1ce.nii.gz
      │   │   └── BraTS19_CBICA_AAB_1_t2.nii.gz
      │   └── BraTS19_CBICA_AAL_1
      │       ├── BraTS19_CBICA_AAL_1_flair.nii.gz
      │       ├── BraTS19_CBICA_AAL_1_seg.nii.gz
      │       ├── BraTS19_CBICA_AAL_1_t1.nii.gz
      │       ├── BraTS19_CBICA_AAL_1_t1ce.nii.gz
      │       └── BraTS19_CBICA_AAL_1_t2.nii.gz
      └── LGG
          └── BraTS19_TCIA09_254_1
              ├── BraTS19_TCIA09_254_1_flair.nii.gz
              ├── BraTS19_TCIA09_254_1_seg.nii.gz
              ├── BraTS19_TCIA09_254_1_t1.nii.gz
              ├── BraTS19_TCIA09_254_1_t1ce.nii.gz
              └── BraTS19_TCIA09_254_1_t2.nii.gz
                  </pre>
          </p>
        </el-row>
      </el-tab-pane>

      <el-tab-pane label="标准化/切片处理">
        <div class="left1">
          <span>标准化</span> <br><br>
          <el-row>
            <el-input ref="data_pre_dir" v-model="dataPreDir1" type="text" placeholder="请粘贴绝对路径" class="input-with-select" style="width:400px; max-width:100%;" @input="dataPreDirInputInput" />
            <el-button type="primary" icon="el-icon-document" :disabled="dataPreDisabled1" @click="dataPreBtnChange">开始数据标准化</el-button>
            <div v-if="this.showPreLoading" v-loading="loadingPre" />
          </el-row>
        </div>
        <div class="right1">
          <span>切片</span>
          <br>
          <br>
          <el-row>
            <el-input v-model="dataPreOutPutPath2" class="input-with-select" style="width:400px; max-width:100%;" disabled />
            <el-button type="primary" icon="el-icon-document" :disabled="dataPreDisabled2" @click="dataPreBtnChange2">开始数据切片</el-button>
            <div v-if="this.showPreLoading" v-loading="loadingPre" />
          </el-row>
        </div>
        <div v-if="this.secondSuccess">
          <div v-if="this.dataPreRequestSuccess">
            <el-row>
              <br>
              <hr>
              <br>
              <el-button type="primary" icon="el-icon-document" @click="showPicClick">{{ picName }}</el-button>
              <img v-if="picHidden" :src="标准化" alt="标准化" class="data-pre-img">
              <img v-if="!picHidden" :src="切片" alt="切片" class="data-pre-img">
            </el-row>
          </div>
        </div>
      </el-tab-pane>

      <el-tab-pane label="裁剪">
        <div class="left1">
          <span>Canny边缘检测</span>
          <br>
          <br>
          <!-- <div v-if="this.dataPreRequestSuccess"></div> -->
          <el-row>
            <el-input v-model="dataPreOutPutPath3" class="input-with-select" style="width:400px; max-width:100%;" disabled />
            <el-button type="primary" icon="el-icon-document" :disabled="dataPreDisabled3" @click="dataPreBtnChange3">开始数据边缘检测</el-button>
            <div v-if="this.showTestLoading" v-loading="loadingTest" />
          </el-row>
          <br>
          <br>
        </div>

        <div class="right1">
          <span>确定最小裁剪框</span>
          <br>
          <br>
          <!-- <div v-if="this.dataPreRequestSuccess"></div> -->
          <el-row>
            <el-input v-model="dataPreOutPutPath4" class="input-with-select" style="width:400px; max-width:100%;" disabled />
            <el-button type="primary" icon="el-icon-document" :disabled="dataPreDisabled4" @click="dataPreBtnChange4">开始确定最小裁剪框</el-button>
            <div v-if="this.showTestLoading" v-loading="loadingTest" />
          </el-row>
          <br>
          <br>
        </div>
        <br>
        <hr>
        <br>
        <div v-if="this.fourSuccess">
          <div v-if="this.dataPreRequestSuccess">
            <el-row>
              <el-button type="primary" icon="el-icon-document" @click="showPicClick2">{{ picName2 }}</el-button>
              <img v-if="picHidden2" :src="边缘检测" alt="边缘检测" class="data-pre-img">
              <img v-if="!picHidden2" :src="裁剪框" alt="裁剪框" class="data-pre-img">
            </el-row>
          </div>
        </div>
      </el-tab-pane>

      <el-tab-pane label="通道连接">
        <span>通道连接</span>
        <br>
        <br>
        <!-- <div v-if="this.dataPreRequestSuccess"></div> -->
        <el-row>
          <span class="span-desc"> 数据存放路径 </span>
          <el-input v-model="dataPreOutPutPath5" class="input-with-select" style="width:400px; max-width:100%;" disabled />
          <el-button type="primary" icon="el-icon-document" :disabled="dataPreDisabled5" @click="dataPreBtnChange5">开始数据连接</el-button>
          <div v-if="this.showTestLoading" v-loading="loadingTest" />
        </el-row>
        <br>
        <br>
      </el-tab-pane>

      <el-tab-pane label="模型预测">
        <div v-if="this.dataPreRequestSuccess">
          <el-row>
            <span class="span-desc">数据预处理结果集</span>
            <el-input v-model="dataPreOutPutPath" class="input-with-select" style="width:400px; max-width:100%;" disabled />
          </el-row>
          <br>
          <br>
          <el-row>
            <span class="span-desc">请选择模型</span>
            <drag-select :select-change="selectChange" />
            <el-button type="primary" icon="el-icon-document" :disabled="!dataPreRequestSuccess" @click="modelTestingBtnChange">开始模型预测</el-button>
            <div v-if="this.showTestLoading" v-loading="loadingTest" />
          </el-row>
        </div>

        <div v-if="this.modelTestingRequestSuccess">
          <br>
          <hr>
          <br>
          <el-row>
            <span class="span-desc"> {{ selectValue[0] }} 模型预测结果</span>
            <el-input
              v-model="modelTestingOutputData"
              class="input-with-select"
              style="width:400px; max-width:100%;"
              disabled
            />
          </el-row>
          <br>
          <div class="chart-container">
            <table class="table">
              <caption><h4>不同分割方法对比分析（dice系数）</h4></caption>
              <th>方法</th><th>WT</th><th>TC</th><th>ET</th>
              <tr>
                <td>U-Net</td><td>0.80</td><td>0.63</td><td>0.60</td>
              </tr>
              <tr>
                <td>SegAN</td><td>0.85</td><td>0.70</td><td>0.66</td>
              </tr>
              <tr>
                <td>Resnet</td><td>0.87</td><td>0.74</td><td>0.78</td>
              </tr>
              <tr>
                <td>本文方法</td><td>0.84</td><td>0.86</td><td>0.78</td>
              </tr>
            </table>
          </div>
        </div>
      </el-tab-pane>

    </el-tabs>

  </div>
</template>

<script>
import DragSelect from './components/drag-select.vue'
import { dataPre } from '@/api/data-pre'
import { dataTest } from '@/api/data-test'

export default {
  name: 'Processing',
  components: { DragSelect },
  data() {
    return {
      selectValue: ['DeepResUNet'],
      fourSuccess: false,
      secondSuccess: false,
      dataPreRequestSuccess: false,
      dataPreDir1: '',
      dataPreDisabled1: true,
      dataPreDisabled2: true,
      dataPreDisabled3: true,
      dataPreDisabled4: true,
      dataPreDisabled5: true,
      dataPreOutPutPath: '',
      dataPreOutPutPath2: '',
      dataPreOutPutPath3: '',
      dataPreOutPutPath4: '',
      dataPreOutPutPath5: '',
      showPreLoading: false,
      loadingPre: {},

      modelTestingRequestSuccess: false,
      modelTestingOutputData: '',
      showTestLoading: false,
      loadingTest: {},
      标准化: require('@/assets/标准化.png'),
      切片: require('@/assets/切片.png'),
      picHidden: true,
      picName: '标准化结果',
      边缘检测: require('@/assets/边缘检测.png'),
      裁剪框: require('@/assets/裁剪框.png'),
      picName2: '边缘检测结果',
      picHidden2: true
    }
  },
  methods: {
    showPicClick(e) {
      this.picHidden = !this.picHidden
      if (this.picHidden) {
        this.picName = '标准化结果'
      } else {
        this.picName = '切片结果'
      }
    },
    showPicClick2(e) {
      this.picHidden2 = !this.picHidden2
      if (this.picHidden2) {
        this.picName2 = '边缘检测结果'
      } else {
        this.picName2 = '确定最小裁剪框结果'
      }
    },
    dataPreDirInputInput(e) {
      this.dataPreDisabled1 = e.length === 0
    },

    dataPreBtnChange() {
      this.loadingPre = this.$loading({
        lock: true,
        text: '数据预处理中',
        spinner: 'el-icon-loading',
        fullscreen: true,
        background: 'rgba(0, 0, 0, 0.7)'
      })
      this.showPreLoading = true
      // 数据预处理
      dataPre(this.dataPreDir1).then(res => {
        this.dataPreRequestSuccessAction(res.data)
        this.showPreLoading = false
        this.loadingPre.close()
        this.dataPreOutPutPath2 = this.dataPreOutPutPath + '/standard'
        this.dataPreDisabled2 = false
        this.PicNoDisplay1 = false
      }).catch(error => {
        console.log(error)
        this.$message({
          message: '数据预处理失败',
          type: 'error',
          duration: 2000
        })
        this.showPreLoading = false
        this.loadingPre.close()
      })
    },
    dataPreRequestSuccessAction(data) {
      this.dataPreRequestSuccess = true
      this.dataPreOutPutPath = data.dataPreOutPutPath
      this.$message({
        message: '数据预处理成功',
        type: 'success',
        duration: 1500
      })
    },
    dataPreBtnChange2() {
      this.loadingPre = this.$loading({
        lock: true,
        text: '数据预处理中',
        spinner: 'el-icon-loading',
        fullscreen: true,
        background: 'rgba(0, 0, 0, 0.7)'
      })
      this.showPreLoading = true
      // 数据预处理
      dataPre(this.dataPreDir1).then(res => {
        this.dataPreRequestSuccessAction(res.data)
        this.showPreLoading = false
        this.loadingPre.close()
        this.dataPreOutPutPath3 = this.dataPreOutPutPath + '/slice'
        this.dataPreDisabled3 = false
        this.secondSuccess = true
      }).catch(error => {
        console.log(error)
        this.$message({
          message: '数据预处理失败',
          type: 'error',
          duration: 2000
        })
        this.showPreLoading = false
        this.loadingPre.close()
      })
    },

    dataPreBtnChange3() {
      this.loadingPre = this.$loading({
        lock: true,
        text: '数据预处理中',
        spinner: 'el-icon-loading',
        fullscreen: true,
        background: 'rgba(0, 0, 0, 0.7)'
      })
      this.showPreLoading = true

      // 数据预处理
      dataPre(this.dataPreDir1).then(res => {
        this.dataPreRequestSuccessAction(res.data)
        this.showPreLoading = false
        this.loadingPre.close()
        this.dataPreOutPutPath4 = this.dataPreOutPutPath + '/edge_detection'
        this.dataPreDisabled4 = false
      }).catch(error => {
        console.log(error)
        this.$message({
          message: '数据预处理失败',
          type: 'error',
          duration: 2000
        })
        this.showPreLoading = false
        this.loadingPre.close()
      })
    },

    dataPreBtnChange4() {
      this.loadingPre = this.$loading({
        lock: true,
        text: '数据预处理中',
        spinner: 'el-icon-loading',
        fullscreen: true,
        background: 'rgba(0, 0, 0, 0.7)'
      })
      this.showPreLoading = true
      // 数据预处理
      dataPre(this.dataPreDir1).then(res => {
        this.dataPreRequestSuccessAction(res.data)
        this.showPreLoading = false
        this.loadingPre.close()
        this.dataPreOutPutPath5 = this.dataPreOutPutPath + '/rectangular_outline'
        this.dataPreDisabled5 = false
        this.fourSuccess = true
      }).catch(error => {
        console.log(error)
        this.$message({
          message: '数据预处理失败',
          type: 'error',
          duration: 2000
        })
        this.showPreLoading = false
        this.loadingPre.close()
      })
    },

    dataPreBtnChange5() {
      this.loadingPre = this.$loading({
        lock: true,
        text: '数据预处理中',
        spinner: 'el-icon-loading',
        fullscreen: true,
        background: 'rgba(0, 0, 0, 0.7)'
      })
      this.showPreLoading = true

      // 数据预处理
      dataPre(this.dataPreDir1).then(res => {
        this.dataPreRequestSuccessAction(res.data)
        this.showPreLoading = false
        this.loadingPre.close()
      }).catch(error => {
        console.log(error)
        this.$message({
          message: '数据预处理失败',
          type: 'error',
          duration: 2000
        })
        this.showPreLoading = false
        this.loadingPre.close()
      })
    },

    selectChange(e) {
      this.selectValue = e
    },

    modelTestingBtnChange() {
      // 模型测试
      if (this.selectValue.length === 0) {
        this.$message({
          message: '模型类型不能为空',
          type: 'error',
          duration: 1500
        })
        return
      }

      if (this.selectValue.length > 1) {
        this.$message({
          message: '模型类型同时只能选一个',
          type: 'error',
          duration: 1500
        })
        return
      }

      this.loadingTest = this.$loading({
        lock: true,
        text: '模型测试中',
        spinner: 'el-icon-loading',
        fullscreen: true,
        background: 'rgba(0, 0, 0, 0.7)'
      })
      this.showTestLoading = true
      this.dataCannyRequestSuccess = true

      dataTest(this.dataPreOutPutPath, this.selectValue[0]).then(res => {
        this.modelTestingSuccessAction(res.data)
        this.showTestLoading = false
        this.loadingTest.close()
      }).catch(error => {
        console.log(error)
        this.$message({
          message: '模型测试失败',
          type: 'error',
          duration: 2000
        })
        this.showTestLoading = false
        this.loadingTest.close()
      })
    },
    modelTestingSuccessAction(data) {
      this.modelTestingRequestSuccess = true
      this.modelTestingOutputData = data.dataTestOutputPath

      this.$message({
        message: '模型测试完成',
        type: 'success',
        duration: 1500
      })
    }
  }
}
</script>

<style lang= "scss" scoped>
.data-preprocessing-container {
  margin: 50px;

  p{
    background: #eef1f6;
    padding: 8px 24px;
    margin-bottom: 20px;
    border-radius: 2px;
    display: block;
    line-height: 32px;
    font-size: 16px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif;
    color: #2c3e50;
  }
}

.chart-container{
  position: relative;
  width: 100%;
  height: calc(100vh - 84px);
  margin: 10px;
  padding: 10px 10px;
}

.span-desc{
  color: rgb(26, 138, 212);
  font-weight: 400;
  padding: 0 10px;
  width: 185px;
  display: inline-block;
  text-align: right;
}

.data-pre-img{
  padding: 10px 200px;
}

.table {
  font-family: verdana,arial,sans-serif;
  font-size: 11px;
  color: #131441;
  border-width: 1px;
  border-color: #666666;
  border-collapse: collapse;
  width: 50%;
  text-align: center;

  th {
    border-width: 1px;
    padding: 8px;
    border-style: solid;
    border-color: #0a205e;
    background-color: #74b5cf;
  }
  td {
    border-width: 1px;
    padding: 8px;
    border-style: solid;
    border-color: #666666;
    background-color: #d2f0f7;
  }
}
.left1 {
color: rgb(26, 138, 212);
width: 50%;
display: inline-block;
}
.right1 {
color: rgb(26, 212, 119);
width: 50%;
display: inline-block;
}

</style>
