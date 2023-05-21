import { createRouter, createWebHistory } from 'vue-router';

// Import your components for the stock symbols
import StocksPage from './pages/StocksPage.vue';
import HomePage from './pages/HomePage.vue';

const routes = [
    { path: '/',  component: HomePage }, // Redirect '/' to default stock symbol
    { name: "StocksPage", path: '/:symbol', component: StocksPage},
    
  ];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;