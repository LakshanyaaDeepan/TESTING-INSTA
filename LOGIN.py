from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


USERNAME = "your_username"
PASSWORD = "your_password"


chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

try:
    
    driver.get("https://www.instagram.com/accounts/login/")

    
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_field.send_keys(USERNAME)

    
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(PASSWORD + Keys.RETURN)

    
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/explore/')]"))
    )
    print("Login successful!")

    
    try:
        not_now_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']"))
        )
        not_now_button.click()
    except:
        pass

    
    try:
        not_now_button2 = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']"))
        )
        not_now_button2.click()
    except:
        pass

    time.sleep(5)

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()

