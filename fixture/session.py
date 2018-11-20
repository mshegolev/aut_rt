class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, creds):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_name("login").click()
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys("%s" % creds.username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("%s" % creds.password)
        driver.find_element_by_name("authButton").click()

    def logout(self):
        driver = self.app.driver
        driver.get(self.app.base_url+"/back/logout.php?logout=yes")

    def ensure_logout(self):
        driver = self.app.driver
        if self.is_logged_in():
            self.logout()

    def is_logged_in_as(self, username):
        driver = self.app.driver
        return username in driver.find_element_by_class_name("topPanel__profileName").text

    def is_logged_in(self):
        driver = self.app.driver
        return len(driver.find_elements_by_class_name('exit')) > 0

    def ensure_login(self, creds):
        driver = self.app.driver
        if self.is_logged_in():
            if self.is_logged_in_as(creds.username):
                return
            else:
                self.logout()
        self.login(creds)