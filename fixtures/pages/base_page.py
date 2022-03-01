from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
options = Options()
options.headless = False
options.add_experimental_option("excludeSwitches", ["enable-logging"])
url = 'https://r7-office.ru/request_personal'
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


def open_auth_page():
    driver.get(url)


def custom_find_element(locator, wait_time=10):
    element = WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located(locator),
        message=f"Cant{locator}",
    )
    return element


def get_list(locator):
    """
    Try to get list of available OS
    """
    driver.implicitly_wait(20)
    elements = driver.find_elements(*locator)
    texts = []
    for element in elements:
        text = element.text
        texts.append(text)
    os = [text for text in texts if text]
    return os


def click_element(locator, wait_time=10):
    """
    Click_element == click()
    """
    element = custom_find_element(locator, wait_time)
    element.click()


def fill_element(data, locator, wait_time=10):
    """
    Fill element == send_keys()
    """
    element = custom_find_element(locator, wait_time)
    if data:
        element.send_keys(data)


def get_text(locator, wait_time=10):
    """
    Get element text
    """
    element = custom_find_element(locator, wait_time)
    return element.text


def close_browser():
    """
    Close the browser
    """
    driver.quit()
