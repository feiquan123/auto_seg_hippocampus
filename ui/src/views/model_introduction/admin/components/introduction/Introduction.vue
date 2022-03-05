
<template>
  <div>
    <div style="width: 100%;height:370px; position: relative; ">

      <img :src="总模型" alt="总模型.png" style="width: 569px; height: 365px;position: absolute; left:50%; top: 50%; margin-left: -300px;margin-top: -180px;">
    </div>
    <p>
      模型(MMIGAN)主要由生成模型和对抗模型组成。生成模型由Residual Block 3残差结构和跳跃连接构成。对抗网络采用卷积神经网络,对生成模型生成的分割结果和专家分割结果进行判别。经过对抗模型的损失计算不断优化生成模型,使生成模型达到分割脑肿瘤的最优状态。
    </p>
  </div>

</template>

<script>
const title = `总模型展示`
export default {
  title: title,
  type: 'introduction',
  data() {
    return {
      总模型: require('/public/image/总模型.png')

    }
  }
}
</script>

