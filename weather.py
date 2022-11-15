#Kyle Wesoloski
#Wind Speed and Direction webscraper

import sys
import requests
from bs4 import BeautifulSoup

#change url to desired location on weather.com 
#example url is for nashville
url = "https://weather.com/weather/hourbyhour/l/11e5d23a774a46624e77e5b3800a3030b94de92607dec513f1e622d6735a4996"

def main():

    #retrieve html page 
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    
    windSpeedDirection = {}

    #get wind speed and direction from html DetailsSummary-wind class tag
    windQuery = soup.findAll('div', attrs={'class': 'DetailsSummary--wind--1tv7t DetailsSummary--extendedData--307Ax'})

    #get time of wind speed and direction with h3 value
    timeQuery = soup.findAll('h3', attrs={'data-testid': 'daypartName'})

    #future hours is the number of hours that will display the wind speed
    #max is 23 since dictionary naming convention uses the time of day at the key
    futureHours = 10

    #append each wind speed and direction to corresponding time. 
    for wind, time in zip(windQuery, timeQuery):
        if futureHours == 0: break

        windParsed = wind.text.replace('Wind', '')

        windParsed = windParsed.replace(' mph', '')

        windParsed = windParsed.split(' ')

        windSpeedDirection[time.text] = windParsed
        futureHours = futureHours - 1
       
    print(windSpeedDirection)
if __name__ == "__main__":
    main()