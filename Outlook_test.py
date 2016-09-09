import time
import unittest
global str
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

from selenium.webdriver.common.keys import Keys

class ASeleniumLogin_1(unittest.TestCase):
    def test001_GotoOutlook(self):
        time.sleep(5)
        driver.get("https://owa.mos.ru/")
        time.sleep(10)
        elem = driver.find_element_by_id("username")
        elem.send_keys("MarenovaTE")
        elem = driver.find_element_by_id("password")
        elem.send_keys("rTZmYVbx")
        elem.send_keys(Keys.RETURN)

    def test002_ViewCalendar(self):
        time.sleep(10)
        driver.find_element_by_id('_ariaId_18').click()
        time.sleep(5)
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.XPATH, ".//*[text()='автотест 4 selenium для совещаний и outlook IPAD Отв.: Соловьев Е. В., участ.: Соловьев Е. В., Соловьев Е']/..").click()
        time.sleep(2)
        driver.find_element(By.XPATH,".//*[text()='ИЗМЕНИТЬ']/..").click()
        time.sleep(4)
        driver.find_element_by_xpath('//div[2]/div[2]/div/button').click()
        time.sleep(3)
        driver.find_element_by_css_selector('span._cm_K').click()
        time.sleep(3)
        driver.find_element_by_xpath('//li[2]/div/div[2]/div/div/div/input').clear()
        time.sleep(2)
        driver.find_element_by_xpath('//li[2]/div/div[2]/div/div/div/input').send_keys('20:00')
        time.sleep(5)
        driver.find_element_by_xpath('//div[2]/button[2]').click()
        time.sleep(4)

    def test003_GotoEOP(self):
        driver.get("https://dev.eor.gosapi.ru/site/login")
        assert "Login" in driver.title
        # wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)

    def test004_Not500or404andLoginIsVisible(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(3)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))

    def test005_GotoMeetings(self):
        time.sleep(2)
        driver.find_element_by_css_selector("i.entypo-menu").click()
        time.sleep(2)
        driver.find_element_by_link_text("Расписание").click()
        time.sleep(6)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))

        if __name__ == '__main__':
            unittest.main()
