import math
import time
import os

from selenium import webdriver



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
	driver = webdriver.Chrome()
	driver.get('http://suninjuly.github.io/file_input.html')

	driver.find_element_by_css_selector("[name='firstname']").send_keys("First name")
	driver.find_element_by_css_selector("[name='lastname']").send_keys("Last name")
	driver.find_element_by_css_selector("[name='email']").send_keys("Email")

	file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.txt')
	driver.find_element_by_id("file").send_keys(file_path)

	driver.find_element_by_css_selector("[type='submit']").click()
	
finally:
	time.sleep(5)
	driver.quit()
