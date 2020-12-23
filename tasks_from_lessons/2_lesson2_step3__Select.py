import math
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
	driver = webdriver.Chrome()
	driver.get('http://suninjuly.github.io/selects1.html')

	num1 = driver.find_element_by_id('num1').text.strip()
	num2 = driver.find_element_by_id('num2').text.strip()

	nums_sum = int(num1) + int(num2)

	Select(driver.find_element_by_id('dropdown')).select_by_value(str(nums_sum))

	driver.find_element_by_css_selector("[type='submit']").click()

	
finally:
	time.sleep(5)
	driver.quit()
