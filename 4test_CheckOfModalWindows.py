# ПРОВЕРКА НАЛИЧИЯ МОДАЛЬНЫХ ОКОН
import time
import unittest
import HTMLTestRunner
import sys
import datetime

global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

oracle = 'https://task.eor.gosapi.ru/oracle/site/login'
pgs = 'https://task.eor.gosapi.ru/pgs/site/login'
dev = 'https://dev.eor.gosapi.ru/new/site/login'

driver = webdriver.Chrome()
driver.get(dev)
driver.maximize_window()
wait = WebDriverWait(driver, 40)
test_time = datetime.datetime.now()
test_day = test_time.day
test_month = test_time.month

class ASeleniumLogin_1(unittest.TestCase):
    def test_001_LoginInEORDev(self):
        assert "Login" in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
        print('\n 1. Логинимся в систему\n')
        # yes
    def test_002_Not500or404andLoginIsVisible(self):
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        print(' 2. Логин пользователя отображается\n')
        # yes
    def test_003_CreateCPfromDT(self):
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='cps_panel']/div/div/ul/div/a/i")))
        driver.find_element_by_xpath("//div[@id='cps_panel']/div/div/ul/div/a/i").click()
        print(' 3. Создаём контрольтную точку с рабочего стола\n')
        # yes
    def test_004_FillingCPForm(self):
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "i.fa.fa-angle-down")))
        driver.find_element_by_css_selector("i.fa.fa-angle-down").click()
        driver.find_element_by_css_selector("input.form-control").send_keys("Selenium")
        driver.find_element_by_css_selector('span.find-text').click()
        driver.find_element_by_id('Checkpoint_TITLE').send_keys("Selenium _1")
        # ответственный
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//div[5]/div/span/span/span/span[2]").click()
        driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('Selenium' + Keys.ENTER)
        driver.implicitly_wait(10)
        # new responsible name
        driver.find_element_by_xpath('//div[6]/div/span/span/span/span[2]').click()
        driver.find_element_by_xpath('//span/input').send_keys('Selenium_1' + Keys.ENTER)
        # сроки
        driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('123' + Keys.ENTER)
        driver.find_element_by_xpath("//div/div[3]/span[2]").click()
        print(' 4. Заполняем форму контрольной точки и сохраняем её\n')
        # yes
    def test_005_OpenWindowTwo(self):
        time.sleep(2)
        driver.execute_script("window.open('https://dev.eor.gosapi.ru/new/','_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        print(' 5. Открываем новую вкладку\n')
        # yes
    def test_006_SearchCPinNewTab(self):
        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='cps_panel']/div/div/ul/li[2]/a/span[2]/span").click()
        time.sleep(1)
        driver.implicitly_wait(15)
        driver.find_element(By.XPATH, "// a[contains(text(), 'Selenium _1')]").click()
        print('Клик по ссылке ')
        # yes
    def test_007_DeleteThisCP(self):
        wait.until(EC.element_to_be_clickable((By.NAME, 'yt2')))
        driver.find_element_by_name('yt2').click()
        driver.find_element_by_xpath('//div[3]/div/button').click()
        print(' 7. Удаляем КТ\n')
        time.sleep(4)  #10
        # yes
    def test_008_GoToPreviousTab(self):
        time.sleep(1)
        #driver.switch_to.window(driver.window_handles[-1])
        print(' 8. Закрываем вкладку\n')
        driver.close()
        time.sleep(2)
        #yes
    def test_009_TryToEditCP(self):
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.NAME, 'yt0')))
        driver.find_element_by_name('yt0').click()
        print(' 9. В паспорте КТ на вкладке 1 нажимаем кнопку "Редактровать"\n')
        time.sleep(4)   #10
        # yes
    def test_010_CatchWindow(self):
        try:
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[3]/div/button')))
            driver.find_element_by_xpath('//div[3]/div/button').click()
            print(' 10. Модальное окно "Контрольная точкаSelenium _2 была удалена.", появилось и было закрыто \n')
        except:
            self.fail(print(' 10. Модальное окно "Контрольная точкаSelenium _2 была удалена.", не появилось \n'))
        # yes
    def test_011_BlockOperation(self):
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        driver.find_element_by_css_selector("i.entypo-menu").click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Все проекты')))
        driver.find_element_by_link_text("Все проекты").click()
        print(' 11. Переходим в раздел "Все проекты"\n')
        # yes
    def test_012_BlockCreate(self):
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID,'create-cp')))
        driver.find_element_by_id("create-cp").click()
        wait.until(EC.element_to_be_clickable((By.ID, 'Checkpoint_TITLE')))
        driver.find_element_by_id("Checkpoint_TITLE").send_keys('Selenium +1')
        driver.find_element_by_name("yt0").click()
        print(' 12. Создаём Блок\n')
        # yes
    def test_013_SearchThisBlock(self):
        time.sleep(5)
        driver.find_element_by_id('search-show').click()
        driver.find_element_by_id('search-text').send_keys('Selenium +1'+Keys.ENTER)
        print(' 13. Ищем только что созданный блок через поиск\n')
        # yes
    def test_014_OpenNewTabAndSearchBlock(self):
        time.sleep(4)
        driver.execute_script("window.open('https://dev.eor.gosapi.ru/new/','_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Все проекты")))
        driver.find_element_by_link_text("Все проекты").click()
        tex = driver.find_element_by_link_text("Все проекты").text
        print(tex)
        print(' 14. Открываем новую вкладку и ищем созданный блок\n')
        # yes
    def test_015_DeleteBlockAndCloseTab(self):
        wait.until(EC.element_to_be_clickable((By.ID, 'search-show')))
        driver.find_element_by_id('search-show').click()
        driver.find_element_by_id('search-text').send_keys('Selenium +1'+Keys.ENTER)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//td[2]/button[2]')))
        driver.find_element_by_xpath('//td[2]/button[2]').click()
        driver.find_element_by_xpath('//div[3]/div/button').click()
        print(' 15. Удаляем Блок\n')
        # yes

    def test_016_TryEditBlock(self):
        time.sleep(3)
        driver.close()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])
        wait.until(EC.element_to_be_clickable((By.XPATH, '//td[2]/button[2]')))
        driver.find_element_by_xpath('//td[2]/button').click()
        time.sleep(1)
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, '//div[3]/div/button')))
            driver.find_element_by_xpath('//div[3]/div/button').click()
            print(' 16. Модальное окно "Блок Selenium +1 была удалена.", появилось и было закрыто \n')
        except:
            self.fail(print(' 16. Модальное окно "Блок Selenium +1 была удалена.", не появилось \n'))
        # yes
    def test_017_ProjectOperationS(self):
        time.sleep(1)
        driver.find_element_by_id('search-text').clear()
        time.sleep(1)   #2
        driver.find_element_by_id('search-text').send_keys('Создал Selenium _для редактирования'+Keys.ENTER)
        time.sleep(2)   #4
        driver.find_element_by_xpath("//a[contains(text(),'Создал Selenium _для редактирования')]").click()
        time.sleep(2)   #5
        wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        driver.find_element_by_id("create-cp").click()
        driver.find_element_by_class_name('warn-cp')    #есть текст "Вы собираетесь создать проект."
        wait.until(EC.element_to_be_clickable((By.ID, 'Checkpoint_TITLE')))
        driver.find_element_by_id('Checkpoint_TITLE').send_keys('Selenium +3')
        autorDown = driver.find_element_by_xpath("//div[@id='DIV_ID_RESPONSIBLE']/div/span/span/span/span").click()
        autorName = driver.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys("багреева" + Keys.ENTER)
        pjctMansger = driver.find_element_by_xpath("//div[@id='DIV_PROJECT_CURATOR']/div/span/span/span/span[2]").click()
        pjctMansgerName = driver.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys("DIT" + Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_name("yt0").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        driver.find_element_by_name("yt0").click()
        print(' 17. Создаём новый проект\n')
        # yes
    def test_018_OpenNewTab(self):
        time.sleep(2)
        driver.execute_script("window.open('https://dev.eor.gosapi.ru/new/','_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        driver.find_element_by_link_text("Все проекты").click()
        wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        time.sleep(2)
        driver.find_element_by_id('search-show').click()
        driver.find_element_by_id('search-text').send_keys('Selenium +3'+Keys.ENTER)
        time.sleep(2)   #4
        driver.find_element_by_css_selector('a.cps-link').click()
        time.sleep(1)
        driver.find_element_by_xpath('//div[2]/table/tbody/tr/td[2]/button[2]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//div[3]/div/button').click()
        time.sleep(1)
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])
        print(' 18. Открываем новую вкладку, находим проект, и удаляаем его. Закрываем вкладку\n')

    def test_019_TryEditToProject(self):
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.NAME, 'yt0')))
        driver.find_element_by_name('yt0').click()
        print(' 19. Во вкладке 1 нажимаем кнопку "Редактировать"\n')

    def test_020_CatchWindow(self):
        time.sleep(1)
        try:
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[3]/div/button')))
            driver.find_element_by_xpath('//div[3]/div/button').click()
            print(' 20. Модальное окно "Проект Selenium +3 был удалена.", появилось и было закрыто \n')
        except:
            self.fail(print(' 20. Модальное окно "Проект Selenium +3 был удалена.", не появилось \n'))

    def test_021_CPOperation(self):
        time.sleep(1)
        driver.find_element_by_id('search-text').clear()
        time.sleep(2)
        driver.find_element_by_id('search-text').send_keys('Selenium'+Keys.ENTER)  # click()
        time.sleep(2)   #2
        print(' 21. В поиске задаём слово Selenium\n')

    def test_022_FindBlock(self):
        # находим блок
        driver.find_element_by_link_text('Создал Selenium _для редактирования').click()
        time.sleep(3)
        print(' 23. Находим блок\n')

    def test_023_FindProject(self):
        # находим проект
        driver.find_element_by_xpath('//div[2]/div[2]/table/tbody/tr/td[1]/h4/strong/a/span').click()
        time.sleep(3)
        print(' 23. Переходим от блока к проекту\n')

    def test_024_CreateCP(self):
        # создаем контрольную точку
        driver.find_element_by_id('create-cp').click()
        time.sleep(3)
        print(' 24. Переходим в раздел контрльных точек и нажимаем Создать\n')

    def test_025_FillingCPForm(self):
        wait.until(EC.element_to_be_clickable((By.ID, 'Checkpoint_TITLE')))
        driver.find_element_by_id('Checkpoint_TITLE').send_keys("Selenium +4")
        driver.find_element_by_xpath("//div[@id='DIV_ID_RESPONSIBLE']/div/span/span/span/span[2]").click()
        driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('ipad' + Keys.ENTER)
        driver.implicitly_wait(10)
        driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('123' + Keys.ENTER)
        print(' 25. Заполняем форму контрольной точки\n')

    def test_026_ConfirmCreation(self):
        time.sleep(1)
        driver.find_element_by_name('yt0').send_keys(Keys.PAGE_DOWN)
        driver.find_element_by_name('yt0').click()
        print(' 26. Сохраняем контрольную точку \n')

    def test_027_OpenNewTab(self):
        time.sleep(2)
        driver.execute_script("window.open('https://dev.eor.gosapi.ru/new/','_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        driver.find_element_by_link_text("Все проекты").click()
        print(' 27. Открываем новую вкладку и переходим во "Все проекты"\n')

    def test_028_SearchCPAndDelete(self):
        time.sleep(1)
        driver.find_element_by_id('search-show').click()
        driver.find_element_by_id('search-text').send_keys('Selenium +4'+Keys.ENTER)
        time.sleep(2)   #4
        driver.find_element_by_css_selector('a.cps-link').click()
        time.sleep(2)
        driver.find_element_by_link_text('Selenium').click()
        time.sleep(2)
        driver.find_element_by_xpath('//button[3]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//div[3]/div/button').click()
        time.sleep(2)
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])
        print(' 28. Находим контрольную точку и удаляем её\n')

    def test_029_TryToEditCP(self):
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.NAME, 'yt0')))
        driver.find_element_by_name('yt0').click()
        print(' 29. Во вкладке 1 нажимаем кнопку "Редактировать"\n')

    def test_030_CatchWindow(self):
        time.sleep(1)
        try:
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[3]/div/button')))
            driver.find_element_by_xpath('//div[3]/div/button').click()
            print(' 30. Модальное окно "Проект Selenium +4 был удалена.", появилось и было закрыто \n')
        except:
            self.fail(print(' 30. Модальное окно "Проект Selenium +4 был удалена.", не появилось \n'))

    def test_031_meetingTest(self):
        time.sleep(1)
        driver.find_element_by_link_text("Расписание").click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))
        print(' 31. Переход в раздел "Расписание"\n')

    def test_032_CreateNewMeeting(self):
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='bs-example-navbar-collapse-3']/div[5]/div[2]")))
        driver.find_element_by_xpath("//div[@id='bs-example-navbar-collapse-3']/div[5]/div[2]").click()
        wait.until(EC.element_to_be_clickable((By.ID, 'MeetingsData_S_NAME')))
        name = driver.find_element_by_id('MeetingsData_S_NAME').send_keys('Selenium +5')
        invite = driver.find_element_by_id('MeetingsData_S_INVITED').send_keys('Selenium +5')
        place = driver.find_element_by_id('MeetingsData_S_PLACE').send_keys('Москва')
        responsibleName = driver.find_element_by_xpath('//div[8]/div/span/span/span/span[2]').click()
        time.sleep(2)
        responsibleName = driver.find_element_by_xpath('//body[@id="ui-id-1"]/span/span/span/input').send_keys('Багреева' + Keys.ENTER)
        comment = driver.find_element_by_id('MeetingsData_S_COMMENT').send_keys('комментарий к совещанию')
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').clear()
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').send_keys('19:07' + Keys.ENTER)
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').clear()
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').send_keys('20:07' + Keys.ENTER)
        driver.find_element_by_name('yt0').click()
        print(' 32. Заполняем форму создания совещания\n')

    def test_033_OpenNewTab(self):
        time.sleep(2)
        driver.execute_script("window.open('https://dev.eor.gosapi.ru/new/','_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        driver.find_element_by_link_text("Расписание").click()
        print(' 33. Открываем новую вкладку и переходим в "Расписание"\n')

    def test_034_SearchMeetingAndDelete(self):
        time.sleep(4)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//span[. = '19:07 - 20:07' ]").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[4]")))
        driver.find_element_by_xpath('//button[4]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//div[3]/div/button').click()
        time.sleep(2)
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])
        print(' 34. Находим созданное совещание и уалеяем его\n')

    def test_035_TryToEditCP(self):
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[. = '19:07 - 20:07' ]")))
        driver.find_element_by_xpath("//span[. = '19:07 - 20:07' ]").click()
        print(' 35. Во вкладке 1 нажимаем кнопку "Редактировать"\n')

    def test_036_CatchWindow(self):
        time.sleep(1)
        try:
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[3]/div/button')))
            driver.find_element_by_xpath('//div[3]/div/button').click()
            print(' 36. Модальное окно "Совещание Selenium +5 было удалено.", появилось и было закрыто \n')
        except:
            self.fail(print(' 36. Модальное окно "Совещание Selenium +5 было удалено.", не появилось \n'))

    def test_037_Question(self):
        time.sleep(1)
        driver.find_element_by_link_text("Вопросы/Приоритеты").click()
        print(' 37. Переходим в раздел "Вопросы/Приоритеты"\n')

    def test_038_CreateNewQuestion(self):
        wait.until(EC.element_to_be_clickable((By.ID, 'btn_create_user')))
        driver.find_element_by_id('btn_create_user').click()
        wait.until(EC.element_to_be_clickable((By.NAME, 'yt0')))
        driver.find_element_by_id('Question_S_DESCRIPTION').send_keys('Selenium +6')
        driver.find_element_by_css_selector("span.select2-selection__arrow").click()
        driver.find_element_by_xpath('//span/input').send_keys('ipad' + Keys.ENTER)
        driver.find_element_by_name('yt0').click()
        print(' 38. Создаём новый вопрос\n')
        time.sleep(2)

    def test_039_OpenNewTab(self):
        driver.execute_script("window.open('https://dev.eor.gosapi.ru/new/','_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        driver.find_element_by_link_text("Вопросы/Приоритеты").click()
        print(' 39. Открываем новую вкладку и переходим в раздел "Вопросы/Приоритеты"\n')

    def test_040_FindQAndDelete(self):
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, 'btn_create_user')))
        driver.find_element_by_link_text('Selenium +6').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'btn_remove')))
        driver.find_element_by_id('btn_remove').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'ui-id-2')))
        driver.find_element_by_xpath('//div[3]/div/button').click()
        time.sleep(2)
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])
        print(' 40. Находим созданный вопрос и удаляем его\n')

    def test_041_TryToEditQ(self):
        time.sleep(2)
        driver.find_element_by_link_text('Selenium +6').click()
        print(' 41. В первой вкладке пытаемся открыть паспорт вопроса\n')

    def test_042_CatchWindow(self):
        time.sleep(1)
        try:
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[3]/div/button')))
            driver.find_element_by_xpath('//div[3]/div/button').click()
            print(' 42. Модальное окно "Вопрос Selenium +6 был удалено.", появилось и было закрыто \n')
        except:
            self.fail(print(' 42. Модальное окно "Вопрос Selenium +6 был удалено.", не появилось \n'))

    def test_043_NPA(self):
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Нормативно-правовые акты')))
        driver.find_element_by_link_text('Нормативно-правовые акты').click()
        print(' 43. Переходим в раздел "Нормативно-правовые акты"\n')

    def test_044_CreateNPA(self):
        wait.until(EC.element_to_be_clickable((By.ID, 'btn_create_user')))
        driver.find_element_by_id('btn_create_user').click()
        print(' 44. Нажимаем кнопку создать в раздете НПА\n')

    def test_045_FillingNPAForm(self):
        # сокращение списка, выбираем правовые акты ДЭПР
        wait.until(EC.element_to_be_clickable((By.ID, 'npa_type_selectSelectBoxItArrowContainer')))
        driver.find_element_by_id('npa_type_selectSelectBoxItArrowContainer').click()
        time.sleep(1)
        driver.find_element_by_link_text('Правовые акты ДЭПР').click()
        time.sleep(1)
        driver.find_element_by_id('Checkpoint_TITLE').send_keys('Selenium +7')
        driver.find_element_by_css_selector('span.select2-selection__arrow').click()
        #
        driver.find_element_by_css_selector('input.select2-search__field').send_keys('ipad' + Keys.ENTER)
        #
        driver.find_element_by_id('date_106_74').send_keys('1234' + Keys.ENTER)
        driver.find_element_by_id('date_106_76').send_keys('1234' + Keys.ENTER)
        driver.find_element_by_id('date_106_83').send_keys('1234' + Keys.ENTER)
        driver.find_element_by_css_selector('span.input-group-addon').click()
        time.sleep(1)
        driver.find_element_by_xpath('//div/div/div[2]/div/div/div[2]/div/div/input').send_keys('Selenium')
        time.sleep(1)
        driver.find_element_by_css_selector('div.title-item > span.find-text').click()
        driver.find_element_by_name('yt0').click()
        time.sleep(2)
        print(' 45. заполняем форму НПА\n')

    def test_046_OpenNewTab(self):
        driver.execute_script("window.open('https://dev.eor.gosapi.ru/new/','_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        driver.find_element_by_link_text("Нормативно-правовые акты").click()
        print(' 46. Открываем новую вкладку и переходим в раздел "Нормативно-правовые акты"\n')

    def test_047_SearchNPAAndDelete(self):
        #driver.find_element_by_css_selector('span.title_executor').click()
        #driver.find_element_by_id('btn_executor').click()
        #driver.find_element_by_id('btn_success_executor').click()

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'h4')))
        driver.find_element_by_css_selector('h4').click()
        wait.until(EC.element_to_be_clickable((By.NAME, 'yt1')))
        driver.find_element_by_name('yt1').click()
        time.sleep(2)
        driver.find_element_by_xpath('//div[3]/div/button').click()
        time.sleep(2)
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])
        print(' 47. Находим созданный вопрос и удаляем его\n')

    def test_048_TryToEditNPA(self):
        time.sleep(2)
        driver.find_element_by_name('yt0').click()
        print(' 48. В первой вкладке пытаемся открыть паспорт вопроса\n')

    def test_049_CatchWindow(self):
        time.sleep(1)
        try:
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[3]/div/button')))
            driver.find_element_by_xpath('//div[3]/div/button').click()
            print(' 49. Модальное окно "НПА Selenium +7 был удален.", появилось и было закрыто \n')
        except:
            self.fail(print(' 49. Модальное окно "НПА Selenium +7 был удален.", не появилось \n'))

    def test_050_CloseBrowser(self):
        print(' 50. Закрываем браузер \n')
        driver.close()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))
    # File
    buf = open("at_for_CHECK_MODAL_WINDOWS.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='ПРОВЕРКА НАЛИЧИЯ МОДАЛЬНЫХ МОДАЛЬНЫХ ОКОН',
        description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)