"""
Class extending Flask.

Called when the app need Flask, it
contains the CORS implementation
"""

from flask import Flask
from flask_cors import CORS, cross_origin

class AppFlask(Flask):
	def __init__(self, name):
		super().__init__(name)
		CORS(self)
