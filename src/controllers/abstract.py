"""
Abstract controller
"""

import json
from flask import request, jsonify, Response, Flask

class AbstractController:
	"""
	Contructor which will be extended.
	
	Param1: the dependency injector
	Param2: the prefix url of the extended controller
	Param3: the name of the extended controller
	
	Set the different url rules with the extended controller informations
	"""
	def __init__(self, injector, prefixUrl, nameController):
		self.app = injector.resolve("Flask")

		self.app.add_url_rule(prefixUrl, nameController + ".get", self.get, methods=["GET"])
		self.app.add_url_rule(prefixUrl + "/<string:identifier>", nameController + ".getbyid", self.getById, methods=["GET"])

	"""
	Response method.
	
	Param: the serialized return data
	
	Return the response in a json format,
	from a serialized content
	"""
	def buildResponse(self, data):
		serialized = json.dumps({
			"success": True,
			"data": data
		})

		return Response(serialized, mimetype="application/json")

	"""
	Error method.
	
	Param: the serialized error
	
	Return the error in a json format
	"""
	def buildError(self, error):
		serialized = json.dumps({
			"success": False,
			"detail": error
		})

		return Response(serialized, mimetype="application/json", status_code=400)
