import time, sys
import unittest, HTMLTestRunner

global str
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 120)

class ASeleniumLogin_1(unittest.TestCase):
    def test001_GotoOutlook(self):
        driver.get("https://owa.mos.ru/")
        driver.maximize_window()
        wait.until(EC.presence_of_element_located((By.ID, "username")))
        elem = driver.find_element_by_id("username")
        elem.send_keys("MarenovaTE")
        elem = driver.find_element_by_id("password")
        elem.send_keys("rTZmYVbx")
        elem.send_keys(Keys.RETURN)
        print(' Авторизуемся в Outlook')

    def test002_ViewCalendar(self):
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, './/*[text()="Календарь"]/..')))
        driver.find_element(By.XPATH, ".//*[text()='Календарь']/..").click()
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='Создать событие']/..")))
        driver.find_element(By.XPATH, ".//*[text()='Создать событие']/..").click()
        # Получатели
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[2]/div[2]/div[2]/div/div/input")))
        driver.find_element_by_xpath('//div[2]/div[2]/div[2]/div/div/input').send_keys('Selenium из Outlook. Отв.: ipad Ip.А., Уч. DIT Di.')
        time.sleep(2)
        driver.find_element_by_xpath('//li/div[2]/div/div/div/input').clear()
        driver.find_element_by_xpath('//li/div[2]/div/div/div/input').send_keys('21:41')
        time.sleep(2)
        driver.find_element(By.XPATH, ".//*[text()='СОХРАНИТЬ']/..").click()
        print(' Переходим в раздел календарь и создаём новое совещание')

    def test003_GotoSync(self):
        time.sleep(1)
        driver.get("https://dev.eor.gosapi.ru/ewsup")
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
        print(" Открываем страницу синхронизатора и синхронизируем Outlook - ЭОР")

    def test004_Sync(self):
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'btn-ewsup')))
        driver.find_element_by_id('btn-ewsup').click()
        #time.sleep(3)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'COMPLETE')]")))
            print(' Синхронизация прошла успешно ')
        except:
            self.fail(print(' \n \n ОШИБКА СИНХРОНИЗАЦИИ \n \n'))

    def test005_Meet(self):
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        driver.find_element_by_css_selector("i.entypo-menu").click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Расписание')))
        driver.find_element_by_link_text("Расписание").click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))
        print(' Переход в раздел "Расписание"')
        driver.implicitly_wait(10)
        try:
            driver.find_element_by_xpath("//span[. = '21:41 - 22:11' ]").click()
        except:
            self.fail(print('В РАСПИСАНИИ НЕТ МЕРОПРИЯТИЯ ИЗ OUTLOOK'))
        try:
            _ = driver.find_element_by_class_name('col-md-12').text == 'Selenium из Outlook. Отв.: ipad Ip.А., Уч. DIT Di.'
            print('Название совещания соответствует переданному из outlook')
        except:
            print('Название совещания не соответствует переданному из outlook')

    def test006_EditMeet(self):
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[2]')))
        driver.find_element_by_xpath('//button[2]').click()
        # MeetingsData_S_NAME
        wait.until(EC.element_to_be_clickable((By.ID, 'MeetingsData_S_NAME')))
        driver.find_element_by_id('MeetingsData_S_NAME').clear()
        time.sleep(1)
        driver.find_element_by_id('MeetingsData_S_NAME').send_keys('Selenium из Outlook (1)')
        #driver.find_element_by_css_selector('input.select2-search__field').send_keys('Web'+Keys.ENTER)
        driver.find_element_by_xpath('//div[8]/div/span/span/span/span').click()
        driver.find_element_by_xpath('//span/input').send_keys('Web'+Keys.ENTER)
        driver.find_element_by_name('yt0').click()
        print(" Изменяем название совещания в ЭОР")

    def test007_ISeePopup(self):
        try:
            popUp = driver.find_element_by_css_selector('div.toast-message')
            print('POPUP с тектом: "',popUp.text,'" отображен')
        except:
            print("I DON'T SEE POPUP")

    def test008_Sync(self):
        driver.get("https://dev.eor.gosapi.ru/ewsup")
        print(" Пререходим к синхронизатору")
        ASeleniumLogin_1.test004_Sync(self)

    def test009_GotoOutlook(self):
        driver.get("https://owa.mos.ru/")
        print(" Переходим в Outlook")

    def test010_CheckMeet(self):
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, './/*[text()="Календарь"]/..')))
        driver.find_element(By.XPATH, ".//*[text()='Календарь']/..").click()
        try:
            driver.find_element_by_xpath(".//*[text()='Selenium из Outlook (1) Отв.: Web w.w.']/..").click()
            print(' Совещание созданное в ЭОР найдено')
        except:
            print('аутглюк завис')
        try:
            time.sleep(2)
            driver.find_element_by_xpath(".//*[text()='ИЗМЕНИТЬ']/..").click()
            print(' Редактируем совещение')
        except:
            print(' аутглюк завис')

    def test011_editMeetInOutL(self):
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[2]/div[2]/div[2]/div/div/input')))
        driver.find_element_by_xpath('//div[2]/div[2]/div[2]/div/div/input').clear()
        driver.find_element_by_xpath('//div[2]/div[2]/div[2]/div/div/input').send_keys('Selenium из Outlook + участники')
        time.sleep(1)
        driver.find_element(By.XPATH, ".//*[text()='СОХРАНИТЬ']/..").click()
        time.sleep(1)
        print(" Изменив название сохраняем")

    def test012_gotoEOR(self):
        ASeleniumLogin_1.test008_Sync(self)

    def test013_gotoMeet(self):
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Расписание')))
        driver.find_element_by_link_text("Расписание").click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))
        print(' Переход в раздел "Расписание"')

    def test014_bricktest(self):
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='bs-example-navbar-collapse-3']/div[5]/div[2]")))
        crMeeting = driver.find_element_by_xpath("//div[@id='bs-example-navbar-collapse-3']/div[5]/div[2]").click()
        print(' Нажимаем кнопку "Создать" на открывшейся форме')
        wait.until(EC.element_to_be_clickable((By.ID, "MeetingsData_S_NAME")))
        name = driver.find_element_by_id('MeetingsData_S_NAME').send_keys('ЭОР to Outlook (Selenium)')
        #unit = driver.find_element_by_css_selector('ul.select2-selection__rendered').click()
        #unit = driver.find_element_by_xpath('//form/div[5]/div/span/span[1]/span/ul/li/input').send_keys('Соловьев Е' + Keys.ENTER)
        place = driver.find_element_by_id('MeetingsData_S_PLACE').send_keys('Москва')
        responsibleName = driver.find_element_by_xpath('//div[8]/div/span/span/span/span[2]').click()
        time.sleep(1)
        responsibleName = driver.find_element_by_xpath('//body[@id="ui-id-1"]/span/span/span/input').send_keys('Web' + Keys.ENTER)
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').clear()
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').send_keys('22:01' + Keys.ENTER)
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').clear()
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').send_keys('22:31' + Keys.ENTER)
        print(' Заполняем форму создания совещания')
        time.sleep(2)
        driver.find_element_by_name('yt0').click()
        try:
            popUp = driver.find_element_by_css_selector('div.toast-message')
            print(' Всплывающее уведомлние: "',popUp.text, '" - выведено')
        except:
            print("I DON'T SEE POPUP")

    def test015_bricktestGotoSync(self):
        print(" Пререходим к синхронизатору")
        #driver.get("https://dev.eor.gosapi.ru/ewsup")      # раскомментировать
        #ASeleniumLogin_1.test004_Sync(self)

    def test016_gotoOut(self):
        driver.get("https://owa.mos.ru/")
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, './/*[text()="Календарь"]/..')))
        driver.find_element(By.XPATH, ".//*[text()='Календарь']/..").click()
        print(" Переходим в Outlook, затем в раздел календарь")

    def test017_editMeet(self):
        time.sleep(1)
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='ЭОР to Outlook (Selenium) Отв.: Web w.w.']/..")))
        driver.find_element_by_xpath(".//*[text()='ЭОР to Outlook (Selenium) Отв.: Web w.w.']/..").click()
        try:
            time.sleep(1)
            driver.find_element_by_xpath(".//*[text()='ИЗМЕНИТЬ']/..").click()
            print(' Редактируем совещение, добавляем участников')
        except:
            print(' аутглюк завис')
        time.sleep(1)
        driver.find_element_by_xpath('//div[2]/div[2]/div[2]/div/div/input').send_keys(Keys.END + ' DIT')
        time.sleep(1)
        driver.find_element(By.XPATH, ".//*[text()='СОХРАНИТЬ']/..").click()
        time.sleep(1)

    def test018_GotoEOR(self):
        ASeleniumLogin_1.test008_Sync(self)
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Расписание')))
        driver.find_element_by_link_text("Расписание").click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))
        print(' Переход в раздел "Расписание"')

    def test019_brickIsVisible(self):
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[. = '21:41 - 22:11' ]")))
        try:
            driver.find_element_by_xpath('//div[2]/i')
            print(" 'Кирпич' отображен")
        except:
            print(" 'Кирпич' не отображен")

    def test020_DelAllObj(self):
        driver.find_element_by_xpath("//span[. = '21:41 - 22:11' ]").click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='Удалить']/..")))
        time.sleep(1)
        driver.find_element(By.XPATH, ".//*[text()='Удалить']/..").click()
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[3]/div/button")))
        driver.find_element(By.XPATH, "//div[3]/div/button").click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[. = '22:01 - 22:31' ]")))
        time.sleep(1)
        driver.find_element_by_xpath("//span[. = '22:01 - 22:31' ]").click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='Удалить']/..")))
        time.sleep(1)
        driver.find_element(By.XPATH, ".//*[text()='Удалить']/..").click()
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[3]/div/button")))
        driver.find_element(By.XPATH, "//div[3]/div/button").click()
        print(" Удаляем совещания созданные в ЭОР и Outlook")

    def test021_CheckYouSelf(self):
        time.sleep(5)
        try:
            driver.find_element_by_xpath("//span[. = '21:41 - 22:11' ]").click()
            self.fail(print(' что-то пошло не так, первое совещание не удалено, \nвозможно, программа сохранила дубликат из прошлой сессии'))
        except:
            print(' Первое совещание удалено')
        try:
            driver.find_element_by_xpath("//span[. = '22:01 - 22:31' ]").click()
            self.fail(print(' что-то пошло не так, второе совещание не удалено, \nвозможно, программа сохранила дубликат из прошлой сессии'))
        except:
            print(' Второе совещание удалено')

    def test022_CloseBrowser(self):
        print(' Проверка совещаний на весь день')

    def test023_GotoScheduler(self):
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))
        print(' Переход в раздел "Расписание"')

    def test024_ClickCreateMeeting(self):
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='bs-example-navbar-collapse-3']/div[5]/div[2]")))
        crMeeting = driver.find_element_by_xpath("//div[@id='bs-example-navbar-collapse-3']/div[5]/div[2]").click()
        print(' Нажимаем кнопку "Создать" на открывшейся форме')
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'MeetingsData_S_NAME')))
        name = driver.find_element_by_id('MeetingsData_S_NAME').send_keys('sync selenium')
        triggerAllDay = driver.find_element_by_css_selector('span.switch-right').click()
        time.sleep(1)
        driver.find_element_by_name('yt0').click()
        time.sleep(1)
        print(' Создаем совещание на весь день')

    def test025_GotoOutlook(self):
        time.sleep(3)
        driver.get("https://owa.mos.ru/")
        print(' Авторизуемся в Outlook')

    def test026_ViewCalendar(self):
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, './/*[text()="Календарь"]/..')))
        driver.find_element(By.XPATH, ".//*[text()='Календарь']/..").click()
        try:
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='sync selenium']/..")))
            driver.find_element_by_xpath(".//*[text()='sync selenium']/..").click()
            print(' Совещание созданное в ЭОР найдено')
        except:
            self.fail(print(' аутглюк завис'))
        try:
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='ИЗМЕНИТЬ']/..")))
            driver.find_element_by_xpath(".//*[text()='ИЗМЕНИТЬ']/..").click()
            print(' Открываем на просмотр совещание:')
        except:
            self.fail(print(' аутглюк завис'))
        try:
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='Весь день']/..")))
            driver.find_element(By.XPATH, ".//*[text()='Весь день']/..")
            print(" Совещение созданно на весь день")
        except:
            self.fail(print("\n\n\n ОШИБКА! СОВЕЩАНИЕ СОЗДАНО НЕ НА ВЕСЬ ДЕНЬ ИЛИ ПЕРЕДАЛОСЬ НЕ КОРРЕКТНО! \n\n\n"))

    def test027_GotoEOR(self):
        time.sleep(3)
        driver.get("https://dev.eor.gosapi.ru/ewsup")
        print(" Открываем страницу синхронизатора и синхронизируем Outlook - ЭОР")

    def test028_Sync(self):
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'btn-ewsup')))
        driver.find_element_by_id('btn-ewsup').click()
        time.sleep(1)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'COMPLETE')]")))
            print(' Синхронизация прошла успешно')
        except:
            self.fail(print(' \n \n ОШИБКА СИНХРОНИЗАЦИИ \n \n'))
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Расписание')))
        driver.find_element_by_link_text("Расписание").click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))
        print(' Переход в раздел "Расписание"')
        try:
            time.sleep(1)
            driver.find_element(By.XPATH, ".//*[text()='sync selenium']/..")
            print(" Совещение найдено")
        except:
            print("\n\n\n ОШИБКА! СОВЕЩАНИЕ СОЗДАНО НЕ НА ВЕСЬ ДЕНЬ ИЛИ ПЕРЕДАЛОСЬ НЕ КОРРЕКТНО! \n\n\n")

        driver.find_element(By.XPATH, ".//*[text()='sync selenium']/..").click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='Удалить']/..")))
        try:
            time.sleep(1)
            driver.find_element(By.XPATH, "//button[2]").click()
            print(" Открываем совещение на редактирование")
        except:
            self.fail(print("\n\n\n ОШИБКА! \n\n\n"))
        try:
            time.sleep(1)
            val = driver.find_element_by_css_selector('span.switch-left').text == 'Да'
            print(' Триггер "Целый день" установелн в положении -', val)
        except:
            val = driver.find_element_by_css_selector('span.switch-left').text == 'Да'
            self.fail(print(' Триггер "Целый день" установелн в положении -', val))

    def test029_GotoOutlook(self):
        driver.get("https://owa.mos.ru/")
        print(' Переходим в Outlook')
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, './/*[text()="Календарь"]/..')))
        driver.find_element(By.XPATH, ".//*[text()='Календарь']/..").click()
        try:
            time.sleep(1)
            driver.find_element_by_xpath(".//*[text()='sync selenium']/..").click()
            print(' Совещание созданное в ЭОР найдено')
        except:
            self.fail(print(' аутглюк завис'))
        try:
            time.sleep(1)
            driver.find_element_by_xpath(".//*[text()='УДАЛИТЬ']/..").click()
            print(' Удаляем совещание')
        except:
            self.fail(print(' аутглюк завис'))
        try:
            time.sleep(1)
            driver.find_element_by_xpath(".//*[text()='Удалить']/..").click()
            print(' Совещание успешно удалено')
        except:
            self.fail(print("\n\n\n ОШИБКА! ВОЗНИКЛИ ПРОБЛЕМЫ ПРИ УДАЛЕНИИ СОВЕЩАНИЯ \n\n\n"))
