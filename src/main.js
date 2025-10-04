import './assets/main.css'

import { createApp } from 'vue';
import { VueQueryPlugin } from '@tanstack/vue-query'
import App from './App.vue'
import router from '../src/router'
import './index.css'

const app = createApp(App);

app.use(router);
app.use(VueQueryPlugin);


app.mount('#app');
