from src.domain.interactor.podcast_interactor import PodcastInteractor
from src.domain.repository.podcast_repository import PodcastRepository
from src.domain.repository.events_repository import EventsRepository
import json


def test_should_return_an_empty_list_if_there_are_not_listened_podcasts_yet(database):
    events_repository = EventsRepository(None, database)
    podcast_repository = PodcastRepository(None, database)
    podcast_interactor = PodcastInteractor(
        None, podcast_repository, events_repository)
    all_podcasts = podcast_interactor.get_all_podcasts(by="popularity")
    assert all_podcasts == []


def test_should_return_all_the_listened_podcasts_order_by_popularity(database):
    database.executescript(f"""
    INSERT INTO events (user_id, timestamp, type, data) values 
        ("user-1", "2021-05-18T10:23:39Z", "listen", '{json.dumps({"episode_id": "test-episode-1"})}'),
        ("user-1", "2021-05-19T10:23:39Z", "listen", '{json.dumps({"episode_id": "test-episode-2"})}'),
        ("user-1", "2021-05-20T10:23:39Z", "listen", '{json.dumps({"episode_id": "test-episode-2"})}'),
        ("user-1", "2021-05-21T10:23:39Z", "listen", '{json.dumps({"episode_id": "test-episode-2"})}'),
        ("user-1", "2021-05-22T10:23:39Z", "listen", '{json.dumps({"episode_id": "test-episode-3"})}'),
        ("user-1", "2021-05-23T10:23:39Z", "listen", '{json.dumps({"episode_id": "test-episode-3"})}'),
        ("user-1", "2021-05-24T10:23:39Z", "listen", '{json.dumps({"episode_id": "test-episode-2"})}'),
        ("user-1", "2021-05-24T10:23:39Z", "listen", '{json.dumps({"episode_id": "test-episode-4"})}'),
        ("user-1", "2021-05-24T10:23:39Z", "listen", '{json.dumps({"episode_id": "test-episode-2"})}'),
        ("user-1", "2021-05-24T10:23:39Z", "listen", '{json.dumps({"episode_id": "test-episode-6"})}'),
        ("user-1", "2021-05-24T10:23:39Z", "listen", '{json.dumps({"episode_id": "test-episode-7"})}'),
        ("user-1", "2021-05-24T10:23:39Z", "listen", '{json.dumps({"episode_id": "test-episode-8"})}');

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
    events_repository = EventsRepository(None, database)
    podcast_repository = PodcastRepository(None, database)
    podcast_interactor = PodcastInteractor(
        None, podcast_repository, events_repository)
    all_podcasts = podcast_interactor.get_all_podcasts(by="popularity")
    assert len(all_podcasts) == 4
    assert all_podcasts[0].id == "test-podcast-2"
    assert all_podcasts[1].id == "test-podcast-3"
    assert all_podcasts[2].id == "test-podcast-4"
    assert all_podcasts[3].id == "test-podcast-1"
