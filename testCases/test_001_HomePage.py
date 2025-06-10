from webbrowser import Chrome

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from ProjectObject.HomePage import HomePage
from Utilities.customLog import LogGen
from Utilities.readproperties import ReadConfig


class TestHomePage:
    url="https://testautomationpractice.blogspot.com/"
    # url=ReadConfig.getApplicationurl()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_home_page(self,setup):
        self.driver=setup
        self.logger.info("Starting Home Page Test")
        self.driver=webdriver.Chrome()
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.logger.info("Launching Home Page")

        self.hp=HomePage(self.driver)
        self.hp.clickHomebtn()
        self.logger.info("Filling the form")
        self.hp.enterName("Ama")
        self.hp.enterEmail("tiyumiddi@gmail.com")
        self.hp.enterPhone("0700000000")
        self.hp.enterAddress("M 23, Greenbelt")
        self.hp.clickGender()
        self.hp.clickDays()
        self.hp.selectCountry("France")
        self.hp.selectColor()
        self.hp.selectSort()
        self.hp.selectDate("05/26/2025")
        self.hp.clickSubmitbtn()
        self.logger.info("Submitting the form")
        self.driver.quit()

