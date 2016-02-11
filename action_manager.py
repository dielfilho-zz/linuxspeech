# -*- coding: utf-8 -*-
import json
from action import Action

class ActionManager(object):
	
	def  __init__(self):
		self.actions = []

	def loadActions(self):
		actionsFile = open(".actions")
		for row in actionsFile:
			row = row.rstrip()

			jsonAction = json.loads(row)

			action = Action(jsonAction["voiceCommand"], jsonAction["args"], jsonAction["active"])
			# Load actives actions from actions file
			if action.active:
				self.actions.append(action)
		return self.actions
	def showActions(self):
		for action in self.actions:
			print action.voiceCommand

