#Handling Data in Popup and checking result
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
driver = webdriver.Chrome(executable_path="/Users/makumarc/PycharmProjects/Selenium_Assignment2/venv/bin/chromedriver")

driver.get("https://the-internet.herokuapp.com/")
driver.implicitly_wait(2)
driver.find_element(By.LINK_TEXT, "JavaScript Alerts").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[3]/button").click()
driver.implicitly_wait(2)
driver.switch_to.alert.send_keys("Test Data")
driver.implicitly_wait(3)
driver.switch_to.alert.accept()
result= driver.find_element(By.XPATH, "//p[@id='result']").text
print(result)
if result=="You entered: Test Data":
    print("pass")

print("Result is matching")
#driver.switch_to.alert.send_keys("Test sukant")
#driver.close()