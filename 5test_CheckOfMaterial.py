import unittest
import HTMLTestRunner
global str
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://dev.eor.gosapi.ru/site/login")
driver.maximize_window()
wait = WebDriverWait(driver, 20)
driver.implicitly_wait(20)
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

    def test_002_GotoMaterial(self):
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        driver.find_element_by_css_selector("i.entypo-menu").click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Материалы')))
        driver.find_element_by_link_text("Материалы").click()
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'search-show')))
        print(' 2. Переходим в раздел "Материалы"')

    def test_003_FilterSetting(self):
        driver.find_element_by_id('search-show').click()
        driver.find_element_by_id('search-text').send_keys('1')
        driver.find_element_by_id('search-text-push').click()
        print(' 3. В поиске вводим "1"')

    def test_004_SecondTry(self):
        driver.find_element_by_css_selector('b.caret').click()
        driver.find_element(By.XPATH,"// a[contains(text(), 'Не учитывать')]").click()
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.find-text')))
            driver.find_element_by_css_selector('span.find-text')
            print(' 4. Материалы найден')
        except:
            self.fail(print(' 4. Материалы не найден'))

#if __name__ == "__main__":
#    unittest.main()
    def test_005_CloseDriver(self):
        print(' 5. Тест завершен, браузер закрыт')
        driver.close()

if __name__ == '__main__':
    unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))
    # File
    buf = open("at_for_MATERIAL.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
    stream=buf,
    title='ПРОВЕРКА РАЗДЕЛА "МАТЕРИАЛЫ" НА ОТОБРАЖЕНИЕ МАТЕРИАЛОВ ПО ПОИСКУ БЕЗ УЧЁТА ВРЕМЕНИ',
    description='Отчет по тестированию'
    )
    runner.run(suite)
    #exit()