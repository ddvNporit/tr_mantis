# Name : test_add_project.py
# Author : "Denisov Dmitry"
# Time : 07.04.2023
import string, random
from model.project import Project


def test_add_project(app):
    old_list = app.project.get_project_list()
    testdata = Project(name=random_string(10))
    app.session.login('administrator', 'root')
    app.project.add_project(testdata)


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
