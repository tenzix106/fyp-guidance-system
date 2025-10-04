<script lang="ts">
import { createRouter, createWebHistory } from 'vue-router';
import Index from '@/pages/Index.vue';
import NotFound from '@/pages/NotFound.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Index,
  },
  // ADD ALL CUSTOM ROUTES ABOVE THE CATCH-ALL "*" ROUTE
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: NotFound,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});


</script>