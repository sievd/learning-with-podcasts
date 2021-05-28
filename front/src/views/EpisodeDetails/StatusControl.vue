<template>
  <section class="container">
    <p>Select</p>
    <div class="options">
      <div
        v-for="n in 5"
        :key="n"
        :class="[
          isDisabled ? 'disabled' : currentStatus == n - 1 ? 'selected' : '',
          'status-' + (n - 1),
        ]"
        @click="onStatusClicked(n)"
      >
        {{ n }}
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "TermStatus",
  props: {
    currentWord: { type: String, required: false },
    currentStatus: { type: Number, required: false },
  },
  computed: {
    isDisabled: function () {
      return !this.currentWord;
    },
  },
  methods: {
    onStatusClicked(n) {
      const nextStatus = n - 1;
      if (this.currentStatus != nextStatus) {
        this.$emit("status-clicked", nextStatus);
      }
    },
  },
};
</script>

<style scoped>
.container {
  height: 3em;
  padding: 0 0.2em;
  display: flex;
  justify-content: flex-end;
  align-items: center;
}

p {
  font-size: 0.8em;
}

.options {
  display: flex;
}

.status-0,
.status-1,
.status-2,
.status-3,
.status-4 {
  width: 2em;
  height: 1.6em;
  border-radius: 1px;
  margin: 0.2em;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.status-4 {
  border: 1px solid lightgray;
}

.status-0:hover,
.status-1:hover,
.status-2:hover,
.status-3:hover,
.status-4:hover {
  cursor: pointer;
  opacity: 0.6;
}

.status-0.disabled,
.status-1.disabled,
.status-2.disabled,
.status-3.disabled,
.status-4.disabled {
  cursor: default;
  opacity: 0.6;
}

.status-0.selected,
.status-1.selected,
.status-2.selected,
.status-3.selected,
.status-4.selected {
  opacity: 0.1;
  cursor: default;
}
</style>
