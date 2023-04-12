# Name : test_singup_new_account.py
# Author : "Denisov Dmitry"
# Time : 12.04.2023
def test_signup_account(app):
    username ="user1"
    password = "test"
    app.james.ensure_user_exists(username, password)
