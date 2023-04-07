# Name : test_delete_project.py
# Author : "Denisov Dmitry"
# Time : 07.04.2023
from model.project import Project


def test_add_project(app):
    app.session.login('administrator', 'root')
    app.project.delete_project(Project(id="5"))
