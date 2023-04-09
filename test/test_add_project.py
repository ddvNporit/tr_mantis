# Name : test_add_project.py
# Author : "Denisov Dmitry"
# Time : 07.04.2023
import string, random
from model.project import Project


def test_add_project(app):
    app.session.login('administrator', 'root')
    old_list = app.project.get_project_list()
    testdata = Project(name=random_string(10))
    app.project.add_project(testdata)
    new_list = app.project.get_project_list()
    old_list.append(testdata)
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
