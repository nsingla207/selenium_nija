from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

class scrollToview:
    def learnScrollToview(self):

        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://artoftesting.com/samplesiteforselenium")

        height=driver.execute_script("return window.innerHeight;")
        width=driver.execute_script("return window.innerWidth;")

        print("height is :",height)
        print("width is : ",width)

        # scroll to bottom 
        driver.execute_script("window.scrollTo(0,1500);")
        time.sleep(2)
        #scroll to top
        driver.execute_script("window.scrollTo(0,-1500);")
        time.sleep(3)

        # scroll to particular element on the page
        dd_testing= driver.find_element(By.ID,"testingDropdown")
        driver.execute_script("arguments[0].scrollIntoView();",dd_testing)
        time.sleep(2)

obj=scrollToview()
obj.learnScrollToview()