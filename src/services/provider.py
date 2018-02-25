import inspect

class Provider:
	modules = {}

	def register(self, name, instance):
		if(inspect.isclass(instance)):
			resource = instance(self)
		else:
			resource = instance
		self.modules[name] = resource

	def resolve(self, name):
		if(name in self.modules):
			return self.modules[name]
		else:
			raise Exception("Dependency not found : " + name)