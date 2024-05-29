from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'
browser = Firefox()

browser.get(url)

sleep(3)

a = browser.find_element(By.TAG_NAME, 'a')
p = browser.find_element(By.TAG_NAME, 'p')

a.click()
a.click()
a.click()
a.click()

print(f'texto a = {a.text}')
print(f'texto a = {p.text}')

# min 52:04