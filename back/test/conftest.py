import pytest  # type: ignore

import sqlite3

from src.domain.model.user import hash_password


@pytest.fixture
def database():
    conn = sqlite3.connect(":memory:")
    conn.executescript(
        f"""
       DROP TABLE IF EXISTS users;
        CREATE TABLE users (
            id varchar primary key,
            username varchar,
            image_filename varchar,
            name varchar,
            password varchar,
            is_admin boolean
        );

        DROP TABLE IF EXISTS events;
        CREATE TABLE events (
            user_id varchar,
            timestamp varchar,
            type varchar,
            data varchar
        );

        DROP TABLE IF EXISTS podcasts_categories;
        CREATE TABLE podcasts_categories (
            category_id varchar primary key,
            name varchar,
            description varchar,
            image_filename varchar
        );

        DROP TABLE IF EXISTS authors;
        CREATE TABLE authors (
            id varchar primary key,
            name varchar,
            bio varchar,
            image_filename varchar
        );

        DROP TABLE IF EXISTS podcasts;
        CREATE TABLE podcasts (
            podcast_id varchar primary key,
            author_id varchar,
            image_filename varchar,
            title varchar, 
            description varchar,
            category_id varchar,
            lang_code varchar,
            FOREIGN KEY ("author_id") REFERENCES authors("id"),
            FOREIGN KEY ("category_id") REFERENCES podcasts_categories("category_id"),
            FOREIGN KEY ("lang_code") REFERENCES languages("lang_code")
        );

        DROP TABLE IF EXISTS podcasts_episodes;
        CREATE TABLE podcasts_episodes (
            episode_id varchar primary key,
            title varchar,
            podcast_id varchar,
            author_id varchar,
            release_date varchar,
            audio_filename varchar,
            transcript varchar,
            FOREIGN KEY ("podcast_id") REFERENCES podcasts("podcast_id"),
            FOREIGN KEY ("author_id") REFERENCES authors("id")
        );

        DROP TABLE IF EXISTS user_libraries;
        CREATE TABLE user_libraries (
            podcast_id varchar,
            user_id varchar,
            FOREIGN KEY ("podcast_id") REFERENCES podcasts("podcast_id"),
            FOREIGN KEY ("user_id") REFERENCES users("user_id")
        );

        DROP TABLE IF EXISTS languages;
        CREATE TABLE languages (
            lang_code varchar primary key,
            name varchar
        );

        DROP TABLE IF EXISTS terms;
        CREATE TABLE terms (
            term varchar,
            lang_code varchar,
            status integer NOT NULL,
            user_id varchar,
            FOREIGN KEY ("lang_code") REFERENCES languages("lang_code"),
            FOREIGN KEY ("user_id") REFERENCES users("user_id")
        );

        INSERT INTO users (id, username, image_filename, name, password, is_admin) values 
            ("user-1", "user-1@example.com", "picture-1.jpg", "User 1", '{hash_password("user-1-password")}', 1),
            ("user-2", "user-2@example.com", "picture-2.jpg", "User 2", '{hash_password("user-2-password")}', 0),
            ("user-3", "user-3@example.com", "picture-3.jpg", "User 3", '{hash_password("user-3-password")}', 0),
            ("user-4", "user-4@example.com", "picture-4.jpg", "User 4", '{hash_password("user-4-password")}', 0);
        """
    )
    return conn
