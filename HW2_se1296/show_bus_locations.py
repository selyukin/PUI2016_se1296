
# Author: Sofiya Elyukin, se1296

# Python Script for Assignment 1 of HW2 for PUI2016

#import necessary libraries
from __future__ import print_function
import json
import sys
import urllib2

#set variables
MTA_KEY = sys.argv[1]
BUS_LINE = sys.argv[2]
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(MTA_KEY, BUS_LINE)
    
response = urllib2.urlopen(url)
data = response.read().decode("utf-8")

dataDict = json.loads(data)

#got these two lines of code from Sebastian, sbg389. Understood the concept, but was having trouble getting the correct path.
trail = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'] 
BusQuantity = len(trail[0]['VehicleActivity'])

print ('Bus Line : %s' %BUS_LINE)
print ('Number of Active Buses : %s' %BusQuantity)

for i in range (0, BusQuantity):
    print ('Bus %s is at latitude %s and longitude %s' % (i, (trail[0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']), (trail[0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])))