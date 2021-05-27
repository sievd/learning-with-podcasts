from src.lib.errors import NotFoundError, NotAuthorizedError
import re


class PodcastInteractor:
    def __init__(self, config, podcast_repository=None, events_repository=None, user_repository=None):
        self.podcast_repository = podcast_repository
        self.events_repository = events_repository
        self.user_repository = user_repository

    # Platform.
    def get_all_podcasts_by_category(self, category_id):
        category = self.podcast_repository.get_category_by_id(category_id)
        if not category:
            raise NotFoundError(
                {"msg": f"Category with id '{category_id}' not found."})
        all_podcasts = self.podcast_repository.get_all_podcasts_by_category(
            category_id)
        return all_podcasts

    def get_all_episodes_by_podcast_id(self, podcast_id):
        podcast = self.podcast_repository.get_podcast_by_id(podcast_id)
        if podcast is None:
            raise NotFoundError(
                {"msg": f"Podcast with id '{podcast_id}' not found."})
        all_episodes = self.podcast_repository.get_all_episodes_by_podcast_id(
            podcast_id)
        return all_episodes

    def get_episode_by_id(self, episode_id):
        episode = self.podcast_repository.get_episode_by_id(episode_id)
        if episode is None:
            raise NotFoundError(
                {"msg": f"Episode with id '{episode_id}' not found."})
        return episode

    def get_all_podcasts(self, by):
        if by == "popularity":
            return self.get_podcast_by_popularity()

    def get_podcast_by_popularity(self):
        listenings_by_podcast = self._get_all_listenings_by_podcast()
        listenings_by_podcast_desc = sorted(
            listenings_by_podcast, key=lambda x: -x[1])
        podcasts_by_popularity_desc = [self.podcast_repository.get_podcast_by_id(tuple[0])
                                       for tuple in listenings_by_podcast_desc]
        return podcasts_by_popularity_desc

    def _get_all_listenings_by_podcast(self):
        all_listening_events = self.events_repository.get_all_events(
            type="listen")
        d = {}
        for event in all_listening_events:
            episode_id = event.data["episode_id"]
            podcast_id = self.podcast_repository.get_podcast_id_of(episode_id)
            d[podcast_id] = d.get(podcast_id, 0) + 1
        listenings = [(key, value) for key, value in d.items()]
        return listenings

    def get_podcast_by_id(self, podcast_id):
        podcast = self.podcast_repository.get_podcast_by_id(podcast_id)
        if not podcast:
            raise NotFoundError(
                {"msg": f"Podcast with id '{podcast_id}' not found."})
        return podcast

    # Users.
    def get_all_podcast_in_the_library(self):
        self._validate_auth()
        current_user = self.user_repository.get_current_user()
        user_library = self.podcast_repository.get_library_podcasts_by_user_id(
            current_user.id)
        return user_library

    def get_latests_listened_podcasts_in_the_library(self):
        self._validate_auth()
        current_user = self.user_repository.get_current_user()
        listened_podcasts_ids_by_date = self._get_all_listened_podcasts_by_user(
            current_user.id)
        latest_listened_podcasts_ids_desc = self._sort_podcasts_ids_by_listening_timestamp(
            listened_podcasts_ids_by_date)
        latests_listened_podcasts_desc = [self.podcast_repository.get_podcast_by_id(
            podcast_id) for podcast_id in latest_listened_podcasts_ids_desc]
        return latests_listened_podcasts_desc

    # def get_novelties_in_the_library(self):
    #     library = self.get_user_library()
    #     current_user = self.user_repository.get_current_user()
    #     listened_eps_by_date = self._get_all_listened_episodes_by_user(
    #         current_user.id)
        # listened_podcasts_ids_by_date = self._get_all_listened_podcasts_by_user()

    def get_terms_statuses_by_episode_id(self, episode_id):
        self._validate_auth()
        current_user = self.user_repository.get_current_user()
        episode = self.get_episode_by_id(episode_id)
        lang_code = self._get_episode_lang_code(episode_id)
        unique_terms = set(self._split_text_in_terms(episode.transcript))
        terms_statuses = {}
        for term in unique_terms:
            term_status = self.podcast_repository.get_term_status(
                term, lang_code, current_user.id)
            terms_statuses[term] = term_status if term_status else 0
        return terms_statuses

    def _get_episode_lang_code(self, episode_id):
        podcast_id = self.podcast_repository.get_podcast_id_of(
            episode_id)
        podcast = self.podcast_repository.get_podcast_by_id(podcast_id)
        return podcast.lang_code

    def _split_text_in_terms(self, text):
        raw_splitted_text = text.replace("\\n", " ").strip().split(" ")
        splitted_text_no_marks = [
            self._remove_standard_punctuation_marks(elem) for elem in raw_splitted_text
        ]
        splitted_text_no_cases = [elem.lower()
                                  for elem in splitted_text_no_marks]
        return splitted_text_no_cases

    def _remove_standard_punctuation_marks(self, text):
        end_marks = r"([\w|\d])([,?!;:.]+)"
        pair_marks_left = r"([\(\[\{<]+)([\w\d\-_]+)"
        pair_marks_right = r"([\w\d\-_]+)([\)\]\}>]+)"
        text_without_end_marks = re.sub(end_marks, r"\1", text)
        text_without_pair_marks_left = re.sub(
            pair_marks_left, r"\2", text_without_end_marks
        )
        text_without_pair_marks_right = re.sub(
            pair_marks_right, r"\1", text_without_pair_marks_left
        )
        return text_without_pair_marks_right

    def _get_all_listened_episodes_by_user(self, user_id):
        user_events = self.events_repository.get_events_by_user_id(
            user_id, "listen")
        listened_eps_by_date = [(event.data["episode_id"], event.timestamp)
                                for event in user_events]
        return listened_eps_by_date

    def _get_all_listened_podcasts_by_user(self, user_id):
        listened_eps_by_date = self._get_all_listened_episodes_by_user(user_id)
        listened_podcasts_by_date = [(self.podcast_repository.get_podcast_id_of(
            tuple[0]), tuple[1]) for tuple in listened_eps_by_date]
        return listened_podcasts_by_date

    def _sort_podcasts_ids_by_listening_timestamp(self, all_listenings):
        d = {}
        for podcast_id, timestamp in all_listenings:
            current_value = d.get(podcast_id, [])
            current_value.append(timestamp)
            d[podcast_id] = current_value
        for key in d.keys():
            d[key] = sorted(d[key])
        all_podcasts_ids_and_timestamps = d.items()
        all_podcasts_ids_and_timestamps_desc = sorted(
            all_podcasts_ids_and_timestamps, key=lambda x: x[1][-1], reverse=True)
        all_podcasts_ids_order_desc = [tuple[0]
                                       for tuple in all_podcasts_ids_and_timestamps_desc]
        return all_podcasts_ids_order_desc

    # Validations.
    def _validate_auth(self):
        current_user = self.user_repository.get_current_user()
        if current_user is None:
            raise NotAuthorizedError(
                {"msg": "This operation is not authorized. Please, log in."})
