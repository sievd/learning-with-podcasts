<template>
  <aside>
    <section class="logo">
      <img src="@/assets/logo.png" @click="onLogoClicked" />
    </section>

    <section>
      <header>Menu</header>
      <ul>
        <li
          @click="onHomeLinkClicked"
          :class="[active == 'Home' ? 'active' : '']"
        >
          <span class="material-icons md-8">home</span><span>Home</span>
        </li>
        <li
          @click="onExploreLinkClicked"
          :class="[active == 'Explore' ? 'active' : '']"
        >
          <span class="material-icons md-8">explore</span><span>Explore</span>
        </li>
      </ul>
    </section>

    <section>
      <header>Library</header>
      <ul>
        <li>
          <span class="material-icons md-8">explore</span><span>For You</span>
        </li>
        <li>
          <span class="material-icons md-8">cached</span><span>Recent</span>
        </li>
        <li>
          <span class="material-icons md-8">favorite</span
          ><span>Favourites</span>
        </li>
        <li
          @click="onLibraryPodcastsLinkClicked"
          :class="[active == 'LibraryPodcasts' ? 'active' : '']"
        >
          <span class="material-icons md-8">headset</span><span>Podcasts</span>
        </li>
        <li
          @click="onLibraryAuthorsLinkClicked"
          :class="[active == 'LibraryAuthors' ? 'active' : '']"
        >
          <span class="material-icons md-8">mic</span><span>Authors</span>
        </li>
      </ul>
    </section>

    <section>
      <header>Playlists</header>
      <ul>
        <li @click="onAddPlaylistButtonClicked">
          <span class="material-icons md-12">add_box</span
          ><span>Submit new</span>
        </li>
        <li>
          <span class="material-icons md-8">playlist_play</span
          ><span>Example playlist</span>
        </li>
      </ul>
    </section>
  </aside>
</template>

<script>
export default {
  name: "Aside",
  computed: {
    active() {
      const path = this.$route.path;
      if (path.includes("explore")) {
        return "Explore";
      } else if (path.includes("library")) {
        if (path.includes("podcasts")) {
          return "LibraryPodcasts";
        } else if (path.includes("authors")) {
          return "LibraryAuthors";
        } else {
          return "";
        }
      } else if (path == "/") {
        return "Home";
      } else {
        return "";
      }
    },
  },
  methods: {
    onAddPlaylistButtonClicked() {
      console.log("playlist added!");
    },
    onLogoClicked() {
      this.$router.push("/");
    },
    onHomeLinkClicked() {
      this.$router.push("/");
    },
    onExploreLinkClicked() {
      this.$router.push("/explore");
    },
    onLibraryPodcastsLinkClicked() {
      this.$router.push("/library/podcasts");
    },
    onLibraryAuthorsLinkClicked() {
      this.$router.push("/library/authors");
    },
  },
};
</script>

<style scoped>
aside {
  background-color: #18181d;
  margin: 0;
  font-size: 0.55em;
  font-weight: 600;
  height: 100vh;
}

aside > section {
  width: 80%;
  margin: 0 auto;
}

header {
  color: #6e6f6f;
  font-size: 1.1em;
  margin-bottom: 0.5em;
  font-weight: 900;
}

section {
  padding: 1em 0;
}

section:nth-child(3) {
  border-top: 2px solid #1a1a1e;
  border-bottom: 2px solid #1a1a1e;
}

.logo {
  display: flex;
  justify-content: center;
}

img {
  max-width: 50%;
}

img:hover {
  cursor: pointer;
}

li {
  display: flex;
  align-items: center;
}

li span:first-child {
  width: 2.1rem;
}

span.material-icons {
  cursor: default;
}

span.material-icons:hover {
  cursor: pointer;
}

li:hover {
  cursor: pointer;
  color: #448ecf;
}

.active {
  color: #448ecf;
}
</style>
