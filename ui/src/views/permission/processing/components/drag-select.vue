<template>
  <div class="components-container">
    <el-drag-select v-model="value" style="width:500px;" placeholder="请选择模型" @change="selectChange">
      <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value" />
    </el-drag-select>
  </div>
</template>

<script>
import ElDragSelect from '@/components/DragSelect' // base on element-ui

export default {
  name: 'DragSelectArch',
  components: { ElDragSelect },
  props: {
    selectChange: {
      type: Function,
      default: () => ({})
    }
  },
  data() {
    return {
      value: ['DeepResUNet'],
      options: [{
        value: 'DeepResUNet',
        label: 'DeepResUNet'
      }, {
        value: 'HybridResUNet',
        label: 'HybridResUNet'
      }, {
        value: 'ONet',
        label: 'ONet'
      }]
    }
  }
}
</script>

<style lang="scss" scoped>
.components-container {
  display: inline-block;
  // margin: 30px 50px;
  // position: relative;
}
</style>
