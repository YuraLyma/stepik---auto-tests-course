import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def registation(link):

	try:
		driver = webdriver.Chrome()
		driver.get(link)

		driver.find_element_by_css_selector(".first_block .first").send_keys("FirstName")

		driver.find_element_by_css_selector(".first_block .second").send_keys("Lastname")

		driver.find_element_by_css_selector(".first_block .third").send_keys("Email@email.com")

		driver.find_element_by_css_selector("[type='submit']").click()
	except Exception:
		raise

	try:
		registration_text = WebDriverWait(driver, 2).until(EC.presence_of_element_located(By.TAGNAME, "h1")).text
	except Exception:
		raise

	return registration_text

class TestUniquenessOfSelectors(unittest.TestCase):

	def setUp(self):

		text = 'Congratulations! You have successfully registered!'

	def test_registration_1(self):

		registration_text = registation("http://suninjuly.github.io/registration1.html")

		self.assertEqual(registration_text, text)

	def test_registatrion_2(self):

		registration_text = registation("http://suninjuly.github.io/registration2.html")

		self.assertEqual(registration_text, text)

import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def registation(link):

	driver = webdriver.Chrome()
	driver.get(link)

	driver.find_element_by_css_selector(".first_block .first").send_keys("FirstName")

	driver.find_element_by_css_selector(".first_block .second").send_keys("Lastname")

	driver.find_element_by_css_selector(".first_block .third").send_keys("Email@email.com")

	driver.find_element_by_css_selector("[type='submit']").click()

	try:
		registration_text = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text
	except Exception:
		raise

	return registration_text

class TestUniquenessOfSelectors(unittest.TestCase):

	def setUp(self):

		self.text = 'Congratulations! You have successfully registered!'

	def test_registration_1(self):

		registration_text = registation("http://suninjuly.github.io/registration1.html")

		self.assertEqual(registration_text, self.text)

	def test_registatrion_2(self):

		registration_text = registation("http://suninjuly.github.io/registration2.html")

		self.assertEqual(registration_text, text)


if __name__ == '__main__':
	unittest.main()
