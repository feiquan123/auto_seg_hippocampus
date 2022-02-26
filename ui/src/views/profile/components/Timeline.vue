<template>
  <div class="block">
    <el-timeline>
      <el-timeline-item v-for="(item,index) of timeline" :key="index" :timestamp="item.timestamp" placement="top">
        <el-card>
          <h4>{{ item.title }}</h4>
          <p>{{ item.content }}</p>
        </el-card>
      </el-timeline-item>
    </el-timeline>
  </div>
</template>

<script>
export default {
  data() {
    return {
      timeline: [
        {
          timestamp: '2019年9月20日',
          title: '研究生',
          content: '美国麻省理工学院 2019年9月20日 08:46'
        },
        {
          timestamp: '2015年9月20日',
          title: '大学',
          content: '清华大学 2015年9月20日 10:46'
        },
        {
          timestamp: '2012年9月21日',
          title: '高中',
          content: '清华附中国际部 2012年9月21日 20:46'
        },
        {
          timestamp: '2009年1月27日',
          title: '初中',
          content: '北京市第四中学 2009年1月27日 09:46'
        },
        {
          timestamp: '2003年9月3日',
          title: '小学',
          content: '北京市海淀区七一小学 2003年9月3日 20:46'
        }
      ]
    }
  }
}
</script>
