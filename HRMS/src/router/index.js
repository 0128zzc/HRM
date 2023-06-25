import Vue from 'vue';
import VueRouter from 'vue-router'

Vue.use(VueRouter);

import Layout from '@/layout'


export let routes = [
    {
        path: '/',
        redirect: '/file-upload',
        meta: {
            showInSidebar: false,
        }
    },
    {
        path: '/file-upload',
        name: "FileUpload",
        component: Layout,
        redirect: '/file-upload/index',
        children: [
            {
                path: 'index',
                component: () => import('@/views/file-upload/index.vue')
            }
        ],
        meta: {
            showInSidebar: true,
            icon: '',
            title: '简历上传',
        }
    },
    {
        path: '/statistics',
        name: 'statistics',
        component: Layout,
        redirect: '/statistics/index',
        children: [
            {
                path: 'index',
                component: () => import('@/views/statistics/index.vue'),
            }
        ],
        meta: {
            showInSidebar: true,
            icon: '',
            title: '数据分析总览',
        }
    },
    {
        path: '/candidates',
        name: 'Candidates',
        component: Layout,
        redirect: '/candidates/index',
        children: [
            {
                path: 'index',
                component: () => import('@/views/candidates'),
            }

        ],
        meta: {
            showInSidebar: true,
            icon: '',
            title: '人员匹配'
        }

    }

]
const router = new VueRouter({
    mode: 'history',
    routes: routes
})

export default router;