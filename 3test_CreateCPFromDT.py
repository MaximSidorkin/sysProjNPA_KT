# СОЗДАНИЕ КОНТРОЛЬНОЙ ТОЧКИ C РАБОЧЕГО СТОЛА
import time
import unittest
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

class ASeleniumLogin_1(unittest.TestCase):
    def test_001_LoginInEORDev(self):
        assert "Login" in driver.title
        #wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
    def test_002_Not500or404andLoginIsVisible(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(3)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))

    def test_003_CreateCPfromDT(self):
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='cps_panel']/div/div/ul/div/a/i").click()
        time.sleep(2)

    def test_004_FillingCPForm(self):
        time.sleep(4)
        #имя родителя
        driver.find_element_by_css_selector("i.fa.fa-angle-down").click()
        time.sleep(1)
        driver.find_element_by_css_selector("input.form-control").send_keys("Тестовый проект созданный Selenium")
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
        responsibleNameText.send_keys('ipad' + Keys.ENTER)
        time.sleep(2)
        driver.implicitly_wait(10)
        # new responsible name
        driver.find_element_by_xpath('//div[6]/div/span/span/span/span[2]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//span/input').send_keys('DIT' + Keys.ENTER)
        time.sleep(1)
        #сроки
        terms = driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('123' + Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_xpath("//div/div[3]/span[2]").click()

    def test_005_GotoAllPjct(self):
        time.sleep(3)
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(2)
        allpj = driver.find_element_by_link_text("Все проекты")
        allpj.click()

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

    def test_007_SearchCP(self):
        time.sleep(4)
        driver.find_element_by_css_selector('a.cps-link').click()
        driver.implicitly_wait(10)
        time.sleep(2)
        driver.find_element_by_xpath("//div[2]/table/tbody/tr/td/h4/strong/a").click()
        time.sleep(1)
        try:
            driver.find_element_by_link_text('контрольная точка созданная с рабочего стола Selenium')
            print('\n КТ созданная с рабочего стола найдена и удалена, тест пройден \n')
        except:
            print('\n КТ созданная с рабочего стола не найдена, тест не пройден \n')

        driver.find_element_by_xpath("//button[3]").click()
        time.sleep(1)
        driver.find_element_by_xpath('//div[3]/div/button').click()

if __name__ == '__main__':
    unittest.main()

