<template>
  <ul v-if="active">
    <li
      :class="[active == 'playlists' ? 'active' : '']"
      @click="onTabClicked('playlists')"
    >
      Playlists
    </li>
    <li
      :class="[active == 'podcasts' ? 'active' : '']"
      @click="onTabClicked('podcasts')"
    >
      Podcasts
    </li>
    <li
      :class="[active == 'authors' ? 'active' : '']"
      @click="onTabClicked('authors')"
    >
      Authors
    </li>
  </ul>
</template>

<script>
export default {
  name: "LibrarySubmenu",
  props: {
    active: { type: String, required: true },
  },
  methods: {
    onTabClicked(name) {
      this.$emit("tab-clicked", name);
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
