<template>
  <div>
    <div class="cards">
      <Card
        v-for="item in items.slice(0, maxItems)"
        :key="JSON.stringify(item, null, 2)"
        :item="item"
        :baseLink="baseLink"
      ></Card>
    </div>
    <div class="view-more-wrapper" v-if="maxItems < items.length">
      <div class="view-more" @click="onViewMoreButtonClicked">
        <span>View more</span
        ><span class="material-icons md-3">double_arrow</span>
      </div>
    </div>
  </div>
</template>

<script>
import Card from "@/components/Card.vue";

export default {
  name: "CardsSummaryGrid",
  components: { Card },
  props: {
    items: { type: Array, required: true },
    baseLink: { type: String, required: true },
    maxItems: { type: Number, required: true },
  },
  methods: {
    onViewMoreButtonClicked() {
      this.$emit("view-more-clicked");
    },
  },
};
</script>

<style scoped>
.cards {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0.8em;
}

.view-more-wrapper {
  display: flex;
  justify-content: flex-end;
  margin-top: 0.1em;
}

.view-more {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.6em;
  gap: 0.2em;
}

.view-more:hover {
  cursor: pointer;
  color: #448ecf;
}
</style>
