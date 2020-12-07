import requests
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05361000000005&lon=-118.24549999999999#.X7DlNhaIYdU')
# print(response)
# page = requests.get('https://weather.com/fa-IR/weather/tenday/l/99af92d56c39592dd032045644262b7e574ff1d0c5fe7f8ca1603a0440491d79')
# print(page)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
week = soup.find(id="seven-day-forecast-body")
# week = soup.find(id="MainContent")
# print(week)
items = week.find_all(class_= 'tombstone-container')
# items = week.find_all(class_=" region-contentTop regionContentTop DaybreakLargeScreen--regionContentTop--2jVIh")

# print(items)
# print(items.find(class_='ListItem--listItem--1r7mf WeatherDetailsListItem--WeatherDetailsListItem--3w7Gx'))
# print(items[0].find(class_='period-name').get_text())

# print(items[0].find(class_='short-desc').get_text())
# print(items[0].find(class_='temp').get_text())
period_names = [item.find(class_='period-name').get_text() for item in items]
short_descripotion = [item.find(class_='short-desc').get_text() for item in items]
temperature = [item.find(class_='temp').get_text() for item in items]
#
# print(period_names)
# print(short_descripotion)
# print(temperature)
weather = pd.DataFrame(
    {
    'periode':period_names,
    'short-decs':short_descripotion,
    'temp':temperature
})
print(weather)
weather.to_csv('result.csv')