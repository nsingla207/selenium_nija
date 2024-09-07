
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from utilites.commonMethod import commonForLocator

class DropDown:

    def learnDropDowm(self):


        # print(" path of the python file #######")

        # print(os.path.dirname(__file__))

        # print(" path of the file parent  #######")
        # print(os.path.join(os.path.dirname(__file__),".."))

        # print(" abouste path of file dir")

        # print(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

        driver= webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://artoftesting.com/samplesiteforselenium")
        
        time.sleep(2)
        cmobj=commonForLocator(driver)

        dd_testing= cmobj.getelement("id","testingDropdown")

        # dd_testing= driver.find_element(By.ID,"testingDropdown")

        sel=Select(dd_testing)

        sel.select_by_index("1")
        time.sleep(2)

        sel.select_by_value("Manual")
        time.sleep(2)

        sel.select_by_visible_text("Database Testing")
        time.sleep(2)

        sel.select_by_index(0)
        time.sleep(2)

        count=driver.find_elements(By.XPATH,"//select[@id='testingDropdown']/option")
        print("total option for dd are :", len(count))

        counter=0
        for x in count:
            if x.text=="Database Testing":
                print(" Data base testing found ")
                counter+=1
            
        print("data abse testing count is : ",counter)


obj=DropDown()
obj.learnDropDowm()



