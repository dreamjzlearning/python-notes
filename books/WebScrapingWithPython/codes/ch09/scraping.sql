-- create db
CREATE DATABASE IF NOT EXISTS scraping CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- select db
USE scraping;

-- create table pages
CREATE TABLE IF NOT EXISTS pages (
    id BIGINT(7) NOT NULL AUTO_INCREMENT,
    title VARCHAR(200),
    content VARCHAR(10000),
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- table info
DESCRIBE pages;

-- insert test data
INSERT INTO
    pages (title, content)
VALUES
    ("test_title", "test_content");

-- search 
SELECT
    *
FROM
    pages;