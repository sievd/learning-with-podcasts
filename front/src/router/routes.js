export const routes = [
  {
    path: "/",
    component: () => import("@/views/Home/HomePage.vue"),
  },
  {
    path: "/explore",
    component: () => import("@/views/Explore/ExplorePage.vue"),
  },
  {
    path: "/recent",
    component: () => import("@/views/RecentlyPlayed/RecentlyPlayedPage.vue"),
  },
  {
    path: "/library",
    component: () => import("@/views/Library/LibraryPage.vue"),
  },
  {
    path: "/library/playlists",
    component: () => import("@/views/Library/LibraryPage.vue"),
  },
  {
    path: "/library/podcasts",
    component: () => import("@/views/Library/LibraryPage.vue"),
  },
  {
    path: "/library/authors",
    component: () => import("@/views/Library/LibraryPage.vue"),
  },
  {
    path: "/podcasts/:id",
    component: () => import("@/views/PodcastDetails/PodcastDetailsPage.vue"),
  },
  {
    path: "/podcasts/:podcastId/:episodeId",
    component: () => import("@/views/EpisodeDetails/EpisodeDetailsPage.vue"),
  },
  {
    path: "/login",
    component: () => import("@/views/Login/LoginPage.vue"),
  },
];
