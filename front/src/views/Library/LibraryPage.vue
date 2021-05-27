<template>
  <div>
    <LibrarySubmenu class="submenu"></LibrarySubmenu>
    <section>
      <CardsSummaryGrid
        :items="libraryPodcasts"
        :maxItems="libraryPodcasts.length"
        baseLink="/"
        viewMoreLink="/"
      ></CardsSummaryGrid>
    </section>
  </div>
</template>

<script>
import api from "@/services/api";
import LibrarySubmenu from "./LibrarySubmenu.vue";
import CardsSummaryGrid from "@/components/CardsSummaryGrid.vue";

export default {
  name: "Library",
  components: { LibrarySubmenu, CardsSummaryGrid },
  data() {
    return {
      libraryPodcasts: [],
    };
  },
  methods: {
    async getLibraryPodcasts() {
      const userId = this.$auth.user.id;
      this.libraryPodcasts = await api.getPodcastsByUserLibrary(userId);
    },
  },
  async created() {
    await this.getLibraryPodcasts();
  },
};
</script>

<style scoped>
.submenu {
  margin-bottom: 1em;
}
</style>
