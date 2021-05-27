<template>
  <div id="app">
    <Header v-if="!isLoginPage"></Header>
    <Aside id="aside" v-if="!isLoginPage"></Aside>
    <div id="main">
      <router-view />
    </div>
    <Footer v-if="!isLoginPage"></Footer>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from "@/views/_common/Header.vue";
import Aside from "@/views/_common/Aside.vue";
import Footer from "@/views/_common/Footer.vue";

export default {
  name: "App",
  components: {
    Header,
    Aside,
    Footer,
  },
  computed: {
    isLoginPage() {
      return this.$route.path == "/login";
    },
  },
};
</script>

<style>
#main {
  flex: 1;
}

#app {
  display: grid;
  grid-template-columns: 15% 85%;
  grid-template-rows: 10vh auto 10vh;
  grid-template-areas:
    "aside nav"
    "aside view"
    "aside footer";
}

#header {
  grid-area: nav;
}

#aside {
  grid-area: aside;
  justify-self: left;
  position: sticky;
  top: 0;
}

#main {
  grid-area: view;
  padding: 1rem 2rem;
  height: 100%;
}

#main > * {
  max-width: 100%;
  height: 100%;
}

#footer {
  grid-area: footer;
}
</style>
