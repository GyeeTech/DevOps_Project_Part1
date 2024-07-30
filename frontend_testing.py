from selenium import webdriver
from selenium.webdriver.common.by import By

# Start a Selenium Webdriver session
driver = webdriver.Chrome()

try:
    # Navigate to web interface URL using an existing user id
    driver.get("http://127.0.0.1:5000/users/1")

    # Check that the user name element is showing (web element exists)
    user_name_element = driver.find_element(By.CSS_SELECTOR,"body > pre")

    if user_name_element:
        # Print user name
        print("User Name is:", user_name_element.text)
    else:
        print("User name element not found.")
except Exception as e:
    print("An error occurred:", e)
finally:
    # Close the browser session
    driver.quit()
