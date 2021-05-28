<template>
  <div class="container">
    <TrendingPodcast
      :podcast="{
        title: 'La vida moderna',
        description:
          'Lorem ipsum dolot et sit amet. Lorem ipsum dolot et sit amet',
      }"
    ></TrendingPodcast>
    <section>
      <h3>Continue listening</h3>
      <CardsSummaryGrid
        :items="latestPodcasts"
        :maxItems="maxItems"
        baseLink="/podcasts"
        @view-more-clicked="onViewMoreButtonClicked('recent')"
      ></CardsSummaryGrid>
    </section>
    <section>
      <h3>Recommended podcasts for you</h3>
      <CardsSummaryGrid
        :items="recommendedPodcasts"
        :maxItems="maxItems"
        baseLink="/podcasts"
        @view-more-clicked="onViewMoreButtonClicked('recommended')"
      ></CardsSummaryGrid>
    </section>
    <section>
      <h3>Genres you may like</h3>
      <div>Recommended Genres</div>
    </section>
    <section>
      <h3>New episodes in your library</h3>
      <div>New Episodes</div>
    </section>
  </div>
</template>

<script>
import api from "@/services/api";
import TrendingPodcast from "./TrendingPodcast.vue";
import CardsSummaryGrid from "@/components/CardsSummaryGrid.vue";

export default {
  name: "Home",
  components: { TrendingPodcast, CardsSummaryGrid },
  data() {
    return {
      latestPodcasts: [],
      recommendedPodcasts: [],
      maxItems: 6,
    };
  },
  methods: {
    async getLatestPodcasts() {
      const userId = this.$auth.user.id;
      this.latestPodcasts = await api.getLatestPlayedPodcastsByUserId(userId);
    },
    async getRecommendedPodcasts() {
      const userId = this.$auth.user.id;
      this.recommendedPodcasts = await api.getRecommendedPodcastsByUserId(
        userId
      );
    },
    async getRecommendedGenres() {
      const userId = this.$auth.user.id;
      this.recommendedGenres = await api.getRecommendedGenresByUserId(userId);
    },
    async getNewEpisodes() {
      const userId = this.$auth.user.id;
      this.newEpisodes = await api.getNewEpisodesByUserLibrary(userId);
    },
    onViewMoreButtonClicked(section) {
      if (section == "recent") {
        this.$router.push("/recent");
      }
    }
  },
  async created() {
    if (!this.$auth.isUserLogged) {
      this.$router.push("/login");
    }
    await this.getLatestPodcasts();
    await this.getRecommendedPodcasts();
  },
};
</script>

<style scoped>
h3 {
  margin-top: 1em;
  margin-bottom: 0.75em;
  font-size: 1.1em;
}
</style>
