#Author: Gregory Mayes, NYU, September 2016
############################
#Code written to pull tracking information for each vehicle
#on a bus line from the MTA API interface and output formatted results.
#For HW2 of PUI2016.
############################

from __future__ import print_function
import json
import urllib2
import sys
import numpy
import matplotlib
matplotlib.use('agg')
import pylab as pl

#input error message

if not len(sys.argv) == 3:
    print("Invalid number of arguments. Run as: python show_bus_locations.py MTA_KEY BUS_LINE")
    sys.exit()

#Pull json data from MTA bustime
#key = 5d9e7639-7cac-45c2-934d-2f274b5e63c7
    
mtakey = sys.argv[1]
busline = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(mtakey, busline)

response = urllib2.urlopen(url)
data = response.read().decode("utf-8")

#Print Output code by Matt Hart (mattdhart@gmail.com), a personal friend outside of class. I was able to output the longitude and Latitude, 
#but got stuck numbering the buses and getting the total active bus count. My count function would only return 0, see my code below:

#f = pl.figure()
#for it in data1['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
#    print (it['MonitoredVehicleJourney']['VehicleLocation']['Longitude'], it['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
#    
#num_buses = [data1['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']]
#print(num_buses.count(['Monitored']))

def main():
    data1 = json.loads(data)

    # Set up our top level array (M. Hart)
    container = data1['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

    # Make sure we have at least one element (M. Hart)
    if len(container) > 0:
        # Grab the first element in the container and get the line name (M. Hart)
        line_name = container[0]['MonitoredVehicleJourney']['PublishedLineName']
        print("Bus Line : {0}".format(line_name))
    else:
        print("Could not find Bus Line")

    # Once we know we have elements, we can assume each element in the container
    # represents one and just look at the length (M. Hart)
    print("Number of Active Buses : {0}".format(len(container)))

    # Then we can use a nifty builtin function called enumerate to keep track of
    # the index when we loop, in addition to the vehicle name. Instead of
    # returning a single element, it returns a two-element tuple, which we
    # expand inline (M. Hart)
    for idx, elem in enumerate(container):
        lat = elem['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        lon = elem['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        print("Bus {0} is at latitude {1} and longitude {2}".format(idx, lat, lon))


if __name__ == '__main__':
    main()
