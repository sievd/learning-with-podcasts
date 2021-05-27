<template>
  <ul>
    <li :class="[active == 'playlists' ? 'active' : '']">
      <router-link to="/library/playlists">Playlists</router-link>
    </li>
    <li :class="[active == 'podcasts' ? 'active' : '']">
      <router-link to="/library/podcasts">Podcasts</router-link>
    </li>
    <li :class="[active == 'authors' ? 'active' : '']">
      <router-link to="/library/authors">Authors</router-link>
    </li>
  </ul>
</template>

<script>
export default {
  name: "LibrarySubmenu",
  computed: {
    active() {
      const path = this.$route.path;
      if (path.includes("podcasts")) {
        return "podcasts";
      } else if (path.includes("authors")) {
        return "authors";
      } else {
        return "playlists";
      }
    },
  },
};
</script>

<style scoped>
ul {
  display: flex;
  gap: 1em;
  font-size: 0.75em;
}

li:hover {
  cursor: pointer;
  color: #448ecf;
}

.active {
  border-bottom: 2px solid #448ecf;
}
</style>
