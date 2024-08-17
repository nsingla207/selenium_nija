import time

from selenium import webdriver
import selenium.webdriver.common
from selenium.webdriver.common.by import By



class firstBrowser:

    def launchBrowser(self):      

        driver=webdriver.Chrome()

        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(5)

        def highlight(element, effect_time, color, border):
            """Highlights (blinks) a Selenium Webdriver element"""
            driver = element._parent
            def apply_style(s):
                driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                    element, s)
            original_style = element.get_attribute('style')
            apply_style("border: {0}px solid {1};".format(border, color))
            time.sleep(effect_time)
            apply_style(original_style)
       # username=driver.find_element(By.LINK_TEXT,value='OrangeHRM, Inc')
       # password=driver.find_element(By.PARTIAL_LINK_TEXT,value='OrangeHRM')

        username= driver.find_element(by=By.NAME,value='username')
        password= driver.find_element(By.NAME,'password')

        print("By class found : ", username.get_attribute('name'))
      #  highlight(username,6,'blue',5)
       # highlight(password,6,'blue',5)
        
        #username= driver.find_element(by=By.NAME,value='username')
       # password= driver.find_element(By.NAME,'password')
        
        username.send_keys('Admin')
        password.send_keys('admin123')
        time.sleep(1)
        driver.find_element(by=By.XPATH,value="//button[@type='submit']").click()
        
        time.sleep(4)
        dashBroad_element=driver.find_element(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")

        if(dashBroad_element.text=='Dashborad'):
            print('user is on the dashboard page')

        print("property : ",dashBroad_element.get_attribute("class"))

        
        dashBroad_element_active=driver.find_element(By.XPATH,"//span[text()='Dashboard']/..")

        if(dashBroad_element_active.get_attribute("class").__contains__("active")):
            print("dashboard is active")

        

        
    

obj=firstBrowser()
obj.launchBrowser()