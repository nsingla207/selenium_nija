
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class dynamicDD:

    def redbusDD(self):

        parvesh= webdriver.Chrome()

        parvesh.maximize_window()
        parvesh.get("https://www.redbus.in/")

        WebDriverWait(parvesh,5).until(ec.element_to_be_clickable((By.XPATH,"//input[@id='src']")))

        parvesh.find_element(By.XPATH,"//input[@id='src']").send_keys("new")

        WebDriverWait(parvesh,2).until(ec.visibility_of_element_located((By.XPATH,"//ul[@class='sc-dnqmqq dZhbJF']")))

        autolist=parvesh.find_element(By.XPATH,"//ul[@class='sc-dnqmqq dZhbJF']")
        autolistvalue=autolist.get_attribute("innerHTML")

        lilist=autolist.find_elements(By.TAG_NAME,'li')

        textneedtoselect="Avinashi New Bus Stand"
        for name in lilist:
            #print(name.text)
            if textneedtoselect in name.text:
                name.click()
                break

        time.sleep(2)

        


obj=dynamicDD()
obj.redbusDD()

