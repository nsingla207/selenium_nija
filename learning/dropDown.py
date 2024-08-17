
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DropDown:

    def learnDropDowm(self):

        driver= webdriver.Chrome()
        driver.get("https://artoftesting.com/samplesiteforselenium")

        driver.maximize_window()
        time.sleep(2)

        dd_testing= driver.find_element(By.ID,"testingDropdown")

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



