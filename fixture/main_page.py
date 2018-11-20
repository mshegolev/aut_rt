import os


class MainPageHelper:
    def __init__(self, app):
        self.app = app
        self.timeoute=10
        self.button_my_cabinet = '//a[contains(text(),"Личный кабинет")]'

    def open_my_cabinet(self):
        driver = self.app.driver
        driver.get(self.app.base_url + "/#personal=true")