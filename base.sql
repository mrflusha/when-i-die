Create database VK;
USE VK;

CREATE TABLE post_text(
	id int(254) NOT NULL AUTO_INCREMENT,
	text varchar(16382),
	PRIMARY KEY (id)
);