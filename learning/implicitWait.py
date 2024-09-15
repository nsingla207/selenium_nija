
from datetime import date, datetime
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class learnWait:

    def learnImplicitWait(self):

        dirpath= os.path.join(os.path.dirname(__file__),"..")
        print("********* Dir Path********")
        print(dirpath)

        filepath=os.path.join(os.path.abspath(dirpath),"DelayedElement.html")
        print("########## File Path ###########")

        print(filepath)

        driver=webdriver.Edge()
        driver.implicitly_wait(3)
        driver.get(filepath)
        print(datetime.now())
        element=driver.find_element(By.XPATH,"//input[@type='text']")
        element.send_keys("test")
        print(datetime.now())               
        print(" input value is : ", element.get_attribute('value'))   
        print("**********")

        #element = webDriverWait(driver,10).until()


obj=learnWait()
obj.learnImplicitWait()



        