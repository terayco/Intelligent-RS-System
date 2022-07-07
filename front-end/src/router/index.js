import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

const Home = () => import('@/views/Home.vue')
const DetectChanges = () => import('@/views/mainfun/DetectChanges.vue')
const DetectTargets = () => import('@/views/mainfun/DetectTargets.vue')
const ObtainTargets = () => import('@/views/mainfun/ObtainTargets.vue')
const Classify = () => import('@/views/mainfun/Classify.vue')

const History = () => import('@/views/history/History.vue')
const FeedBackHis = () => import("@/views/history/FeedBackHis.vue")

const VisualData = () => import('@/views/VisualData.vue')
const LogReg = () => import('@/views/LogReg.vue')

const Intro = () => import('@/views/introduce/Intro.vue')
const RemoteSense = () => import('@/views/introduce/RemoteSense.vue')
const Intelligent = () => import('@/views/introduce/Intelligent.vue')
const Technology = () => import('@/views/introduce/Technology.vue')

const BackEnd = () => import('@/views/backend/BackEnd.vue')
const FeedBackList = () =>import('@/views/backend/FeedBackList.vue')
const UserList = () => import('@/views/backend/UserList.vue')
const NotFound = () => import('@/views/NotFound.vue')
let whiteList = ['login', 'remotesense', 'intelligent', 'introduce', 'technology']
const routes = [
  {
    path: '/',
    redirect: '/remotesense'
  },
  {

    path: '/login',
    name: 'login',
    component: LogReg

  },
  {
    path: '/backend',
    redirect:'/userlist',
    name: 'backend',
    component: BackEnd,
    children:[{
      path:'/userlist',
      name:'userlist',
      component:UserList
    },
    {
      path:'/feedbacklist',
      name:'feedbacklist',
      component:FeedBackList
    }
  ]
  },
  {
    path: '/introduce',
    // redirect:'/intelligent',
    name: 'introduce',
    component: Intro,
    children: [{
      path: '/remotesense',
      name: 'remotesense',
      component: RemoteSense
    }, {
      path: '/intelligent',
      name: 'intelligent',
      component: Intelligent
    }, {
      path: '/technology',
      name: 'technology',
      component: Technology
    },

    ]
  },
  {
    path: '/home',
    name: 'home',
    component: Home,
    children: [
       {
        path: '/detectchanges',
        name: 'detectchanges',
        component: DetectChanges,

      }, {
        path: '/detecttargets',
        name: 'detecttargets',
        component: DetectTargets
      }, {
        path: '/obtaintargets',
        name: 'obtaintargets',
        component: ObtainTargets
      }, {
        path: '/classify',
        name: 'classify',
        component: Classify
      }, {
        path: '/history',
        name: 'history',
        component: History,
      }, {
        path: '/feedbackhistory',
        name: 'feedbackhistory',
        component: FeedBackHis
      }
      , {
        path: '/visualdata',
        name: 'visualdata',
        component: VisualData
      },
    ]
  },
  {
    path: "/:pathMatch(.*)*",
      name: 'notfound',
      component: NotFound
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  if (whiteList.indexOf(to.name) == -1 && !token)
   { next({ path: '/remotesense' })}
  else {next()}
})
export default router
