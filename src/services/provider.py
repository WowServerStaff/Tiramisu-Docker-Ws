"""
Class used as dependency injector.

Allows the app to register and retrieve any class.
"""

import inspect

class Provider:
	modules = {}

	"""
	Registering method.
	
	Param1: the call name one the class is registered
	Param2: the class itself
	
	The function test if the instance is a class, and invoke its
	constructor in this case (the provider is injected inside).
	In the other case, we admit it's an instanciated object.
	We put it inside the modules object with the proper name
	"""
	def register(self, name, instance):
		if(inspect.isclass(instance)):
			resource = instance(self)
		else:
			resource = instance
		self.modules[name] = resource

	"""
	Resolving method.
	
	Param: the name of the module we try to invoke
	
	If the name correspond to one of the modules, we return it.
	In the other case, raise an exception.
	"""
	def resolve(self, name):
		if(name in self.modules):
			return self.modules[name]
		else:
			raise Exception("Dependency not found : " + name)
