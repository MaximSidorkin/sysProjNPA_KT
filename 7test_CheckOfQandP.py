import unittest, HTMLTestRunner, time, sys
global str
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

oracle = 'https://task.eor.gosapi.ru/oracle/site/login'
pgs = 'https://task.eor.gosapi.ru/pgs/site/login'

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.get(oracle)
driver.maximize_window()
wait = WebDriverWait(driver, 40)
driver.implicitly_wait(40)
body = driver.find_element_by_tag_name('body')

class ASeleniumLogin_1(unittest.TestCase):

    def test_001_LoginInEORDev(self):
        assert "Login" in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
        print('\n Логинимся в систему')
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))

    def test_002_GotoQuestions(self):
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        driver.find_element_by_css_selector("i.entypo-menu").click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Вопросы/Приоритеты')))
        driver.find_element_by_link_text("Вопросы/Приоритеты").click()
        wait.until(EC.element_to_be_clickable((By.ID, 'search-show')))
        print('Переходим в раздел "Вопросы/Приоритеты"')

    def test_003_CreateQ(self):
        wait.until(EC.element_to_be_clickable((By.ID, 'btn_create_user')))
        driver.find_element_by_id('btn_create_user').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'Question_S_DESCRIPTION')))
        # Question
        try:
            time.sleep(1)
            q = driver.find_element_by_id('typeCaption').text == 'важного вопроса'
            print('Проверка триггера. \n В положении "Приоритет НЕТ, отображен заголовок "Создание важного вопроса"\n')
        except:
            print('\n\nОШИБКА! ЗАГОЛОВОК НЕ СООТВЕТСТВУЕТ ПОЛОЖЕНИЮ ТРИГГЕРА\n\n')
        # Priority
        driver.find_element_by_class_name('switch-right').click()
        time.sleep(1)
        try:
            p = driver.find_element_by_id('typeCaption').text == 'приоритета'
            print('Проверка триггера. \n В положении "Приоритет ДА, отображен заголовок "Создание Приоритета"\n')
        except:
            print('\n\nОШИБКА! ЗАГОЛОВОК НЕ СООТВЕТСТВУЕТ ПОЛОЖЕНИЮ ТРИГГЕРА\n\n')

    def test_004_AddDescription(self):
        driver.find_element_by_id('Question_S_DESCRIPTION').send_keys('Selenium priority')
        print('Добавляем описание')

    def test_006_AddInit(self):
        driver.find_element_by_xpath('//div/span/span/span/span').click()
        driver.find_element_by_xpath('//span/input').send_keys('яIpad'+Keys.ENTER)
        print('Добавляем инициатора')

    def test_007_Create(self):
        driver.find_element_by_name('yt0').click()
        print("Подтверждаем создание приоритета")
        time.sleep(5)

    def test_008_DelPrior(self):
        driver.find_element_by_xpath("//li/label[2]").click()
        driver.find_element_by_link_text('Selenium priority').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'btn_remove')))
        driver.find_element_by_id('btn_remove').click()
        driver.find_element_by_xpath("//span[. = 'Да' ]").click()
        print('Удаляем приоритет')

    def test_009_More(self):
        print('Проверяем наличие ранее созданных АТ приоритетов:')
        try:
            if driver.find_element_by_link_text('Selenium priority'):
                driver.find_element_by_link_text('Selenium priority').click()
                wait.until(EC.element_to_be_clickable((By.ID, 'btn_remove')))
                driver.find_element_by_id('btn_remove').click()
                driver.find_element_by_xpath("//span[. = 'Да' ]").click()
                print('Удаляем лишний приоритет созданный ранее')
            else:
                print("Был только один приоритет")
        except:
            print("Был только один приоритет")
        driver.close()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))
    # File
    buf = open("at_for_QUESTIONS_AND_PRIORITY.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='СОЗДАНИЕ И УДАЛЕНИЕ ПРИОРИТЕТА',
        description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)


