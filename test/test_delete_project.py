# Name : test_delete_project.py
# Author : "Denisov Dmitry"
# Time : 07.04.2023
from model.project import Project
import random

def test_delete_project(app):
    old_list = app.soap.get_project_list()
    if not old_list:
        name = app.project.random_string(10)
        app.project.add_project(Project(name=name))
        old_list = app.soap.get_project_list()
    project = random.choice(old_list)
    app.project.delete_project(Project(id=project.id))
    # new_list = app.project.get_project_list()
    new_list = app.soap.get_project_list()
    old_list.remove(project)
    if new_list is None:
        new_list = []
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)
