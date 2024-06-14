from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pathlib import Path

debugging = True
script_dir = Path(__file__).resolve().parent
diver_path = script_dir.joinpath("chromedriver-linux64","chromedriver")
service = Service(diver_path)
chrome_options= Options()
#keeps the chrome open until operation is completed
if debugging:
    chrome_options.add_experimental_option("detach", True)
    #input("Enter to exit")from selenium.webdriver.chrome.service import Service
else:
    chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.google.com")

if not debugging:
    driver.quit()