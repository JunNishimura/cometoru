import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

//---------- Base Components ----------//
import BaseBoard from '@/components/UI/BaseBoard.vue';
import BaseCard from '@/components/UI/BaseCard.vue';
import BaseButton from '@/components/UI/BaseButton.vue';
import BaseTab from '@/components/UI/BaseTab.vue';
import BaseTag from '@/components/UI/BaseTag.vue';
import vuetify from './plugins/vuetify';

//---------- Font Awesome ----------//
import { library } from '@fortawesome/fontawesome-svg-core';
import { faUser, faUsers, faMapMarkerAlt, faCheck, faEnvelope, faUniversity, faBookOpen, faTimes, faTag, faSearch, faComments, faDollarSign, faDownload, faHome} from '@fortawesome/free-solid-svg-icons';
import { faFacebookSquare, faTwitterSquare } from '@fortawesome/free-brands-svg-icons';
import { faEdit, faLightbulb, faGrinTongueWink } from '@fortawesome/free-regular-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
library.add(faUser, faUsers, faMapMarkerAlt, faCheck, faEnvelope, faUniversity, faBookOpen, faTimes, faTag, faSearch, faComments, faDollarSign, faDownload, faHome,
            faFacebookSquare, faTwitterSquare, 
            faEdit, faLightbulb, faGrinTongueWink);
Vue.component('FontAwesomeIcon', FontAwesomeIcon);

Vue.config.productionTip = false
// add base components
Vue.component('BaseBoard', BaseBoard);
Vue.component('BaseCard', BaseCard);
Vue.component('BaseButton', BaseButton);
Vue.component('BaseTab', BaseTab);
Vue.component('BaseTag', BaseTag);

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
