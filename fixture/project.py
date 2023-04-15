# Name : project.py
# Author : "Denisov Dmitry"
# Time : 07.04.2023
from model.project import Project
import string, random


class ProjectHelper():
    def __init__(self, app):
        self.app = app

    def add_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        self.open_form_add_project()
        #ver2
        # self.fill_project_form(id_el="project-name", name=project.name)
        # wd.find_element_by_xpath(u"//input[@value='Добавить проект']").click()

        # ver1.20.2
        self.fill_project_form(id_el="name", name=project.name)
        wd.find_element_by_xpath(u"//input[@value='Add Project']").click()

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
        #ver1.20.2
        # self.change_field_xpath(id_el, name)
        #ver2
        self.change_field_name(id_el, name)


    def change_field_xpath(self, x_path, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_xpath(x_path).click()
            wd.find_element_by_xpath(x_path).clear()
            wd.find_element_by_xpath(x_path).send_keys(text)

    def change_field_id(self, id_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_id(id_name).click()
            wd.find_element_by_id(id_name).clear()
            wd.find_element_by_id(id_name).send_keys(text)

    def change_field_name(self, tag_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(tag_name).click()
            wd.find_element_by_name(tag_name).clear()
            wd.find_element_by_name(tag_name).send_keys(text)

    def open_project_page(self):
        wd = self.app.wd
        #ver2
        # wd.find_element_by_css_selector("i.fa.fa-gears.menu-icon").click()
        # wd.find_element_by_link_text(u"Управление проектами").click()
        # ver1.20.2

        wd.find_element_by_xpath('/ html / body / table[2] / tbody / tr / td[1] / a[7]').click()
        wd.find_element_by_xpath('/html/body/div[2]/p/span[2]/a').click()

    def open_form_add_project(self):
        wd = self.app.wd
        # ver2
        # wd.find_element_by_xpath("// input[ @ value = 'Add Project']']").click()
        # ver1.20.2
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        self.project_cache = []
        for element in wd.find_elements_by_xpath(
                "/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/table/*/tr"):
            if element.find_element_by_tag_name("a").get_attribute("href").split("=")[-1] != 'DESC':
                id = element.find_element_by_tag_name("a").get_attribute("href").split("=")[-1]
                name = element.find_element_by_tag_name("a").text
                self.project_cache.append(Project(id=id, name=name))
        return list(self.project_cache)

    def count(self):
        wd = self.app.wd
        self.open_project_page()
        return len(wd.find_elements_by_xpath(
            "/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/table/*/tr"))

    def random_string(self, maxlen):
        symbols = string.ascii_letters + string.digits + " " * 10
        return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
