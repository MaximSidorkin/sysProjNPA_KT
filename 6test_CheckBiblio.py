import unittest, HTMLTestRunner, time
global str
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

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
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password1")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
        print('\n 1. Логинимся в систему')
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))

    def test_002_GotoBiblio(self):
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        driver.find_element_by_css_selector("i.entypo-menu").click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Библиотека')))
        driver.find_element_by_link_text("Библиотека").click()
        wait.until(EC.element_to_be_clickable((By.ID, 'search-show')))
        print('2. переходим в раздел "Библиотека"')

    def test_003_CreateCatalog(self):
        driver.find_element_by_link_text("Создать каталог").click()
        wait.until(EC.element_to_be_clickable((By.ID, "Document_S_NAME")))
        driver.find_element_by_id("Document_S_NAME").send_keys('Selenium catalog')
        driver.find_element_by_xpath("//div/div[3]/span").click()
        print('3. Создаём каталог')

    def test_004_CreateSubcatalog(self):
        driver.find_element_by_id('search-show').click()
        driver.find_element_by_id('search-text').send_keys('Selenium catalog')
        driver.find_element_by_id("search-text-push").click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'span.find-text')))
        driver.find_element_by_css_selector('span.find-text').click()
        ASeleniumLogin_1.test_003_CreateCatalog(self)
        time.sleep(2)
        driver.find_element_by_id("search-text-push").click()
        print("4. В созданном каталоге создаём подкаталог")

    def test_005_DeleteMainCatalog(self):
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.find-text')))
        coords = driver.find_element_by_css_selector('span.find-text')
        #coords.
        hover = ActionChains(driver).move_to_element(coords)
        hover.perform()
        driver.find_element_by_xpath('//div/div[2]/span').click()
        driver.find_element_by_xpath('//div[3]/div/button').click()
        driver.find_element_by_id("search-text-push").click()
        try:
            _ = driver.find_element_by_css_selector('p').text == 'По вашему запросу ничего не найдено'        # По вашему запросу ничего не найдено
            print('5. Через поиск находим созданный каталог и удаляем его, затем проверяем, что и \nсвязанный с ним подкаталог удалён, выведен текст: "По вашему запросу ничего не найдено"\n')
        except:
            self.fail(print('\n \n 5. ОШИБКА! НЕ БЫЛ УДАЛЁН ОСНОВНОЙ СОЗДАННЙ КАТАЛОГ ИЛИ ПОДКАТАЛОГ\n \n'))

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))
    # File
    buf = open("at_for_BIBLIO.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
    stream=buf,
    title='ПРОВЕРКА РАЗДЕЛА "БИБЛИОТЕКА" ',
    description='Отчет по тестированию'
    )
    runner.run(suite)