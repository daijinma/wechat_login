from flask import Flask, send_file
from configparser import ConfigParser
from lib import wechat_login 

app = Flask(__name__)
config = ConfigParser()
config.read('config.ini')


wechatLogin = wechat_login.Login

@app.route('/')
def hello():
    return 'Hello, world!'


@app.route('/wechat')
def wechatlogin():
    wechat = wechatLogin()
    id = config.get("DEFAULT", "WX_ACCOUNT")
    pw = config.get("DEFAULT", "WX_PASSWORD")
    wechat.login(id,pw)
    # wechat.get_token()
    image_path = 'screenshot.png'
    return send_file(image_path, mimetype='image/jpeg')

@app.route('/wechat2')
def wechatlogin2():
    wechat = wechatLogin()
    
    return wechat.get_token()



if __name__ == '__main__':
    app.run(port=4001)
