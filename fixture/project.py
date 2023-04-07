# Name : project.py
# Author : "Denisov Dmitry"
# Time : 07.04.2023
from model.project import Project


class ProjectHelper():
    def __init__(self, app):
        self.app = app

    def add_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        self.open_form_add_project()
        self.fill_project_form(id="project-name", name=project.name)
        wd.find_element_by_xpath(u"//input[@value='Добавить проект']").click()

    def fill_project_form(self, id, name):
        wd = self.app.wd
        self.change_field_id(id, name)

    def change_field_id(self, id_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_id(id_name).click()
            wd.find_element_by_id(id_name).clear()
            wd.find_element_by_id(id_name).send_keys(text)

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='sidebar']/ul/li[7]/a/i").click()
        wd.find_element_by_link_text(u"Управление проектами").click()

    def open_form_add_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//button[@type='submit']").click()
