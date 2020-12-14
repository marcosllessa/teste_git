from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.uol.com.br/")

print(driver.title)
print(driver.current_url)


driver.find_element_by_xpath("//*[@id='HU_header']/div[2]/div/div[2]/div[1]/div/div/a").click()

time.sleep()

driver.close()