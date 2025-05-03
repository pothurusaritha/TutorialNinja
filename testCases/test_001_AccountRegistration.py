import os.path

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegisterPage
from utilities import randomString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
class Test_001_AccountReg:
    baseURL = ReadConfig.getApplicationURL()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_account_reg(self,setup):
        self.driver=setup
        self.logger.info("**** test_001_Account Registration started ****")
        self.driver.get(self.baseURL)
        self.logger.info("**** Launching Application ****")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.hp=HomePage(self.driver)
        self.regpage=AccountRegisterPage(self.driver)
        self.logger.info("**** Clicking My Account--->Register ****")
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.logger.info("**** Providing Customer details for registration ****")
        self.regpage.setFirstName("pothuru")
        self.regpage.setLastName("saritha")
        self.email=randomString.random_string_geerator()+"@gmail.com"
        self.regpage.setEmail(self.email)
        # self.regpage.setEmail("admin123@gmail.com")
        self.regpage.setTelephone("23456789")
        self.regpage.setPassword("saritha123")
        self.regpage.setConfirmPassword("saritha123")
        self.regpage.setNewsletterRadio()
        self.regpage.setPrivacyPolicy()
        self.regpage.setClickContinue()
        self.confmsg=self.regpage.getConfirmMsg()
        if self.confmsg=="Your Account Has Been Created!":
            self.logger.info("**** Account Registration Passed ****")
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.getcwd())+"\\screenshots\\"+"test_account_reg.png")
            self.logger.info("**** Account Registration Failed ****")

            assert False
        self.logger.info("**** test_001_Account Registration finished ****")
