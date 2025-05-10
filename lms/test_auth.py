# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # Set Chrome options
# chrome_options = Options()
# chrome_options.add_argument("--start-maximized")

# # Initialize WebDriver with ChromeDriverManager
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# # Wait object for explicit waits
# wait = WebDriverWait(driver, 10)

# # Step 1: Go to the signup page
# driver.get("http://127.0.0.1:8000/signup/")  # Replace with the correct URL of your signup page

# # Step 2: Wait for the elements to be available (explicit wait)
# username_field = wait.until(EC.presence_of_element_located((By.ID, "id_username")))
# email_field = wait.until(EC.presence_of_element_located((By.ID, "id_email")))
# password_field = wait.until(EC.presence_of_element_located((By.ID, "id_password1")))
# confirm_password_field = wait.until(EC.presence_of_element_located((By.ID, "id_password2")))

# # Step 3: Fill out the form fields
# username_field.send_keys("testuser")
# email_field.send_keys("testuser@example.com")
# password_field.send_keys("TestPassword123")
# confirm_password_field.send_keys("TestPassword123")

# # Step 4: Submit the form (click the Register button)
# register_button = driver.find_element(By.XPATH, "//button[@type='submit']")
# register_button.click()

# # Step 5: Wait for redirection to the login page
# time.sleep(3)  # Wait a bit for the page to load after submitting the form

# # Verify if the page was redirected to the login page
# current_url = driver.current_url
# print("Current URL after signup:", current_url)

# # If the user is still on the signup page, manually navigate to the login page
# if "signup" in current_url:
#     print("Redirection failed. Manually navigating to the login page...")
#     driver.get("http://127.0.0.1:8000/login/")  # Manually navigate to the login page

# # Step 6: Wait for login form to appear and login
# username_login_field = wait.until(EC.presence_of_element_located((By.ID, "id_username")))  # Login form's username field
# password_login_field = wait.until(EC.presence_of_element_located((By.ID, "id_password")))  # Login form's password field

# # Fill in login credentials
# username_login_field.send_keys("testuser")
# password_login_field.send_keys("TestPassword123")

# # Step 7: Submit the login form (click the Login button)
# login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
# login_button.click()

# # Step 8: Wait for redirection to the home page after successful login
# time.sleep(3)  # Wait a bit for the page to load after submitting the login form

# # Verify if the page was redirected to the home page (replace 'home' with your actual homepage URL segment)
# current_url = driver.current_url
# print("Current URL after login:", current_url)

# # Check if the user is redirected to the home page
# assert "home" in current_url, f"Login failed. Current URL is: {current_url}"

# # Step 9: Close the browser
# driver.quit()

# print("Test completed successfully!")
