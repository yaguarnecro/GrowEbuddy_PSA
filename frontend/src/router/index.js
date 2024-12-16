import { createRouter, createWebHistory } from 'vue-router';
import HelloWorld from '../components/HelloWorld.vue'; // Adjust the path as necessary

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HelloWorld, // This will render the HelloWorld component at the root path
  },
  // You can add more routes here as needed
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router; 