from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

USERNAME = ""
PASSWORD = ""
ACCOUNT_TO_FOLLOW = " "

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 15)

try:
    driver.get("https://www.instagram.com/accounts/login/")
    
    
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD + Keys.RETURN)

    
    try:
        not_now = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not now')]")))
        not_now.click()
    except:
        pass
    try:
        not_now2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
        not_now2.click()
    except:
        pass

    
    driver.get(f"https://www.instagram.com/{ACCOUNT_TO_FOLLOW}/")
    time.sleep(3)

    
    try:
        follow_btn = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[normalize-space()='Follow' or normalize-space()='Follow Back']"
        )))
        follow_btn.click()
        print(f"✅ Follow request sent to {ACCOUNT_TO_FOLLOW}")
    except:
        try:
    
            requested_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Requested') or contains(text(),'Following')]")
            print(f"⚠️ Already following or request already sent to {ACCOUNT_TO_FOLLOW}")
        except:
            print("❌ Couldn't locate the Follow button. Instagram UI may have changed.")

    time.sleep(5)

finally:
    driver.quit()

