import os

class pathMaker:
	def __init__(self):
		pass
	def get_parts(self, totalPath):
		if(totalPath==None):
			return []
		return totalPath.strip("/").split("/")

	def get_paths(self, totalPath):
		parts = self.get_parts(totalPath)
		paths =[]
		path = "/"
		for p in parts:
			path = os.path.join(path,p)
			paths.append(path)
		return paths

	def make_path(self, totalPath):
		pass

