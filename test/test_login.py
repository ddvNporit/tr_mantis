# Name : test_login.py
# Author : "Denisov Dmitry"
# Time : 07.04.2023
def test_login(app):
    app.session.login('administrator', 'root')
    assert app.session.is_logged_in_as("administrator")