from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
browser.get("http://the-internet.herokuapp.com/login")
username_input = browser.find_element(By.XPATH,'//input[@id="username"]')
username_input.send_keys("tomsmith" )

password_input = browser.find_element(By.XPATH,'//input[@id="password"]')
password_input.send_keys("SuperSecretPassword!" )

button = browser.find_element(By.CSS_SELECTOR, "button.radius")
button.click()