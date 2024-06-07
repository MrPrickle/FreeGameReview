from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import chromedriver_autoinstaller

# Automatically download and install chromedriver
chromedriver_autoinstaller.install()

gameLink = input("Paste the link of the game you would like to run game review on: ")

def run_script():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.get('https://www.chess.com')

    # Allow time for the page to load
    time.sleep(2)

    # Click the login button
    login_button = driver.find_element(By.LINK_TEXT, 'Log In')
    login_button.click()

    # Allow time for the login page to load
    time.sleep(2)

    # Enter username
    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys('your_username')

    # Enter password
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys('your_password')

    # Submit the login form
    login_submit = driver.find_element(By.XPATH, '//button[contains(text(), "Log In")]')
    login_submit.click()

    # Allow time for login to complete
    time.sleep(5)

    # Click on the "Play" button to start a new game
    play_button = driver.find_element(By.LINK_TEXT, 'Play')
    play_button.click()

    # Allow time to observe the result of the click
    time.sleep(5)

    # Close the browser
    driver.quit()

if __name__ == '__main__':
    run_script()
