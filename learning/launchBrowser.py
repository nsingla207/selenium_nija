import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class firstBrowser:

    def launchBrowser(self):      

        driver=webdriver.Chrome()

        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(5)

        
        username= driver.find_element(by=By.NAME,value='username')
        password= driver.find_element(By.NAME,'password')

        username.send_keys('Admin')
        password.send_keys('admin123')
        time.sleep(1)
        driver.find_element(by=By.XPATH,value="//button[@type='submit']").click()

        time.sleep(5)

        if username is not None:
            print(" Username ------------> found ")        
        


obj=firstBrowser()
obj.launchBrowser()