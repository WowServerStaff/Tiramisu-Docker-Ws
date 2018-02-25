from .abstract import *
from json import JSONEncoder
import json
import docker

class ContainersController(AbstractController):
	def __init__(self, injector):
		self.dockerClient = docker.from_env()
		nameController = str(type(self)).lower()
		prefixUrl = "/containers"
		super(ContainersController, self).__init__(injector, prefixUrl, nameController)

	def _parseData(self, container):
		return {
			"id": container.id,
			"short_id": container.short_id,
			"name": container.name,
			"status":  container.status,
			"attrs": container.attrs,
			"image": {
				"id": container.image.id,
				"short_id": container.image.short_id,
				"tags": container.image.tags,
				"attrs": container.image.attrs
			}
		}

	def get(self):
		containers = self.dockerClient.containers.list()
		parsedContainers = list()
		for container in containers:
			parsedContainers.append(self._parseData(container))
		return super(ContainersController, self).buildResponse(parsedContainers)

	def getById(self, identifier):
		container = self.dockerClient.containers.get(identifier)
		return super(ContainersController, self).buildResponse(self._parseData(container))
