# Name : test_delete_project.py
# Author : "Denisov Dmitry"
# Time : 07.04.2023
from model.project import Project
import random

def test_add_project(app):
    app.session.login('administrator', 'root')
    if app.project.count() < 1:
        app.project.add_project(Project(name="test"))
    old_list = app.project.get_project_list()
    project = random.choice(old_list)
    app.project.delete_project(Project(id=project.id))
    new_list = app.project.get_project_list()
    old_list.remove(project)
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)
