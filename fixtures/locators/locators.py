from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_FIRST_NAME = (By.NAME, "first_name")
    LOGIN_LAST_NAME = (By.NAME, "last_name")
    LOGIN_EMAIL = (By.NAME, "email")
    LOGIN_PHONE = (By.NAME, "tildaspec-phone-part[]")
    LOGIN_CHECKBOX_ACC = (By.XPATH, "//*[@id='form344591620']/div[2]/div[5]/div/label/div[1]")
    LOGIN_BTN = (By.XPATH, '//*[@id="form344591620"]/div[2]/div[8]/button')
    OS = (By.XPATH, '//a[contains(@href,"#1_")]')

