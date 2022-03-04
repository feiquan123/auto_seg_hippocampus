
<template>
  <div>
    <div style="width: 100%;height:1000px; position: relative; ">

      <img :src="分割模型" alt="分割模型.png" style="width: 729px; height: 753px;position: absolute; left:50%; top: 15%; margin-left: -350px;margin-top: -120px;">
    </div>
  </div>

</template>

<script>
const title = `分割模型`
export default {
  title: title,
  type: 'theories_technology',
  data() {
    return {
      分割模型: require('/public/image/分割模型.png')

    }
  }
}
</script>
