import tkinter as tk
from tkinter import messagebox
import logging
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime


class LogHandler:
    def __init__(self):
        self.log_data = []

    def log_to_html(self, log_message, level):
        self.log_data.append(f'<tr><td>{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</td><td>{level}</td><td>{log_message}</td></tr>')

    def log_to_excel(self):
        df = pd.DataFrame(self.log_data, columns=["Timestamp", "Log Level", "Message"])
        df.to_excel("instagram_login_logs.xlsx", index=False)

log_handler = LogHandler()


username = ""  
password = ""  

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def show_alert(msg):
    root = tk.Tk()
    root.withdraw()  
    messagebox.showerror("Login Error", msg) 
    root.mainloop()

logging.info("Starting Instagram login process...")
log_handler.log_to_html("Starting Instagram login process...", "INFO")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.instagram.com/accounts/login/")

time.sleep(10)

try:
    logging.info("Entering username...")
    log_handler.log_to_html("Entering username...", "INFO")
    
   
    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys(username)

    logging.info("Entering password...")
    log_handler.log_to_html("Entering password...", "INFO")

    
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)

    time.sleep(10) 

    
    error_elements = driver.find_elements(By.XPATH, '//p[@id="slfErrorAlert"] | //div[@role="alert"]')

    if error_elements:
        error_text = error_elements[0].text.lower()
        
      
        if "incorrect" in error_text or "invalid" in error_text:
            logging.error("Login failed: Incorrect username or password")
            log_handler.log_to_html("Login failed: Incorrect username or password", "ERROR")
            show_alert("Incorrect username or password!")
            driver.quit()
            exit()

    logging.info("Login successful!")
    log_handler.log_to_html("Login successful!", "INFO")

except Exception as e:
    logging.error(f"An exception occurred: {e}")
    log_handler.log_to_html(f"An exception occurred: {e}", "ERROR")
    driver.quit()

log_handler.log_to_html("</table>", "INFO")  
with open("instagram_login_logs.html", "w") as html_file:
    html_file.write("<html><body><table border='1'>" + "".join(log_handler.log_data) + "</table></body></html>")

log_handler.log_to_excel() 

class LogHandler:
    def __init__(self):
        self.logs = []  
    
    def add_log(self, log_level, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {
            "Timestamp": timestamp,
            "Log Level": log_level,
            "Message": message
        }
        self.logs.append(log_entry) 
    def save_to_excel(self, filename="instagram_login_logs.xlsx"):
        df = pd.DataFrame(self.logs)
        df.to_excel(filename, index=False, engine='openpyxl')

        print(f"Log file saved to {filename}")
    def check_logs(self, expected_log_count=0):
        assert len(self.logs) == expected_log_count, f"Expected {expected_log_count} logs, but got {len(self.logs)}"
def run_instagram_login_test(username, password):
    log_handler = LogHandler()

  
    if username == "valid_user" and password == "valid_password":
        log_handler.add_log("INFO", "Login successful!")
        print("Login successful!")
        log_handler.check_logs(expected_log_count=1) 
    else:
        log_handler.add_log("ERROR", "Login failed: Incorrect username or password")
        print("Login failed!")
        log_handler.check_logs(expected_log_count=1)  
    
 
    log_handler.save_to_excel("instagram_login_logs.xlsx")

run_instagram_login_test("valid_user", "valid_password")
run_instagram_login_test("invalid_user", "invalid_password")


