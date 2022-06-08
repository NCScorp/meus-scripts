from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('http://localhost:8000/admin/')
username = driver.find_element_by_id('jsusername')
pwd = driver.find_element_by_id('jspassword')

username.send_keys('admin')
pwd.send_keys('Caraca!SRE!321')
sleep(2)

login_attempt = driver.find_element(By.XPATH, "//*[@type='submit']")
login_attempt.submit()
sleep(3)

driver.get('http://localhost:8000/admin/configure-plugin/pluginWpImporter')
sleep(3)

wp_nasajon = driver.find_element(By.XPATH, "//*[@type='text']")
wp_nasajon.send_keys('https://compilacoes.nasajon.com.br/')
btn_import_posts = driver.find_element(By.XPATH, "//*[contains(text(), 'Import Posts')]")
btn_import_posts.click()
sleep(3)

i = 1

while i < 100:
    import_all = driver.find_element(By.XPATH, "//*[contains(text(), 'Import all')]")
    import_all.click()
    sleep(2)

    next_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Next')]")
    next_button.click()

    sleep(4)

    print(f"pagina {i} concluída")

    i += 1
