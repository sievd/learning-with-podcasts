<template>
  <div>
    <ul>
      <li>Recently Played</li>
    </ul>
    <CardsSummaryGrid
      :items="latestPodcasts"
      :maxItems="maxItems"
      baseLink="/podcasts"
    ></CardsSummaryGrid>
  </div>
</template>

<script>
import api from "@/services/api";
import CardsSummaryGrid from "@/components/CardsSummaryGrid.vue";

export default {
  name: "RecentlyPlayed",
  components: { CardsSummaryGrid },
  data() {
    return {
      latestPodcasts: [],
    };
  },
  methods: {
    async getLatestPodcasts() {
      const userId = this.$auth.user.id;
      this.latestPodcasts = await api.getLatestPlayedPodcastsByUserId(userId);
    },
  },
  async created() {
    if (!this.$auth.isUserLogged) {
      this.$router.push("/login");
    }
    await this.getLatestPodcasts();
  },
};
</script>

<style scoped>
li {
  font-size: 0.75em;
  margin-bottom: 1em;
}
</style>
