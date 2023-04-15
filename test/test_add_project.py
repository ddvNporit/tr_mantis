# Name : test_add_project.py
# Author : "Denisov Dmitry"
# Time : 07.04.2023
from model.project import Project


def test_add_project(app):
    # old_list = app.project.get_project_list()
    old_list = app.soap.get_project_list()
    name = app.project.random_string(10)
    testdata = Project(name=name)
    app.project.add_project(testdata)
    # new_list = app.project.get_project_list()

    new_list = app.soap.get_project_list()
    if old_list is None:
        old_list = []
    old_list.append(testdata)
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)
