#!/usr/bin/env python
#encoding=utf-8

from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import url_for
import re
import sys
import types
from flask_cors import CORS

import hashlib
import time


app=Flask(__name__)
# r'/*' 是通配符，让本服务器所有的 URL 都允许跨域请求
reload(sys)
sys.setdefaultencoding("utf-8")
CORS(app,resources={r"/*": {"origins": "*"}})
#sys.setdefaultencoding('utf-8')


@app.route('/', methods=['POST','GET'])
def index():
        # return [request.values.get("username"),request.values.get("pwd")]
        # js = [{'username': request.values.get("username"),"password":request.values.get("pwd")}]
        if request.values.get("username") == '12345':  # 判断变量否为'python'
            arr_res = {
                'status': 1,
                'token': token()
            }
        else:
            arr_res = {
                'status': 0,
                'token': token()
            }
        return jsonify(arr_res);

@app.route('/index', methods=['POST','GET'])
def index_():
    return render_template('index.html')

@app.route('/data_get', methods=['POST','GET'])
def data_get():
    username =request.values.get("username").encode('utf-8')
    password = request.values.get("password").encode('utf-8')
    print username
    print password
    arr_res = {
        'username': username,
        'password': password,
    }
    return jsonify(arr_res)

@app.route('/data_post', methods=['POST','GET'])
def data_post():
    username = request.values.get("username").encode('utf-8')
    password = request.values.get("password").encode('utf-8')
    print username
    print password
    arr_res = {
        'username': username,
        'password': password,
    }
    return jsonify(arr_res)

if __name__=='__main__':
    app.run(debug=True)

def t_stamp():
    t = time.time()
    t_stamp = int(t)
    print('当前时间戳:', t_stamp)
    return t_stamp

def token():
    # API_SECRET = "xxxx" #从接口对接负责人处拿到
    # project_code = "xxxx"  #GET传递的项目编码，参数值请根据需要自行定义
    account = "admin"   #GET传递的登录帐号，参数值请根据需要自行定义
    time_stamp =str(t_stamp())  #int型的时间戳必须转化为str型，否则运行时会报错
    hl = hashlib.md5()  # 创建md5对象，由于MD5模块在python3中被移除，在python3中使用hashlib模块进行md5操作
    # strs = project_code + account + time_stamp + API_SECRET # 根据token加密规则，生成待加密信息
    # strs = account + time_stamp   # 根据token加密规则，生成待加密信息
    strs = account # 根据token加密规则，生成待加密信息
    hl.update(strs.encode("utf8"))  # 此处必须声明encode， 若为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
    token=hl.hexdigest()  #获取十六进制数据字符串值
    arr_res = {
        'status': 0,
        'token': token,
    }
    # print('MD5加密前为 ：',strs)
    # print('MD5加密后为 ：',token)
    return token
