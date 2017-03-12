# Python SLA Calculator
## Overview
A little project I threw together after reading about an HP storage system purporting to deliver 14 nines of uptime (99.999999999%). I wondered how much downtime this would actually allow in a year, so worked it out the hard way; by writing a script to work it out :)
## Pre-requisites
I wrote and tested this with Python 2.7.10, on macOS, the only packages this uses are `sys` and `math` so this will not require pip to install any packages
## Running the script
Once downloaded, the script will need to be made executable:
```
chmod +x ./downtime_calc.py
```
It can then be run as follows:
* No parameters passed - will return the following:
```
Icarus:Python root$ ./downtime_calc.py
No input received, or input was not a number, defaulting to 5
Result is: a 5 nines SLA ( 99.999 % ) allows for 5.256 minutes of downtime per year
Icarus:Python root$
```
* A single numerical parameter passed, between 1 and 16, this will return the following:
```
Icarus:Python root$ ./downtime_calc.py 7
Result is: a 7 nines SLA ( 99.99999 % ) allows for 3.1536 seconds of downtime per year
Icarus:Python root$
```
