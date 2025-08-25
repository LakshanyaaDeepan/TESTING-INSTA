from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

USERNAME = ""
PASSWORD = ""

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 25)

try:
    driver.get("https://www.instagram.com/accounts/login/")

    # Login
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD + Keys.RETURN)

    # Handle "Save Your Login Info?" popup
    try:
        save_info = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save info')]"))
        )
        save_info.click()
    except:
        pass

    # Handle "Turn On Notifications" popup
    try:
        not_now = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not now') or contains(text(), 'Not Now')]"))
        )
        not_now.click()
    except:
        pass

    # Wait until logged in (Home icon visible)
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'/explore/')]")))
    print("✅ Logged in successfully!")

    # Navigate to Explore Feed
    driver.get("https://www.instagram.com/explore/")

    # Wait for Explore feed grid to appear
    wait.until(EC.presence_of_element_located((By.XPATH, "//article")))
    print("✅ Explore feed loaded.")

    # Find scrollable container (Instagram uses <div> inside <main>)
    scroll_container = wait.until(
        EC.presence_of_element_located((By.XPATH, "//main//div[contains(@class, 'x9f619') or contains(@class, 'x78zum5')]"))
    )

    # Scroll inside the container
    for i in range(10):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_container)
        print(f"🔽 Scrolled {i+1} times...")
        time.sleep(2)

    print("✅ Scrolled through Explore feed successfully!")

    time.sleep(5)

finally:
    driver.quit()
