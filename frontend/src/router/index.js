import { createRouter, createWebHistory } from 'vue-router'
import PhoneLoginView from '../views/PhoneLoginView.vue'
import VerifyOtpView from '../views/VerifyOtpView.vue'
import WelcomeView from '../views/WelcomeView.vue'

const routes = [
  {
    path: '/login',
    name: 'PhoneLoginView',
    component: PhoneLoginView
  },
  {
    path: '/verify-otp/:phoneNumber',
    name: 'VerifyOtpView',
    component: VerifyOtpView,
    props: true // This allows the route param to be passed as a prop
  },
  {
    path: '/welcome',
    name: 'WelcomeView',
    component: WelcomeView,
    meta: { requiresAuth: true }
  },
  {
    path: '/',
    redirect: '/login'
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  const loggedIn = localStorage.getItem('token');

  if (to.matched.some(record => record.meta.requiresAuth) && !loggedIn) {
    next('/login')
  } else {
    next()
  }
})

export default router
