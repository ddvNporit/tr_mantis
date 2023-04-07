# Name : project.py
# Author : "Denisov Dmitry"
# Time : 07.04.2023
from model.project import Project
class ProjectHelper():
    def __init__(self, app):
        self.app = app
    def add_project(self, project):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='sidebar']/ul/li[7]/a/i").click()
        wd.find_element_by_link_text(u"Управление проектами").click()
        wd.find_element_by_xpath("//button[@type='submit']").click()
        wd.find_element_by_id("project-name").click()
        wd.find_element_by_id("project-name").clear()
        wd.find_element_by_id("project-name").send_keys(project.name)
        wd.find_element_by_xpath(u"//input[@value='Добавить проект']").click()

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_id("project-name", project.name)

    def change_field_id(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_id(field_name).click()
            wd.find_element_by_id(field_name).clear()
            wd.find_element_by_id(field_name).send_keys(text)

