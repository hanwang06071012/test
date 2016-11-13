#-*- coding=utf-8 -*-
__author__ ='hanwang'

from flask import Flask, request,url_for

from web import app

@app.route('/test/',methods=['GET','POST'])
def test():
	if request.method=='GET':
		namelast=request.args.get('lastname','hanwangtest')
		return ("hello %s ... " % (namelast))
	else:
		return ("no lastname")

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5022)
