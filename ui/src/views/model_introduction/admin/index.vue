<template>
  <div class="introduction-editor-container">
    <github-corner class="github-corner" />

    <panel-group @handleSetIntroductionData="handleSetIntroductionData" />

    <el-row style="background:#fff;padding:16px 16px 0;margin-bottom:32px;">
      <div class="title">
        {{ title }}
      </div>
      <div class="msg">
        <pre class="msg-pre"> {{ msg }} </pre>
      </div>
    </el-row>
  </div>
</template>

<script>
import GithubCorner from '@/components/GithubCorner'
import PanelGroup from './components/IntroductionPanel'

// 文案内容
import introduction from './components/introduction/introduction'
import theories_technology from './components/introduction/theories_technology'
import image_preprocessing from './components/introduction/image_preprocessing'
import bt_seg from './components/introduction/bt_seg'

const msgs = {
  introduction: introduction,
  theories_technology: theories_technology,
  image_preprocessing: image_preprocessing,
  bt_seg: bt_seg
}

export default {
  name: 'ModelIntroductionAdmin',
  components: {
    GithubCorner,
    PanelGroup
  },
  data() {
    return {
      title: msgs.introduction.title,
      msg: msgs.introduction.msg
    }
  },
  methods: {
    handleSetIntroductionData(type) {
      this.title = msgs[type].title
      this.msg = msgs[type].msg
    }
  }
}
</script>

<style lang="scss" scoped>
.title {
  word-break:break-all;
  text-align:center;
  padding:16px 16px 0px;
  font-weight:bold;
  color:#103838;
}

.msg{
  line-height:2.5em;
  word-break:break-all;
  padding: 16px;
  color:#185757;
}

.msg-pre{
  white-space:pre-wrap;
  word-wrap:normal;
}

.introduction-editor-container {
  padding: 32px;
  background-color: rgb(240, 242, 245);
  position: relative;

  .github-corner {
    position: absolute;
    top: 0px;
    border: 0;
    right: 0;
  }

  .chart-wrapper {
    background: #fff;
    padding: 0px 16px 16px 0px;
    margin-bottom: 32px;
  }
}

@media (max-width:1024px) {
  .chart-wrapper {
    padding: 8px;
  }
}
</style>
