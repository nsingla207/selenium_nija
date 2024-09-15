
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class learnWaits:

    def learnExplicitWait(self):

        dirpath=os.path.join(os.path.dirname(__file__),"..")
        filepath=os.path.join(os.path.abspath(dirpath),"TitleChange.html")

        driver= webdriver.Chrome()
        driver.maximize_window()
        driver.get(filepath)

        old_title=driver.title
        print("Old title is :", old_title)
        element=driver.find_element(By.XPATH,"//button[text()='Change Title']")
        element.click()     
        
        #  wait=WebDriverWait(driver,10).until(lambda d:d.title!=old_title)
        wait=WebDriverWait(driver,10).until_not(EC.title_is(old_title))
        new_title=driver.title

        # flag=True
        # while(flag):  
        #     new_title=driver.title          
        #     if old_title != new_title:
        #         flag= False
            
        print("new title is :", new_title)


obj=learnWaits()
obj.learnExplicitWait()