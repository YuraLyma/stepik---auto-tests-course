import math
import time

from selenium import webdriver



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
	driver = webdriver.Chrome()
	driver.get('http://suninjuly.github.io/redirect_accept.html')

	driver.find_element_by_css_selector("[type='submit']").click()

	time.sleep(1)
	driver.switch_to.window(driver.window_handles[1])

	x = driver.find_element_by_id("input_value").text.strip()
	x = calc(x)

	driver.find_element_by_id("answer").send_keys(x)

	driver.find_element_by_css_selector("[type='submit']").click()
	
finally:
	time.sleep(5)
	driver.quit()
