class Action(object):
	
	def __init__(self, command, args, active):
		self.voiceCommand = command
		self.args = args
		self.active = active
		
	def toJson(self):
		return self.__dict__