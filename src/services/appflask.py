from flask import Flask
from flask_cors import CORS, cross_origin

class AppFlask(Flask):
	def __init__(self, name):
		super().__init__(name)
		CORS(self)
