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
            @input="dataPreDirInputInput($event)"
          />
          <el-button type="primary" icon="el-icon-document" :disabled="dataPreDisabled" @click="dataPreBtnChange(dataPreDir,$event)">开始预处理</el-button>
        </el-row>
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
              v-model="dataPreOutputData"
              class="input-with-select"
              style="width:400px; max-width:100%;"
              disabled
            />
            <el-button type="primary" icon="el-icon-document" :disabled="!dataPreRequestSuccess" @click="modelTestingBtnChange(dataPreOutputData,$event)">开始模型预测</el-button>
          </el-row>
        </div>

        <div v-if="this.modelTestingRequestSuccess">
          <br>
          <hr>
          <br>
          <el-row>
            <span class="span-desc">Unet 模型预测结果</span>
            <el-input
              v-model="modelUnetTestingOutputData"
              class="input-with-select"
              style="width:400px; max-width:100%;"
              disabled
            />
          </el-row>
          <br>
          <el-row>
            <span class="span-desc">ResUnet 模型预测结果</span>
            <el-input
              v-model="modelResUnetTestingOutputData"
              class="input-with-select"
              style="width:400px; max-width:100%;"
              disabled
            />
          </el-row>
          <br>
          <el-row>
            <span class="span-desc">MMIgan 模型预测结果</span>
            <el-input
              v-model="modelMMIganTestingOutputData"
              class="input-with-select"
              style="width:400px; max-width:100%;"
              disabled
            />
          </el-row>
          <br>
          <div class="chart-container">
            <model-testing-dice-chart :height="chartHeight" :width="chartWidth" />
          </div>
        </div>
      </el-tab-pane>

    </el-tabs>

  </div>
</template>

<script>
import ModelTestingDiceChart from './components/charts/ModelTestingDiceChart.vue'

export default {
  name: 'Processing',
  components: {
    ModelTestingDiceChart
  },
  data() {
    return {
      chartHeight: '400px',
      chartWidth: '100%',

      dataPreRequestSuccess: false,
      dataPreDir: '',
      dataPreDisabled: true,
      dataPreOutputData: '',

      modelTestingRequestSuccess: false,
      modelUnetTestingOutputData: '',
      modelResUnetTestingOutputData: '',
      modelMMIganTestingOutputData: '',

      实验预处理步骤: require('/public/image/实验预处理步骤.jpg')
    }
  },
  methods: {
    dataPreDirInputInput(e) {
      this.dataPreDisabled = e.length === 0
    },
    dataPreBtnChange(dir, e) {
      // 数据预处理
      // 请求成功

      const data = '/tmp/pre_dataset'
      this.dataPreRequestSuccessAction(data)
    },
    dataPreRequestSuccessAction(data) {
      this.dataPreRequestSuccess = true
      this.dataPreOutputData = data
      this.$message({
        message: '数据预处理成功',
        type: 'success',
        duration: 1500
      })
    },

    modelTestingBtnChange(dir, e) {
      // 模型测试
      console.log('modelTestingBtnChange')
      // 请求成功

      const data = {
        Unet: '/tmp/unet_model_testing',
        ResUnet: '/tmp/resunet_model_testing',
        MMIgan: '/tmp/mmigan_model_testing'
      }
      this.modelTestingSuccessAction(data)
    },
    modelTestingSuccessAction(data) {
      this.modelTestingRequestSuccess = true
      this.modelUnetTestingOutputData = data.Unet
      this.modelResUnetTestingOutputData = data.ResUnet
      this.modelMMIganTestingOutputData = data.MMIgan

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
</style>
