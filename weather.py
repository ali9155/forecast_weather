import requests
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get('https://www.worldometers.info/coronavirus/?_hsenc=p2ANqtz--rZXdvpxgMsH2oK-1Gnu8BHPWc7J_QFtZPsrVwAQqpHNrXQyllzVBZ-CG04OGICUPv9WB0pw6m8Xj09Ixp0oS-m2EepfHxZxugXc-OjvBoFnnxDpI&_hsmi=84525637')

print(page)
#
text = text_website
soup = BeautifulSoup(text, 'html.parser')
# print(soup)
week = soup.find(id="main_table_countries_today_wrapper")
# print((week).get_text())
today = week.find(class_="total_row_world odd")
items = [today.find_all(class_='odd') for item in today]
print(items)
#
# # x=[]
# for i in items:
#     x.append(i)
# # print(x)
# y=["Max","Wind","Humidity","Dew-point","Pressure","Indicator_UV","Visibility","Moon_step"]
#
# data=pd.DataFrame({
#     "Status":items
# })
# print(data)
# data.to_csv('r1.csv')
class alaki:
  def tefff:
    if alaki nabood:
      print("alaki nist")
  tamam
