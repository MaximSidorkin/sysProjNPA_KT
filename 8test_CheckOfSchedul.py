import unittest, time, sys

global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
#
dev = 'https://dev.eor.gosapi.ru/new/'
oracle = 'https://task.eor.gosapi.ru/oracle/site/login'
pgs = 'https://task.eor.gosapi.ru/pgs/site/login'


driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.get(oracle)
driver.maximize_window()
wait = WebDriverWait(driver, 20)
driver.implicitly_wait(20)

class ASeleniumAutoTest_1(unittest.TestCase):
    def test001_CreatedInEORDev(self):
        assert "Login" in driver.title
        try:
            assert 'ЭОР - Error' not in driver.title
        except:
            print('ошибка 500!')
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
        print('\nтест №1 - Нет ошибок при вводе логина')

    def test_002_Not500or404andLoginIsVisible(self):
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        print('тест №2 - проверка на 404 и 500 ошибку после ввода логина/пароля')
        try:
            driver.find_element_by_class_name('hidden-xs')
        except:
            self.fail(print('Не отобразился / не подгрузился логин пользователя'))

    def test_003_GotoScheduler(self):
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        driver.find_element_by_css_selector("i.entypo-menu").click()
        _ = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Расписание')))
        driver.find_element_by_link_text("Расписание").click()
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))
        print('тест №3 - переход в раздел "Расписание"')

if __name__ == '__main__':
    unittest.main()
