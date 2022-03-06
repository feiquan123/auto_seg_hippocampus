# auto_seg_hippocampus
Brain tumor automatic segmentation system

## 前序准备
你需要在本地安装
1. [node v16.10.0](http://nodejs.org/)
2. [git](https://git-scm.com/)
3. [python 3.9.9](https://www.python.org/getit/)

## 开发
```js
# 克隆项目
git clone https://github.com/feiquan123/auto_seg_hippocampus

```

### 后端开发
```sh
# 进入项目目录
cd auto_seg_hippocampus

# 创建虚拟环境
python -m venv venv

# 使用虚拟环境
source ./venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 启动后端项目
python service/main.py
```

### 前端开发
```sh
# 进入项目目录
cd auto_seg_hippocampus/ui

# 安装依赖
npm install

# 建议不要直接使用 cnpm 安装依赖，会有各种诡异的 bug。可以通过如下操作解决 npm 下载速度慢的问题
npm install --registry=https://registry.npm.taobao.org

# 启动服务
npm run dev
```
浏览器访问 http://localhost:9528/

#### 发布

```bash
# 构建测试环境
npm run build:stage

# 构建生产环境
npm run build:prod
```

##### 其它

```bash
# 预览发布环境效果
npm run preview

# 预览发布环境效果 + 静态资源分析
npm run preview -- --report

# 代码格式检查
npm run lint

# 代码格式检查并自动修复
npm run lint -- --fix
```

## 模型下载
```
模型路径：auto_seg_hippocampus/service/models/hublock1_DeepResUNet_woDS

百度网盘下载：
链接: https://pan.baidu.com/s/1pyzrks0IhLT47FZKUATQVQ?pwd=62mq 提取码: 62mq 
```