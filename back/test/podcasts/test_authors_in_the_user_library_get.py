from src.domain.interactor.podcast_interactor import PodcastInteractor
from src.domain.repository.podcast_repository import PodcastRepository
from src.domain.repository.events_repository import EventsRepository
from src.domain.repository.user_repository import UserRepository
from src.lib.errors import NotFoundError, NotAuthorizedError
import json
import pytest


def test_should_return_an_empty_list_if_the_user_doesnt_have_saved_podcasts_yet(database):
    events_repository = EventsRepository(None, database)
    podcast_repository = PodcastRepository(None, database)
    user_repository = UserRepository(
        None, database, get_current_user_id=lambda: "user-1")
    podcast_interactor = PodcastInteractor(
        None, podcast_repository, events_repository, user_repository)
    all_authors = podcast_interactor.get_all_authors_in_the_library()
    assert all_authors == []


def test_should_return_the_user_library_if_the_user_have_saved_podcasts(database):
    database.executescript(f"""
    INSERT INTO podcasts (podcast_id, author_id, image_filename, title, description, category_id) values
        ("test-podcast-1", "test-author-1", "test_picture_1.jpg", "Title of podcast 1", "Description of podcast 1", "test-category-1"),
        ("test-podcast-2", "test-author-2", "test_picture_2.jpg", "Title of podcast 2", "Description of podcast 2", "test-category-2"),
        ("test-podcast-3", "test-author-3", "test_picture_3.jpg", "Title of podcast 3", "Description of podcast 3", "test-category-1"),
        ("test-podcast-4", "test-author-4", "test_picture_4.jpg", "Title of podcast 4", "Description of podcast 4", "test-category-3"),
        ("test-podcast-5", "test-author-5", "test_picture_5.jpg", "Title of podcast 5", "Description of podcast 5", "test-category-4");

    INSERT INTO podcasts_categories (category_id, name, description) values
        ("test-category-1", "Test category 1", "Description of the category 1"),
        ("test-category-2", "Test category 2", "Description of the category 2"),
        ("test-category-3", "Test category 3", "Description of the category 3"),
        ("test-category-4", "Test category 4", "Description of the category 4");

    INSERT INTO authors (id, name, bio, image_filename) values
        ("test-author-1", "Test Author 1", "Bio of the test author 1", "test_author_1.jpeg"),
        ("test-author-2", "Test Author 2", "Bio of the test author 2", "test_author_2.jpeg"),
        ("test-author-3", "Test Author 3", "Bio of the test author 3", "test_author_3.jpeg"),
        ("test-author-4", "Test Author 4", "Bio of the test author 4", "test_author_4.jpeg"),
        ("test-author-5", "Test Author 5", "Bio of the test author 5", "test_author_5.jpeg");

    INSERT INTO podcasts_episodes (episode_id, podcast_id, author_id, release_date, audio_filename, transcript) values
        ("test-episode-1", "test-podcast-1", "test-author-1", "2021-05-18", "test-audio-filename", "test-transcript"),
        ("test-episode-2", "test-podcast-2", "test-author-2", "2021-05-19", "test-audio-filename", "test-transcript"),
        ("test-episode-3", "test-podcast-3", "test-author-3", "2021-05-20", "test-audio-filename", "test-transcript"),
        ("test-episode-4", "test-podcast-4", "test-author-4", "2021-05-21", "test-audio-filename", "test-transcript"),
        ("test-episode-5", "test-podcast-1", "test-author-1", "2021-05-22", "test-audio-filename", "test-transcript"),
        ("test-episode-6", "test-podcast-2", "test-author-2", "2021-05-23", "test-audio-filename", "test-transcript"),
        ("test-episode-7", "test-podcast-3", "test-author-3", "2021-05-24", "test-audio-filename", "test-transcript"),
        ("test-episode-8", "test-podcast-4", "test-author-4", "2021-05-25", "test-audio-filename", "test-transcript");

    INSERT INTO user_libraries(podcast_id, user_id) values
        ("test-podcast-1", "user-1"),
        ("test-podcast-3", "user-1"),
        ("test-podcast-4", "user-3");
    """)
    events_repository = EventsRepository(None, database)
    podcast_repository = PodcastRepository(None, database)
    user_repository = UserRepository(
        None, database, get_current_user_id=lambda: "user-1")
    podcast_interactor = PodcastInteractor(
        None, podcast_repository, events_repository, user_repository)
    all_authors = podcast_interactor.get_all_authors_in_the_library()
    assert len(all_authors) == 2
    assert all_authors[0].id == "test-author-1"
    assert all_authors[1].id == "test-author-3"


def test_should_return_NotAuthorizedError_if_the_user_is_not_logged_in(database):
    events_repository = EventsRepository(None, database)
    podcast_repository = PodcastRepository(None, database)
    user_repository = UserRepository(
        None, database, get_current_user_id=lambda: None)
    podcast_interactor = PodcastInteractor(
        None, podcast_repository, events_repository, user_repository)
    with pytest.raises(NotAuthorizedError) as exception:
        podcast_interactor.get_all_authors_in_the_library()
    assert exception.value.data == {
        "msg": "This operation is not authorized. Please, log in."
    }
