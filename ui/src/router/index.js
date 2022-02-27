import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

export const constantRoutes = [{
  path: '/redirect',
  component: Layout,
  hidden: true,
  children: [{
    path: '/redirect/:path(.*)',
    component: () =>
      import ('@/views/redirect/index')
  }]
},
{
  path: '/login',
  component: () =>
    import ('@/views/login/index'),
  hidden: true
},
{
  path: '/auth-redirect',
  component: () =>
    import ('@/views/login/auth-redirect'),
  hidden: true
},
{
  path: '/404',
  component: () =>
    import ('@/views/error-page/404'),
  hidden: true
},
{
  path: '/401',
  component: () =>
    import ('@/views/error-page/401'),
  hidden: true
},
{
  path: '/',
  component: Layout,
  redirect: '/model_introduction',
  children: [{
    path: 'model_introduction',
    component: () =>
      import ('@/views/model_introduction/index'),
    name: 'ModelIntroduction',
    meta: { title: '模型介绍', icon: 'documentation', affix: true }
  }]
},
{
  path: '/profile',
  component: Layout,
  redirect: '/profile/index',
  hidden: true,
  children: [{
    path: 'index',
    component: () =>
      import ('@/views/profile/index'),
    name: 'Profile',
    meta: { title: '用户信息', icon: 'user', noCache: true }
  }]
}
]

/**
 * asyncRoutes
 * the routes that need to be dynamically loaded based on user roles
 */
export const asyncRoutes = [{
  path: '/permission',
  component: Layout,
  redirect: '/permission/processing',
  alwaysShow: true, // will always show the root menu
  name: 'Permission',
  meta: {
    title: '脑肿瘤分割',
    icon: 'example',
    roles: ['admin', 'editor'] // you can set roles in root nav
  },
  children: [{
    path: 'processing',
    component: () =>
      import ('@/views/permission/processing/index'),
    name: 'Processing',
    meta: {
      title: '脑肿瘤分割流程处理',
      roles: ['admin']
    }
  }]
},

{
  path: '/error',
  component: Layout,
  redirect: 'noRedirect',
  name: 'ErrorPages',
  meta: {
    title: '页面丢失',
    icon: '404'
  },
  children: [{
    path: '401',
    component: () =>
      import ('@/views/error-page/401'),
    name: '401',
    meta: { title: '页面丢失401', noCache: true }
  },
  {
    path: '404',
    component: () =>
      import ('@/views/error-page/404'),
    name: '404',
    meta: { title: '页面丢失404', noCache: true }
  }
  ]
},

{
  path: '/error-log',
  component: Layout,
  children: [{
    path: 'log',
    component: () =>
      import ('@/views/error-log/index'),
    name: 'ErrorLog',
    meta: { title: '错误日志', icon: 'bug' }
  }]
},

{
  path: '/excel',
  component: Layout,
  redirect: '/excel/export-excel',
  name: 'Excel',
  meta: {
    title: 'Excel',
    icon: 'excel'
  },
  children: [{
    path: 'export-excel',
    component: () =>
      import ('@/views/excel/export-excel'),
    name: 'ExportExcel',
    meta: { title: 'Export Excel' }
  },
  {
    path: 'export-selected-excel',
    component: () =>
      import ('@/views/excel/select-excel'),
    name: 'SelectExcel',
    meta: { title: 'Export Selected' }
  },
  {
    path: 'export-merge-header',
    component: () =>
      import ('@/views/excel/merge-header'),
    name: 'MergeHeader',
    meta: { title: 'Merge Header' }
  },
  {
    path: 'upload-excel',
    component: () =>
      import ('@/views/excel/upload-excel'),
    name: 'UploadExcel',
    meta: { title: 'Upload Excel' }
  }
  ]
},

{
  path: '/zip',
  component: Layout,
  redirect: '/zip/download',
  alwaysShow: true,
  name: 'Zip',
  meta: { title: 'Zip', icon: 'zip' },
  children: [{
    path: 'download',
    component: () =>
      import ('@/views/zip/index'),
    name: 'ExportZip',
    meta: { title: 'Export Zip' }
  }]
},

{
  path: '/pdf',
  component: Layout,
  redirect: '/pdf/index',
  children: [{
    path: 'index',
    component: () =>
      import ('@/views/pdf/index'),
    name: 'PDF',
    meta: { title: 'PDF', icon: 'pdf' }
  }]
},
{
  path: '/pdf/download',
  component: () =>
    import ('@/views/pdf/download'),
  hidden: true
},

{
  path: '/theme',
  component: Layout,
  children: [{
    path: 'index',
    component: () =>
      import ('@/views/theme/index'),
    name: 'Theme',
    meta: { title: 'Theme', icon: 'theme' }
  }]
},

{
  path: '/clipboard',
  component: Layout,
  children: [{
    path: 'index',
    component: () =>
      import ('@/views/clipboard/index'),
    name: 'ClipboardDemo',
    meta: { title: 'Clipboard', icon: 'clipboard' }
  }]
},

{
  path: 'external-link',
  component: Layout,
  children: [{
    path: 'https://github.com/PanJiaChen/vue-element-admin',
    meta: { title: 'External Link', icon: 'link' }
  }]
},

// 404 page must be placed at the end !!!
{ path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
