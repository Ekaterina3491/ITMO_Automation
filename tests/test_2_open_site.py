from selenium import webdriver
from selenium.webdriver.common.by import By

def test():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/")


    icon = driver.find_elements(By.CSS_SELECTOR, 'header > a > img')
    if icon is None:
        print('Элемент не найден')
    else:
        print('Элемент  найден')