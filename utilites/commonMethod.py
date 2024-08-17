from selenium import webdriver
from selenium.webdriver.common.by import By
from traceback import print_stack

class commonForLocator:

    def __init__(self,driver) :
        self.driver=driver

    
    def getlocator(self,locatorType):

        lctype=locatorType.lower()
        if lctype=="id" :
            return By.ID
        elif lctype=="xpath" :
            return By.XPATH
        
    
    def getelement(self, locatorType,locator):

        element=None
        # if locatorType == "id":
        #     locatorType= By.ID
        try:

            locaType=self.getlocator(locatorType)  
            element=self.driver.find_element(locaType,locator)
            print("element found")
        
        except:
            print("element not found")
            print_stack()
        
        return element
            