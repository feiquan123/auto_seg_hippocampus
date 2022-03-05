
<template>
  <div>
    <p>
      在Windows系统下，多模态脑肿瘤自动分割系统搭建需要的依赖环境有node.js、vue.js。在Visual Studio Code集成环境下进行编码调试。所用的版本分别是node -v16.14.0，npm -v8.3.1,vue -v2.9.6。node在搭建vue的开发环境之前，需要先下载node.js，vue的运行是要依赖于node的npm的管理工具来实现。
    </p>
    <p>
      打开命令提示符窗口，cd到存放系统的文件路径下，输入npm run dev命令，等待几秒钟，打开浏览器，首先是用户登录界面，默认账号是admin，密码是admin_pwd,登录成功后，进入主界面，用户可以使用该系统。
    </p>

  </div>
</template>

<script>
const title = '系统使用说明'
export default {
  title: title,
  type: 'bt_seg'
}
</script>
