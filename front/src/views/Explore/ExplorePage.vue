<template>
  <div>
    <section>
      <h3>Top genres</h3>
      <!-- <div>New Episodes</div> -->
    </section>
    <section>
      <h3>Popular in Podcaster</h3>
      <CardsSummaryGrid
        :items="popularPodcasts"
        :maxItems="maxItems"
        baseLink="/"
        viewMoreLink="/"
      ></CardsSummaryGrid>
    </section>
    <section>
      <h3>Trending now</h3>
      <!-- <CardsSummaryGrid
        :items="recommendedPodcasts"
        baseLink="/"
        viewMoreLink="/"
      ></CardsSummaryGrid> -->
    </section>
    <section>
      <h3>Latest podcasts</h3>
      <!-- <div>Recommended Genres</div> -->
    </section>
  </div>
</template>

<script>
import api from "@/services/api";
import CardsSummaryGrid from "@/components/CardsSummaryGrid.vue";

export default {
  name: "Explore",
  components: { CardsSummaryGrid },
  data() {
    return {
      popularPodcasts: [],
      maxItems: 6,
    };
  },
  methods: {
    async getPopularPodcasts() {
      this.popularPodcasts = await api.getPopularPodcasts();
    },
  },
  async created() {
    await this.getPopularPodcasts();
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
