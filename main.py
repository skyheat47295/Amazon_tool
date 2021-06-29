# Retrieve list of Agenda Report URL's

from selenium import webdriver
import subprocess
import re

images = []
url = 'https://www.amazon.com/dp/B08TQJ7W4D'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path='./chromedriver.exe')

driver.get(url)
all_elements = driver.find_elements_by_xpath('//*[@id="main-image-container"]/ul/li[1]/span/span/div/img')
ul = driver.find_elements_by_css_selector(".li.image.item.itemNo1.maintain-height.selected")
for elem in all_elements:
    # Grab the Agenda Report url
    images.append(elem.get_property('attributes')[0].get('value'))


print('done')
