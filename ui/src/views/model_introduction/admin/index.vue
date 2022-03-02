<template>
  <div class="introduction-editor-container">
    <github-corner class="github-corner" />

    <introduction-panel @handleSetIntroductionData="handleSetIntroductionData" />

    <el-row style="background:#fff;padding:16px 16px 0;margin-bottom:32px;">
      <div class="title">
        {{ title }}
      </div>
      <div class="msg">
        <div class="msg-pre">
          <introduction v-if="this.type === 'introduction'" />
          <theories-technology v-if="this.type === 'theories_technology'" />
          <image-preprocessing v-if="this.type === 'image_preprocessing'" />
          <bt-seg v-if="this.type === 'bt_seg'" />
        </div>
      </div>
    </el-row>
  </div>
</template>

<script>
import GithubCorner from '@/components/GithubCorner'
import IntroductionPanel from './components/IntroductionPanel'

// 文案内容
import Introduction from './components/introduction/Introduction'
import TheoriesTechnology from './components/introduction/TheoriesTechnology'
import ImagePreprocessing from './components/introduction/ImagePreprocessing'
import BtSeg from './components/introduction/BtSeg'

const titles = {
  introduction: Introduction,
  theories_technology: TheoriesTechnology,
  image_preprocessing: ImagePreprocessing,
  bt_seg: BtSeg
}

export default {
  name: 'ModelIntroductionAdmin',
  components: {
    GithubCorner,
    IntroductionPanel,

    Introduction,
    TheoriesTechnology,
    ImagePreprocessing,
    BtSeg
  },
  data() {
    return {
      title: Introduction.title,
      type: Introduction.type
    }
  },
  methods: {
    handleSetIntroductionData(type) {
      this.title = titles[type].title
      this.type = titles[type].type
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
  text-indent: 2em;
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
