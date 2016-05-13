import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("http://dev.eor.gosapi.ru/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)


class ASeleniumLogin_1(unittest.TestCase):
    def test_1LoginInEORDev(self):
        assert "Login" in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
    def test_2Not500or404andLoginIsVisible(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))

class BSeleniumOpenAllPjct_2(unittest.TestCase):
    def test_1OpenAllPjct(self):
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(2)
        allpj = driver.find_element_by_link_text("Все проекты")
        allpj.click()

    def test_2Not500or404(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

class CSeleniumCreateNewCP(unittest.TestCase):
    def test_1OpenForm(self):
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        btn1 = driver.find_element_by_id("create-cp")
        btn1.click()
        time.sleep(1)
        assert "ЭОР" in driver.title
        elem = driver.find_element_by_link_text('Поиск')
        elem.click()
        elemSearch = driver.find_element_by_id('search-text')
        elemSearch.click()
        elemSearch.send_keys('Для контрольной точки')
        elemSearch.send_keys(Keys.ENTER)
        time.sleep(2)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_2FindBlock(self):
        #находим блок
        findBlock = driver.find_element_by_xpath('//div[2]/div[2]/div/table/tbody/tr/td[1]/h4/strong/a')
        findBlock.click()
        time.sleep(1)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_3FindProject(self):
        #находим проект
        findProject = driver.find_element_by_xpath('//div[2]/div[2]/table/tbody/tr/td[1]/h4/strong/a/span')
        findProject.click()
        time.sleep(1)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_4CreateCP(self):
        #создаем контрольную точку
        CreateCP = driver.find_element_by_xpath('html/body/div[1]/div[2]/div[4]/nav/div/div[2]/ul[7]/li/button')
        CreateCP.click()
        time.sleep(1)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

class DSeleniumTestCPForm(unittest.TestCase):
    def test_1FillingCPForm(self):
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        _ = driver.find_element_by_class_name('warn-cp').text == 'контрольную точку'  # test
        time.sleep(1)
        #имя контрольной точки
        nameCP = driver.find_element_by_xpath('//div[2]/div[2]/div[4]/form/div/div[2]/div[4]/div/textarea')
        nameCP.click()
        nameCP.send_keys("контрольная точка созданная Selenium")
        time.sleep(1)
        #автор
        autorName = driver.find_element_by_xpath('//form/div/div[2]/div[8]/div/span/span[1]/span/span[2]')
        autorName.click()
        autorNameText = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        autorNameText.send_keys('Багреева')
        #time.sleep(1)
        autorNameText.send_keys(Keys.ENTER)
        #time.sleep(1)
        #ответственный
        responsibleName = driver.find_element_by_xpath('//form/div/div[2]/div[9]/div/span/span[1]/span/span[2]')
        responsibleName.click()
        responsibleNameText = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleNameText.send_keys('DIT')
        time.sleep(1)
        responsibleNameText.send_keys(Keys.ENTER)
        time.sleep(1)
        #сроки
        terms = driver.find_element_by_xpath('//div[2]/div[2]/div[4]/form/div/div[2]/div[11]/div/input')
        terms.click()
        terms.send_keys("12345")
        terms.send_keys(Keys.ENTER)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    if __name__ == '__main__':
        unittest.main()

    def test_2TriggersCPTest(self):
        EditProject = driver.find_element_by_name('yt0')
        EditProject.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        #туда
        triggerKPI = driver.find_element_by_xpath('//div[2]/div[4]/form/div/div[2]/div[17]/div/div/div/label')
        triggerKPI.click()
        time.sleep(1)
        triggerPriority = driver.find_element_by_xpath('//div[2]/div[4]/form/div/div[2]/div[18]/div/div/div/label')
        triggerPriority.click()
        time.sleep(1)
        triggerDone = driver.find_element_by_xpath('//div[2]/div[4]/form/div/div[2]/div[19]/div/div[1]/div/label')
        triggerDone.click()
        time.sleep(1)
        #и обратно
        triggerKPI.click()
        time.sleep(1)
        triggerPriority.click()
        time.sleep(1)
        triggerDone.click()
        time.sleep(1)

        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_3ConfirmCPCreating(self):
        finishButton = driver.find_element_by_xpath('//div[2]/div[2]/div[4]/form/div/div[2]/div[23]/input[2]')
        finishButton.click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(3)

class ESeleniumEditCP(unittest.TestCase):
    def test_1ClickEditButton(self):
        editButton = driver.find_element_by_xpath('//div[2]/div[4]/div/div[2]/div/div[2]/div[11]/input[1]')
        editButton.click()
        time.sleep(2)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(3)

    def test_2editCP(self):
        _ = driver.find_element_by_class_name('warn-cp').text == 'контрольную точку'
        nameCP = driver.find_element_by_xpath('//form/div/div[2]/div[4]/div/textarea')
        nameCP.click()
        nameCP.send_keys(' редактировано ')
        EditProject = driver.find_element_by_name('yt0')
        EditProject.send_keys(Keys.PAGE_DOWN)
        saveButton = driver.find_element_by_xpath('//div[2]/div[2]/div[4]/div/div/form/div/div[2]/div[23]/input[2]')
        saveButton.click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_3AllRight(self):
        time.sleep(3)
        _ = driver.find_element_by_id('C_TITLE').text == ' редактировано '
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

class FSeleniumSeekAndDestroy(unittest.TestCase):
    def test_1FilterSetting(self):
        assert "ЭОР" in driver.title
        FilterSetting = driver.find_element_by_xpath('html/body/div[1]/div[2]/div[4]/nav/div/div[2]/ul[2]/li/a/span')
        FilterSetting.click()
        SnipClick = driver.find_element_by_xpath('//nav/div/div[2]/ul[2]/li/ul/li[3]/div/ul/li[1]/div/label[1]/div')
        SnipClick.click()
        ConfirmFilter = driver.find_element_by_xpath('//div[1]/div[2]/div[4]/nav/div/div[2]/ul[2]/li/ul/li[4]/button[2]')
        ConfirmFilter.click()
        time.sleep(3)

    def test_2TextFilterSetting(self):
        ClearText = driver.find_element_by_xpath('html/body/div[1]/div[2]/div[4]/nav/div/div[2]/ul[8]/li[1]/span')
        ClearText.click()
        FindNew = driver.find_element_by_xpath('html/body/div[1]/div[2]/div[4]/nav/div/div[2]/ul[8]/li[1]/input')
        FindNew.send_keys('контрольная точка созданная Selenium редактировано ')
        FindNew.send_keys(Keys.ENTER)
        time.sleep(2)

    def test_3BlockAndProjectListing(self):
        findBlock = driver.find_element_by_xpath('//div[2]/div[4]/div[2]/div[2]/div/table/tbody/tr/td[1]/h4/strong/a')
        findBlock.click()
        time.sleep(1)
        findProject = driver.find_element_by_xpath('//div[2]/div[4]/div[2]/div[2]/div[2]/table/tbody/tr/td[1]/h4/strong/a')
        findProject.click()
        time.sleep(2)

class GSeleniumCreateNPA(unittest.TestCase):
    def test_1NPAButtonClick(self):
        assert "ЭОР" in driver.title
        findCheckPoint = driver.find_element_by_css_selector('span.find-text')
        findCheckPoint.click()
        time.sleep(1)
        editButton = driver.find_element_by_xpath('//div[2]/div[4]/div/div[2]/div/div[2]/div[11]/input[1]')
        editButton.click()
        time.sleep(2)
        nameNPA = driver.find_element_by_xpath('//form/div/div[2]/div[4]/div/textarea')
        nameNPA.click()
        nameNPA.send_keys(' НПА ')
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(3)
        selectNPA = driver.find_element_by_xpath('//form/div/div[2]/div[15]/div/span/span[1]/span/span[2]')
        selectNPA.click()
        writeField = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        writeField.click()
        writeField.send_keys('Норм')
        writeField.send_keys(Keys.ENTER)
        EditProject = driver.find_element_by_name('yt0')
        EditProject.send_keys(Keys.PAGE_DOWN)
        EditProject.click()

    def test_2NPAedit(self):
        time.sleep(4)
        assert "ЭОР" in driver.title
        EditProject = driver.find_element_by_name('yt0')
        EditProject.click()
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Создать НПА"]')))
        #wait.until(EC.element_to_be_clickable)
        NPACr = driver.find_element_by_xpath('//button[text()="Создать НПА"]')
        NPACr.click()

if __name__ == '__main__':
    unittest.main()