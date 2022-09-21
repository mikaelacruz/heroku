from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




if __name__ == "__main__":

    driver = Chrome()
    driver.get("https://syndio-qa-interview-dashboard.herokuapp.com/")
    wait = WebDriverWait(driver, 10)


    # Verify Two Tabs + Functionality
    # QA-6, QA-4
    # Race Tab
    race_tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li#tab-race > button')))
    race_tab.click()
    time.sleep(5)
    print("PASSED: CLICK RACE TAB")
    # Gender Tab
    gender_tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li#tab-gender > button')))
    gender_tab.click()
    time.sleep(5)
    print("PASSED: CLICK GENDER TAB")

    # Verify Dropdown Button + Functionality
    # QA-10, QA-5
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#dropdown-button > span')))
    element.click()
    time.sleep(5)
    print("PASSED: CLICK DROPDOWN BUTTON")


    driver.close()
