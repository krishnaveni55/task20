from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.keys import Keys
import time
paths = r"C:\Users\HP\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver: WebDriver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.cowin.gov.in/')
driver.maximize_window()
time.sleep(5)
faq_link = driver.find_element(By.XPATH, "//*[@id='navbar']/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a")
partners_link = driver.find_element(By.XPATH, '//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a')
ActionChains(driver).key_down(Keys.CONTROL).click(faq_link).key_up(Keys.CONTROL).perform()
ActionChains(driver).key_down(Keys.CONTROL).click(partners_link).key_up(Keys.CONTROL).perform()
time.sleep(5)
window_handles = driver.window_handles
for index, handle in enumerate(window_handles):
    print(f"Window {index} Handle: {handle}")
for handle in window_handles:
    driver.switch_to.window(handle)
    print(f"Switched to window with handle: {handle}")
    print(f"Title: {driver.title}")
driver.close()
time.sleep(3)
driver.quit()
