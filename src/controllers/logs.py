"""
Docker logs controller.
Extends the abstract controller.
"""

from .abstract import *
from json import JSONEncoder
import json
import docker

class LogsController(AbstractController):
	"""
	Logs controller constructor.
	
	Set the docker client and reuse the parent constructor
	to create the url rules
	"""
	def __init__(self, injector):
		self.dockerClient = docker.from_env()
		nameController = str(type(self)).lower()
		prefixUrl = "/logs"
		super(LogsController, self).__init__(injector, prefixUrl, nameController)

	"""
	Getbyid method.
	
	Param: Container identifier
	
	Get the container logs by fetching it with its identifier.
	Reuse the abstract build response to return json data.
	"""
	def getById(self, identifier):
		container = self.dockerClient.containers.get(identifier)
		logs = container.logs().decode("utf-8")
		return super(LogsController, self).buildResponse(logs)

	"""
	Get method.
	
	Returns false to deactivate it. We just want the
	getById method in this controller.
	"""
	def get(self):
		return false
