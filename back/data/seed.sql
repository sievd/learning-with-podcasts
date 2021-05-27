BEGIN TRANSACTION;

DELETE FROM users;
INSERT INTO users (id, username, image_filename, name, password, is_admin) values 
    ("user-1", "user-1@example.com", "picture-1.png", "User 1", '{hash_password[user-1-password]}', 1),
    ("user-2", "user-2@example.com", "picture-2.jpeg", "User 2", '{hash_password[user-2-password]}', 0),
    ("user-3", "user-3@example.com", "picture-3.png", "User 3", '{hash_password[user-3-password]}', 0),
    ("user-4", "user-4@example.com", "picture-4.png", "User 4", '{hash_password[user-4-password]}', 0);

DELETE FROM podcasts_categories;
INSERT INTO podcasts_categories (category_id, name, description, image_filename) values
    ("test-category-1", "Test category 1", "Description of the category 1", "test_category_1.jpeg"),
    ("test-category-2", "Test category 2", "Description of the category 2", "test_category_2.jpeg"),
    ("test-category-3", "Test category 3", "Description of the category 3", "test_category_3.jpeg"),
    ("test-category-4", "Test category 4", "Description of the category 4", "test_category_4.jpeg"),
    ("test-category-5", "Test category 5", "Description of the category 5", "test_category_5.jpeg"),
    ("test-category-6", "Test category 6", "Description of the category 6", "test_category_6.jpeg"),
    ("test-category-7", "Test category 7", "Description of the category 7", "test_category_7.jpeg"),
    ("test-category-8", "Test category 8", "Description of the category 8", "test_category_8.jpeg"),
    ("test-category-9", "Test category 9", "Description of the category 9", "test_category_9.jpeg"),
    ("test-category-10", "Test category 10", "Description of the category 10", "test_category_10.jpeg");

DELETE FROM podcasts;
INSERT INTO podcasts (podcast_id, image_filename, title, description, category_id) values
    ("test-podcast-1", "test_picture_1.jpeg", "Title of podcast 1", "Description of podcast 1", "test-category-1"),
    ("test-podcast-2", "test_picture_2.jpeg", "Title of podcast 2", "Description of podcast 2", "test-category-2"),
    ("test-podcast-3", "test_picture_3.jpeg", "Title of podcast 3", "Description of podcast 3", "test-category-3"),
    ("test-podcast-4", "test_picture_4.jpeg", "Title of podcast 4", "Description of podcast 4", "test-category-4"),
    ("test-podcast-5", "test_picture_5.jpeg", "Title of podcast 5", "Description of podcast 5", "test-category-5"),
    ("test-podcast-6", "test_picture_6.jpeg", "Title of podcast 6", "Description of podcast 6", "test-category-6"),
    ("test-podcast-7", "test_picture_7.jpeg", "Title of podcast 7", "Description of podcast 7", "test-category-7"),
    ("test-podcast-8", "test_picture_8.jpeg", "Title of podcast 8", "Description of podcast 8", "test-category-8"),
    ("test-podcast-9", "test_picture_9.jpeg", "Title of podcast 9", "Description of podcast 9", "test-category-9"),
    ("test-podcast-10", "test_picture_10.jpeg", "Title of podcast 10", "Description of podcast 10", "test-category-10"),
    ("test-podcast-11", "test_picture_11.jpeg", "Title of podcast 11", "Description of podcast 11", "test-category-1"),
    ("test-podcast-12", "test_picture_12.jpeg", "Title of podcast 12", "Description of podcast 12", "test-category-2"),
    ("test-podcast-13", "test_picture_13.jpeg", "Title of podcast 13", "Description of podcast 13", "test-category-3"),
    ("test-podcast-14", "test_picture_14.jpeg", "Title of podcast 14", "Description of podcast 14", "test-category-4"),
    ("test-podcast-15", "test_picture_15.jpeg", "Title of podcast 15", "Description of podcast 15", "test-category-5"),
    ("test-podcast-16", "test_picture_16.jpeg", "Title of podcast 16", "Description of podcast 16", "test-category-6"),
    ("test-podcast-17", "test_picture_17.jpeg", "Title of podcast 17", "Description of podcast 17", "test-category-7"),
    ("test-podcast-18", "test_picture_18.jpeg", "Title of podcast 18", "Description of podcast 18", "test-category-8"),
    ("test-podcast-19", "test_picture_19.jpeg", "Title of podcast 19", "Description of podcast 19", "test-category-9"),
    ("test-podcast-20", "test_picture_20.jpeg", "Title of podcast 20", "Description of podcast 20", "test-category-10"),
    ("test-podcast-21", "test_picture_21.jpeg", "Title of podcast 21", "Description of podcast 21", "test-category-1"),
    ("test-podcast-22", "test_picture_22.jpeg", "Title of podcast 22", "Description of podcast 22", "test-category-2"),
    ("test-podcast-23", "test_picture_23.jpeg", "Title of podcast 23", "Description of podcast 23", "test-category-3"),
    ("test-podcast-24", "test_picture_24.jpeg", "Title of podcast 24", "Description of podcast 24", "test-category-4"),
    ("test-podcast-25", "test_picture_25.jpeg", "Title of podcast 25", "Description of podcast 25", "test-category-5"),
    ("test-podcast-26", "test_picture_26.jpeg", "Title of podcast 26", "Description of podcast 26", "test-category-6"),
    ("test-podcast-27", "test_picture_27.jpeg", "Title of podcast 27", "Description of podcast 27", "test-category-7"),
    ("test-podcast-28", "test_picture_28.jpeg", "Title of podcast 28", "Description of podcast 28", "test-category-8"),
    ("test-podcast-29", "test_picture_29.jpeg", "Title of podcast 29", "Description of podcast 29", "test-category-9"),
    ("test-podcast-30", "test_picture_30.jpeg", "Title of podcast 30", "Description of podcast 30", "test-category-10");

