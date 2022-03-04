
<template>
  <div>
    <div style="width: 100%;height:370px; position: relative; ">

      <img :src="判别模型" alt="判别模型.png" style="width: 739px; height: 324px;position: absolute; left:50%; top: 50%; margin-left: -390px;margin-top: -180px;">
    </div>
    <p>
      判别模型如图3（Critic）使用普通的神经网络，将预分割结果和专家分割结果分别与原图像进行点乘作为该模型的输入，采用多尺度L1 Loss函数来判别两者之间的差异，最后将梯度反馈给分割模型进行优化。
    </p>
  </div>

</template>

<script>
const title = `判别模型`
export default {
  title: title,
  type: 'image_preprocessing',
  data() {
    return {
      判别模型: require('/public/image/判别模型.png')

    }
  }
}
</script>
