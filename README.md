# Mach-GoGoGo
System monitoring using the Ookla Speedtest API

The Data Pipeline for this project is
1. Cron job executes the python script every 5 minutes on a Linux machine
2. Script connects to the Ookla servers, runs the test, and stores the data in a mariadb database
3. Timeseries data is consumed by a grafana dashboard
