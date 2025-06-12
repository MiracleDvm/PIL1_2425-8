import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import './assets/styles.css';
import './assets/animations.css';
import './assets/theme.css';
import './assets/responsive.css';

createApp(App)
  .use(router)
  .use(store)
  .mount('#app');
