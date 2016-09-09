# ТЕСТИРОВАНИЕ СИНХРОНИЗАЦИИ ОТПРАВКИ ОПОВЕЩЕНИЙ НА OUTLOOK ИЗ ЭОР
import time
import unittest
global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.get("https://dev.eor.gosapi.ru/site/login")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

class ASeleniumLogin_1(unittest.TestCase):
    def test001_LoginInEORDev(self):
        assert "Login" in driver.title
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
    def test002_Not500or404andLoginIsVisible(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(3)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))

    def test003_GotoMeetings(self):
        time.sleep(2)
        driver.find_element_by_css_selector("i.entypo-menu").click()
        time.sleep(2)
        driver.find_element_by_link_text("Расписание").click()
        time.sleep(6)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))

    def test004_CreateMeeting(self):
        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='bs-example-navbar-collapse-3']/div[5]/div[2]").click()
        print('тест №4 - нажимаем кнопку "Создать" на открывшейся форме')

    def test005_FillingMeetingForm_1(self):
        time.sleep(7)
        driver.find_element_by_id('MeetingsData_S_NAME').send_keys('Selenium. ЭОР (для редактирования в ЭОР)')  # заполняем название мероприятия

    def test006_ForSolov(self):
        driver.find_element_by_css_selector('ul.select2-selection__rendered').click()   # кликаем по выпадающему списку пользователей
        driver.find_element_by_xpath('//form/div[5]/div/span/span[1]/span/ul/li/input').send_keys('яAnd' + Keys.ENTER)  # выбираем пользователя Android
        driver.find_element_by_xpath('//div[8]/div/span/span/span/span[2]').click() # кликаем по выпадающему списку ответственных
        time.sleep(1)
        driver.find_element_by_xpath('//body[@id="ui-id-1"]/span/span/span/input').send_keys('яAnd' + Keys.ENTER) # выбираем пользователя Android

    def test007_NewTime(self):
        driver.find_element_by_id('MeetingsData_D_START').clear()    # очищаем время начала мероприятия
        driver.find_element_by_id('MeetingsData_D_START').send_keys('21:12' + Keys.ENTER)    # устанавливаем свое время начала мероприятия
        driver.find_element_by_id('MeetingsData_D_END').clear()  # очищаем время окончания мероприятия
        driver.find_element_by_id('MeetingsData_D_END').send_keys('21:31' + Keys.ENTER)  # устанавливаем свое время окончанию мероприятия
        driver.save_screenshot('C:\PyTest\inish.png')
        driver.find_element_by_name('yt0').click()
        print('тест №5 - заполняем форму создания совещания')

    def test008(self):
        time.sleep(6)
        ASeleniumLogin_1.test004_CreateMeeting(self)
        time.sleep(6)
        driver.find_element_by_id('MeetingsData_S_NAME').send_keys('Selenium. ЭОР (для редактирования в Outlook)')
        ASeleniumLogin_1.test006_ForSolov(self)
        driver.find_element_by_id('MeetingsData_D_START').clear()    # очищаем время начала мероприятия
        driver.find_element_by_id('MeetingsData_D_START').send_keys('21:31' + Keys.ENTER)    # устанавливаем свое время начала мероприятия
        driver.find_element_by_id('MeetingsData_D_END').clear()  # очищаем время окончания мероприятия
        driver.find_element_by_id('MeetingsData_D_END').send_keys('21:51' + Keys.ENTER)  # устанавливаем свое время окончанию мероприятия
        driver.find_element_by_name('yt0').click()

    def test009_GoToOutlook(self):  # переходим в outlook и вводим логин/пароль для Мареновой
        time.sleep(6)
        driver.get("https://owa.mos.ru/")
        time.sleep(10)
        elem = driver.find_element_by_id("username")
        elem.send_keys("MarenovaTE")
        elem = driver.find_element_by_id("password")
        elem.send_keys("rTZmYVbx")
        elem.send_keys(Keys.RETURN)
        time.sleep(7)
        driver.find_element_by_id('_ariaId_18').click()

    def test010_CreateOutlookMeeting(self):
        time.sleep(5)
        driver.find_element(By.XPATH, ".//*[text()='создать событие']/..").click()
        time.sleep(3)

    def test011_NameMeeting(self):
        driver.find_element_by_xpath('//div[2]/div[2]/div[2]/div/div/input').send_keys('Selenium. Outlook (для редактирвоания в ЭОР)')
        time.sleep(1)

    def test012_CreateOutlookMeeting(self):
        driver.find_element_by_xpath('//div/div/span/div/form/input').send_keys('яAnd')
        time.sleep(1)
        driver.find_element_by_xpath('//div/div/span/div/form/input').send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_xpath('//li[1]/div[2]/div/div/div/input').clear()
        time.sleep(1)

    def test013_MeetingTime(self):
        driver.find_element_by_xpath('//li[1]/div[2]/div/div/div/input').send_keys('19:19')
        time.sleep(3)

    def test014_ConfirmOM(self):
        driver.find_element(By.XPATH, ".//*[text()='ОТПРАВИТЬ']/..").click()
        time.sleep(4)

    def test015_CreateOutlookMeeting(self):
        ASeleniumLogin_1.test010_CreateOutlookMeeting(self)
        driver.find_element_by_xpath('//div[2]/div[2]/div[2]/div/div/input').send_keys('Selenium. Outlook (для редактирвоания в Outlook)')
        time.sleep(1)
        ASeleniumLogin_1.test012_CreateOutlookMeeting(self)
        driver.find_element_by_xpath('//li[1]/div[2]/div/div/div/input').send_keys('19:49')
        ASeleniumLogin_1.test014_ConfirmOM(self)

    def test016_EditEORMeeting(self):
        time.sleep(3)
        #driver.find_element(By.XPATH, ".//*[text()='*(для редактирования в Outlook)*'/..").click()   #Selenium. ЭОР  Отв.: яAndroid1 An. 3., участ.: яAndroid1 An. 3., ']
        try:
            driver.find_element(By.XPATH, ".//*[text()='*для редактирования в Outlook'/..")
        except(NoSuchElementException):
            print('ПОЧЕМУ-ТО НЕ НАШЕЛ ТЕКСТ!')

        #if driver.find_element_by_xpath("//*[contains(text(), '*(для редактирования в Outlook)*')]"):
        #    print('НЕУЖЕЛИ?!')
        #else:
        #    print('ПОЧЕМУ-ТО НЕ НАШЕЛ ТЕКСТ!')
        #    time.sleep(3)

        #driver.find_element(By.XPATH, ".//*[text()='ИЗМЕНИТЬ']/..").click()
        #time.sleep(4)
        #driver.find_element_by_xpath('//li[2]/div/div[2]/div/div/div/input').clear()
        #time.sleep(2)
        #driver.find_element_by_xpath('//li[2]/div/div[2]/div/div/div/input').send_keys('21:41')
        #time.sleep(5)
        #driver.find_element_by_xpath('//div[3]/div/div/div[2]/button').click()
        #time.sleep(4)

    #def test017_GotoEOR(self):
    #    driver.get("https://dev.eor.gosapi.ru/")
    #    time.sleep(5)
    #    driver.find_element_by_link_text("Расписание").click()
    #   time.sleep(9)

    # тест 18 должен запускаться в через 10 минут после теста 17
    #def test018_FindOutlookEditionMeeting(self):
    #    driver.find_element_by_xpath("//span[. = '21:31 - 21:41' ]").click()
    #    time.sleep(3)


    #def test019_EditOutlookMeeting(self):
    #    time.sleep(1)


        if __name__ == '__main__':
            unittest.main()
