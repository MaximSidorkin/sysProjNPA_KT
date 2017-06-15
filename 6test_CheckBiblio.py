import unittest, HTMLTestRunner, time, sys
global str
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

oracle = 'https://task.eor.gosapi.ru/oracle/site/login'
pgs = 'https://task.eor.gosapi.ru/pgs/site/login'
dev = 'https://dev.eor.gosapi.ru/new/'
perm = 'http://dev.perm.gosapi.ru/top/'

driver = webdriver.Chrome()
driver.get(perm)
driver.maximize_window()
wait = WebDriverWait(driver, 50)
driver.implicitly_wait(50)
body = driver.find_element_by_tag_name('body')

class ASeleniumLogin_1(unittest.TestCase):
    def test_001_LoginInEORDev(self):
        assert "Login" in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("ipad")
        elem = driver.find_element_by_id("LoginForm_password")
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
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Создать каталог")))
        driver.find_element_by_link_text("Создать каталог").click()
        wait.until(EC.element_to_be_clickable((By.ID, "Document_S_NAME")))
        driver.find_element_by_id("Document_S_NAME").send_keys('Selenium catalog')
        driver.find_element_by_xpath("//div/div[3]/span").click()
        print('3. Создаём каталог')

    def test_004_CreateSubcatalog(self):
        driver.find_element(By.XPATH, ".//*[text()='Selenium catalog']/..").click()

        #driver.find_element_by_id('search-show').click()
        #driver.find_element_by_id('search-text').send_keys('Selenium catalog')
        #driver.find_element_by_id("search-text-push").click()
        #wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'span.find-text')))
        #driver.find_element_by_css_selector('span.find-text').click()
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Создать каталог")))
        driver.find_element_by_link_text("Создать каталог").click()
        wait.until(EC.element_to_be_clickable((By.ID, "Document_S_NAME")))
        driver.find_element_by_id("Document_S_NAME").send_keys('Selenium catalog')
        driver.find_element_by_xpath("//div/div[3]/span").click()
        print('3. Создаём каталог\n4. В созданном каталоге создаём подкаталог')
        time.sleep(2)
        #driver.find_element_by_id("search-text-push").click()
        #print('4. В созданном каталоге создаём подкаталог')
#
    def test_005_DeleteMainCatalog(self):
        driver.implicitly_wait(10)
        #time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "a.cursor").click()
        #wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.find-text')))
        time.sleep(2)
        coords = driver.find_element(By.XPATH, ".//*[text()='Selenium catalog']/..")
        #coords = driver.find_element_by_css_selector('span.find-text')
        #coords.
        time.sleep(2)
        hover = ActionChains(driver).move_to_element(coords)
        hover.perform()
        time.sleep(2)
        driver.find_element_by_xpath('//div/div[2]/span').click()
        time.sleep(2)
        driver.find_element_by_xpath('//div[3]/div/button').click()
        time.sleep(2)
        #driver.find_element_by_id("search-text-push").click()
        #time.sleep(2)
        try:
            _ = driver.find_element(By.XPATH, ".//*[text()='Selenium catalog']/..")
            #_ = driver.find_element_by_css_selector('p').text == 'По вашему запросу ничего не найдено'        # По вашему запросу ничего не найдено
            #print('5. Через поиск находим созданный каталог и удаляем его, затем проверяем, что и \nсвязанный с ним подкаталог удалён, выведен текст: "По вашему запросу ничего не найдено"\n')
            print('5. Папка с названием Selenium catalog НЕ удалена')
        except:
            print('5. Папка с названием Selenium catalog удалена')
            #self.fail(print('\n \n 5. ОШИБКА! НЕ БЫЛ УДАЛЁН ОСНОВНОЙ СОЗДАННЙ КАТАЛОГ ИЛИ ПОДКАТАЛОГ\n \n'))

    def test_006_addAttach(self):
        driver.find_element_by_link_text('Добавить документы').click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.fa.fa-link')))
        driver.find_element_by_css_selector('i.fa.fa-link').click()
        driver.find_element_by_xpath('//div[2]/div[2]/input').send_keys('Selenium')
        driver.find_element_by_xpath('//div[2]/input[2]').send_keys('Selenium')
        driver.find_element_by_xpath('//span[3]/span/i').click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Selenium')))
        driver.find_element_by_xpath('//div/div[3]/span').click()

        driver.find_element_by_id('search-show').click()
        driver.find_element_by_id('search-text').send_keys('Selenium')
        driver.find_element_by_id("search-text-push").click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'span.find-text')))

        coords = driver.find_element_by_css_selector('span.find-text')
        time.sleep(2)
        hover = ActionChains(driver).move_to_element(coords)
        hover.perform()
        driver.find_element_by_xpath('//div/div[2]/span').click()
        time.sleep(2)
        driver.find_element_by_xpath('//div[3]/div/button').click()
        time.sleep(1)
        print("6. Создаём вложение - ссылку и удаляем его")
        try:
            check = driver.find_element_by_css_selector('div.toast-message')
            print(check.text)
        except:
            self.fail(print('Не выведено сообщение о успешном удалении вложения'))

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
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)