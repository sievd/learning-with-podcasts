BEGIN TRANSACTION;

DELETE FROM users;
INSERT INTO users (id, username, picture, name, password, is_admin) values 
    ("user-1", "user-1@example.com", "picture-1.png", "User 1", '{hash_password[user-1-password]}', 1),
    ("user-2", "user-2@example.com", "picture-2.jpeg", "User 2", '{hash_password[user-2-password]}', 0),
    ("user-3", "user-3@example.com", "picture-3.png", "User 3", '{hash_password[user-3-password]}', 0),
    ("user-4", "user-4@example.com", "picture-4.png", "User 4", '{hash_password[user-4-password]}', 0);

DELETE FROM podcasts_categories;
INSERT INTO podcasts_categories (category_id, name, description) values
    ("test-category-1", "Test category 1", "Description of the category 1"),
    ("test-category-2", "Test category 2", "Description of the category 2"),
    ("test-category-3", "Test category 3", "Description of the category 3"),
    ("test-category-4", "Test category 4", "Description of the category 4");

DELETE FROM podcasts;
INSERT INTO podcasts (podcast_id, image_filename, title, description, category_id) values
    ("test-podcast-1", "test_picture_1.jpg", "Title of podcast 1", "Description of podcast 1", "test-category-1"),
    ("test-podcast-2", "test_picture_2.jpg", "Title of podcast 2", "Description of podcast 2", "test-category-2"),
    ("test-podcast-3", "test_picture_3.jpg", "Title of podcast 3", "Description of podcast 3", "test-category-3"),
    ("test-podcast-4", "test_picture_4.jpg", "Title of podcast 4", "Description of podcast 4", "test-category-4");

DELETE FROM podcasts_episodes;
INSERT INTO podcasts_episodes (episode_id, podcast_id) values
    ("test-episode-1", "test-podcast-1"),
    ("test-episode-2", "test-podcast-2"),
    ("test-episode-3", "test-podcast-3"),
    ("test-episode-4", "test-podcast-4"),
    ("test-episode-5", "test-podcast-1"),
    ("test-episode-6", "test-podcast-2"),
    ("test-episode-7", "test-podcast-3"),
    ("test-episode-8", "test-podcast-4");

DELETE FROM user_libraries;
INSERT INTO user_libraries (podcast_id, user_id) values
    ("test-episode-1", "user-1"),
    ("test-episode-2", "user-1"),
    ("test-episode-3", "user-1"),
    ("test-episode-4", "user-1"),
    ("test-episode-5", "user-1"),
    ("test-episode-6", "user-1");

INSERT INTO events (user_id, timestamp, type, data) values 
    ("user-1", "2021-05-18T10:23:39Z", "listen", '{episode_id[test-episode-1]}'),
    ("user-1", "2021-05-19T10:23:39Z", "listen", '{episode_id[test-episode-2]}'),
    ("user-1", "2021-05-20T10:23:39Z", "listen", '{episode_id[test-episode-2]}'),
    ("user-1", "2021-05-21T10:23:39Z", "listen", '{episode_id[test-episode-2]}'),
    ("user-1", "2021-05-22T10:23:39Z", "listen", '{episode_id[test-episode-3]}'),
    ("user-1", "2021-05-23T10:23:39Z", "listen", '{episode_id[test-episode-3]}'),
    ("user-1", "2021-05-24T10:23:39Z", "listen", '{episode_id[test-episode-2]}'),
    ("user-1", "2021-05-24T10:23:39Z", "listen", '{episode_id[test-episode-4]}'),
    ("user-1", "2021-05-24T10:23:39Z", "listen", '{episode_id[test-episode-2]}'),
    ("user-1", "2021-05-24T10:23:39Z", "listen", '{episode_id[test-episode-6]}'),
    ("user-1", "2021-05-24T10:23:39Z", "listen", '{episode_id[test-episode-7]}'),
    ("user-1", "2021-05-24T10:23:39Z", "listen", '{episode_id[test-episode-8]}');

COMMIT;
