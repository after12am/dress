$ sqlite3 ~/Desktop/dress.db

CREATE TABLE `docclass_cc` (
    `id` integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    `category` text NOT NULL,
    `count` integer unsigned NOT NULL DEFAULT '1',
    UNIQUE (`category`)
);

CREATE TABLE `docclass_fc` (
    `id` integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    `feature` text NOT NULL COMMENT 'feature name',
    `category` text NOT NULL,
    `count` integer unsigned NOT NULL DEFAULT '1',
    UNIQUE (`feature`,`category`)
);

CREATE TABLE `docclass_fisher` (
    `id` integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    `category` text NOT NULL,
    `minimum` double NOT NULL,
    UNIQUE (`category`)
);

CREATE TABLE `docclass_naivebayes` (
    `id` integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    `category` text NOT NULL,
    `threshold` double NOT NULL,
    UNIQUE (`threshold`)
);

CREATE TABLE `wiki_title` (
    `id` integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` varchar(255) NOT NULL DEFAULT '',
    `locale` varchar(2) NOT NULL DEFAULT ''
);
