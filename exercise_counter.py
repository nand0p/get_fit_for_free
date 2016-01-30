#!/usr/bin/python

push_ups = 10
sit_ups = 25
pull_ups = 0
day = 1
year = 1

print "get fit for free"

while year <= 3:
    while day <= 365:
        print "\nyear %d day %d push_ups %d" % (year, day, push_ups)
        print "year %d day %d sit_ups %d" % (year, day, sit_ups)
        print "year %d day %d pull_ups %d" % (year, day, pull_ups)
        day = day + 1
        push_ups = push_ups + 1
        sit_ups = sit_ups + 2
        if day % 7 == 0:
            pull_ups = pull_ups + 1
    day = 1
    year = year + 1
