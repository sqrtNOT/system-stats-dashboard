# Mach GoGoGo
System monitoring using the Ookla Speedtest API

The Data Pipeline for this project is
1. Cron job executes the python script every 5 minutes on a Linux machine
2. Script connects to the Ookla servers, runs the test, and stores the data in a mariadb database
3. Timeseries data is consumed by a grafana dashboard

# Cron config
`*/5     *       *       *       *       /path/to/speed.py`

# SQL config
```
create database stats;
use stats;
create table speedtest (ping float, upload bigint, download bigint, testedon datetime default current_timestamp primary key);
create user 'speedy'@'localhost' identified by htI3V03xesIcATC8gsuTVd5eM5ImyddgxrvNw3bVjcat3QtK;
grant insert on speedtest to 'speedy'@'localhost';
```
