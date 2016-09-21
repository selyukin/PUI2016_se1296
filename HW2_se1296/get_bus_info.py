
# Author: Sofiya Elyukin, se1296

# Python Script for Assignment 2 of HW2.

# The first three sections are taken from the NYC Weather API example, adjusted for the MTA data parameters.
# https://github.com/fedhere/PUI2016_fb55/blob/master/Lab2_fb55/NYCweatherAPI.py

# 1. Import necessary libraries
from __future__ import print_function
import json
import sys
import urllib2
from pandas import DataFrame
import pandas as pd

# 2. Set variables
MTA_KEY = sys.argv[1]
BUS_LINE = sys.argv[2]
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(MTA_KEY, BUS_LINE)

# 3. Get the data
response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
dataDict = json.loads(data)

#4. Determine the quantity of active buses for the specified line
# Adjusted Sebastian's code now that I have a better understanding of the path
eachBus = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
BusQuantity = len(eachBus)


'''# Testing before exporting to CSV
# 5. Get the detailed location information of each active bus of the given line
# Adjusted the code from Assignment 1
for i in range (0, BusQuantity):
    Latitude = eachBus[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    Longitude = eachBus[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    Stop = eachBus[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    Distance = eachBus[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    print ('Bus %s is at latitude %s and longitude %s, %s from %s' % (i, Latitude, Longitude, Distance, Stop))'''

# Create CSV file for Assignment 2 output
# Code a mixture of PandasDataWrangling from \ https://github.com/fedhere/UInotebooks/blob/master/dataWrangling/PandasDataWrangling-Chap7.ipynb and Sebastian's code. \ The need for an If/Else within the For loop in order to enable an "N/A" value was realized jointly during a discussion with Sebastian, Jonathan, and Fernando.
df = DataFrame(columns=['Latitude', 'Longitude', 'Stop', 'Distance'])

for i in range (0, BusQuantity):
    df.loc[i, 'Latitude'] = eachBus[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    df.loc[i, 'Longitude'] = eachBus[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    if (eachBus[i]['MonitoredVehicleJourney']['OnwardCalls']!={}):
        df.loc[i, 'Stop'] = eachBus[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        df.loc[i, 'Distance'] = eachBus[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    else: 
        df.loc[i, 'Stop'] = 'N/A'
        df.loc[i, 'Stop'] = 'N/A'

df.to_csv(sys.argv[3], index=False)