#!/usr/bin/python

import sys
import math

# Take and validate input
try:
    numOfNines = int(sys.argv[1])
except:
    print "No input received, or input was not a number, defaulting to 5"
    numOfNines = 5

if numOfNines > 16:
    print "Input was over 16, this will break the code, setting to 5"
    numOfNines = 5
elif numOfNines < 1:
    print "Input was less than 1, this doesn't make sense, setting to 5"
    numOfNines = 5

# Constants
daysPerYear         = 365
hoursPerDay         = 24
minutesPerHour      = 60
secondsPerMinute    = 60
msPerSecond         = 1000
usPerMs             = 1000
nsPerUs             = 1000

# Calculation
def calcDowntime (numOfNines):
  multiplier = float(1 / float(10**numOfNines))
  counter = float(daysPerYear * multiplier)
  unit = "days"
  while counter < 1:
      if unit == "days":
        unit = "hours"
        counter = counter * hoursPerDay
      elif unit == "hours":
        unit = "minutes"
        counter = counter * minutesPerHour
      elif unit == "minutes":
        unit = "seconds"
        counter = counter * secondsPerMinute
      elif unit == "seconds":
        unit = "milliseconds"
        counter = counter * msPerSecond
      elif unit == "milliseconds":
        unit = "microseconds"
        counter = counter * usPerMs
      elif unit == "microseconds":
        unit = "nanoseconds"
        counter = counter * nsPerUs
  strResult = [counter,unit]
  return strResult

# Output
print "Result is: a",numOfNines,"nines SLA (",float(100 - float(1 / float(10**(numOfNines-2)))),"% ) allows for",calcDowntime(numOfNines)[0],calcDowntime(numOfNines)[1],"of downtime per year"
