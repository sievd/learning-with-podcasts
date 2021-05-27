<template>
  <!-- <section>
    {{ podcast.id }}
    <img :src="podcast.image" />
    {{ podcast.title }}
    {{ podcast.description }}
  </section> -->
  <section>
    <p>Trending now</p>
    <h2>{{ podcast.title }}</h2>
    <p>{{ podcast.description }}</p>
    <div class="options">
      <div class="listen-button">Listen Now</div>
      <span class="material-icons md-8 love-button">favorite</span>
    </div>
  </section>
</template>

<script>
export default {
  name: "TrendingPodcast",
  props: {
    podcast: { type: Object, required: true },
  },
};
</script>

<style scoped>
section {
  background-color: gray;
  padding: 1rem;
  border-radius: 8px;
  font-size: 0.8em;
}

h2,
p {
  margin: 0;
}

p {
  margin: 0.1em;
}

h2 {
  font-weight: 900;
}

.options {
  display: flex;
  align-items: center;
  gap: 1em;
  font-size: 0.9em;
}

.listen-button {
  border: 1px solid white;
  padding: 0 3em;
  border-radius: 50px;
}

.love-button {
  border: 1px solid white;
  padding: 0.5em;
  border-radius: 100px;
}
</style>
