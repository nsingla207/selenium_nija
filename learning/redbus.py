from selenium import webdriver
from selenium.webdriver.common.by import By

import time
class redBus:

    def searchBus(self):

        driver=webdriver.Chrome()
        driver.get("https://www.redbus.in/")

        driver.minimize_window()

        driver.implicitly_wait(3)
        
        ddFrom1=(By.XPATH,"//input[@id='src']")

       #print(type(ddFrom))
        ddFrom=driver.find_element(*ddFrom1)
        ddTo=driver.find_element(By.XPATH,"//input[@id='dest']")
        calenderDate=driver.find_element(By.XPATH,"//div[@id='onwardCal' and @role='button']")

        ddFrom.click()
        ddFrom.send_keys("Chandigarh")
        time.sleep(5)
        
        ddTo.click()
        ddTo.send_keys("Delhi")
        time.sleep(5)

        calenderDate.click()
       # driver.execute_script("arguments[0].click();", calenderDate)
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[local-name()='svg' and @id='Layer_1']").click()

        time.sleep(1)
        dateneedToPick=driver.find_element(By.XPATH,"//div[contains(@class,'DayTilesWrapper__RowWrap')][3]/span[contains(@class,'DayTilesWrapper__SpanContainer')]/div[contains(@class,'DayTiles__CalendarDaysBlock')]/span[contains(@class,'DayTiles__CalendarDaysSpan') and text()='5']")
        dateneedToPick.click()
        time.sleep(5)


obj=redBus()
obj.searchBus()
        



