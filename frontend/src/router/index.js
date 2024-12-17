import { createRouter, createWebHistory } from 'vue-router';
import HelloWorld from '../components/HelloWorld.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HelloWorld, // This should render the HelloWorld component
  },
  // Additional routes can be added here
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router; 