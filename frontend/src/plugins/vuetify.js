import "@fortawesome/fontawesome-free/css/all.css";
import "material-design-icons-iconfont/dist/material-design-icons.css";
import "@mdi/font/css/materialdesignicons.css";
import Vue from "vue";
import Vuetify from "vuetify/lib";
import colors from "vuetify/lib/util/colors";

import VueGoogleCharts from "vue-google-charts";

Vue.use(VueGoogleCharts);
Vue.use(Vuetify);

export default new Vuetify({
  icons: {
    iconfont: "fa" || "md" || "mdi",
  },
  theme: {
    themes: {
      light: {
        background: colors.grey.lighten2,
      },
      dark: {
        background: colors.shades.white,
      },
    },
  },
});
