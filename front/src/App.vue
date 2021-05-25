<template>
  <div id="app">
    <Header></Header>
    <Aside id="aside"></Aside>
    <div id="main">
      <router-view />
    </div>
    <Footer></Footer>
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

#aside {
  grid-area: aside;
  justify-self: left;
  position: sticky;
}
</style>
