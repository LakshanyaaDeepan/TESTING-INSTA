from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

USERNAME = ""
PASSWORD = ""

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)

username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")

username_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)

time.sleep(7)

driver.get(f"https://www.instagram.com/{USERNAME}/")
time.sleep(5)

try:
    profile_menu_button = driver.find_element(By.XPATH, '//div[contains(@aria-label,"Profile") or @role="button"]')
    profile_menu_button.click()
    time.sleep(2)

    logout_button = driver.find_element(By.XPATH, "//div[text()='Log out']")
    logout_button.click()
    print("✅ Logged out successfully.")
except Exception as e:
    print(f"❌ Logout failed: {e}")

time.sleep(3)
driver.quit()
