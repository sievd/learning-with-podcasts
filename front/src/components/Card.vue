<template>
  <div class="card">
    <router-link
      class="card-image"
      :to="`${baseLink}/${item.id}`"
      :style="{ 'background-image': `url(${item.image})` }"
      :data-image-full="item.image"
    >
      <img :src="item.image" :alt="item.title" />
    </router-link>
    <router-link class="card-description" :to="`${baseLink}/${item.id}`">
      <h2>{{ item.title }}</h2>
      <p>{{ item.description }}</p>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "Card",
  props: {
    item: { type: Object, required: true },
    baseLink: { type: String, required: true },
  },
};
</script>

<style scoped>
.card {
  padding: 0.5em;
  border-radius: 10px;
  background-color: #18181d;
}

.card-image {
  display: block;
  border-radius: 10px;
  background: #fff center center no-repeat;
  background-size: cover;
  height: 6rem;
  /* filter: blur(3px); */
}

.card-image > img {
  display: block;
  width: 100%;
  opacity: 0;
}

.card-image.is-loaded {
  filter: none;
  transition: filter 1s;
}

.card-list {
  display: block;
  margin: 1rem auto;
  padding: 0;
  font-size: 0;
  text-align: center;
  list-style: none;
}

.card {
  display: inline-block;
  width: 90%;
  max-width: 9rem;
  /* margin: 1rem; */
  font-size: 1rem;
  text-decoration: none;
  overflow: hidden;
  box-shadow: 0 0 3rem -1rem rgba(0, 0, 0, 0.5);
  transition: transform 0.1s ease-in-out, box-shadow 0.1s;
}

.card:hover {
  transform: translateY(-0.5rem) scale(1.0125);
  box-shadow: 0 0.5em 3rem -1rem rgba(0, 0, 0, 0.5);
}

.card-description {
  display: block;
  padding: 0.5em 0.2em 0.1em 0.2em;
  color: #5c5c5c;
  text-decoration: none;
}

.card-description > h2 {
  color: #e8e9e9;
  margin: 0 0 0.2em;
  line-height: 150%;
  font-size: 0.95em;
}

.card-description > p {
  margin: 0;
  line-height: 130%;
  font-size: 0.8em;
}
</style>
