#-*- coding=utf-8 -*-
__author__ ='hanwang'

from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
	return ("hello world for  second  test ... ")

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5022)
