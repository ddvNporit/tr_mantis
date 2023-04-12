# Name : test_singup_new_account.py
# Author : "Denisov Dmitry"
# Time : 12.04.2023
import string, random


def test_signup_account(app):
    username = random_username("user_", 10)
    password = "test"
    email = username + "@localhost"
    app.james.ensure_user_exists(username, password)
    app.signup.new_user(username, email, password)
    app.session.login(username, password)
    assert app.session.is_logged_in_as(username)
    app.session.logout()


def random_username(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
