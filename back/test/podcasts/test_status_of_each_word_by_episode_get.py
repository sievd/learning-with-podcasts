from src.domain.interactor.podcast_interactor import PodcastInteractor
from src.domain.repository.podcast_repository import PodcastRepository
from src.domain.repository.user_repository import UserRepository
from src.lib.errors import NotFoundError, NotAuthorizedError
import pytest


def test_status_of_zero(database):
    """
    Context -> Text exist, single unkown term, no punctuation marks, no upper/lower, English set of chars
    Example input -> "test-term"
    Output -> { "test-term": 0 }
    """

    database.executescript(
        """
      INSERT INTO podcasts (podcast_id, image_filename, title, description, category_id, lang_code) values
          ("test-podcast-1", "test_picture_1.jpg", "Title of podcast 1", "Description of podcast 1", "test-category-1", "EN"),
          ("test-podcast-2", "test_picture_2.jpg", "Title of podcast 2", "Description of podcast 2", "test-category-2", "ES"),
          ("test-podcast-3", "test_picture_3.jpg", "Title of podcast 3", "Description of podcast 3", "test-category-1", "EN"),
          ("test-podcast-4", "test_picture_4.jpg", "Title of podcast 4", "Description of podcast 4", "test-category-3", "ES");

      INSERT INTO podcasts_categories (category_id, name, description) values
          ("test-category-1", "Test category 1", "Description of the category 1"),
          ("test-category-2", "Test category 2", "Description of the category 2"),
          ("test-category-3", "Test category 3", "Description of the category 3"),
          ("test-category-4", "Test category 4", "Description of the category 4");

      INSERT INTO podcasts_episodes (episode_id, podcast_id, author_id, release_date, audio_filename, transcript) values
          ("test-episode-1", "test-podcast-1", "test-author-1", "2021-05-18", "test-audio-filename", "test-word"),
          ("test-episode-2", "test-podcast-2", "test-author-2", "2021-05-19", "test-audio-filename", "test-word"),
          ("test-episode-3", "test-podcast-3", "test-author-3", "2021-05-20", "test-audio-filename", "test-word"),
          ("test-episode-4", "test-podcast-4", "test-author-4", "2021-05-21", "test-audio-filename", "test-word"),
          ("test-episode-5", "test-podcast-1", "test-author-1", "2021-05-22", "test-audio-filename", "test-word"),
          ("test-episode-6", "test-podcast-2", "test-author-2", "2021-05-23", "test-audio-filename", "test-word"),
          ("test-episode-7", "test-podcast-3", "test-author-3", "2021-05-24", "test-audio-filename", "test-word"),
          ("test-episode-8", "test-podcast-4", "test-author-4", "2021-05-25", "test-audio-filename", "test-word");
        """
    )
    user_repository = UserRepository(
        None, database, get_current_user_id=lambda: "user-1")
    podcast_repository = PodcastRepository(None, database)
    podcast_interactor = PodcastInteractor(
        None, podcast_repository, None, user_repository)
    words = podcast_interactor.get_terms_statuses_by_episode_id(
        "test-episode-1")
    assert len(words) == 1
    assert words["test-word"] == 0


