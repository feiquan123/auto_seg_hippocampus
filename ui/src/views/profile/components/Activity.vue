<template>
  <div class="user-activity">
    <div class="post">
      <div class="user-block">
        <img class="img-circle" :src="'https://wpimg.wallstcn.com/fb57f689-e1ab-443c-af12-8d4066e202e2.jpg'+avatarPrefix">
        <span class="username">研一</span>
        <span class="description">如何确定自己的研究方向</span>
      </div>
      <p>
        研一的生活就是适应陌生的环境，适应生活方式的不同，上课不是主要，研究才是重点。每天三分之一的时间是在实验室度过。完成老师交代的任务，翻看近三年的国内外研究现状。在此过程了解自己感兴趣的研究内容是什么，确定它的研究意义，发现研究中存在的不足，因为这是你创新的来源。
      </p>
      <div class="user-images">
        <el-carousel ref="carousel" :interval="6000" type="card" height="220px" class="lun_imgs">
          <el-carousel-item v-for="item in imgs" :key="item.url" class="lun_img">
            <img :src="item.url" width="100%">
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
        <span class="username text-muted">研二</span>
        <span class="description">如何准备开题
        </span>
      </div>
      <p>
        继续文献阅读，这次是精读，在每读一篇文献，搞清楚它解决的问题是什么，再将它所说的复现。在复现过程中，可以在原有的基础上进行增删改操作。记录并保留每次实验的结果。
        搞清楚是什么烟瘾导致实验结果不同。那么你研究的创新点就有了。同时，理论和实验也都有了。这时可以开题。
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
        <span class="username text-muted">研三</span>
        <span class="description">如何找工作和准备毕业</span>
      </div>
      <p>
        找与计算机相关工作的人，研二下学期开始需要在相关网站或其他地方开始刷题，找一种自己喜欢的语言写代码，找一份简历模板，发现自己的不足，在研二下弥补自己的不足。
        研三上开始投简历找工作。再尔开始准备自己的大论文。总结自己研一和研二自己研究的东西。
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
      imgs: [
        { url: require('@/assets/1j.png') },
        { url: require('@/assets/bg.png') },
        { url: require('@/assets/logo.png') },
        { url: require('@/assets/sadmas.png') }
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
