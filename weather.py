#Kyle Wesoloski
#Wind Speed and Direction webscraper

from stadium import *
from windData import *

def main(hours, locFile):
    urls, numLocations = weatherLocations(locFile)
    locations = getWindData(urls, numLocations, hours)
    writeFile(urls, locations, hours)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError('Please provide the number of hours of weather data desired and a location/url text file.')
    elif len(sys.argv) == 3: 
        locFile = sys.argv[2]
    else:
        stad = getRequest()
        createUrlFile(stad)
        locFile = 'request.txt'
    hours = int(sys.argv[1])
    print('\nloading...\n')
    main(hours, locFile)
    print('Done.')