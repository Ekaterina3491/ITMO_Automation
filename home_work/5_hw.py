from selenium import webdriver
from selenium.webdriver.common.by import By
def test():
     driver = webdriver.Chrome()
     driver.get("https://www.saucedemo.com/")

     username_field = driver.find_element(By.ID, 'user-name')
     password_field = driver.find_element(By. ID, 'password')
     submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")

     if username_field and password_field and submit_button:
         print("Элементы найдены")
     else:
         print("Элементы не найдены")
test()