# СОЗДАНИЕ КОНТРОЛЬНОЙ ТОЧКИ C РАБОЧЕГО СТОЛА
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
#
oracle = 'https://task.eor.gosapi.ru/oracle/site/login'
pgs = 'https://task.eor.gosapi.ru/pgs/site/login'
dev = 'https://dev.eor.gosapi.ru/new/site/login'
perm = 'http://dev.perm.gosapi.ru/top/'

driver = webdriver.Chrome()
driver.get(pgs)
driver.maximize_window()
wait = WebDriverWait(driver, 40)

class ASeleniumLogin_1(unittest.TestCase):
    def test_001_LoginInEORDev(self):
        assert "Login" in driver.title
        #wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)

        print('\n 1. Логинимся в систему\n')

    def test_002_Not500or404andLoginIsVisible(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(3)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))

        print('\n 2. Ожидаем окончания загрузки страницы рабочего стола\n - страница загружена успешно')

    def test_003_CreateCPfromDT(self):
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='cps_panel']/div/div/ul/div/a/i").click()
        time.sleep(2)

        print('\n 3. На рабочем столе выбираем создать контрольную\n точку путем нажатия кнопки "+"\n')

    def test_004_FillingCPForm(self):
        #time.sleep(4)
        #имя родителя
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.fa.fa-angle-down')))
        driver.find_element_by_css_selector("i.fa.fa-angle-down").click()
        time.sleep(1)
        driver.find_element_by_css_selector("input.form-control").send_keys("Selenium")
        time.sleep(1)
        driver.find_element_by_css_selector('span.find-text').click()
        time.sleep(1)
        #имя контрольной точки
        nameCP = driver.find_element_by_id('Checkpoint_TITLE').send_keys("контрольная точка созданная с рабочего стола Selenium")
        time.sleep(2)
        #ответственный
        driver.implicitly_wait(10)
        responsibleName = driver.find_element_by_xpath("//div[5]/div/span/span/span/span[2]")
        responsibleName.click()
        time.sleep(2)
        responsibleNameText = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleNameText.send_keys('Selenium' + Keys.ENTER)
        time.sleep(2)
        driver.implicitly_wait(10)
        # new responsible name
        driver.find_element_by_xpath('//div[6]/div/span/span/span/span[2]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//span/input').send_keys('Selenium' + Keys.ENTER)
        time.sleep(1)
        #сроки
        terms = driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('123' + Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_xpath("//div/div[3]/span[2]").click()

        print('\n 4. Заполняем форму контрольной точки\n')

    def test_005_GotoAllPjct(self):
        time.sleep(3)
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(2)
        allpj = driver.find_element_by_link_text("Все проекты")
        allpj.click()

        print('\n 5. Переходим в раздел все проекты\n')

    def test_006_FilterSetting(self):
        time.sleep(8)
        driver.find_element_by_css_selector('span.title_executor').click()
        time.sleep(1)
        driver.find_element_by_id('btn_executor').click()
        time.sleep(1)
        driver.find_element_by_id('btn_success_executor').click()
        time.sleep(2)
        driver.find_element_by_link_text('Поиск').click()
        time.sleep(1)
        driver.find_element_by_id('search-text').send_keys('контрольная точка созданная с рабочего стола Selenium'+Keys.ENTER)
        time.sleep(1)

        print('\n 6. В фильтре вводим название созданной контрольной точки\n')

    def test_007_SearchCP(self):
        time.sleep(5)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.cps-link')))
        driver.find_element_by_css_selector('a.cps-link').click()
        driver.implicitly_wait(10)
        time.sleep(2)
        driver.find_element_by_xpath("//div[2]/table/tbody/tr/td/h4/strong/a").click()
        time.sleep(1)
        try:
            driver.find_element_by_link_text('контрольная точка созданная с рабочего стола Selenium')
            print('\n 7. КТ созданная с рабочего стола найдена и удалена, тест пройден \n')
        except:
            print('\n 7. КТ созданная с рабочего стола не найдена, тест не пройден \n')
        driver.find_element_by_xpath("//button[3]").click()
        time.sleep(1)
        driver.find_element_by_xpath('//div[3]/div/button').click()

        time.sleep(2)
        driver.close()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))
    # File
    buf = open("at_for_CREATE_CHECKPOINT_FROM_DESKTOP.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='ПРОВЕРКА СОЗДАНИЯ КОНТРОЛЬНОЙ ТОЧКИ С РАБОЧЕГО СТОЛА',
        description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)