BEGIN TRANSACTION;

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
    image_filename varchar,
    title varchar, 
    description varchar,
    category_id varchar,
    FOREIGN KEY ("category_id") REFERENCES podcasts_categories("category_id")
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
COMMIT;