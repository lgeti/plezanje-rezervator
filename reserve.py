from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

# Set up the webdriver
options = webdriver.ChromeOptions()
# You can add more options here if needed
driver = webdriver.Chrome(options=options)

try:
    # Navigate to the login page
    driver.get("https://popr.uni-lj.si/unauth/student/login")
    
    # Wait for the button to be present and then click it
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@title="Prijavite se"]'))).click()

    # Wait for the email field to be present and then enter the email
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "i0116"))).send_keys("")

    # Wait for the "Next" button to be present and then click it
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "idSIButton9"))).click()
    
    # Wait for the password field to be present and then enter the password
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "i0118"))).send_keys("")

    # Wait for the "Sign in" button to be present and then click it
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "idSIButton9"))).click()

    # Specify the date and time to start
    start_time = datetime.datetime(year=2024, month=5, day=29, hour=6)

    # Calculate the number of seconds until the start time
    now = datetime.datetime.now()
    delay = (start_time - now).total_seconds()

    # Wait until 6am tomorrow
    time.sleep(delay)

    # Try to reserve the ticket until successful
    reservation_successful = False
    while not reservation_successful:
        try:
            # Wait for the button to be present
            button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Register for Joga, 28. maj 2024, 16:00 - 17:30']")))

            # Scroll the button into view
            driver.execute_script("arguments[0].scrollIntoView();", button)

            # Click the button
            button.click()

            print("Ticket booked successfully!")
            reservation_successful = True

        except Exception as e:
            print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()