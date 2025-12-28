CREATE DATABASE incident_db;
use incident_db;
CREATE USER 'incident_user'@'localhost'
IDENTIFIED WITH mysql_native_password BY 'incident123';
DROP TABLE IF EXISTS incident_status_history;
DROP TABLE IF EXISTS incidents;
DROP TABLE IF EXISTS admin_users;

SHOW TABLES;

DESCRIBE incidents;
DESCRIBE incident_status_history;

SELECT * FROM incidents;

GRANT ALL PRIVILEGES ON incident_db.* TO 'incident_user'@'localhost';

FLUSH PRIVILEGES;
