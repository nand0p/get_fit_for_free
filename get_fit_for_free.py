#!/usr/bin/python

import os
import sys
import subprocess

push_ups = 10
sit_ups = 25
pull_ups = 0
day = 1
year = 1

print sys.argv[0]

while year <= 3:
    while day <= 365:
        future = subprocess.check_output("date -d +" + str(day - 1) \
                  + "days +%Y%m%d", shell=True).strip()
        print "\nyear %d day %d (%s) push_ups %d" \
               % (year, day, future, push_ups)
        print "year %d day %d (%s) sit_ups %d" \
               % (year, day, future, sit_ups)
        print "year %d day %d (%s) pull_ups %d" \
               % (year, day, future, pull_ups)
        day = day + 1
        push_ups = push_ups + 1
        sit_ups = sit_ups + 2
        if day % 7 == 0:
            pull_ups = pull_ups + 1
    day = 1
    year = year + 1
