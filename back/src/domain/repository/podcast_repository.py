from src.lib.sqlite_based_repository import SqliteBasedRepository
from src.domain.model.podcast import Podcast
from src.domain.model.podcast_category import PodcastCategory
from src.domain.model.podcast_episode import PodcastEpisode
from src.domain.model.podcast_author import PodcastAuthor


class PodcastRepository(SqliteBasedRepository):

    def get_podcast_id_of(self, episode_id):
        cursor = self._conn().cursor()
        cursor.execute(
            """SELECT podcast_id 
               FROM podcasts_episodes 
               WHERE episode_id=? 
               LIMIT 1;""", (episode_id,))
        data = cursor.fetchone()
        if data:
            podcast_id = data["podcast_id"]
            return podcast_id
        return None

    def get_podcast_by_id(self, podcast_id):
        cursor = self._conn().cursor()
        cursor.execute(
            """SELECT podcast_id, image_filename, title, 
                      description, category_id, lang_code
               FROM podcasts 
               WHERE podcast_id=? 
               LIMIT 1;""", (podcast_id,))
        data = cursor.fetchone()
        if data:
            podcast = Podcast(*data)
            return podcast
        return None

    def get_episode_by_id(self, episode_id):
        cursor = self._conn().cursor()
        cursor.execute(
            """SELECT episode_id, title, podcast_id, author_id, 
                      release_date, audio_filename, transcript
               FROM podcasts_episodes
               WHERE episode_id=?
               LIMIT 1;""", (episode_id,))
        data = cursor.fetchone()
        if data:
            return PodcastEpisode(*data)

    def get_author_by_id(self, author_id):
        cursor = self._conn().cursor()
        cursor.execute(
            """SELECT *
               FROM authors
               WHERE id=?
               LIMIT 1;""", (author_id,))
        data = cursor.fetchone()
        if data:
            return PodcastAuthor(*data)

    def get_category_by_id(self, category_id):
        cursor = self._conn().cursor()
        cursor.execute(
            """SELECT category_id, name, description, image_filename
               FROM podcasts_categories
               WHERE category_id=?
               LIMIT 1;""", (category_id,))
        data = cursor.fetchone()
        if data:
            return PodcastCategory(*data)
        return None

    def get_library_podcasts_by_user_id(self, user_id):
        cursor = self._conn().cursor()
        cursor.execute(
            """SELECT podcast_id
               FROM user_libraries
               WHERE user_id=?;""", (user_id,))
        data = cursor.fetchall()
        return [self.get_podcast_by_id(row["podcast_id"]) for row in data]

    def get_library_authors_by_user_id(self, user_id):
        cursor = self._conn().cursor()
        cursor.execute(
            """SELECT podcasts.author_id
               FROM user_libraries, podcasts
               WHERE user_libraries.user_id=?
                AND user_libraries.podcast_id=podcasts.podcast_id;""", (user_id,))
        data = cursor.fetchall()
        return [self.get_author_by_id(row["author_id"]) for row in data]

    def get_all_podcasts_by_category(self, category_id):
        cursor = self._conn().cursor()
        cursor.execute(
            """SELECT podcast_id, image_filename, title, 
                      description, category_id, lang_code
               FROM podcasts
               WHERE category_id=?;""", (category_id,))
        data = cursor.fetchall()
        return [Podcast(*record) for record in data]

    def get_all_episodes_by_podcast_id(self, podcast_id):
        cursor = self._conn().cursor()
        cursor.execute(
            """SELECT episode_id, title, podcast_id, author_id, 
                      release_date, audio_filename, transcript
               FROM podcasts_episodes
               WHERE podcast_id=?;""", (podcast_id,))
        data = cursor.fetchall()
        return [PodcastEpisode(*record) for record in data]

    def get_term_status(self, term, lang_code, user_id):
        cursor = self._conn().cursor()
        cursor.execute(
            """SELECT status
               FROM terms
               WHERE term = :term
                AND lang_code = :lang_code
                AND user_id = :user_id
               LIMIT 1;""", {
                "term": term,
                "lang_code": lang_code,
                "user_id": user_id
            })
        data = cursor.fetchone()
        if data:
            return data["status"]
