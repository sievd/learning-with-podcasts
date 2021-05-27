from src.domain.interactor.podcast_interactor import PodcastInteractor
from src.domain.repository.podcast_repository import PodcastRepository
from src.domain.repository.events_repository import EventsRepository
from src.lib.errors import NotFoundError
import json
import pytest


def test_should_return_an_empty_list_if_there_are_not_episodes_of_the_podcast_yet(database):
    database.executescript(f"""
    INSERT INTO podcasts (podcast_id, image_filename, title, description, category_id) values
        ("test-podcast-1", "test_picture_1.jpg", "Title of podcast 1", "Description of podcast 1", "test-category-1"),
        ("test-podcast-2", "test_picture_2.jpg", "Title of podcast 2", "Description of podcast 2", "test-category-2"),
        ("test-podcast-3", "test_picture_3.jpg", "Title of podcast 3", "Description of podcast 3", "test-category-1"),
        ("test-podcast-4", "test_picture_4.jpg", "Title of podcast 4", "Description of podcast 4", "test-category-3"),
        ("test-podcast-5", "test_picture_5.jpg", "Title of podcast 5", "Description of podcast 5", "test-category-4");

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
    """)
    events_repository = EventsRepository(None, database)
    podcast_repository = PodcastRepository(None, database)
    podcast_interactor = PodcastInteractor(
        None, podcast_repository, events_repository)
    all_podcasts = podcast_interactor.get_all_episodes_by_podcast_id(
        "test-podcast-5")
    assert all_podcasts == []


def test_should_return_all_the_episodes_of_the_podcast_if_there_are_episodes(database):
    database.executescript(f"""
    INSERT INTO podcasts (podcast_id, image_filename, title, description, category_id) values
        ("test-podcast-1", "test_picture_1.jpg", "Title of podcast 1", "Description of podcast 1", "test-category-1"),
        ("test-podcast-2", "test_picture_2.jpg", "Title of podcast 2", "Description of podcast 2", "test-category-2"),
        ("test-podcast-3", "test_picture_3.jpg", "Title of podcast 3", "Description of podcast 3", "test-category-1"),
        ("test-podcast-4", "test_picture_4.jpg", "Title of podcast 4", "Description of podcast 4", "test-category-3");

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
    """)
    events_repository = EventsRepository(None, database)
    podcast_repository = PodcastRepository(None, database)
    podcast_interactor = PodcastInteractor(
        None, podcast_repository, events_repository)
    all_episodes = podcast_interactor.get_all_episodes_by_podcast_id(
        "test-podcast-1")
    assert len(all_episodes) == 2
    assert all_episodes[0].episode_id == "test-episode-1"
    assert all_episodes[1].episode_id == "test-episode-5"


def test_should_raise_NotFoundError_if_the_podcast_doesnt_exist(database):
    database.executescript(f"""
    INSERT INTO podcasts (podcast_id, image_filename, title, description, category_id) values
        ("test-podcast-1", "test_picture_1.jpg", "Title of podcast 1", "Description of podcast 1", "test-category-1"),
        ("test-podcast-2", "test_picture_2.jpg", "Title of podcast 2", "Description of podcast 2", "test-category-2"),
        ("test-podcast-3", "test_picture_3.jpg", "Title of podcast 3", "Description of podcast 3", "test-category-1"),
        ("test-podcast-4", "test_picture_4.jpg", "Title of podcast 4", "Description of podcast 4", "test-category-3");

    INSERT INTO podcasts_categories (category_id, name, description) values
        ("test-category-1", "Test category 1", "Description of the category 1"),
        ("test-category-2", "Test category 2", "Description of the category 2"),
        ("test-category-3", "Test category 3", "Description of the category 3"),
        ("test-category-4", "Test category 4", "Description of the category 4");

    INSERT INTO podcasts_episodes (episode_id, podcast_id, author_id, release_date, audio_filename, transcript) values
        ("test-episode-1", "test-podcast-1", "test-author-1", "2021-05-18", "test-audio-filename", "test-transcript"),
        ("test-episode-2", "test-podcast-2", "test-author-2", "2021-05-19", "test-audio-filename", "test-transcript"),
        ("test-episode-3", "test-podcast-3", "test-author-3", "2021-05-20", "test-audio-filename", "test-transcript"),
        ("test-episode-4", "test-podcast-4", "test-author-4", "2021-05-21", "test-audio-filename", "test-transcript"),
        ("test-episode-5", "test-podcast-1", "test-author-1", "2021-05-22", "test-audio-filename", "test-transcript"),
        ("test-episode-6", "test-podcast-2", "test-author-2", "2021-05-23", "test-audio-filename", "test-transcript"),
        ("test-episode-7", "test-podcast-3", "test-author-3", "2021-05-24", "test-audio-filename", "test-transcript"),
        ("test-episode-8", "test-podcast-4", "test-author-4", "2021-05-25", "test-audio-filename", "test-transcript");
    """)
    events_repository = EventsRepository(None, database)
    podcast_repository = PodcastRepository(None, database)
    podcast_interactor = PodcastInteractor(
        None, podcast_repository, events_repository)
    with pytest.raises(NotFoundError) as exception:
        podcast_interactor.get_all_episodes_by_podcast_id(
            "non-existent-podcast")
    assert exception.value.data == {
        "msg": "Podcast with id 'non-existent-podcast' not found."
    }
