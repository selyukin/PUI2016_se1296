
# Author: Sofiya Elyukin, se1296

# Python Script for Assignment 1 of HW2.

# The first three sections are taken from the NYC Weather API example, adjusted for the MTA data parameters.
# https://github.com/fedhere/PUI2016_fb55/blob/master/Lab2_fb55/NYCweatherAPI.py

# 1. Import necessary libraries
from __future__ import print_function
import json
import sys
import urllib2

# 2. Set variables
MTA_KEY = sys.argv[1]
BUS_LINE = sys.argv[2]
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(MTA_KEY, BUS_LINE)

# 3. Get the data
response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
dataDict = json.loads(data)

#4. Determine the quantity of active buses for the specified line
# I got these two lines of code from Sebastian, sbg389 
# (https://github.com/sbg389/PUI2016_sbg389/blob/master/HW2_sbg389/show_bus_locations_sbg389.py). I understood what needed to be done as far 
# as getting to a specific element, but was having trouble getting the correct path through the dictionaries/lists.
trail = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'] 
BusQuantity = len(trail[0]['VehicleActivity'])

print ('Bus Line : %s' %BUS_LINE)
print ('Number of Active Buses : %s' %BusQuantity)

# 5. Get the location of each active bus of the given line
# I knew a for loop was necessary, but again struggled with specifying the correct path to Lat/Lon. Took that from Sebastian's script,
# but formatted my own print statement.
for i in range (0, BusQuantity):
    print ('Bus %s is at latitude %s and longitude %s' % (i, (trail[0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']), (trail[0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])))