from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

username = ""
password = ""
account_to_search = ""

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 20)  

try:
    driver.get("https://www.instagram.com/accounts/login/")
    
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password + Keys.ENTER)
    
    time.sleep(5)

    try:
        not_now = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']")))
        not_now.click()
        time.sleep(2)
    except:
        pass

    try:
        not_now2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']")))
        not_now2.click()
        time.sleep(2)
    except:
        pass

    search_icon = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@aria-label='Search']")))
    search_icon.click()

    search_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@aria-label='Search Input']")))
    search_input.send_keys(account_to_search)
    time.sleep(3)  

    account_result = wait.until(EC.element_to_be_clickable(
        (By.XPATH, f"//a[contains(@href, '/{account_to_search}/')]")))
    account_result.click()

    print(f"Successfully navigated to {account_to_search}'s profile!")

finally:
    time.sleep(5)
    driver.quit()
