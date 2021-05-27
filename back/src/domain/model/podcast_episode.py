class PodcastEpisode:
    def __init__(self, episode_id, podcast_id, author, release_date, duration=None):
        self.episode_id = episode_id
        self.podcast_id = podcast_id
        self.author = author
        self.release_date = release_date
        self.duration = duration
