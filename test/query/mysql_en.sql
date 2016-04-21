$ mysql -uroot -p

mysql> create database dress DEFAULT CHARACTER SET utf8;


CREATE TABLE `docclass_cc` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `category` varchar(64) NOT NULL COMMENT 'category name',
    `count` int(11) unsigned NOT NULL DEFAULT '1' COMMENT 'category count',
    PRIMARY KEY (`id`),
    UNIQUE KEY `category` (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='keep a count of each category';

CREATE TABLE `docclass_fc` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `feature` varchar(64) NOT NULL COMMENT 'feature name',
    `category` varchar(64) NOT NULL COMMENT 'category name',
    `count` int(11) unsigned NOT NULL DEFAULT '1' COMMENT 'feature count',
    PRIMARY KEY (`id`),
    UNIQUE KEY `feature` (`feature`,`category`),
    KEY `idx_feature` (`feature`),
    KEY `idx_category` (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='keep a count of each feature';

CREATE TABLE `docclass_fisher` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `category` varchar(64) NOT NULL COMMENT 'category name',
    `minimum` double NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `category` (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='keep a setting for fisher classification';

CREATE TABLE `docclass_naivebayes` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `category` varchar(64) NOT NULL COMMENT 'category name',
    `threshold` double NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `threshold` (`threshold`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='keep a setting for fisher naivebayes';

CREATE TABLE `wiki_title` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL DEFAULT '' COMMENT 'title',
    `locale` varchar(2) NOT NULL DEFAULT '',
    PRIMARY KEY (`id`),
    KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='store wiki title';


mysql> exit