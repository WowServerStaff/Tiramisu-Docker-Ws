"""
Docker containers controller.
Extends the abstract controller.
"""

from .abstract import *
from json import JSONEncoder
import json
import docker

class ContainersController(AbstractController):
	"""
	Containers controller constructor.
	
	Set the docker client and reuse the parent constructor
	to create the url rules
	"""
	def __init__(self, injector):
		self.dockerClient = docker.from_env()
		nameController = str(type(self)).lower()
		prefixUrl = "/containers"
		super(ContainersController, self).__init__(injector, prefixUrl, nameController)

	"""
	Parsing data method.
	
	Param: container data
	
	Format the output json of a container.
	"""
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

	"""
	Get method.
	
	Get all the containers of the server.
	For each container, format the output json with _parseData.
	"""
	def get(self):
		containers = self.dockerClient.containers.list()
		parsedContainers = list()
		for container in containers:
			parsedContainers.append(self._parseData(container))
		return super(ContainersController, self).buildResponse(parsedContainers)

	"""
	Getbyid method
	
	Param: Container identifier
	
	Get the container related to the identifier in params.
	Reuse the abstract build response to return json data.
	"""
	def getById(self, identifier):
		container = self.dockerClient.containers.get(identifier)
		return super(ContainersController, self).buildResponse(self._parseData(container))
