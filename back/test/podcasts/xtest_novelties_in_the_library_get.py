from src.domain.interactor.podcast_interactor import PodcastInteractor
from src.domain.repository.podcast_repository import PodcastRepository
from src.domain.repository.events_repository import EventsRepository
import json


def test_should_return_an_empty_list_if_there_are_not_new_episodes_yet(database):
    events_repository = EventsRepository(None, database)
    podcast_repository = PodcastRepository(None, database)
    podcast_interactor = PodcastInteractor(
        None, podcast_repository, events_repository)
    all_podcasts = podcast_interactor.get_novelties_in_the_library()
    assert all_podcasts == []
