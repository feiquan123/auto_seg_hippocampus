<template>
  <div class="data-preprocessing-container">
    <el-tabs type="border-card" style="width:100%;">
      <el-tab-pane label="预处理数据集">
        <el-row>
          <p>
            本实验采用公开的brats18和brats19数据集，将brats18数据按照8:2的比例分开分别用于模型的训练和验证，用brats19数据中额外增加的50例数据用于模型的测试。<br>
            <br>实验数据预处理步骤如下：
            <ol>
              <li>标准化多模态</li>
              <li>裁剪</li>
              <li>对各模态及其GT数据进行切片，并抛弃（剔除）无病灶切片</li>
              <li>将T1、T1c、T2、FLAIR模态的相应切片沿通道维度连接，用作MMIgan模型的多通道输入</li>
            </ol>
          </p>
        </el-row>

        <el-row>
          <span class="span-desc"> 文件夹路径 </span>
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

      <el-tab-pane label="模型训练">
        <el-row>
          <p>
            为了提高对脑肿瘤的更小区域（肿瘤核心和增强肿瘤）分割的准确率，本文提出了以生成对抗模型为基本架构的网络模型。提出的模型（MMIGAN）主要由生成模型和对抗模型组成。生成模型由Residual Block 3残差结构和跳跃连接构成。对抗网络采用卷积神经网络，对生成模型生成的分割结果和专家分割结果进行判别。经过对抗模型的损失计算不断优化生成模型，使生成模型达到分割脑肿瘤的最优状态
          </p>
        </el-row>

        <div v-if="this.dataPreRequestSuccess">
          <el-row>
            <span class="span-desc">数据集预处理结果</span>
            <el-input
              v-model="dataPreOutputData"
              class="input-with-select"
              style="width:400px; max-width:100%;"
              disabled
            />
            <el-button type="primary" icon="el-icon-document" :disabled="!dataPreRequestSuccess" @click="modelTrainingBtnChange(dataPreOutputData,$event)">开始模型训练</el-button>
          </el-row>

          <div v-if="this.modelTrainingRequestSuccess">
            <br>
            <hr>
            <br>
            <span class="span-desc">模型预测结果</span>
            <div class="chart-container">
              <model-train-loss-chart :height="chartHeight" :width="chartWidth" />
              <br>
              <model-train-iou-chart :height="chartHeight" :width="chartWidth" />
            </div>
          </div>
        </div>
      </el-tab-pane>

      <el-tab-pane label="模型预测">
        <el-row>
          <p>
            首先将原始brats数据进行标准化、切片裁剪等预处理，然后输入到GAN中得到分割结果，通过评价指标来分析实验结果。本章主要对GAN中的生成模型进行改进从而提高分割精确度。
          </p>
        </el-row>

        <div v-if="this.modelTrainingRequestSuccess">
          <el-row>
            <span class="span-desc">模型训练结果</span>
            <el-input
              v-model="modelTrainingOutputData"
              class="input-with-select"
              style="width:400px; max-width:100%;"
              disabled
            />
            <el-button type="primary" icon="el-icon-document" :disabled="!modelTrainingRequestSuccess" @click="modelTestingBtnChange(dataPreDir,$event)">开始模型预测</el-button>
          </el-row>
        </div>

        <div v-if="this.modelTestingRequestSuccess">
          <br>
          <hr>
          <br>
          <span class="span-desc">模型预测结果</span>
          <el-input
            v-model="modelTestingOutputData"
            class="input-with-select"
            style="width:400px; max-width:100%;"
            disabled
          />
          <div class="chart-container">
            <model-testing-dice-chart :height="chartHeight" :width="chartWidth" />
          </div>
        </div>
      </el-tab-pane>

    </el-tabs>

  </div>
</template>

<script>
import ModelTrainLossChart from './components/charts/ModelTrainLossChart.vue'
import ModelTrainIouChart from './components/charts/ModelTrainIouChart.vue'
import ModelTestingDiceChart from './components/charts/ModelTestingDiceChart.vue'

export default {
  name: 'Processing',
  components: {
    ModelTrainLossChart,
    ModelTrainIouChart,
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

      modelTrainingRequestSuccess: false,
      modelTrainingOutputData: '',

      modelTestingRequestSuccess: false,
      modelTestingOutputData: ''
    }
  },
  methods: {
    dataPreDirInputInput(e) {
      this.dataPreDisabled = e.length === 0
    },
    dataPreBtnChange(dir, e) {
      // 数据预处理请求

      this.dataPreRequestSuccessAction('/tmp/data_preprocessing', e)
    },
    dataPreRequestSuccessAction(data, e) {
      this.dataPreRequestSuccess = true
      this.dataPreOutputData = data
      this.$message({
        message: '数据预处理成功',
        type: 'success',
        duration: 1500
      })
    },

    modelTrainingBtnChange(dir, e) {
      // 模型训练

      this.modelTrainingSuccessAction('/tmp/model_training', e)
    },
    modelTrainingSuccessAction(data, e) {
      this.modelTrainingRequestSuccess = true
      this.modelTrainingOutputData = data
      this.$message({
        message: '模型训练完成',
        type: 'success',
        duration: 1500
      })
    },

    modelTestingBtnChange(dir, e) {
      // 模型测试
      console.log('modelTestingBtnChange')
      this.modelTestingSuccessAction('/tmp/mode_testing')
    },
    modelTestingSuccessAction(data, e) {
      this.modelTestingRequestSuccess = true
      this.modelTestingOutputData = data
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
}
</style>
