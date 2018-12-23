-- schema.sql

DROP database if EXISTS awesome;

CREATE DATABASE awesome;

USE awesome;

GRANT SELECT,INSERT,UPDATE,DELETE ON awesome.* to 'www-data'@'localhost' IDENTIFIED BY 'www-data';

CREATE TABLE users (
    `id` VARCHAR
(50) NOT NULL,
    `email` VARCHAR
(50) NOT NULL,
    `passwd` VARCHAR
(50) NOT NULL,
    `admin` bool NOT NULL,
    `name` VARCHAR
(50) NOT NULL,
    `image` VARCHAR
(500) NOT NULL,
    `created_at` REAL NOT NULL,
    UNIQUE KEY `idx_created_at`
(`created_at`),
    PRIMARY KEY
(`id`)
) engine=innodb DEFAULT charset=utf8;

CREATE TABLE blogs (
    `id` VARCHAR
(50) not null,
    `user_id` VARCHAR
(50) NOT NULL,
    `user_name` VARCHAR
(50) NOT NULL,
    `user_image` VARCHAR
(500) NOT NULL,
    `name` VARCHAR
(50) NOT NULL,
    `summary` VARCHAR
(200) NOT NULL,
    `content` mediumtext NOT NULL,
    `created_at` REAL NOT NULL,
    KEY `idx_created_at`
(`created_at`),
    PRIMARY key
(`id`)
 ) engine=innodb DEFAULT charset=utf8;

CREATE TABLE comments (
     `id` VARCHAR
(50) NOT null,
     `blog_id` VARCHAR
(50) NOT null,
     `user_id` varchar
(50) NOT Null,
     `user_name` VARCHAR
(50) NOT Null,
     `user_image` VARCHAR
(500) NOT NULL,
     `content` mediumtext  NOT NULL,
     `created_at` REAL NOT NULL,
     KEY `idx_created_at`
(`created_at`),
     PRIMARY key
(`id`)
 ) engine=innodb DEFAULT charset=utf8;