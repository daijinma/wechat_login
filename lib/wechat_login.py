import time
import json
import re
from selenium import webdriver
from lxml import html
from selenium.webdriver.common.by import By
from urllib.parse import urlparse, parse_qs

browser = webdriver.Chrome()

class Login: 
    def __init__(self) -> None:
        self.html = ''

    def browserOpen(self):
        if browser is None :
            browser = webdriver.Chrome()
    
    def browserClose(self):
        browser.close()
        browser = None

    # mock login & get cookie
    def login(self, id, pw):
        # if browser is None :
        # browser = webdriver.Chrome()
            
        url = 'https://mp.weixin.qq.com'
        Browner = browser
        Browner.get(url)
        # 获取账号输入框
        Browner.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/div[2]/a').click()
        # Browner.find_element_by_link_text('使用帐号登录').click()
        ID = Browner.find_element(By.NAME, 'account')
        PW = Browner.find_element(By.NAME, 'password')

        ID.send_keys(id)
        PW.send_keys(pw)
        Browner.find_element(By.CLASS_NAME, 'btn_login').click()
        # 等待扫二维码
        time.sleep(5)
        Browner.save_screenshot('screenshot.png')
        ck = Browner.get_cookies()

        with open('../ck.txt', 'w') as f:
            f.write(ck1)
            f.close()

    # 获取token，在页面中提取
    def get_token(self):
        cookies = browser.get_cookies()
        cookie_string = ';'.join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])

        current_url = browser.current_url

        # 解析 URL
        parsed_url = urlparse(current_url)

        # 获取查询字符串部分
        query_string = parsed_url.query

        # 解析查询字符串
        query_params = parse_qs(query_string)

        resp = {
            "query":  query_params['token'][0],
            "cookie": cookie_string
        }
        return resp

