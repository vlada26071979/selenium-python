from selenium import webdriver
from selenium.webdriver.common.by import By

username_element = (By.ID,'user-name')
password_element = (By.CSS_SELECTOR,'#password')
login_btn_element = (By.ID,'login-button')
error_msg_element = (By.CSS_SELECTOR,'h3[data-test="error"]')
