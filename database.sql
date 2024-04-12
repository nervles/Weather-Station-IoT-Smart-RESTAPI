CREATE TABLE `weather_station` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `location` varchar(255)
);

CREATE TABLE `mes` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `temperature` float,
  `humidity` float,
  `created_at` timestamp,
  `device_id` int
);

ALTER TABLE `mes` ADD FOREIGN KEY (`device_id`) REFERENCES `weather_station` (`id`);
