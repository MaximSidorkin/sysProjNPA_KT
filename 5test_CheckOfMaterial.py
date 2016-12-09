import unittest
import HTMLTestRunner

global str
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import sys

driver = webdriver.Firefox()
driver.get("https://dev.eor.gosapi.ru/site/login")
driver.maximize_window()
wait = WebDriverWait(driver, 20)
driver.implicitly_wait(10)
body = driver.find_element_by_tag_name('body')

class ASeleniumLogin_1(unittest.TestCase):
    def test_001_LoginInEORDev(self):
        assert "Login" in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username1")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
        print('\n 1. Логинимся в систему')
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))

if __name__ == '__main__':
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(ASeleniumLogin_1))
        buf = open("at_for_MATERIAL.html", 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=buf,
            title='ПРОВЕРКА РАЗДЕЛА "МАТЕРИАЛЫ" НА ОТОБРАЖЕНИЕ МАТЕРИАЛОВ ПО ПОИСКУ БЕЗ УЧЁТА ВРЕМЕНИ',
            description='Отчет по тестированию'
           )
        runner.run(suite)

        #if __name__ == "__main__":
        #    unittest.main()
        #ret = not runner.run(suite).wasSuccessful()
        #sys.exit(ret)

#if __name__ == '__main__':
        #ret = not runner.run(suite).wasSuccessful()
        #sys.exit(ret)

#    unittest.main(sys.exit())
    #sys.exit()