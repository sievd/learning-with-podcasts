<template>
  <div v-if="libraryPodcasts && libraryAuthors">
    <LibrarySubmenu
      :active="active"
      class="submenu"
      @tab-clicked="onTabClicked"
    ></LibrarySubmenu>
    <section>
      <CardsSummaryGrid
        :items="currentItems"
        :maxItems="libraryPodcasts.length"
        baseLink="/podcasts"
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
      libraryAuthors: [],
      playlists: [],
    };
  },
  computed: {
    currentItems() {
      if (this.active == "podcasts") {
        return this.libraryPodcasts;
      } else if (this.active == "authors") {
        return this.libraryAuthors;
      } else {
        return this.playlists;
      }
    },
    active() {
      if (this.$route.path.includes("podcasts")) {
        return "podcasts";
      } else if (this.$route.path.includes("authors")) {
        return "authors";
      } else {
        return "playlists";
      }
    },
  },
  methods: {
    async getLibraryPodcasts() {
      const userId = this.$auth.user.id;
      this.libraryPodcasts = await api.getPodcastsByUserLibrary(userId);
    },
    async getLibraryAuthors() {
      const userId = this.$auth.user.id;
      this.libraryAuthors = await api.getAuthorsByUserLibrary(userId);
    },
    onTabClicked(name) {
      if (name == "podcasts") {
        this.$router.push("/library/podcasts");
      } else if (name == "authors") {
        this.$router.push("/library/authors");
      } else {
        this.$router.push("/library/playlists");
      }
    },
  },
  async created() {
    if (!this.$auth.isUserLogged) {
      this.$router.push("/login");
    }
    await this.getLibraryPodcasts();
    await this.getLibraryAuthors();
  },
};
</script>

<style scoped>
.submenu {
  margin-bottom: 1em;
}
</style>
