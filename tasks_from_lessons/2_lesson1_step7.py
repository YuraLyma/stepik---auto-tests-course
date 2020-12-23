import math
import time

from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
	driver = webdriver.Chrome()
	driver.get('http://suninjuly.github.io/get_attribute.html')
	
	x = driver.find_element_by_id('treasure').get_attribute('valuex')

	x = calc(x)

	driver.find_element_by_id("answer").send_keys(x)
	driver.find_element_by_id("robotCheckbox").click()
	driver.find_element_by_id("robotsRule").click()
	driver.find_element_by_css_selector("[type='submit']").click()
	
finally:
	time.sleep(5)
	driver.quit()