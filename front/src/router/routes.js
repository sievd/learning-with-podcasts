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
    path: "/about",
    component: () => import("@/views/About/AboutPage.vue"),
  },
  {
    path: "/tasks",
    component: () => import("@/views/TaskList/TaskListPage.vue"),
  },
];
