from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://twitter.com/')
driver.maximize_window()
driver.implicitly_wait(15)

loginButton = driver.find_element(By.XPATH, '//span[text() = "Sign in"]')
loginButton.click()

time.sleep(3)
userName = driver.find_element(By.XPATH, '//input')
userName.send_keys('ozandemirel.93@gmail.com')

nextButton = driver.find_element(By.XPATH, '//span[text() = "Next"]')
nextButton.click()

try:
    userName2 = driver.find_element(By.XPATH, '//input')
    userName2.send_keys('ozandemirel93')
    nextButton2 = driver.find_element(By.XPATH, '//span[text()="Next"]')
    nextButton2.click()
except:
    pass

time.sleep(1)

passElement = driver.find_element(By.XPATH, '//input[@type="password"]')
passElement.send_keys('****************')

loginButton = driver.find_element(By.XPATH, '//span[text()="Log in"]')
loginButton.click()

searchArea = driver.find_element(By.XPATH, '//input[@aria-activedescendant]')
searchArea.send_keys('ozansrobot1')
searchArea.send_keys(Keys.ENTER)

peopleTab = driver.find_elements(By.XPATH, '//span[text() = "People"]')
peopleTab[0].click()

ozansRobot = driver.find_elements(By.XPATH, '//a[@href = "/ozansrobot1"]')
ozansRobot[1].click()

restrictedButton = driver.find_element(By.XPATH, '//span[text() = "Yes, view profile"]')
restrictedButton.click()

driver.implicitly_wait(0)
previousYLocation = -1
while True:
    try:
        likeButtons = driver.find_elements(By.XPATH, '//div[@data-testid = "like"]')
        if len(likeButtons) != 0:
            for likeButton in likeButtons:
                likeButton.click()
    except:
        pass
    driver.execute_script("window.scrollTo(0, "+str(driver.execute_script('return window.pageYOffset')+25)+");")
    currentYLocation = driver.execute_script('return window.pageYOffset')
    if currentYLocation == previousYLocation and currentYLocation != 0:
       break
    previousYLocation = driver.execute_script('return window.pageYOffset')

time.sleep(5)
driver.close()
