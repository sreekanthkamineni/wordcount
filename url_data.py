import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
url = "https://coursehunters.net/course/django-core-polnoe-rukovodstvo-po-osnovnym-koncepciyam-django"
chromed = "c:\\Users\\sreek\\Documents\\PythonScripts\\chromedriver"
# firefox = "c:\\Users\\sreek\\Documents\\PythonScripts\\geckodriver"
driver = webdriver.Chrome(chromed)
# driver = webdriver.Firefox(firefox)
driver.get(url)
# time.sleep(30)
html = driver.execute_script("return document.documentElement.outerHTML")
url_soup = BeautifulSoup(html, 'html.parser')
businesses = url_soup.findAll('ul', {'class': 'lessons-list'})
for buz in businesses:
    name = buz.findAll('li', {'class': 'lessons-list__li'})[0].text
    print(name)
