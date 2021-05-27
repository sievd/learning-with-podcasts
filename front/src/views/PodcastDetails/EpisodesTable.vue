<template>
  <div class="container" v-if="episodes">
    <table>
      <tr>
        <th></th>
        <th>TITLE</th>
        <th>AUTHOR</th>
        <th><span class="material-icons md-8">calendar_today</span></th>
        <th><span class="material-icons md-8">schedule</span></th>
      </tr>
      <tr v-for="episode in episodes" :key="JSON.stringify(episode, null, 2)">
        <td>
          <span class="material-icons md-8">favorite</span>
        </td>
        <td class="title">
          {{ episode.title }}
        </td>
        <td>
          {{ episode.author }}
        </td>
        <td>
          {{
            new Date(episode.release_date).toLocaleString("es-ES", {
              dateStyle: "medium",
            })
          }}
        </td>
        <td>
          {{ episode.duration }}
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: "EpisodesTable",
  props: {
    episodes: { type: Array, required: true },
  },
};
</script>

<style scoped>
.container {
  /* box-shadow: 2px 2px 2px 2px #ccc; */
  /* display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center; */
  font-size: 0.8em;
  /* padding: 1.5em; */
}

table {
  text-align: left;
  font-weight: 100;
  width: 100%;
  border-collapse: collapse;
}

th {
  color: #a2a0a0;
  border-bottom: 2px solid #e8e9e94b;
  font-weight: 600;
  padding-bottom: 1em;
  font-size: 0.7em;
}

td {
  color: #e8e9e9;
  border-bottom: 2px solid #e8e9e94b;
  font-size: 0.75em;
  margin: 1em 0;
}

th,
td {
  padding: 0 1em;
  vertical-align: center;
}

td.title {
  color: white;
  font-weight: 900;
}

td.title:hover {
  cursor: pointer;
}

span {
  display: flex;
  align-items: center;
}
</style>
