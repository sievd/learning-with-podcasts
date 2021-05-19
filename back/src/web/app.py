from src.lib.web import create_app, request, create_access_token, json_response
from flask import Flask, request, send_from_directory  # type: ignore
from pathlib import Path

from config import config

from src.domain.interactor.task_interactor import TaskInteractor
from src.domain.repository.task_repository import TaskRepository
from src.domain.interactor.user_interactor import UserInteractor
from src.domain.repository.user_repository import UserRepository

app = create_app(config)

task_repository = TaskRepository(config)
task_interactor = TaskInteractor(config, task_repository)
user_repository = UserRepository(
    config, get_current_user_id=app.get_current_user_id)
user_interactor = UserInteractor(config, user_repository)


@app.route("/api/static/images/<filename>")
def picture_by_filename_get(filename):
    try:
        return send_from_directory(
            Path(config["root_path"]) / config["images"], filename=filename
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
    access_token = create_access_token(identity=user.id)
    return json_response({"access_token": access_token, "user": user})


# @app.route("/api/podcats", methods=["GET"])
# def podcasts_get():
#     query = request.args.get("q")


# @app.route("/api/tasks", methods=["GET"])
# def tasks_get():
#     return json_response(task_interactor.get_all_tasks()), 200
