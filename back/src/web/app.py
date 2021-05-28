from src.lib.web import create_app, request, create_access_token, json_response
from flask import Flask, request, send_from_directory  # type: ignore
from pathlib import Path

from config import config

from src.domain.interactor.podcast_interactor import PodcastInteractor
from src.domain.repository.podcast_repository import PodcastRepository
from src.domain.interactor.user_interactor import UserInteractor
from src.domain.repository.user_repository import UserRepository
from src.domain.repository.events_repository import EventsRepository

app = create_app(config)

user_repository = UserRepository(
    config, get_current_user_id=app.get_current_user_id)
user_interactor = UserInteractor(config, user_repository)
events_repository = EventsRepository(config)
podcast_repository = PodcastRepository(config)
podcast_interactor = PodcastInteractor(
    config, podcast_repository, events_repository, user_repository)


@app.route("/api/static/pictures/<filename>")
def picture_by_filename_get(filename):
    try:
        return send_from_directory(
            Path(config["root_path"]) / config["pictures"], filename
        )
    except FileNotFoundError:
        return "", 404


@app.route("/api/static/audios/<filename>")
def audio_by_filename_get(filename):
    try:
        return send_from_directory(
            Path(config["root_path"]) / config["audios"], filename
        )
    except FileNotFoundError:
        return "", 404


@app.route("/")
def home():
    return "magic ..."


@app.route("/api/auth/login", methods=["POST"])
def auth_login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = user_interactor.auth_user(username, password)
    user.picture = f"/api/static/pictures/{user.picture}"
    access_token = create_access_token(identity=user.id)
    return json_response({"access_token": access_token, "user": user})


@app.route("/api/users/<user_id>/podcasts", methods=["GET"])
def user_podcasts_get(user_id):
    status = request.args.get("status")
    if status == "active":
        all_podcasts = podcast_interactor.get_latests_listened_podcasts_in_the_library()
    else:
        all_podcasts = podcast_interactor.get_all_podcast_in_the_library()
    for podcast in all_podcasts:
        podcast.image = f"/api/static/pictures/{podcast.image}"
    return json_response(all_podcasts), 200


@app.route("/api/users/<user_id>/authors", methods=["GET"])
def user_authors_get(user_id):
    all_authors = podcast_interactor.get_all_authors_in_the_library()
    for author in all_authors:
        author.image = f"/api/static/pictures/{author.image}"
    return json_response(all_authors), 200


@app.route("/api/podcasts", methods=["GET"])
def podcasts_get():
    by = request.args.get("by")
    popular_podcasts = podcast_interactor.get_all_podcasts(by=by)
    for podcast in popular_podcasts:
        podcast.image = f"/api/static/pictures/{podcast.image}"
    return json_response(popular_podcasts), 200


@app.route("/api/podcasts/<id>", methods=["GET"])
def podcast_by_id_get(id):
    podcast = podcast_interactor.get_podcast_by_id(id)
    podcast.image = f"/api/static/pictures/{podcast.image}"
    return json_response(podcast), 200


@app.route("/api/podcasts/<id>/episodes", methods=["GET"])
def podcast_episodes_by_id_get(id):
    episodes = podcast_interactor.get_all_episodes_by_podcast_id(id)
    return json_response(episodes), 200


@app.route("/api/episodes/<id>", methods=["GET"])
def episode_by_id_get(id):
    episode = podcast_interactor.get_episode_by_id(id)
    episode.audio = f"/api/static/audios/{episode.audio}"
    return json_response(episode), 200


@app.route("/api/episodes/<id>/statuses", methods=["GET"])
def statuses_by_episode_id_get(id):
    statuses = podcast_interactor.get_terms_statuses_by_episode_id(id)
    return json_response(statuses), 200
