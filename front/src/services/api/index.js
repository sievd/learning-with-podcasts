import requestHandler from "./requestHandler";

const api = {
  ...requestHandler,

  async getLatestPlayedPodcastsByUserId(userId) {
    return await this.get(`/api/users/${userId}/podcasts?status=active`);
  },

  async getRecommendedPodcastsByUserId(userId) {
    console.log("recommended podcasts", userId);
    return await this.get(`/api/users/${userId}/podcasts?status=active`);
  },

  async getRecommendedGenresByUserId(userId) {
    console.log("recommended genres", userId);
    return await this.get(`/api/users/${userId}/podcasts?status=active`);
  },

  async getNewEpisodesByUserLibrary(userId) {
    console.log("new episodes", userId);
    return await this.get(`/api/users/${userId}/podcasts?status=active`);
  },

  async getPopularPodcasts() {
    return await this.get("/api/podcasts?by=popularity");
  },

  async getPodcastsByUserLibrary(userId) {
    return await this.get(`/api/users/${userId}/podcasts`);
  },

  async getPodcastById(id) {
    return await this.get(`/api/podcasts/${id}`);
  },

  async getEpisodesByPodcastId(id) {
    return await this.get(`/api/podcasts/${id}/episodes`);
  },

  async getEpisodeById(id) {
    return await this.get(`/api/episodes/${id}`);
  },

  async getWordStatusesByEpisodeId(id) {
    return await this.get(`/api/episodes/${id}/statuses`);
  },
};

export default api;
