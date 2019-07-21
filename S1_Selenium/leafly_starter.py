from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#from bs4 import BeautifulSoup
import re

# Go to the page that we want to scrape
driver = webdriver.Chrome()
driver.get("https://www.leafly.com/explore/sort-alpha")

# Pop-Up: Positive affirmation for age:
PosAffirm_button = driver.find_element_by_xpath('//*[@id="tou-continue"]')
PosAffirm_button.click()

# Click "Load More" button until the list is complete.  Minimum 10 clicks, maximum 60.
loadmore_button = driver.find_element_by_xpath('//button[@class="ga_Explore_LoadMore m-button m-button--green m-button--lg"]')
element_strain_block = driver.find_element_by_xpath('//div[@class="explore-tiles"]')
size = ["{'width': 0, 'height': 0}"]
size.append(str(element_strain_block.size))

i=0
while True:
    loadmore_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH,'//button[@class="ga_Explore_LoadMore m-button m-button--green m-button--lg"]')))
    loadmore_button.click()
    size.append(str(element_strain_block.size))
    i = i + 1
    time.sleep(2.5)
    if i > 10:
        if size[i] == size[i-1]:
            #print('break equal size')
            break
    elif i > 60:
        #print('break greater 60')
        break

# Create a file, 'strain_urls.txt' that contains all the urls within the strain tile block.
for a in driver.find_elements_by_xpath('//div[@class="l-grid strain-tile--explore trademarked"]//a'):
    with open('strain_urls.txt', 'a') as f:
        f.write('\n'+a.get_attribute('href'))









