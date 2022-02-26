<template>
  <div class="user-activity">
    <div class="post">
      <div class="user-block">
        <img class="img-circle" :src="'https://wpimg.wallstcn.com/fb57f689-e1ab-443c-af12-8d4066e202e2.jpg'+avatarPrefix">
        <span class="username">文迪</span>
        <span class="description">前沿分子生物学技术(9) Science | 新方法揭示细胞内蛋白质超微结构 2022-03-10 17:32</span>
      </div>
      <p>
        近日，由来自霍华德·休斯医学研究所（The Howard Hughes Medical Institute, HHMI）Janelia实验室的Harald Hess领导的小组在Science上发表了题为‘Correlativethree-dimensional super-resolution and block-face electron microscopy of wholevitreously frozen cells’的文章。研究者们结合使用低温超分辨荧光显微镜和聚焦离子束扫描电子显微镜（FIB-SEM）来观察整个细胞的蛋白质超微结构的三维关系。两种成像方式的融合使得能够在拥挤的细胞内环境中对形态复杂的结构进行识别和三维分割。
      </p>
      <div class="user-images">
        <el-carousel :interval="6000" type="card" height="220px">
          <el-carousel-item v-for="item in carouselImages" :key="item">
            <img :src="item+carouselPrefix" class="image">
          </el-carousel-item>
        </el-carousel>
      </div>
      <ul class="list-inline">
        <li><span class="link-black text-sm"><i class="el-icon-share" /> 分享</span></li>
        <li>
          <span class="link-black text-sm">
            <svg-icon icon-class="like" /> 点赞</span>
        </li>
      </ul>
    </div>
    <div class="post">
      <div class="user-block">
        <img class="img-circle" :src="'http://www.qbitai.com/wp-content/uploads/2019/06/200-100x100.jpg'+avatarPrefix">
        <span class="username text-muted">白交</span>
        <span class="description">小分子3D结构被AI整明白了 2022-02-23 13:28:30
        </span>
      </div>
      <p>
        此次百度聚焦的研究，是小分子化合物性质预测。
        简单来说，通过小分子结构来预测其性质，帮助药物研发的早期探索，从而解决该领域成本高、时间长、成功率低等难题。
        早在2018年，百度就正式启动了计算生物方向的研究。
        著名的RNA二级结构开源算法LinearFold，将新冠预测从原来的55分钟提速至27秒（接近120倍），就是百度的研究成果之一。
        2020年12月，百度正式将自己研究的一系列生物计算相关技术进行了集成，发布了螺旋桨（PaddleHelix）。
        这是一个囊括了各种各样“AI+计算生物”开源工具的生物计算平台，基于百度飞桨框架开发，可以被用于药物研发、疫苗设计和精准医疗等领域。
      </p>
      <ul class="list-inline">
        <li>
          <span class="link-black text-sm">
            <i class="el-icon-share" />
            分享
          </span>
        </li>
        <li>
          <span class="link-black text-sm">
            <svg-icon icon-class="like" />
            点赞
          </span>
        </li>
      </ul>
    </div>
    <div class="post">
      <div class="user-block">
        <img class="img-circle" :src="'http://upload.idcquan.com/2019/0320/1553047920613.jpg'">
        <span class="username text-muted">孙雨</span>
        <span class="description">医学AI如何从前沿技术到临床应用?  2022-02-20 10:51</span>
      </div>
      <p>
        医学人工智能可加速药物从研发向临床转化。一种新药从研发到上市至少经历10——15年的时间，平均成本26亿美元。其中，药物研发的时间成本高达11.6亿美元。人工智能在药物研发上能够应用于新药发现阶段与临床实验阶段，在靶点筛选、药物发掘、药物优化、服药依从性管理、药物晶型预测等环节。借助人工智能将大幅缩短新药的研发时间，节省大量人工成本，提高新药研发的效率。
      </p>
      <ul class="list-inline">
        <li>
          <span class="link-black text-sm">
            <i class="el-icon-share" />
            分享
          </span>
        </li>
        <li>
          <span class="link-black text-sm">
            <svg-icon icon-class="like" />
            点赞
          </span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
const avatarPrefix = '?imageView2/1/w/80/h/80'
const carouselPrefix = '?imageView2/2/h/440'

export default {
  data() {
    return {
      carouselImages: [
        'https://img1.17img.cn/17img/images/202001/noimg/775b649e-a426-4670-8069-b079cce58d46.gif',
        'https://pic4.zhimg.com/80/v2-9dca618ec56857954ee140102b861d83_1440w.jpg',
        'https://pic1.zhimg.com/80/v2-1c1445f6bb2044d34ba1c45ecf2c6770_1440w.jpg',
        'https://pic3.zhimg.com/80/v2-283129f9d77b1bc8e21a4993296066e2_1440w.jpg'
      ],
      avatarPrefix,
      carouselPrefix
    }
  }
}
</script>

<style lang="scss" scoped>
.user-activity {
  .user-block {

    .username,
    .description {
      display: block;
      margin-left: 50px;
      padding: 2px 0;
    }

    .username{
      font-size: 16px;
      color: #000;
    }

    :after {
      clear: both;
    }

    .img-circle {
      border-radius: 50%;
      width: 40px;
      height: 40px;
      float: left;
    }

    span {
      font-weight: 500;
      font-size: 12px;
    }
  }

  .post {
    font-size: 14px;
    border-bottom: 1px solid #d2d6de;
    margin-bottom: 15px;
    padding-bottom: 15px;
    color: #666;
    line-height: 1.7em;

    .image {
      width: 100%;
      height: 100%;

    }

    .user-images {
      padding-top: 20px;
    }
  }

  .list-inline {
    padding-left: 0;
    margin-left: -5px;
    list-style: none;

    li {
      display: inline-block;
      padding-right: 5px;
      padding-left: 5px;
      font-size: 13px;
    }

    .link-black {

      &:hover,
      &:focus {
        color: #999;
      }
    }
  }

}

.box-center {
  margin: 0 auto;
  display: table;
}

.text-muted {
  color: #777;
}
</style>
