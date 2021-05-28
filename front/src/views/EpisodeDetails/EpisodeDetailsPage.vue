<template>
  <div class="container" v-if="episode && podcast">
    <section class="transcript">
      <h2>{{ episode.title }}</h2>
      <p>
        <router-link :to="`/podcasts/${episode.podcast_id}`">{{
          episode.podcast_id
        }}</router-link>
      </p>
      <Transcript
        class="text-component"
        :transcript="episode.transcript"
        :statuses="statuses"
        :key="JSON.stringify(statuses, null, 2)"
        @word-clicked="onWordClicked"
      ></Transcript>
    </section>
    <section class="status-control">
      <StatusControl
        :currentWord="currentWord"
        :currentStatus="currentStatus"
        @status-clicked="onStatusButtonClicked"
      ></StatusControl>
    </section>
    <section class="iframe-wrapper">
      <iframe
        loading="lazy"
        class="iframe"
        :src="`https://www.wordreference.com/${langCode}/en/translation.asp${search}`"
      >
      </iframe>
    </section>
  </div>
</template>

<script>
import api from "@/services/api";
import Transcript from "./Transcript.vue";
import StatusControl from "./StatusControl.vue";

export default {
  name: "EpisodeDetails",
  components: { Transcript, StatusControl },
  data() {
    return {
      episode: null,
      podcast: null,
      statuses: {},
      currentWord: "",
      currentStatus: 0,
    };
  },
  computed: {
    search() {
      if (this.currentWord != "") {
        return `?spen=${this.currentWord}`;
      }
      return "";
    },
    langCode() {
      return this.podcast.lang_code.toLowerCase();
    },
  },
  methods: {
    onWordClicked(currentWord, currentStatus) {
      this.currentWord = currentWord;
      this.currentStatus = currentStatus;
      console.log(status);
    },
    async onStatusButtonClicked(newStatus) {
      const userId = this.$route.params.id;
      this.currentStatus = newStatus;
      this.statuses[this.currentWord] = newStatus;
      await api.setTermStatus(
        userId,
        this.currentWord,
        this.langCode,
        newStatus
      );
    },
  },
  async created() {
    if (!this.$auth.isUserLogged) {
      this.$router.push("/login");
    }
    const episodeId = this.$route.params.episodeId;
    const podcastId = this.$route.params.podcastId;
    this.episode = await api.getEpisodeById(episodeId);
    this.podcast = await api.getPodcastById(podcastId);
    this.statuses = await api.getWordStatusesByEpisodeId(episodeId);
  },
};
</script>

<style scoped>
.container {
  display: grid;
  grid-gap: 1em;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr;
  grid-template-areas: "transcript .";
}

.transcript {
  grid-area: transcript;
  background-color: #18181daf;
  color: white;
  text-align: left;
  border-radius: 5px;
  padding: 1em 2em;
}

.iframe-wrapper {
  position: fixed;
  top: 9.2rem;
  right: 2rem;
  padding-bottom: 100%;
  overflow: hidden;
  border-radius: 5px;
}

.status-control {
  position: fixed;
  top: 5.2rem;
  right: 2rem;
  height: 5vh;
  width: 75vh;
}

.iframe {
  height: 70vh;
  width: 75vh;
  /* position: absolute; */
  /* top: 0;
  left: 0; */
  border: 0;
}

.iframe,
.iframe-wrapper {
  scrollbar-width: none; /* Firefox 64 */
  -ms-overflow-style: none; /* Internet Explorer 11 */
}
.iframe::-webkit-scrollbar,
.iframe-wrapper::-webkit-scrollbar {
  display: none; /* WebKit */
}

h2 {
  font-size: 1.1em;
  margin-bottom: 0.1em;
}

p {
  font-size: 0.75em;
  margin-top: 0em;
  font-weight: 900;
  opacity: 0.8;
}

p:hover {
  cursor: pointer;
}

/deep/ .status-0 {
  background-color: rgba(137, 137, 243, 0.521);
}

/deep/ .status-1 {
  background-color: rgba(250, 126, 126, 0.918);
}

/deep/ .status-2 {
  background-color: rgba(245, 198, 112, 0.897);
}

/deep/ .status-3 {
  background-color: rgba(125, 252, 109, 0.918);
}

/deep/ .status-0.selected {
  background-color: rgb(88, 88, 255);
}

/deep/ .status-1.selected {
  background-color: rgb(255, 66, 66);
}

/deep/ .status-2.selected {
  background-color: rgb(248, 187, 73);
}

/deep/ .status-3.selected {
  background-color: rgb(100, 255, 80);
}
</style>
