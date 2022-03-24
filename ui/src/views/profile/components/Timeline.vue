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
          timestamp: '2019年9月15日',
          title: '研究生',
          content: '太原理工大学 信息与计算机学院 软件工程 医学图像处理'
        },
        {
          timestamp: '2015年9月15日',
          title: '本科生',
          content: '山西大同大学 教育科学与技术学院 数字媒体技术'
        },
        {
          timestamp: '2012年9月1日',
          title: '高中',
          content: '天镇一中 308  理科 袁权老师'
        },
        {
          timestamp: '2009年9月1日',
          title: '初中',
          content: '天镇二中 '
        },
        {
          timestamp: '2003年9月1日',
          title: '小学',
          content: '西北小学'
        }
      ]
    }
  }
}
</script>
