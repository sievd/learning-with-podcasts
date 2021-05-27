class PodcastEpisode:
    def __init__(self, episode_id, title, podcast_id, author_id, release_date, audio, transcript):
        self.episode_id = episode_id
        self.title = title
        self.podcast_id = podcast_id
        self.author_id = author_id
        self.release_date = release_date
        self.audio = audio
        self.transcript = transcript
