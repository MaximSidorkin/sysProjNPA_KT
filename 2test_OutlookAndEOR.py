# ТЕСТИРОВАНИЕ СИНХРОНИЗАЦИИ ОТПРАВКИ ОПОВЕЩЕНИЙ НА OUTLOOK ИЗ ЭОР
import time
import unittest
import HTMLTestRunner
import sys
global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://dev.eor.gosapi.ru/site/login")
driver.maximize_window()
wait = WebDriverWait(driver, 60)

class ASeleniumLogin_1(unittest.TestCase):
    def test_001_LoginInEORDev(self):
        assert "Login" in driver.title
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
        print(' 1. Логинимся в систему\n')

    def test_002_Not500or404andLoginIsVisible(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(3)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        print(' 2. Логин пользователя отображается\n')

    def test_003_GotoSyncURL(self):
        driver.get("https://dev.eor.gosapi.ru/ewsup")
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'btn-ewsup')))
        print(' 3. Переход на страницу синхронизатора и нажатие кнопки "Синхронизировать" \n')

    def test_004_SyncClick(self):
        driver.find_element_by_id('btn-ewsup').click()
        time.sleep(1)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'COMPLETE')]")))
            print(' 4. Синхронизация прошла успешно \n')
        except:
            self.fail(print(' \n \n ОШИБКА СИНХРОНИЗАЦИИ \n \n'))

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))
    # File
    buf = open("at_for_SYNCHRONIZER.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
    stream=buf,
    title='ПРОВЕРКА ФУНКЦИОНИРОВАНИЯ СИНХРОНИЗАТОРА',
    description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)