import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class firstBrowser:

    def launchBrowser(self):      

        driver=webdriver.Chrome()

        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(5)

        driver.maximize_window()
        username= driver.find_element(by=By.NAME,value='username')
        password= driver.find_element(By.NAME,'password')

        username.send_keys('Admin')
        password.send_keys('admin123')
        time.sleep(1)
        driver.find_element(by=By.XPATH,value="//button[@type='submit']").click()

        time.sleep(5)

        

           
        


obj=firstBrowser()
obj.launchBrowser()