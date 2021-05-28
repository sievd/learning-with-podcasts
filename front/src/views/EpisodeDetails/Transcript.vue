<template>
  <div v-if="transcript && statuses">
    <p v-for="(paragraph, index) in paragraphs" :key="index">
      <span
        v-for="(word, index) in getWordsInParagraph(paragraph)"
        :key="index"
      >
        <br v-if="word == '\n'" />
        <pre
          :class="'status-' + getWordStatus(word)"
          @click="onWordClicked(word, getWordStatus(word))"
          v-else
          >{{ word }}</pre
        >
      </span>
    </p>
  </div>
</template>

<script>
export default {
  name: "Transcript",
  props: {
    transcript: { type: String, required: true },
    statuses: { type: Object, required: true },
  },
  data() {
    return {
      avgCharsInLine: 60,
    };
  },
  computed: {
    lines: function () {
      return this.transcript.split("\\n");
    },
    paragraphs: function () {
      let paragraphs = [];
      let verse = "";
      for (let line of this.lines) {
        if (this.isAVerseLine(line)) {
          verse += line + " \n ";
        } else if (this.isWhiteSpace(line)) {
          paragraphs.push(verse.slice(0, -2));
          verse = "";
        } else {
          console.log("line " + line);
          paragraphs.push(line);
        }
      }
      return paragraphs;
    },
  },
  methods: {
    isWhiteSpace(line) {
      return line.length == 0;
    },
    isAVerseLine(line) {
      return line.length < this.avgCharsInLine && !this.isWhiteSpace(line);
    },
    getWordsInParagraph(paragraph) {
      return paragraph.split(" ");
    },
    formatWord(word) {
      // eslint-disable-next-line no-useless-escape
      const punctuationMarks = /([?!.,:;\(\)\[\]\{\}<>])/g;
      const formattedWord = word.toLowerCase().replace(punctuationMarks, "");
      return formattedWord;
    },
    getWordStatus(word) {
      const formattedWord = this.formatWord(word);
      const isWordOK = Object.keys(this.statuses).includes(formattedWord);
      if (isWordOK) {
        return this.statuses[formattedWord];
      } else if (word == "\n") {
        return "";
      } else {
        console.log("Wrong formatting of word in TextContent -> " + word);
        return "unkown";
      }
    },
    onWordClicked(word, status) {
      word = this.formatWord(word);
      this.$emit("word-clicked", word, status);
    },
  },
};
</script>

<style scoped>
pre {
  margin: 0;
  line-height: 1.3em;
  border-radius: 5px;
  display: inline-block;
  font-size: 0.75em;
  font-family: inherit;
  margin: 0 0.2em;
}

.status-0,
.status-1,
.status-2,
.status-3,
.status-4 {
  cursor: pointer;
}

.status-unkown {
  color: red;
}
</style>
