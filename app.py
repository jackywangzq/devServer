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
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.externals import joblib




app=Flask(__name__)
# r'/*' 是通配符，让本服务器所有的 URL 都允许跨域请求
reload(sys)
sys.setdefaultencoding("utf-8")
CORS(app,resources={r"/*": {"origins": "*"}})
#sys.setdefaultencoding('utf-8')


@app.route('/', methods=['POST','GET'])
def index():
        print(request.values.get("username"))
        # return [request.values.get("username"),request.values.get("pwd")]
        js = {'username': request.values.get("username"),"password":request.values.get("pwd")}
        return jsonify(js)
        # region = request.form.get('region').encode("utf-8")
        # types = request.form.get('types').encode("utf-8")
        # print(region)
        # return printme(a)


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
