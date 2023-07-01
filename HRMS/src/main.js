import Vue from 'vue'
import App from './App.vue'
import ElementUI  from 'element-ui';
import '../src/style/element-ui-reset.scss' 


Vue.config.productionTip = false;
Vue.use(ElementUI)

import store from "@/store";
import router from '@/router';

import '@/style/index.scss';


new Vue({
  render: h => h(App),
  store,
  router,
}).$mount('#app')
