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
        self.fill_project_form(id_el="project-name", name=project.name)
        wd.find_element_by_xpath(u"//input[@value='Добавить проект']").click()

    def delete_project(self, project):
        self.open_project_page()
        self.select_project_on_id(project.id)
        self.delete_selected_project()

    def delete_selected_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath(u"//input[@value='Удалить проект']").click()
        wd.find_element_by_xpath(u"//input[@value='Удалить проект']").click()

    def select_project_on_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=%s')]" % id).click()

    def fill_project_form(self, id_el, name):
        self.change_field_id(id_el, name)

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

    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        for element in wd.find_elements_by_xpath("//table/tbody/tr"):
            text = element.text
            if text is None:
                text = ''
            id = element.find_element_by_name("selected[]").get_attribute("value")
            self.group_cache.append(Project(name=text, id=id))
        return list(self.group_cache)
