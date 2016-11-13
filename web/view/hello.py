#-*- coding=utf-8 -*-
__author__ ='hanwang'

from flask import Flask, render_template
from web import  app
#app=Flask(__name__)

@app.route('/')
def hello():
	#return ("hello world,copy to master ... ")
	return render_template('/test/hello.html')


@app.route('/hello/')
def hello():
	return ("hello world,copy to master ... ")

if __name__ == "__main__":
	app=Flask(__name__)
	app.run(host='0.0.0.0',port=5022)
