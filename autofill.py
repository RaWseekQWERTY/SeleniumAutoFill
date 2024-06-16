import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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
service = Service(diver_path)
chrome_options= Options()

def set_fields(driver):
    firstName_input = driver.find_element(By.ID,"jform_name")
    userName_input = driver.find_element(By.ID,"jform_username")
    password_input = driver.find_element(By.ID,"jform_password1")
    conformPass_input = driver.find_element(By.ID,"jform_password2")
    email_input = driver.find_element(By.ID,"jform_email1")

    if firstName_input and userName_input and password_input and conformPass_input and email_input:
        firstName_input.send_keys(firstName)
        userName_input.send_keys(username)
        password_input.send_keys(password)
        conformPass_input.send_keys(password)
        email_input.send_keys(email)

def submit_click(driver):
    submit_click = driver.find_element(By.XPATH,'//button[@type="submit" and @class="com-users-registration__register btn btn-primary validate"]')
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

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(signup)
    set_fields(driver)

    if not debugging:
        driver.quit()


if __name__ == "__main__":
    main()


