
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    #locators
    home_btn_xpath="//div[@id='PageList2']//a[normalize-space()='Home']"
    name_xpath="//input[@id='name']"
    email_xpath="//input[@id='email']"
    phone_xpath="//input[@id='phone']"
    address_xpath="//textarea[@id='textarea']"
    gender_btn_xpath="//input[@id='male']"
    days_xpath="//input[@id='monday']"
    country_select_xpath="//*[@id='country']"
    color_option_xpath="//select[@id='colors']//option[3]"
    sort_list_xpath="//option[@value='cat']"
    date_picker_xpath="//input[@id='datepicker']"
    # date_picker2_xpath="//input[@id='txtDate']"
    submit_btn_xpath="//button[@class='submit-btn']"

    #constructor
    def __init__(self,driver):
        self.driver=driver

     #Action methods
    def clickHomebtn(self):
        self.driver.find_element(By.XPATH,self.home_btn_xpath).click()

    def enterName(self,name):
        self.driver.find_element(By.XPATH,self.name_xpath).send_keys(name)

    def enterEmail(self,email):
        self.driver.find_element(By.XPATH,self.email_xpath).send_keys(email)

    def enterPhone(self,phone):
        self.driver.find_element(By.XPATH,self.phone_xpath).send_keys(phone)

    def enterAddress(self,address):
        self.driver.find_element(By.XPATH,self.address_xpath).send_keys(address)

    def clickGender(self):
        self.driver.find_element(By.XPATH,self.gender_btn_xpath).click()

    def clickDays(self):
        self.driver.find_element(By.XPATH,self.days_xpath).click()

    def selectCountry(self,country):
        # self.WebDriverWait(self.driver,10).until(lambda driver:driver.find_element(By.XPATH,self.country_select_xpath))
        country_select=Select(self.driver.find_element(By.XPATH,self.country_select_xpath))
        country_select.select_by_visible_text(country)

    def selectColor(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.color_option_xpath)))
        self.driver.find_element(By.XPATH,self.color_option_xpath).click()

    def selectSort(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.sort_list_xpath)))
        self.driver.find_element(By.XPATH,self.sort_list_xpath).click()

    def selectDate(self,date):
        self.driver.find_element(By.XPATH,self.date_picker_xpath).send_keys(date)

    # def selectDate2(self,date):
    #     self.driver.find_element(By.XPATH,self.date_picker2_xpath).send_keys(date)

    def clickSubmitbtn(self):
        self.driver.find_element(By.XPATH,self.submit_btn_xpath).click()

        self.driver.close()





