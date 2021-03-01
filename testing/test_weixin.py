import json
import time
import pytest
from selenium import webdriver
class  TestWeixin():
    def steu_method(self,method):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9322'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.vars = {}

    def teardown_method(self,method):
        self.driver.quit()

    def test_work_weixin(self):
        self.driver.get("https://work.weixin.qq.com/")

        self.driver.find_element_by_xpath("//*[@id='indexTop']/div[2]/aside/a[1]").click()
        time.sleep(6)
        self.driver.close()

    def test_login_work_weixin(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_id("menu_contacts").click()

    def test_cookie_login(self):
        cookies = self.driver.get_cookies()
        with open("tmp.text","w",encoding="utf-8") as f:
            f.write(json.dumps(cookies))
        print(cookies)