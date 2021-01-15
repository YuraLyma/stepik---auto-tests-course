import time
import math
import pytest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


links = [
	f"https://stepik.org/lesson/236895/step/1",
	f"https://stepik.org/lesson/236896/step/1",
	f"https://stepik.org/lesson/236897/step/1",
	f"https://stepik.org/lesson/236898/step/1",
	f"https://stepik.org/lesson/236899/step/1",
	f"https://stepik.org/lesson/236903/step/1",
	f"https://stepik.org/lesson/236904/step/1",
	f"https://stepik.org/lesson/236905/step/1"
]


@pytest.fixture(scope="function")
def browser():
	browser = webdriver.Chrome()
	yield browser
	browser.quit()


@pytest.mark.parametrize('link', links)
def test_feedback(browser, link):
	browser.get(link)
	textarea = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea")))
	answer = math.log(int(time.time()))
	textarea.send_keys(str(answer))
	browser.find_element_by_class_name("submit-submission").click()

	feedback = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text

	assert feedback == "Correct!", "Must be 'Correct!"
