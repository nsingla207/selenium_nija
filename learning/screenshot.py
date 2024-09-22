
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class learnScreenshot:

    def screenshot(self):

        driver= webdriver.Chrome()

        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        WebDriverWait(driver,5).until(ec.element_to_be_clickable((By.XPATH,"//input[@name='username']")))

        driver.find_element(By.XPATH,"//input[@name='username']").send_keys("admin")

        driver.find_element(By.XPATH,"//input[@name='password']").send_keys("321")

        driver.find_element(By.XPATH,"//button[text()=' Login ']").click()

        time.sleep(2)
        filedir=os.path.join(os.path.dirname(__file__),"..")
        folderdir=os.path.join(filedir,"ScreenShot")
        filepath=os.path.join(os.path.abspath(folderdir),"Test.png")

        try:
            driver.save_screenshot(filepath)
        except Exception as e:
            print("exception is :",e)
obj=learnScreenshot()
obj.screenshot()