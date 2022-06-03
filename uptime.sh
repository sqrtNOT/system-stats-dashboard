#!/bin/bash
result=`uptime --pretty`
echo $result
minutes=`grep -oE "[0-9]* minute" <(echo $result)|grep -oE "[0-9]*"`
totaluptime=$minutes

hours=`grep -oE "[0-9]* hour" <(echo $result)|grep -oE "[0-9]*"`
totaluptime="$(($totaluptime + $hours * 60))"

days=`grep -oE "[0-9]* day" <(echo $result)|grep -oe "[0-9]*"`
totaluptime="$(($totaluptime + $days * 24 * 60))"

weeks=`grep -oE "[0-9]* week" <(echo $result)|grep -oe "[0-9]*"`
totaluptime="$(($totaluptime + $weeks * 7 * 24 * 60))"

months=`grep -oE "[0-9]* month" <(echo $result)|grep -oe "[0-9]*"`
totaluptime="$(($totaluptime + $months * 30 * 24 * 60))"

years=`grep -oE "[0-9]* year" <(echo $result)|grep -oe "[0-9]*"`
totaluptime="$(($totaluptime + $years * 365 * 24 * 60))"

echo $totaluptime

mysql --database=stats -u uptime -pQySd1LmQ9GrysxtKNNUI2POFFKBDM6IJ5YmIxX6SSuoUsSHV -e "insert into uptime (uptime) values ($totaluptime)"
