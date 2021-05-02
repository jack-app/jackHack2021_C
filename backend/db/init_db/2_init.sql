CREATE TABLE user
(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(128)
);

CREATE TABLE situation_type
(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(1024)
);

CREATE TABLE topic
(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256),
    situation_type_id INT
);

CREATE TABLE question
(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    content VARCHAR(4096),
    topic_id INT,
    situation_type_id INT
);

CREATE TABLE diary
(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    title VARCHAR(128),
    content VARCHAR(4096),
    user_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);