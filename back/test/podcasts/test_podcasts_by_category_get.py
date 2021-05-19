from src.domain.interactor.podcast_interactor import PodcastInteractor
from src.domain.repository.podcast_repository import PodcastRepository
from src.domain.repository.events_repository import EventsRepository
from src.lib.errors import NotFoundError
import json
import pytest


def test_should_return_an_empty_list_if_there_are_not_podcasts_in_the_category_yet(database):
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

    INSERT INTO podcasts_episodes (episode_id, podcast_id) values
        ("test-episode-1", "test-podcast-1"),
        ("test-episode-2", "test-podcast-2"),
        ("test-episode-3", "test-podcast-3"),
        ("test-episode-4", "test-podcast-4"),
        ("test-episode-5", "test-podcast-1"),
        ("test-episode-6", "test-podcast-2"),
        ("test-episode-7", "test-podcast-3"),
        ("test-episode-8", "test-podcast-4");
    """)
    events_repository = EventsRepository(None, database)
    podcast_repository = PodcastRepository(None, database)
    podcast_interactor = PodcastInteractor(
        None, podcast_repository, events_repository)
    all_podcasts = podcast_interactor.get_all_podcasts_by_category(
        "test-category-4")
    assert all_podcasts == []


def test_should_return_all_the_podcasts_in_the_category_if_there_is_data(database):
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

    INSERT INTO podcasts_episodes (episode_id, podcast_id) values
        ("test-episode-1", "test-podcast-1"),
        ("test-episode-2", "test-podcast-2"),
        ("test-episode-3", "test-podcast-3"),
        ("test-episode-4", "test-podcast-4"),
        ("test-episode-5", "test-podcast-1"),
        ("test-episode-6", "test-podcast-2"),
        ("test-episode-7", "test-podcast-3"),
        ("test-episode-8", "test-podcast-4");
    """)
    events_repository = EventsRepository(None, database)
    podcast_repository = PodcastRepository(None, database)
    podcast_interactor = PodcastInteractor(
        None, podcast_repository, events_repository)
    all_podcasts = podcast_interactor.get_all_podcasts_by_category(
        "test-category-1")
    assert len(all_podcasts) == 2
    assert all_podcasts[0].id == "test-podcast-1"
    assert all_podcasts[1].id == "test-podcast-3"


def test_should_raise_NotFoundError_if_the_category_doesnt_exist(database):
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

    INSERT INTO podcasts_episodes (episode_id, podcast_id) values
        ("test-episode-1", "test-podcast-1"),
        ("test-episode-2", "test-podcast-2"),
        ("test-episode-3", "test-podcast-3"),
        ("test-episode-4", "test-podcast-4"),
        ("test-episode-5", "test-podcast-1"),
        ("test-episode-6", "test-podcast-2"),
        ("test-episode-7", "test-podcast-3"),
        ("test-episode-8", "test-podcast-4");
    """)
    events_repository = EventsRepository(None, database)
    podcast_repository = PodcastRepository(None, database)
    podcast_interactor = PodcastInteractor(
        None, podcast_repository, events_repository)
    with pytest.raises(NotFoundError) as exception:
        podcast_interactor.get_all_podcasts_by_category(
            "non-existent-category")
    assert exception.value.data == {
        "msg": "Category with id 'non-existent-category' not found."
    }
