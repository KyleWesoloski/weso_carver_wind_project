import sys
import requests
import xlwings as xw
from stadium import *
from clear import *
from bs4 import BeautifulSoup
from xlrd import open_workbook
from xlutils.copy import copy

#open locations.txt and store location/url in locations list
def weatherLocations(locFile):
    locations = []
    counter = 0
    numLocations = 0
    with open(locFile) as f:
        while True:
            city = f.readline()
            url = f.readline()
            if not city or not url:
                break
            city = city.replace("\n", "")
            url = url.replace("\n", "")
            locations.insert(numLocations, [city, url])
            numLocations = numLocations + 1
    return locations, numLocations

#open url for each location. Store time, direction, and wind speed in locations list. 
def getWindData(urls, numLocations, hours):
    locations = []
    for i in range(numLocations):
        #retrieve html page 
        html = requests.get(urls[i][1]).content
        soup = BeautifulSoup(html, 'html.parser')
        windSpeedDirection = []

        #get wind speed and direction from html DetailsSummary-wind class tag
        windQuery = soup.findAll('div', attrs={'class': 'DetailsSummary--wind--1tv7t DetailsSummary--extendedData--307Ax'})
        #get time of wind speed and direction with h3 value
        timeQuery = soup.findAll('h3', attrs={'data-testid': 'daypartName'})
        
        #future hours is the number of hours that will display the wind speed
        #max is 23 since dictionary naming convention uses the time of day at the key
        futureHours = hours

        #append each wind speed and direction to corresponding time. 
        for wind, time in zip(windQuery, timeQuery):
            if futureHours == 0: break

            windParsed = wind.text.replace('Wind', '')

            windParsed = windParsed.replace(' mph', '')

            windParsed = windParsed.split(' ')
            windParsed.append(time.text)

            windSpeedDirection.append(windParsed)
            futureHours = futureHours - 1

        locations.insert(i, windSpeedDirection)
    return locations

#update xls file with wind data
def writeFile(urls, locations, hours):

    #clear old xls file
    clearSheet()

    #open work bork
    rb = open_workbook("windSpeedDirection.xls")
    wb = copy(rb)
    sheet1 = wb.get_sheet('Sheet 1')

    futureHours = hours
    row = 1
    column = 0
    index = 0

    for loc in locations:
        sheet1.write(0, column, urls[index][0])
        index = index+1
        for i in range(futureHours):
            if futureHours == 0: break
            sheet1.write(row, column, str(loc[i][2]))
            sheet1.write(row, column + 1, str(loc[i][0]))
            sheet1.write(row, column + 2, int(loc[i][1]))
            row = row+1
            futureHours = futureHours - 1
        row = 1
        column = column + 4
        futureHours = hours

    wb.save('windSpeedDirection.xls')
    openBook = xw.Book("C:/Users/Kylew/CS/sports betting/windSpeedDirection.xls")