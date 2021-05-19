from src.lib.errors import NotFoundError


class PodcastInteractor:
    def __init__(self, config, podcast_repository=None, events_repository=None, user_repository=None):
        self.podcast_repository = podcast_repository
        self.events_repository = events_repository
        self.user_repository = user_repository

    def get_all_podcasts_by_category(self, category_id):
        category = self.podcast_repository.get_category_by_id(category_id)
        if not category:
            raise NotFoundError(
                {"msg": f"Category with id '{category_id}' not found."})
        all_podcasts = self.podcast_repository.get_all_podcasts_by_category(
            category_id)
        return all_podcasts

    def get_all_podcasts(self, by):
        if by == "popularity":
            return self.get_podcast_by_popularity()

    def get_podcast_by_popularity(self):
        listenings_by_podcast = self.get_all_listenings_by_podcast()
        listenings_by_podcast_desc = sorted(
            listenings_by_podcast, key=lambda x: -x[1])
        podcasts_by_popularity_desc = [self.podcast_repository.get_podcast_by_id(tuple[0])
                                       for tuple in listenings_by_podcast_desc]
        return podcasts_by_popularity_desc

    def get_all_listenings_by_podcast(self):
        all_listening_events = self.events_repository.get_all_events(
            type="listen")
        d = {}
        for event in all_listening_events:
            episode_id = event.data["episode_id"]
            podcast_id = self.podcast_repository.get_podcast_id_of(episode_id)
            d[podcast_id] = d.get(podcast_id, 0) + 1
        listenings = [(key, value) for key, value in d.items()]
        return listenings

    def get_user_library(self):
        current_user = self.user_repository.get_current_user()
        user_library = self.podcast_repository.get_library_by_user_id(
            current_user.id)
        return user_library