DELETE FROM podcasts_episodes;
INSERT INTO podcasts_episodes (episode_id, podcast_id) values
    ("test-episode-1", "test-podcast-1"),
    ("test-episode-2", "test-podcast-2"),
    ("test-episode-3", "test-podcast-3"),
    ("test-episode-4", "test-podcast-4"),
    ("test-episode-5", "test-podcast-1"),
    ("test-episode-6", "test-podcast-2"),
    ("test-episode-7", "test-podcast-3"),
    ("test-episode-8", "test-podcast-4"),
    ("test-episode-9", "test-podcast-5"),
    ("test-episode-10", "test-podcast-6"),
    ("test-episode-11", "test-podcast-7"),
    ("test-episode-12", "test-podcast-8"),
    ("test-episode-13", "test-podcast-8"),
    ("test-episode-14", "test-podcast-8"),
    ("test-episode-15", "test-podcast-9"),
    ("test-episode-16", "test-podcast-10"),
    ("test-episode-17", "test-podcast-11"),
    ("test-episode-18", "test-podcast-12"),
    ("test-episode-19", "test-podcast-13"),
    ("test-episode-20", "test-podcast-13"),
    ("test-episode-21", "test-podcast-13"),
    ("test-episode-22", "test-podcast-13"),
    ("test-episode-23", "test-podcast-14"),
    ("test-episode-24", "test-podcast-15"),
    ("test-episode-25", "test-podcast-16");

DELETE FROM user_libraries;
INSERT INTO user_libraries (podcast_id, user_id) values
    ("test-podcast-1", "user-1"),
    ("test-podcast-2", "user-1"),
    ("test-podcast-3", "user-1"),
    ("test-podcast-4", "user-1"),
    ("test-podcast-5", "user-1"),
    ("test-podcast-6", "user-1"),
    ("test-podcast-8", "user-1"),
    ("test-podcast-9", "user-1"),
    ("test-podcast-10", "user-1"),
    ("test-podcast-11", "user-1"),
    ("test-podcast-12", "user-1"),
    ("test-podcast-13", "user-1");

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
    ("user-1", "2021-05-25T10:23:39Z", "listen", '{episode_id[test-episode-12]}'),
    ("user-1", "2021-05-26T10:23:39Z", "listen", '{episode_id[test-episode-13]}'),
    ("user-1", "2021-05-27T10:23:39Z", "listen", '{episode_id[test-episode-14]}'),
    ("user-1", "2021-05-28T10:23:39Z", "listen", '{episode_id[test-episode-15]}'),
    ("user-1", "2021-05-29T10:23:39Z", "listen", '{episode_id[test-episode-16]}'),
    ("user-1", "2021-05-20T10:23:39Z", "listen", '{episode_id[test-episode-17]}');
COMMIT;
