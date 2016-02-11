# -*- coding: utf-8 -*-

import subprocess
import shlex
from voice_recognizer import VoiceRecognizer
from espeak import espeak 
from action_manager import ActionManager

class CommandHandler(object):

	CONST_TURN_OFF = "turn off"
	CONST_TURN_ON = "turn on"
	CONST_GOODBYE = "goodbye"

	def __init__(self):

		espeak.synth("Hello Master!")

		self.rec = VoiceRecognizer()

		self.actions = ActionManager().loadActions()

		# Variable used for command voice control, if True the voice command is executed
		self.canHear = True;

	def callSubProcess(self, args, text):
		try:
			espeak.synth(text)
			# Breaks the arguments to execute on terminal.
			args = args.split(" ")
			# Execute the command on terminal
			subprocess.Popen(args)
		except Exception as e:
			print "Error on callSubProcess: "+str(e)
			espeak.synth("Sorry, I can't "+text)

	def handle(self):
		voiceCommand = self.rec.speechToText().lower()
		if voiceCommand != "":
			if self.CONST_TURN_OFF in voiceCommand:
				espeak.synth("Turning off the microphone")
				self.canHear = False
			elif self.CONST_TURN_ON in voiceCommand:
				espeak.synth("Turning on the microphone")
				self.canHear = True
				return True

			if self.canHear:
				if self.CONST_GOODBYE in voiceCommand:
					espeak.synth("bye")
					return False
				espeak.synth("You said "+voiceCommand)

				for action in self.actions:
					# For each action on list of actions if voice command is found on list and he's active, he's is executed
					if voiceCommand in action.voiceCommand:
						self.callSubProcess(action.args, "Executing "+voiceCommand)		
				

		return True
