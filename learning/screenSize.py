
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

class screensize:
    def getscreenSize(self):

        driver=webdriver.Chrome()
        #driver.maximize_window()
        driver.get("https://artoftesting.com/samplesiteforselenium")

        height=driver.execute_script("return window.innerHeight;")
        width=driver.execute_script("return window.innerWidth;")

        print("height is :",height)
        print("width is : ",width)

obj=screensize()
obj.getscreenSize()
