# ПРОВЕРКА НАЛИЧИЯ МОДАЛЬНЫХ ОКОН
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
        print('\n 1. Логинимся в систему\n')

    def test_002_Not500or404andLoginIsVisible(self):
        time.sleep(3)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        print(' 2. Логин пользователя отображается\n')

    def test_003_CreateCPfromDT(self):
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='cps_panel']/div/div/ul/div/a/i")))
        driver.find_element_by_xpath("//div[@id='cps_panel']/div/div/ul/div/a/i").click()
        print(' 3. Создаём контрольтную точку с рабочего стола\n')

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
        nameCP = driver.find_element_by_id('Checkpoint_TITLE').send_keys("Selenium _2")
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
        print(' 4. Заполняем форму контрольной точки и сохраняем её\n')

    ### open new tab
    def test_005_OpenWindowTwo(self):
        wait.until(EC.element_to_be_clickable((By.NAME, "yt0")))
        body = driver.find_element_by_tag_name('body')
        body.send_keys(Keys.CONTROL + 't')
        driver.get('https://dev.eor.gosapi.ru/')
        print(' 5. Открываем новую вкладку\n')

    def test_006_SearchCPinNewTab(self):
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        driver.find_element_by_xpath("//div[@id='cps_panel']/div/div/ul/li[2]/a/span[2]/span").click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Selenium _2")))
        driver.find_element_by_link_text('Selenium _2').click()
        print(' 6. на рабочем столе ищем созданную КТ\n')

    def test_007_DeleteThisCP(self):
        wait.until(EC.element_to_be_clickable((By.NAME, 'yt2')))
        driver.find_element_by_name('yt2').click()
        time.sleep(2)
        driver.find_element_by_xpath('//div[3]/div/button').click()
        print(' 7. Удаляем КТ\n')

    def test_008_GoToPreviousTab(self):
        body = driver.find_element_by_tag_name('body')
        body.send_keys(Keys.CONTROL+'w')#(Keys.CONTROL+Keys.PAGE_UP)
        print(' 8. Закрываем вкладку\n')

    def test_009_TryToEditCP(self):
        time.sleep(3)
        body = driver.find_element_by_tag_name('body')
        body.send_keys(Keys.TAB)
        wait.until(EC.element_to_be_clickable((By.NAME, 'yt0')))
        driver.find_element_by_name('yt0').click()
        print(' 9. В паспорте КТ на вкладке 1 нажимаем кнопку "Редактровать"\n')

    def test_010_CatchWindow(self):
        time.sleep(1)
        try:
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[3]/div/button')))
            driver.find_element_by_xpath('//div[3]/div/button').click()
            print('\n Модальное окно "Контрольная точкаSelenium _2 была удалена.", появилось и было закрыто \n')
        except:
            print('\n Модальное окно "Контрольная точкаSelenium _2 была удалена.", не появилось \n')

    def test_011_BlockOperation(self):
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        driver.find_element_by_css_selector("i.entypo-menu").click()
        driver.find_element_by_link_text("Все проекты").click()
        print(' 11. Переходим в раздел "Все проекты"\n')

    def test_012_BlockCreate(self):
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID,'create-cp')))
        driver.find_element_by_id("create-cp").click()
        wait.until(EC.element_to_be_clickable((By.ID, 'Checkpoint_TITLE')))
        driver.find_element_by_id("Checkpoint_TITLE").send_keys('Selenium +1')
        driver.find_element_by_name("yt0").click()
        print(' 12. Создаём Блок\n')

    def test_013_SearchThisBlock(self):
        time.sleep(5)
        driver.find_element_by_id('search-show').click()
        driver.find_element_by_id('search-text').send_keys('Selenium +1'+Keys.ENTER)
        print(' 13. Ищем только что созданный блок через поиск\n')

    def test_014_OpenNewTabAndSearchBlock(self):
        time.sleep(2)
        body = driver.find_element_by_tag_name('body')
        body.send_keys(Keys.CONTROL + 't')
        driver.get('https://dev.eor.gosapi.ru/')
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        driver.find_element_by_link_text("Все проекты").click()
        wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        time.sleep(2)
        driver.find_element_by_id('search-show').click()
        driver.find_element_by_id('search-text').send_keys('Selenium +1'+Keys.ENTER)
        print(' 14. Открываем новую вкладку и ищем созданный блок\n')

    def test_015_DeleteBlockAndCloseTab(self):
        wait.until(EC.element_to_be_clickable((By.XPATH, '//td[2]/button[2]')))
        driver.find_element_by_xpath('//td[2]/button[2]').click()
        driver.find_element_by_xpath('//div[3]/div/button').click()
        body = driver.find_element_by_tag_name('body')
        body.send_keys(Keys.CONTROL+'w')
        print(' 15. Удаляем Блок\n')

    def test_016_TryEditBlock(self):
        time.sleep(1)
        driver.find_element_by_xpath('//td[2]/button').click()
        time.sleep(1)
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, '//div[3]/div/button')))
            driver.find_element_by_xpath('//div[3]/div/button').click()
            print('\n Модальное окно "Блок Selenium +1 была удалена.", появилось и было закрыто \n')
        except:
            print('\n Модальное окно "Блок Selenium +1 была удалена.", не появилось \n')

    def test_017_ProjectOperationS(self):
        time.sleep(1)
        driver.find_element_by_id('search-text').clear()
        time.sleep(2)
        driver.find_element_by_id('search-text').send_keys('Создал Selenium _для редактирования'+Keys.ENTER)
        time.sleep(4)
        driver.find_element_by_xpath("//a[contains(text(),'Создал Selenium _для редактирования')]").click()
        time.sleep(5)
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

    def test_018_OpenNewTab(self):
        time.sleep(2)
        body = driver.find_element_by_tag_name('body')
        body.send_keys(Keys.CONTROL + 't')
        driver.get('https://dev.eor.gosapi.ru/')
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        driver.find_element_by_link_text("Все проекты").click()
        wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        time.sleep(2)
        driver.find_element_by_id('search-show').click()
        driver.find_element_by_id('search-text').send_keys('Selenium +3'+Keys.ENTER)
        time.sleep(4)
        driver.find_element_by_css_selector('a.cps-link').click()
        time.sleep(1)
        driver.find_element_by_xpath('//div[2]/table/tbody/tr/td[2]/button[2]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//div[3]/div/button').click()
        time.sleep(1)
        body = driver.find_element_by_tag_name('body')
        body.send_keys(Keys.CONTROL+'w')
        print(' 18. Открываем новую вкладку, находим проект, и удаляаем его. Закрываем вкладку\n')

    def test_019_TryEditToProject(self):
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.NAME, 'yt0')))
        driver.find_element_by_name('yt0').click()
        print(' 19. Во вкладке 1 нажимаем кнопку "Редактировать"\n')

    def test_020_CatchWindow(self):
        time.sleep(1)
        try:
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[3]/div/button')))
            driver.find_element_by_xpath('//div[3]/div/button').click()
            print('\n Модальное окно "Проект Selenium +3 был удалена.", появилось и было закрыто \n')
        except:
            print('\n Модальное окно "Проект Selenium +3 был удалена.", не появилось \n')

    def test_021_CPOperation(self):
        time.sleep(1)
        driver.find_element_by_id('search-text').clear()
        time.sleep(2)
        driver.find_element_by_id('search-text').send_keys('Selenium'+Keys.ENTER)  # click()
        #elemSearch.send_keys('Selenium'+Keys.ENTER)
        time.sleep(5)
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
        driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('Ipad' + Keys.ENTER)
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
        body = driver.find_element_by_tag_name('body')
        body.send_keys(Keys.CONTROL + 't')
        driver.get('https://dev.eor.gosapi.ru/')
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        driver.find_element_by_link_text("Все проекты").click()
        print(' 27. Открываем новую вкладку и переходим во "Все проекты"\n')

    def test_028_SearchCPAndDelete(self):
        time.sleep(1)
        driver.find_element_by_id('search-show').click()
        driver.find_element_by_id('search-text').send_keys('Selenium +4'+Keys.ENTER)
        time.sleep(4)
        driver.find_element_by_css_selector('a.cps-link').click()
        time.sleep(1)
        driver.find_element_by_link_text('Selenium').click()
        time.sleep(1)
        driver.find_element_by_xpath('//button[3]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//div[3]/div/button').click()
        time.sleep(1)
        body = driver.find_element_by_tag_name('body')
        body.send_keys(Keys.CONTROL+'w')
        print(' 28. Находим контрольную точку и удаляем её\n')

    def test_029_TryToEditCP(self):
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.NAME, 'yt0')))
        driver.find_element_by_name('yt0').click()
        print(' 29. Во вкладке 1 нажимаем кнопку "Редактировать"\n')

    def test_030_CatchWindow(self):
        time.sleep(1)
        try:
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[3]/div/button')))
            driver.find_element_by_xpath('//div[3]/div/button').click()
            print('\n Модальное окно "Проект Selenium +3 был удалена.", появилось и было закрыто \n')
        except:
            print('\n Модальное окно "Проект Selenium +3 был удалена.", не появилось \n')


if __name__ == '__main__':
    unittest.main()
