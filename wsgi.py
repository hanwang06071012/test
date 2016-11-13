#-*- coding=utf-8 -*-

__author__= 'hanwang'

from flask import Flask
from web import app


if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5022,debug=True)
