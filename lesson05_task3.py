from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)


browser.get("http://the-internet.herokuapp.com/inputs")


number_input = browser.find_element(By.XPATH,'//input[@type="number"]')
number_input.send_keys("1234", Keys.RETURN)


number_input.clear()


number_input = browser.find_element(By.XPATH, '//input[@type="number"]')
number_input.send_keys("000", Keys.RETURN)


browser.quit()



