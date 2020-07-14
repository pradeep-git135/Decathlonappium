from appium import webdriver

desired_capabilities = {
    "platformName": "Android",
    "deviceName": "3f1b6aa0",
    "appPackage": "com.evamall.evacustomer",
    "appActivity": "com.evamall.evacustomer.splash.SplashActivity"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
driver.implicitly_wait(20)