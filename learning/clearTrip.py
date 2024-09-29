
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver=webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.cleartrip.com/bus")

wait=WebDriverWait(driver,4)

wait.until(ec.element_to_be_clickable((By.XPATH,"//input[@id='departure']")))

driver.find_element(By.XPATH,"//input[@id='departure']").send_keys("new")


wait.until(ec.element_to_be_clickable((By.XPATH,"//p[contains(text(),'Newton')]")))
driver.find_element(By.XPATH,"//p[contains(text(),'Newton')]").click()


time.sleep(3)

