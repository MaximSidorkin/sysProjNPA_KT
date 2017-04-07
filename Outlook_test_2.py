import unittest, sys, HTMLTestRunner, time

global str
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
#driver = webdriver.Firefox()   #
driver.get("https://dev.eor.gosapi.ru/new")
driver.maximize_window()
wait = WebDriverWait(driver, 150)
driver.implicitly_wait(40)
body = driver.find_element_by_tag_name('body')

class ASeleniumLogin_1(unittest.TestCase):
    def test001_LoginInEORDev(self):
        assert "Login" in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username").send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password").send_keys("ipad"+Keys.RETURN)
        #elem.send_keys(Keys.RETURN)
        print('\n Логинимся в систему')
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))

    def test002_GotoScheduler(self):
        driver.get('https://dev.eor.gosapi.ru/new/schedule')
        print(' Переходим в расписнание')

    def test003_DelMeetAnotherUser(self):
        print(' Создаём совещание пользователем 1 с участником 2, \nи удаляем совещание у ползователя 2,\n Создаём новое совещение пользователем Ipad')
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='bs-example-navbar-collapse-3']/div[5]/div[2]")))
        crMeeting = driver.find_element_by_xpath("//div[@id='bs-example-navbar-collapse-3']/div[5]/div[2]").click()
        print(' Нажимаем кнопку "Создать" на открывшейся форме')
        #time.sleep(3)
        name = driver.find_element_by_id('MeetingsData_S_NAME').send_keys('for LOGIN')
        unit = driver.find_element_by_xpath('//div[5]/div/div/div/input').click()
        unit = driver.find_element_by_xpath('//div[5]/div/div/div/input').send_keys('Афанасьев')
        time.sleep(2)
        driver.find_element_by_xpath('//div[5]/div/div/div/input').send_keys(Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(1)
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').clear()
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').send_keys('23:00' + Keys.ENTER)
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').clear()
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').send_keys('23:30' + Keys.ENTER)
        print(' Заполняем форму создания совещания')
        time.sleep(2)
        driver.find_element_by_name('yt0').click()
        try:
            popUp = driver.find_element_by_css_selector('div.toast-message')
            print(' Всплывающее уведомлние: "', popUp.text, '" - выведено')
        except:
            print("I DON'T SEE POPUP")

    def test004_Relog(self):
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.caret')))
        driver.find_element_by_css_selector('span.caret').click()
        driver.find_element_by_link_text('Выход').click()
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("login")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("login" + Keys.RETURN)
        print(' Перезаходим в систему под пользователем login/login ')

    def test005_gotoScheduler(self):
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        driver.get('https://dev.eor.gosapi.ru/new/schedule')
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))
        print(" Переходим в раздел расписания пользователя login")

    def test006_searchMeet(self):
        driver.find_element_by_xpath("//span[. = '23:00 - 23:30' ]").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='Удалить']/..")))
        time.sleep(1)
        driver.find_element(By.XPATH, ".//*[text()='Удалить']/..").click()
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[3]/div/button")))
        driver.find_element(By.XPATH, "//div[3]/div/button").click()
        time.sleep(1)
        print(' В разделе расписания находим созданное пользоватлеме ipad совещание\n и удаляем его')
        try:
            delMess = driver.find_element_by_css_selector('div.toast-message')
            print(delMess.text)
        except:
            print('NO POPUP MSG')

    def test007_loginIpad(self):
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.caret')))
        driver.find_element_by_css_selector('span.caret').click()
        driver.find_element_by_link_text('Выход').click()
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad"+Keys.RETURN)
        print(' Перезаходим в систему под пользователем ipad/ipad ')

    def test008_gotoMeet(self):
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        driver.get('https://dev.eor.gosapi.ru/new/schedule')
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))
        driver.find_element_by_xpath("//span[. = '23:00 - 23:30' ]").click()
        try:
            driver.find_element_by_xpath(".//*[text()='Афанасьев В.П']/..")
            self.fail(print(' Совещание найдено, участник найден. ОШИБКА!'))
        except:
            print(' Тест прошёл успешно - участник удалён')
        wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='Удалить']/..")))
        time.sleep(1)
        driver.find_element(By.XPATH, ".//*[text()='Удалить']/..").click()
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[3]/div/button")))
        driver.find_element(By.XPATH, "//div[3]/div/button").click()
        time.sleep(1)
        print(' Удаляем совещание пользоватлеме ipad')
        try:
            delMess = driver.find_element_by_css_selector('div.toast-message')
            print(delMess.text)
        except:
            print('NO POPUP MSG')

    def test009__CreateInEORDelInOutlook(self):
        print(' Создание совещаний из раздела расписания и рабочий\n стол для Вед. и Уч. и удаление их в Outlook')
        ASeleniumLogin_1.test003_DelMeetAnotherUser(self)
        print(' Переходим в рабочий стол')
        time.sleep(2)
        driver.get('https://dev.eor.gosapi.ru/new/')
        driver.implicitly_wait(15)
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//tr[23]/td[2]")))
        driver.find_element_by_xpath('//tr[23]/td[2]').click()
        time.sleep(2)
        name = driver.find_element_by_id('MeetingsData_S_NAME').send_keys('for LOGIN_2')
        unit = driver.find_element_by_xpath('//div[5]/div/div/div/input').click()
        unit = driver.find_element_by_xpath('//div[5]/div/div/div/input').send_keys('Афанасьев')
        time.sleep(1)
        unit = driver.find_element_by_xpath('//div[5]/div/div/div/input').send_keys(Keys.ARROW_DOWN+Keys.ENTER)
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').clear()
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').send_keys('23:00' + Keys.ENTER)
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').clear()
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').send_keys('23:30' + Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_name('yt0').click()
        print(' Создаем совещание с рабочего стола')
        try:
            delMess = driver.find_element_by_css_selector('div.toast-message')
            print(delMess.text)
        except:
            print('NO POPUP MSG')

    def test010_GotoSync(self):
        time.sleep(2)
        driver.set_page_load_timeout(20)
        driver.get("https://owa.mos.ru/")
        wait.until(EC.presence_of_element_located((By.ID, "username")))
        elem = driver.find_element_by_id("username")
        elem.send_keys("MarenovaTE")
        elem = driver.find_element_by_id("password")
        elem.send_keys("rTZmYVbx"+Keys.RETURN)
        print(' Переходим в Outlook')
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, './/*[text()="Календарь"]/..')))
        driver.find_element(By.XPATH, ".//*[text()='Календарь']/..").click()
        try:
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[12]/div/div/div/div/div/div/div[3]/button')))
            driver.find_element_by_xpath('//div[12]/div/div/div/div/div/div/div[3]/button')
            driver.find_element_by_xpath('//div[4]/div/button').click()
            print(' Всплывающее окно появлилось и было закрыто')
        except:
            print(' Всплывающее уведомление не поялвилось')
        try:
            time.sleep(1)
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='for LOGIN Участ.: Афанасьев В.П.']/..")))
            driver.find_element_by_xpath(".//*[text()='for LOGIN Участ.: Афанасьев В.П.']/..").click()
            print(' Совещание созданное в ЭОР - Расписание найдено')
        except:
            self.fail(print(' аутглюк завис'))
        try:
            time.sleep(1)
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='УДАЛИТЬ']/..")))
            driver.find_element_by_xpath(".//*[text()='УДАЛИТЬ']/..").click()
            print(' Удаляем совещание')
        except:
            self.fail(print(' аутглюк завис'))
        try:
            time.sleep(1)
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='Удалить']/..")))
            driver.find_element_by_xpath(".//*[text()='Удалить']/..").click()
            print(' Совещание успешно удалено')
        except:
            self.fail(print("\n\n\n ОШИБКА! ВОЗНИКЛИ ПРОБЛЕМЫ ПРИ УДАЛЕНИИ СОВЕЩАНИЯ \n\n\n"))
        time.sleep(3)
        try:
            time.sleep(1)
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='for LOGIN_2 Участ.: Афанасьев В.П.']/..")))
            driver.find_element_by_xpath(".//*[text()='for LOGIN_2 Участ.: Афанасьев В.П.']/..").click()
            print(' Совещание созданное в ЭОР - Расписание найдено')
        except:
            self.fail(print(' аутглюк завис'))
        try:
            time.sleep(1)
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='УДАЛИТЬ']/..")))
            driver.find_element_by_xpath(".//*[text()='УДАЛИТЬ']/..").click()
            print(' Удаляем совещание')
        except:
            self.fail(print(' аутглюк завис'))
        try:
            time.sleep(1)
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='Удалить']/..")))
            driver.find_element_by_xpath(".//*[text()='Удалить']/..").click()
            print(' Совещание успешно удалено')
        except:
            self.fail(print("\n\n\n ОШИБКА! ВОЗНИКЛИ ПРОБЛЕМЫ ПРИ УДАЛЕНИИ СОВЕЩАНИЯ \n\n\n"))

    def test011_GotoEOR(self):
        time.sleep(4)
        print(" Запускаем синхронизацию")
        driver.get("https://dev.eor.gosapi.ru/new/ewsup")
        time.sleep(4)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'btn-ewsup')))
        driver.find_element_by_id('btn-ewsup').click()
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'COMPLETE')]")))
            print(' Синхронизация прошла успешно ')
        except:
            self.fail(print(' \n \n ОШИБКА СИНХРОНИЗАЦИИ \n \n'))
        driver.get('https://dev.eor.gosapi.ru/new/schedule')
        try:
            time.sleep(3)
            #wait.until(EC.presence_of_element_located((By.XPATH, "//span[. = '23:00 - 23:30' ]")))
            driver.find_element_by_xpath("//span[. = '23:00 - 23:30' ]")
            self.fail(' Мероприятие не удалено у пользователя ipad')
        except:
            print(' Мероприятие удалено корректно')
        print(' Переход в раздел "Расписание"')

    def test012_GotoEORforAnotherUser(self):        # ex 45
        time.sleep(1)
        ASeleniumLogin_1.test004_Relog(self)
        time.sleep(2)
        driver.get('https://dev.eor.gosapi.ru/new/schedule')
        time.sleep(2)
        try:
            driver.find_element_by_xpath("//span[. = '23:00 - 23:30' ]")
            self.fail(' Мероприятие не удалено у пользователя login')
        except:
            print(' Мероприятие удалено корректно')

    def test013_CreateMeetInEORAndCheckEmail(self):
        time.sleep(2)
        print(' Проверка почтовых уведомлений для созданных в ЭОР совещаний')
        crMeeting = driver.find_element_by_xpath("//div[@id='bs-example-navbar-collapse-3']/div[5]/div[2]").click()
        print(' Нажимаем кнопку "Создать" на открывшейся форме')
        time.sleep(3)
        name = driver.find_element_by_id('MeetingsData_S_NAME').send_keys('Проверка почтовых уведомлений')
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').clear()
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').send_keys('22:01' + Keys.ENTER)
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').clear()
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').send_keys('22:31' + Keys.ENTER)
        driver.find_element_by_xpath('//div[5]/div/div/div/input').send_keys('ipad')
        time.sleep(2)
        driver.find_element_by_xpath('//div[5]/div/div/div/input').send_keys(Keys.ENTER)
        time.sleep(1)
        print(' Заполняем форму создания совещания')
        time.sleep(1)
        driver.find_element_by_name('yt0').click()
        try:
            popUp = driver.find_element_by_css_selector('div.toast-message')
            print(' Всплывающее уведомлние: "', popUp.text, '" - выведено')
        except:
            print("I DON'T SEE POPUP")

    def test014_GotoOut(self):
        driver.get("https://owa.mos.ru/")
        driver.set_page_load_timeout(25)
        print(' Переходим в Outlook')
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, './/*[text()="Календарь"]/..')))
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Проверка почтовых уведомлений')]")))
            print(' Уведомление по почте о создании совещания пришло, всё правильно')
        except:
            print(' \n\n\n ОШИБКА! НЕТ УВЕДОМЛЕНИЯ НА ПОЧТУ \n (НЕ ПРИШЛО В ТЕЧЕНИИ 2х МИНУТ) \n\n\n')

    def test015_DelMeet(self):
        time.sleep(3)
        driver.get('https://dev.eor.gosapi.ru/new/schedule')
        time.sleep(5)
        driver.find_element_by_xpath("//span[. = '22:01 - 22:31' ]").click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='Удалить']/..")))
        time.sleep(1)
        driver.find_element(By.XPATH, ".//*[text()='Удалить']/..").click()
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[3]/div/button")))
        driver.find_element(By.XPATH, "//div[3]/div/button").click()
        time.sleep(1)
        print(' Находим совещание созданное для проверки почтовых уведомлений\n и удаляем его')

        driver.close()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))
    buf = open("at_for_SYNCHRON_EOR_and_OUTLOOK_part2.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
    stream=buf,
    title='ПРОВЕРКА СИНХРОНИЗАЦИИ СОВЕЩАНИЙ СОЗДАННЫХ В OUTLOOK И ЭОР (часть 2)',
    description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)