
import time
from selenium import webdriver
import selenium.webdriver.common
from selenium.webdriver.common.by import By

class expedia:
    def traveler(self):
        driver=webdriver.Edge()
        driver.get("https://www.expedia.com/")
        driver.maximize_window()
        time.sleep(2)

        traveler_count=driver.find_element(By.XPATH,"//button[@class='uitk-menu-trigger open-room-picker-observer-root uitk-fake-input uitk-form-field-trigger']")
        traveler_count.click()
        time.sleep(5)
        child_age=driver.find_element(By.XPATH,"//div[@class='uitk-field uitk-field-select-field uitk-field-select-empty-state has-floatedLabel-label is-required']")
        #child_age_display=child_age.is_displayed()
        if child_age.is_displayed():
            print("Child age selection is displayed")
        else:
            print("Child age selection is not displayed")


obj=expedia()
obj.traveler()
