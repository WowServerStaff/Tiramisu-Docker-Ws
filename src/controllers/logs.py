from .abstract import *
from json import JSONEncoder
import json
import docker

class LogsController(AbstractController):
	def __init__(self, injector):
		self.dockerClient = docker.from_env()
		nameController = str(type(self)).lower()
		prefixUrl = "/logs"
		super(LogsController, self).__init__(injector, prefixUrl, nameController)

	def getById(self, identifier):
		container = self.dockerClient.containers.get(identifier)
		logs = container.logs().decode("utf-8")
		return super(LogsController, self).buildResponse(logs)

	def get(self):
		return false
