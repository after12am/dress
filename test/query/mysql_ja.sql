$ mysql -uroot -p

mysql> create database dress DEFAULT CHARACTER SET utf8;


CREATE TABLE `docclass_cc` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `category` varchar(64) NOT NULL COMMENT 'カテゴリ名',
    `count` int(11) unsigned NOT NULL DEFAULT '1' COMMENT 'カウント数',
    PRIMARY KEY (`id`),
    UNIQUE KEY `category` (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='各カテゴリのカウントを保持';

CREATE TABLE `docclass_fc` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `feature` varchar(64) NOT NULL COMMENT '特徴',
    `category` varchar(64) NOT NULL COMMENT 'カテゴリ名',
    `count` int(11) unsigned NOT NULL DEFAULT '1' COMMENT 'カウント数',
    PRIMARY KEY (`id`),
    UNIQUE KEY `feature` (`feature`,`category`),
    KEY `idx_feature` (`feature`),
    KEY `idx_category` (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='各特徴のカウントを保持';

CREATE TABLE `docclass_fisher` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `category` varchar(64) NOT NULL COMMENT 'カテゴリ名',
    `minimum` double NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `category` (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='フィッシャー分類の設定を保持';

CREATE TABLE `docclass_naivebayes` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `category` varchar(64) NOT NULL COMMENT 'カテゴリ名',
    `threshold` double NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `threshold` (`threshold`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='ナイーブベイズ分類の設定を保持';

CREATE TABLE `wiki_title` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL DEFAULT '' COMMENT 'title',
    `locale` varchar(2) NOT NULL DEFAULT '',
    PRIMARY KEY (`id`),
    KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='store wiki title';


mysql> exit