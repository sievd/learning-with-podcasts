<template>
  <section v-if="podcast && episodes">
    <div class="podcast-description">
      <div class="bg">
        <img :src="podcast.image" class="bg-picture" />
      </div>
      <img :src="podcast.image" class="description-picture" />
      <div>
        <p class="type">Podcast</p>
        <p class="title">{{ podcast.title }}</p>
        <p class="description">{{ podcast.description }}</p>
        <p class="ep">
          {{ episodes.length }} episode{{ episodes.length != 1 ? "s" : "" }}
        </p>
        <span class="material-icons md-8 love-button">favorite</span>
      </div>
    </div>
    <EpisodesTable class="table" :episodes="episodes"></EpisodesTable>
  </section>
</template>

<script>
import api from "@/services/api";
import EpisodesTable from "./EpisodesTable.vue";

export default {
  name: "PodcastDetails",
  components: { EpisodesTable },
  data() {
    return {
      podcast: null,
      episodes: null,
    };
  },
  async created() {
    if (!this.$auth.isUserLogged) {
      this.$router.push("/login");
    }
    const id = this.$route.params.id;
    this.podcast = await api.getPodcastById(id);
    this.episodes = await api.getEpisodesByPodcastId(id);
  },
};
</script>

<style scoped>
.bg {
  position: absolute;
  z-index: -1;
  top: 0;
  left: 0;
  min-width: 100vw;
  height: 35%;
  overflow: hidden;
  filter: contrast(175%) grayscale(80%) opacity(50%);
}

.bg-picture {
  background: #fff center center no-repeat;
  background-size: cover;
  min-width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center center;
  filter: blur(3px);
}

.description-picture {
  border-radius: 5px;
  width: 13rem;
  max-height: 13rem;
  object-fit: cover;
  object-position: center center;
}

.podcast-description {
  display: flex;
  gap: 1.5rem;
}

p {
  margin: 0;
  padding: 0;
  line-height: 150%;
}

p.type {
  font-size: 0.6em;
  text-transform: capitalize;
  margin-top: 0.3rem;
  opacity: 0.8;
}

p.title {
  font-weight: 900;
  margin-top: 0.9rem;
  margin-bottom: 0.2rem;
  font-size: 1.1em;
  color: white;
}

p.description {
  font-size: 0.7em;
  margin-bottom: 0.9rem;
  font-weight: 300;
}

p.ep {
  font-size: 0.6em;
  opacity: 0.8;
}

.love-button {
  border: 1px solid white;
  padding: 0.5em;
  border-radius: 100px;
  margin-top: 1.2em;
}

.love-button:hover {
  color: #448ecf;
  border-color: #448ecf;
  cursor: pointer;
}

.table {
  margin-top: 2em;
}
</style>
