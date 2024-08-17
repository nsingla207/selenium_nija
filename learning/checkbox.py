
import time
from selenium import webdriver
import selenium.webdriver.common
from selenium.webdriver.common.by import By

class learnCheckbox:

    def clickCheckbox(self):

        driver=webdriver.Chrome()
        driver.get("https://artoftesting.com/samplesiteforselenium")
      #  driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
        driver.maximize_window()

        driver.implicitly_wait(2)
        time.sleep(2)

        '''artOfTesting=driver.find_element(By.XPATH,"//a[text()='ArtOfTesting']")
        
        if artOfTesting.text =="ArtOfTesting":
            print(" we are on the right page")'''

        count=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
        print("number of checkbox are :",len(count))

        # for x in count:
        #     x.click()
        #     time.sleep(2)
        
        driver.find_element(By.XPATH,"//input[@type='checkbox' and @value='Performance']").click()
        time.sleep(4)






obj=learnCheckbox()
obj.clickCheckbox()


