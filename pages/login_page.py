from settings import driver

class Login:
    allow1 = "android:id/button1"
    allow = "com.android.packageinstaller:id/permission_allow_button"
    nxtbtn = "com.evamall.evacustomer:id/next"
    nxtbtn = "com.evamall.evacustomer:id / next"
    nxtbtn = "com.evamall.evacustomer:id / next"
    nxtbtn = "com.evamall.evacustomer:id / next"
    finishbtn = "com.evamall.evacustomer:id / next"

    def allow_access(self):
        print("entered the allow_access fxn")
        driver.implicitly_wait(20)
        driver.find_element_by_id(self.allow1).click()
        driver.find_element_by_id(self.allow).click()
        driver.find_element_by_id(self.nxtbtn).click()
obj_login = Login()
obj_login.allow_access()







