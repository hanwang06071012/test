#-*- coding=utf-8 -*-

__author__ = "hanwang"

from flask import Flask

app=Flask(__name__)


from web.view import hello, test
