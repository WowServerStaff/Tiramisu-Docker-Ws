import json
from bson import json_util
from flask import request, jsonify, Response, Flask

class AbstractController:
	def __init__(self, injector, prefixUrl, nameController)
		self.app = injector.resolve("Flask")

		self.app.add_url_rule(prefixUrl, nameController + ".get", self.get, methods=["GET"])
		self.app.add_url_rule(prefixUrl + "</string:identifier>", nameController + ".getbyid", self.getById, methods=["GET"])

	def buildResponse(self, data):
		serialized = json_util.dumps({
			"success": True,
			"data": data
		})

		return Response(serialized, mimetype="application/json")

	def buildError(self, error):
		serialized = json_util.dumps({
			"success": False,
			"detail": error
		})

		return Response(serialized, mimetype="application/json", status_code=400)
