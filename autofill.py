import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException
from pathlib import Path

load_dotenv()
#declarations
debugging = True
firstName = os.getenv("FIRST_NAME")
lastName = os.getenv("LAST_NAME")
email=os.getenv("EMAIL")
phNo=os.getenv("PH_NO")
password=os.getenv("PASSWORD")
username=os.getenv("USERNAME")
signup = os.getenv("SIGNUP_PAGE")

"""
def set_fieldEncryption(driver, element):
    driver.execute_script(f"document.getElementById('{element}).type="'password'")
"""
#driver path
script_dir = Path(__file__).resolve().parent
diver_path = script_dir.joinpath("chromedriver-linux64","chromedriver")

chrome_options= Options()

def wait_for_element(driver, by,element_identifier,timeout=5):
    try:
        presentElement=EC.presence_of_element_located((by, element_identifier))

    except TimeoutException:
        print(f"Timed out waiting for {element_identifier} to load")
        return None
    return driver.find_element(by,element_identifier)

def set_fields(driver):
    firstName_input = wait_for_element(driver,By.ID,"jform_name")
    userName_input = wait_for_element(driver,By.ID,"jform_username")
    password_input = wait_for_element(driver,By.ID,"jform_password1")
    conformPass_input = wait_for_element(driver,By.ID,"jform_password2")
    email_input = wait_for_element(driver,By.ID,"jform_email1")

    if firstName_input and userName_input and password_input and conformPass_input and email_input:
        firstName_input.send_keys(firstName)
        userName_input.send_keys(username)
        password_input.send_keys(password)
        conformPass_input.send_keys(password)
        email_input.send_keys(email)

def submit_click(driver):
    submit_click = wait_for_element(driver,By.XPATH,'//button[@type="submit" and @class="com-users-registration__register btn btn-primary validate"]')
    print(submit_click)
    if submit_click:
        submit_click.click()

def main():
    #keeps the chrome open until operation is completed
    if debugging:
        chrome_options.add_experimental_option("detach", True)
    #input("Enter to exit")from selenium.webdriver.chrome.service import Service
    else:
        chrome_options.add_argument("--headless")
    service = Service(diver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(signup)
    try:
        set_fields(driver)
        submit_click(driver)
    except WebDriverException as e:
        print(f"WebDriver Error {e}")
    finally:
        if not debugging:
         driver.quit()




if __name__ == "__main__":
    main()


