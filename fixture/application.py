# -*- coding: utf-8 -*-
import time

from pyvirtualdisplay import Display
from selenium import webdriver
import os.path

from fixture.api import Api
from fixture.main_page import MainPageHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        drivername = 'geckodriver'
        self.display = Display(visible=False, size=(1280, 1024))
        self.display.start()
        executable_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "driver", drivername)
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.folderList', 2)  # custom location
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        self.file_path = os.path.join(os.getcwd(), "..", "..", "tmp")
        os.makedirs(self.file_path,exist_ok=True)
        profile.set_preference('browser.download.dir', self.file_path)
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
        self.driver = webdriver.Firefox(executable_path=executable_path, service_log_path=executable_path + '.log',firefox_profile=profile)
        self.base_url = "https://rithm-time.tv"
        self.v1 = "/api/v1"
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.session = SessionHelper(self)
        self.main_page = MainPageHelper(self)
        self.api = Api(self)

    def open_home_page(self):
        driver = self.driver
        driver.get(self.base_url)

    def is_valid(self):
        try:
            self.driver.current_url()
            return True
        except:
            return False

    def destroy(self):
        self.driver.quit()
        self.display.stop()
