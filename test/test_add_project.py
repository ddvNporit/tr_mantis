# Name : test_add_project.py
# Author : "Denisov Dmitry"
# Time : 07.04.2023
from model.project import Project
def test_add_project(app):
    app.session.login('administrator', 'root')
    app.project.add_project(Project(name="2345"))