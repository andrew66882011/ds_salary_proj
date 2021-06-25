# Selenium Tutorial #1
# https://sites.google.com/a/chromium.org/chromedriver/downloads

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = "/Users/jjhua/Desktop/Python for Data Science/ds_salary_proj/chromedriver"
driver = webdriver.Chrome(path)

driver.get("https://www.techwithtim.net/")
print(driver.title)

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)
print(driver.page_source)
time.sleep(5)


driver.quit()
