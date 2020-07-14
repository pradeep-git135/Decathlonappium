from pages.login_page import Login
import pytest

class Test_login:
    def test_login(self):
        obj_login = Login()
        obj_login.allow_access()
