# -*- coding: utf-8 -*-
class SessionHelper():
    def __init__(self, app):
        self.app = app
    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        # wd.find_element_by_xpath(u"//input[@value='Вход']").click()
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        #ver 2
        # wd.find_element_by_xpath(u"//input[@value='Вход']").click()
        wd.find_element_by_xpath("//input[@type='submit']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def get_logged_user(self):
        wd = self.app.wd
        #ver2
        # return wd.find_element_by_css_selector("td.loin-info-left span").text
        return wd.find_element_by_css_selector("td.loin-info-left span").text


    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0
    def is_logged_in_as(self,username):
        return self.get_logged_user() == username
    def get_logged_user(self):
        wd = self.app.wd
        # ver 2
        # return  wd.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a/span").text
        return wd.find_element_by_css_selector("td.login-info-left span").text

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()