#
# разделить на 2 теста отсюда.
#
    def test030_DelMeetInOut(self):
        print(' Проверка корректности удаления совещания в outlook и передачи \n данных в ЭОР')
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, './/*[text()="Календарь"]/..')))
        driver.find_element(By.XPATH, ".//*[text()='Календарь']/..").click()
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='Создать событие']/..")))
        driver.find_element(By.XPATH, ".//*[text()='Создать событие']/..").click()
        # Получатели
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[2]/div[2]/div[2]/div/div/input')))
        driver.find_element_by_xpath('//div[2]/div[2]/div[2]/div/div/input').send_keys('Selenium from Outlook Delete')
        time.sleep(1)
        driver.find_element_by_xpath('//li/div[2]/div/div/div/input').clear()
        driver.find_element_by_xpath('//li/div[2]/div/div/div/input').send_keys('23:00')
        time.sleep(1)
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='СОХРАНИТЬ']/..")))
        driver.find_element(By.XPATH, ".//*[text()='СОХРАНИТЬ']/..").click()
        print(' Переходим в раздел календарь и создаём новое совещание')

    def test031_GotoSync(self):
        time.sleep(1)
        print(" Запускаем синхронизацию")
        driver.get("https://dev.eor.gosapi.ru/ewsup")
        time.sleep(4)
        ASeleniumLogin_1.test004_Sync(self)

    def test032_GotoSedul(self):
        time.sleep(2)
        ASeleniumLogin_1.test013_gotoMeet(self)

    def test033_ConfirmExistMeet(self):
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[. = '23:00 - 23:30' ]")))
        try:
            driver.find_element_by_xpath("//span[. = '23:00 - 23:30' ]")
            print(' Совещание передалось в ЭОР корректно')
        except:
            self.fail(print('ОШИБКА СОВЕЩАНИЕ НЕ ПЕРЕДАЛОСЬ\n ИЛИ НЕБЫЛО СОХРАНЕНО В OUTLOOK!'))

    def test034_GotoOut(self):
        time.sleep(1)
        ASeleniumLogin_1.test031_GotoSync(self)
        driver.get("https://owa.mos.ru/")
        print(' Переходим в Outlook')
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, './/*[text()="Календарь"]/..')))
        driver.find_element(By.XPATH, ".//*[text()='Календарь']/..").click()
        try:
            time.sleep(1)
            driver.find_element_by_xpath(".//*[text()='Selenium from Outlook Delete']/..").click()
            print(' Совещание созданное в ЭОР найдено')
        except:
            self.fail(print(' аутглюк завис'))
        try:
            time.sleep(1)
            driver.find_element_by_xpath(".//*[text()='УДАЛИТЬ']/..").click()
            print(' Удаляем совещание')
        except:
            self.fail(print(' аутглюк завис'))
        try:
            time.sleep(1)
            driver.find_element_by_xpath(".//*[text()='Удалить']/..").click()
            print(' Совещание успешно удалено')
        except:
            self.fail(print("\n\n\n ОШИБКА! ВОЗНИКЛИ ПРОБЛЕМЫ ПРИ УДАЛЕНИИ СОВЕЩАНИЯ \n\n\n"))

    def test035_GotoEOR(self):
        time.sleep(2)
        ASeleniumLogin_1.test031_GotoSync(self)
        time.sleep(2)
        ASeleniumLogin_1.test013_gotoMeet(self)
        try:
            driver.find_element_by_xpath(".//*[text()='Selenium from Outlook Delete']/..")
            self.fail(print(' Совещние не удалено'))
        except:
            print(' Совещание удалено корректно, проверка прошла успешно')

    def test036_DelMeetAnotherUser(self):
        print(' Создаём совещание пользователем 1 с участником 2, \nи удаляем совещание у ползователя 2')
        print(' Создаём новое совещение пользователем Ipad')
        crMeeting = driver.find_element_by_xpath("//div[@id='bs-example-navbar-collapse-3']/div[5]/div[2]").click()
        print(' Нажимаем кнопку "Создать" на открывшейся форме')
        time.sleep(3)
        name = driver.find_element_by_id('MeetingsData_S_NAME').send_keys('for LOGIN')
        unit = driver.find_element_by_xpath('//div[5]/div/div/div/input').click()
        unit = driver.find_element_by_xpath('//div[5]/div/div/div/input').send_keys('Афа')
        time.sleep(2)
        unit = driver.find_element_by_xpath('//div[5]/div/div/div/input').send_keys(Keys.ENTER)
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

    def test037_Relog(self):
        time.sleep(1)
        body = driver.find_element_by_tag_name('body')
        body.send_keys(Keys.CONTROL+'t')
        driver.get("https://dev.eor.gosapi.ru/")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.caret')))
        driver.find_element_by_css_selector('span.caret').click()
        driver.find_element_by_link_text('Выход').click()
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("login")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("login")
        elem.send_keys(Keys.RETURN)
        print(' Перезаходим в систему под пользователем login/login ')

    def test038_gotoSedul(self):
        time.sleep(3)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        time.sleep(2)
        schedul = driver.find_element_by_link_text("Расписание")
        schedul.click()
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))
        print(" Переходим в раздел расписания пользователя login")

    def test039_searchMeet(self):
        driver.find_element_by_xpath("//span[. = '23:00 - 23:30' ]").click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='Удалить']/..")))
        time.sleep(1)
        driver.find_element(By.XPATH, ".//*[text()='Удалить']/..").click()
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[3]/div/button")))
        driver.find_element(By.XPATH, "//div[3]/div/button").click()
        time.sleep(1)
        print(' В разделе расписания находим созданное пользоватлеме ipad совещание\n и удаляем его')

    def test040_loginIpad(self):
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.caret')))
        driver.find_element_by_css_selector('span.caret').click()
        driver.find_element_by_link_text('Выход').click()
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
        print(' Перезаходим в систему под пользователем ipad/ipad ')

    def test041_gotoMeet(self):
        time.sleep(3)
        ASeleniumLogin_1.test013_gotoMeet(self)
        time.sleep(2)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))
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

    def test042_CreateInEORDelInOutlook(self):
        print(' Создание совещаний из раздела расписания и рабочий\n стол для Вед. и Уч. и удаление их в Outlook')
        ASeleniumLogin_1.test036_DelMeetAnotherUser(self)
        print(' Переходим в рабочий стол')
        time.sleep(2)
        driver.find_element_by_link_text("Рабочий стол").click()
        driver.implicitly_wait(15)
        time.sleep(5)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//tr[23]/td[2]")))
        driver.find_element_by_xpath('//tr[23]/td[2]').click()
        time.sleep(2)
        name = driver.find_element_by_id('MeetingsData_S_NAME').send_keys('for LOGIN_2')
        unit = driver.find_element_by_xpath('//div[5]/div/div/div/input').click()
        unit = driver.find_element_by_xpath('//div[5]/div/div/div/input').send_keys('Афа')
        time.sleep(2)
        unit = driver.find_element_by_xpath('//div[5]/div/div/div/input').send_keys(Keys.ENTER)
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').clear()
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').send_keys('23:00' + Keys.ENTER)
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').clear()
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').send_keys('23:30' + Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_name('yt0').click()
        print(' Создаем совещание с рабочего стола')

    def test043_GotoSync(self):
        #ASeleniumLogin_1.test031_GotoSync(self)        # раскомментировать
        time.sleep(2)
        driver.get("https://owa.mos.ru/")
        print(' Переходим в Outlook')
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, './/*[text()="Календарь"]/..')))
        driver.find_element(By.XPATH, ".//*[text()='Календарь']/..").click()
        try:
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='for LOGIN Участ.: Афанасьев В.П., ']/..")))
            driver.find_element_by_xpath(".//*[text()='for LOGIN Участ.: Афанасьев В.П., ']/..").click()
            print(' Совещание созданное в ЭОР - Расписание найдено')
        except:
            self.fail(print(' аутглюк завис'))
        try:
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
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='for LOGIN_2 Участ.: Афанасьев В.П., ']/..")))
            driver.find_element_by_xpath(".//*[text()='for LOGIN_2 Участ.: Афанасьев В.П., ']/..").click()
            print(' Совещание созданное в ЭОР - Расписание найдено')
        except:
            self.fail(print(' аутглюк завис'))
        try:
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

    def test044_GotoEOR(self):
        ASeleniumLogin_1.test031_GotoSync(self)
        ASeleniumLogin_1.test013_gotoMeet(self)
        try:
            driver.find_element_by_xpath("//span[. = '23:00 - 23:30' ]")
            self.fail(' Мероприятие не удалено у пользователя ipad')
        except:
            print(' Мероприятие удалено корректно')

    def test045_GotoEORforAnotherUser(self):
        time.sleep(1)
        ASeleniumLogin_1.test037_Relog(self)
        time.sleep(2)
        ASeleniumLogin_1.test038_gotoSedul(self)
        time.sleep(2)
        try:
            driver.find_element_by_xpath("//span[. = '23:00 - 23:30' ]")
            self.fail(' Мероприятие не удалено у пользователя login')
        except:
            print(' Мероприятие удалено корректно')

    def test046_CreateMeetInEORAndCheckEmail(self):
        time.sleep(4)
        ASeleniumLogin_1.test040_loginIpad(self)
        print(' Проверка почтовых уведомлений для созданных в ЭОР совещаний')
        time.sleep(4)
        ASeleniumLogin_1.test013_gotoMeet(self)
        time.sleep(4)
        crMeeting = driver.find_element_by_xpath("//div[@id='bs-example-navbar-collapse-3']/div[5]/div[2]").click()
        print(' Нажимаем кнопку "Создать" на открывшейся форме')
        time.sleep(3)
        name = driver.find_element_by_id('MeetingsData_S_NAME').send_keys('Проверка почтовых уведомлений')
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').clear()
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').send_keys('22:01' + Keys.ENTER)
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').clear()
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').send_keys('22:31' + Keys.ENTER)
        print(' Заполняем форму создания совещания')
        time.sleep(1)
        driver.find_element_by_name('yt0').click()
        try:
            popUp = driver.find_element_by_css_selector('div.toast-message')
            print(' Всплывающее уведомлние: "', popUp.text, '" - выведено')
        except:
            print("I DON'T SEE POPUP")

    def test047_GotoSync(self):
        #ASeleniumLogin_1.test008_Sync(self)        # раскомментировать
        time.sleep(2)

    def test048_GotoOut(self):
        driver.get("https://owa.mos.ru/")
        print(' Переходим в Outlook')
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, './/*[text()="Календарь"]/..')))
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Проверка почтовых уведомлений')]")))
            print(' Уведомление по почте о создании совещания пришло, всё правильно')
        except:
            self.fail(print(' \n\n\n ОШИБКА! НЕТ УВЕДОМЛЕНИЯ НА ПОЧТУ \n (НЕ ПРИШЛО В ТЕЧЕНИИ 2х МИНУТ) \n\n\n'))

    def test049_DelMeet(self):
        time.sleep(3)
        driver.get('https://dev.eor.gosapi.ru/schedule')
        ASeleniumLogin_1.test013_gotoMeet(self)
        time.sleep(3)
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

    def test050_CloseBrowser(self):
        print(' Браузер закрыт')
        driver.close()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))
    buf = open("at_for_SYNCHRON_EOR_and_OUTLOOK.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
    stream=buf,
    title='ПРОВЕРКА СИНХРОНИЗАЦИИ СОВЕЩАНИЙ СОЗДАННЫХ В OUTLOOK И ЭОР',
    description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)