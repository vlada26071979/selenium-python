'''Verify that user is able to log in successfully with valid username and password - "Happy path"
   Verify that user can't log in with invalid username and invalid password - "Sad path" '''

# Importing all necessary libraries and modules
from selenium import webdriver
import locator
from locator import *
import time

# Open Chrome browser


# Navigating to the web page
#def test_open_web_page():

def test_happy_path():
    driver = webdriver.Edge()
    url = "https://www.saucedemo.com/"
    driver.get(url)
    print(f"Successfully navigated to {url}")
    # Finding web elements
    username_field = driver.find_element(*locator.username_element)
    password_field = driver.find_element(*locator.password_element)
    login_btn = driver.find_element(*locator.login_btn_element)

    # Entering username,password and clicking on the 'Login' button
    username_field.send_keys('standard_user')
    time.sleep(2)
    password_field.send_keys('secret_sauce')
    time.sleep(2)
    login_btn.click()

    # making sure that we are on the expected page after login
    current_url = driver.current_url
    expected_url = 'https://www.saucedemo.com/inventory.html'
    assert current_url == expected_url, 'Login failed, something went wrong!'

    # creating test evidence and quiting the browser
    driver.save_screenshot('inventory_page.png')
    print('TEST PASSED!')
    time.sleep(5)
    driver.quit()

def test_sad_path():
    driver = webdriver.Edge()
    url = "https://www.saucedemo.com/"
    driver.get(url)
    print(f"Successfully navigated to {url}")
    # Finding web elements
    username_field = driver.find_element(*locator.username_element)
    password_field = driver.find_element(*locator.password_element)
    login_btn = driver.find_element(*locator.login_btn_element)

    # Entering username,password and clicking on the 'Login' button
    username_field.send_keys('extra_user')
    password_field.send_keys('abcdef')
    login_btn.click()

    # # making sure that appropriate error message is displayed
    expected_error_msg = 'Epic sadface: Username and password do not match any user in this service'
    error_msg = driver.find_element(*locator.error_msg_element)
    error_msg_text = error_msg.text
    assert error_msg_text == expected_error_msg, 'Ooooops wrong message displayed!!!'

    # creating test evidence and quiting the browser
    driver.save_screenshot('error_message.png')
    print('TEST PASSED')
    driver.quit()

# def main():
#     open_web_page('https://www.saucedemo.com/')
#     test_happy_path()
#     #test_sad_path()

# if __name__ == '__main__':
#    main()













