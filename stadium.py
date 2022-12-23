import os

stadiums = {
            '1': ['Every Location'], 
            '2': ['Anaheim'], 
            '3': ['St. Louis'], 
            '4': ['Phoenix'], 
            '5': ['Queens'], 
            '6': ['Philadelphia'], 
            '7': ['Detroit'], 
            '8': ['Denver'], 
            '9': ['Los Angeles'], 
            '10': ['Boston'], 
            '11': ['Arlington'], 
            '12': ['Cincinnati'], 
            '13': ['Chicago'], 
            '14': ['Kansas City'], 
            '15': ['Miami'], 
            '16': ['Houston'], 
            '17': ['D.C.'], 
            '18': ['San Fransico'], 
            '19': ['Pittsburgh'], 
            '20': ['Cleveland'], 
            '21': ['Oakland'], 
            '22': ['Toronto'], 
            '23': ['Seattle'], 
            '24': ['Minneapolis'], 
            '25': ['St. Petersburg'], 
            '26': ['Cumberland'], 
            '27': ['Chicago'], 
            '28': ['Bronx'],
            '29': ['Milwaukee']
        }

def getDirection(locations):
    direction = []
    for loc in locations:
        direction.insert(stadiums[loc])
    return direction

def getRequest():
    count = 1
    locationList = []

    for loc in stadiums.values():
        print(str(count) + ': ' + loc[0])
        count = count+1
    print("\nEnter number(s) of desired locations seperated by spaces\n")
    print("Example: 2 5 18 22\n")

    locations = input("Locations: ")
    locations = locations.split(' ')
    if '1' in locations: 
        for i in range (28):
            locationList.append(i)
    else:
        for num in locations:
            if num in stadiums:
                locationList.append(int(num)-2)
            else:
                raise ValueError('Invalid input')
    return locationList

def createUrlFile(locations):
    urls = []
    names = getCityNames(locations)

    if os.path.exists("request.txt"):
        os.remove("request.txt")
    
    with open('urls.txt', 'r') as urlFile:
        
        while True:
            url = urlFile.readline()
            if not url:
                break
            url = url.replace("\n", "")
            urls.append(url)
    
    with open('request.txt', 'w') as requestFile:
        index = 0
        for loc in locations:
            requestFile.write(names[index])
            requestFile.write('\n')
            requestFile.write(urls[int(loc)])
            requestFile.write('\n')
            index = index+1


#can get both direction and city if delete [0]
def getCityNames(locations):
    cities = []
    for loc in locations:
        cities.append(stadiums[str(int(loc+2))][0])  
    return cities  