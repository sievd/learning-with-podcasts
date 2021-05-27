from src.domain.interactor.podcast_interactor import PodcastInteractor
from src.domain.repository.podcast_repository import PodcastRepository
from src.lib.errors import NotFoundError
import pytest


def test_should_get_the_podcast_if_it_exists(database):
    database.executescript(f"""
    INSERT INTO podcasts (podcast_id, image_filename, title, description, category_id) values
        ("test-podcast-1", "test_picture_1.jpg", "Title of podcast 1", "Description of podcast 1", "test-category-1"),
        ("test-podcast-2", "test_picture_2.jpg", "Title of podcast 2", "Description of podcast 2", "test-category-2"),
        ("test-podcast-3", "test_picture_3.jpg", "Title of podcast 3", "Description of podcast 3", "test-category-3"),
        ("test-podcast-4", "test_picture_4.jpg", "Title of podcast 4", "Description of podcast 4", "test-category-4");

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
    podcast_repository = PodcastRepository(None, database)
    podcast_interactor = PodcastInteractor(None, podcast_repository)
    podcast = podcast_interactor.get_podcast_by_id("test-podcast-1")
    assert podcast.id == "test-podcast-1"
    assert podcast.image == "test_picture_1.jpg"
    assert podcast.title == "Title of podcast 1"
    assert podcast.description == "Description of podcast 1"
    assert podcast.category_id == "test-category-1"


def test_should_get_NotFoundError_if_the_podcast_doesnt_exist(database):
    podcast_repository = PodcastRepository(None, database)
    podcast_interactor = PodcastInteractor(None, podcast_repository)
    with pytest.raises(NotFoundError) as exception:
        podcast_interactor.get_podcast_by_id("non-existent-podcast")
    assert exception.value.data == {
        "msg": "Podcast with id 'non-existent-podcast' not found."
    }
