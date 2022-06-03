#!/bin/bash
#get CPU temp from sensors utility
tempresult=`sensors -u 2>/dev/null| grep -ia temp1_input: | grep -o '[0-9.]*$'`
echo $tempresult
mysql --database=stats -u sensor -pqj7NdkPtFSiWPhVJcB0odH19ADz2OduRAqk9fmHfyYHspjVL -e "insert into temps (CPU_EDGE) values ($tempresult)"

#get min, max, and average CPU clockspeed from proc
mhzarray=($(grep -i MHz /proc/cpuinfo | awk '{print $4}' | sort -h))
minclock=${mhzarray[0]}
maxclock=${mhzarray[-1]}
sum=0
count=0
IFS='+'
avgclock=$(echo "(${mhzarray[*]})/${#mhzarray[@]}" | bc -l)
echo $minclock $maxclock $avgclock
mysql --database=stats -u hertz -pLfwaU4x0hVSWgJgCAcjJBAnT8fAlYOgO8nVTSUkJSK7qld0o -e "insert into clocks (minclock, maxclock, avgclock) values ($minclock, $maxclock, $avgclock)"
