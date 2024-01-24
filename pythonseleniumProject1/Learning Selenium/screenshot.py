import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class FindElementByCssSelector:
    def locate_by_id_demo(self):
        chrome_service = webdriver.chrome.service.Service(executable_path="C:\\browserdrivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=chrome_service)
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.fullscreen_window()
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\python-selenium\\pythonseleniumProject1\\Learning Selenium\\beforeerror.png")
        continue_demo=driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
        time.sleep(2)
        continue_demo.screenshot(".\\target.png")
        time.sleep(2)
        continue_demo.click()
        time.sleep(2)
        driver.save_screenshot(".\\aftererror.png")

findbycssselector = FindElementByCssSelector()
findbycssselector.locate_by_id_demo()
