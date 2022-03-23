<template>
  <div class="data-preprocessing-container">
    <el-tabs type="border-card" style="width:100%;">
      <el-tab-pane label="数据预处理">
        <el-row>
          <p>
            本实验采用公开的brats18和brats19数据集，将brats18数据按照8:2的比例分开分别用于模型的训练和验证，用brats19数据中额外增加的50例数据用于模型的测试。<br>
            <img :src="实验预处理步骤" alt="实验预处理步骤" class="data-pre-img">
          </p>
          <div />
        </el-row>

        <el-row>
          <span class="span-desc"> 预处理文件夹路径 </span>
          <el-input
            ref="data_pre_dir"
            v-model="dataPreDir"
            type="text"
            placeholder="请粘贴绝对路径"
            class="input-with-select"
            style="width:400px; max-width:100%;"
            @input="dataPreDirInputInput"
          />
          <el-button type="primary" icon="el-icon-document" :disabled="dataPreDisabled" @click="dataPreBtnChange">开始预处理</el-button>
          <div v-if="this.showPreLoading" v-loading="loadingPre" />
        </el-row>

        <el-button type="primary" icon="el-icon-document" @click="showDescClick">展示描述</el-button>
        <el-button type="primary" icon="el-icon-document" @click="showPicClick">{{ picName }}</el-button>

        <img v-if="picHidden" :src="实验预处理步骤" alt="实验预处理步骤" class="data-pre-img">
        <img v-if="!picHidden" :src="分割模型" alt="分割模型" class="data-pre-img">

        <div v-if="this.showDesc">
          <el-row>
            <div>{{ showDescCount }}</div>
            <p>
              <pre>注 </pre>
            </p>
          </el-row>
        </div>

      </el-tab-pane>

      <el-tab-pane label="模型预测">
        <el-row>
          <p>
            首先将原始brats数据进行标准化、切片裁剪等预处理，然后输入到GAN中得到分割结果，通过评价指标来分析实验结果。本章主要对GAN中的生成模型进行改进从而提高分割精确度。
          </p>
        </el-row>

        <div v-if="this.dataPreRequestSuccess">
          <el-row>
            <span class="span-desc">数据预处理结果集</span>
            <el-input
              v-model="dataPreOutPutPath"
              class="input-with-select"
              style="width:400px; max-width:100%;"
              disabled
            />
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
import { showDesc } from '@/api/show-desc'

export default {
  name: 'Processing',
  components: { DragSelect },
  data() {
    return {
      selectValue: ['DeepResUNet'],

      dataPreRequestSuccess: false,
      dataPreDir: '',
      dataPreDisabled: true,
      dataPreOutPutPath: '',
      showPreLoading: false,
      loadingPre: {},

      modelTestingRequestSuccess: false,
      modelTestingOutputData: '',
      showTestLoading: false,
      loadingTest: {},
      实验预处理步骤: require('/public/image/实验预处理步骤.jpg'),
      分割模型: require('/public/image/分割模型.png'),

      showDesc: false,
      showDescCount: 0,
      picHidden: true,
      picName: '实验预处理步骤'
    }
  },
  methods: {
    showPicClick(e) {
      this.picHidden = !this.picHidden
      if (this.picHidden) {
        this.picName = '实验预处理步骤'
      } else {
        this.picName = '分割模型'
      }
    },
    showDescClick(e) {
      showDesc(this.showDescCount).then(res => {
        this.showDescCount = res.data.count
        this.showDesc = true
      })
    },
    dataPreDirInputInput(e) {
      this.dataPreDisabled = e.length === 0
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

      if (this.modelTestingRequestSuccess) {
        this.modelTestingRequestSuccess = false
      }
      // 数据预处理
      dataPre(this.dataPreDir).then(res => {
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
    dataPreRequestSuccessAction(data) {
      this.dataPreRequestSuccess = true
      this.dataPreOutPutPath = data.dataPreOutPutPath
      this.$message({
        message: '数据预处理成功',
        type: 'success',
        duration: 1500
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

<style lang="scss" scoped>
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
  font-size:11px;
  color:#131441;
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

</style>
