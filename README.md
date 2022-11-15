# weso_carver_wind_project
Pulls current and future wind speed and direction with given city from weather.com 

Usage:
1. Input desired url into the weather.py code. 
  -It must be a valid hour by hour weather url from weather.com. 
  -The example uses Nashville

2. Change futureHours in weather.py to desired number of hours in the future you want the wind speed and direction.


Result is stored in a dictionary 'windSpeedDirection' with the hour as the key and a list of direction and speed (mph) as the value. 