def test_status_from_one_to_four(database):
    """
    Context -> Text exist, single known word, no punctuation marks, no upper/lower, English set of chars
    Example input -> "test-term"
    Output ->
        case 1: { "test-term": 1 }
        case 2: { "test-term": 2 }
        case 3: { "test-term": 3 }
        case 4: { "test-term": 4 }
    """

    database.executescript(
        """
    INSERT INTO podcasts (podcast_id, image_filename, title, description, category_id, lang_code) values
        ("test-podcast-1", "test_picture_1.jpg", "Title of podcast 1", "Description of podcast 1", "test-category-1", "EN"),
        ("test-podcast-2", "test_picture_2.jpg", "Title of podcast 2", "Description of podcast 2", "test-category-2", "ES"),
        ("test-podcast-3", "test_picture_3.jpg", "Title of podcast 3", "Description of podcast 3", "test-category-1", "EN"),
        ("test-podcast-4", "test_picture_4.jpg", "Title of podcast 4", "Description of podcast 4", "test-category-3", "ES");

    INSERT INTO podcasts_categories (category_id, name, description) values
        ("test-category-1", "Test category 1", "Description of the category 1"),
        ("test-category-2", "Test category 2", "Description of the category 2"),
        ("test-category-3", "Test category 3", "Description of the category 3"),
        ("test-category-4", "Test category 4", "Description of the category 4");

    INSERT INTO podcasts_episodes (episode_id, podcast_id, author_id, release_date, audio_filename, transcript) values
        ("test-episode-1", "test-podcast-1", "test-author-1", "2021-05-18", "test-audio-filename", "test-word-1"),
        ("test-episode-2", "test-podcast-2", "test-author-2", "2021-05-19", "test-audio-filename", "test-word-2"),
        ("test-episode-3", "test-podcast-3", "test-author-3", "2021-05-20", "test-audio-filename", "test-word-3"),
        ("test-episode-4", "test-podcast-4", "test-author-4", "2021-05-21", "test-audio-filename", "test-word-4"),
        ("test-episode-5", "test-podcast-1", "test-author-1", "2021-05-22", "test-audio-filename", "test-word-2"),
        ("test-episode-6", "test-podcast-2", "test-author-2", "2021-05-23", "test-audio-filename", "test-word-1"),
        ("test-episode-7", "test-podcast-3", "test-author-3", "2021-05-24", "test-audio-filename", "test-word-2"),
        ("test-episode-8", "test-podcast-4", "test-author-4", "2021-05-25", "test-audio-filename", "test-word-2");

      INSERT INTO languages (lang_code, name) values
          ("EN", "English"),
          ("ES", "Spanish");

      INSERT INTO terms (term, lang_code, status, user_id) values
          ("test-word-1", "EN", 1, "user-1"),
          ("test-word-2", "ES", 2, "user-1"),
          ("test-word-3", "EN", 3, "user-1"),
          ("test-word-4", "ES", 4, "user-1");
      """
    )
    user_repository = UserRepository(
        None, database, get_current_user_id=lambda: "user-1")
    podcast_repository = PodcastRepository(None, database)
    podcast_interactor = PodcastInteractor(
        None, podcast_repository, None, user_repository)

    words_1 = podcast_interactor.get_terms_statuses_by_episode_id(
        "test-episode-1")
    assert len(words_1) == 1
    assert words_1["test-word-1"] == 1

    words_2 = podcast_interactor.get_terms_statuses_by_episode_id(
        "test-episode-2")
    assert len(words_2) == 1
    assert words_2["test-word-2"] == 2

    words_3 = podcast_interactor.get_terms_statuses_by_episode_id(
        "test-episode-3")
    assert len(words_3) == 1
    assert words_3["test-word-3"] == 3

    words_4 = podcast_interactor.get_terms_statuses_by_episode_id(
        "test-episode-4")
    assert len(words_4) == 1
    assert words_4["test-word-4"] == 4


def test_should_get_NotFoundError_if_the_episode_doesnt_exist(database):
    user_repository = UserRepository(
        None, database, get_current_user_id=lambda: "user-1")
    podcast_repository = PodcastRepository(None, database)
    podcast_interactor = PodcastInteractor(
        None, podcast_repository, None, user_repository)
    with pytest.raises(NotFoundError) as exception:
        podcast_interactor.get_terms_statuses_by_episode_id(
            "non-existent-episode")
    assert exception.value.data == {
        "msg": "Episode with id 'non-existent-episode' not found."
    }


def test_should_get_NotAuthorizedError_if_the_user_is_not_logged_in(database):
    user_repository = UserRepository(
        None, database, get_current_user_id=lambda: None)
    podcast_repository = PodcastRepository(None, database)
    podcast_interactor = PodcastInteractor(
        None, podcast_repository, None, user_repository)
    with pytest.raises(NotAuthorizedError) as exception:
        podcast_interactor.get_terms_statuses_by_episode_id("test-episode-1")
    assert exception.value.data == {
        "msg": "This operation is not authorized. Please, log in."
    }
