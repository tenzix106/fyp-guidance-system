const routes = [
  {
    path: '/',
    component: () => import('../layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('../pages/IndexPage.vue') },
      { path: '/dashboard', component: () => import('../pages/Dashboard.vue') },
      { path: '/projects', component: () => import('../pages/Projects.vue') },
      { path: '/tasks', component: () => import('../pages/Tasks.vue') },
      { path: '/calendar', component: () => import('../pages/Calendar.vue') },
      { path: '/profile', component: () => import('../pages/Profile.vue') },
      { path: '/settings', component: () => import('../pages/Settings.vue') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('../pages/ErrorNotFound.vue')
  }
]

export default routes
