# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import octoprint.settings
import octoprint.util
from octoprint.events import eventManager, Events
from flask import jsonify, request
import logging
import logging.handlers
import RPi.GPIO as GPIO

class PhysicalButtonsPlugin(octoprint.plugin.StartupPlugin,
							octoprint.plugin.SettingsPlugin,
							octoprint.plugin.EventHandlerPlugin,
							octoprint.plugin.BlueprintPlugin):

	def initialize(self):
		self._logger.setLevel(logging.DEBUG)
		
		self._logger.info("Running RPi.GPIO version '{0}'...".format(GPIO.VERSION))
		if GPIO.VERSION < "0.6":
			raise Exception("RPi.GPIO must be greater than 0.6")
			
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		
		self._logger.info("Filament Sensor Plugin [%s] initialized..."%self._identifier)

	def on_after_startup(self):
		self.PIN_PAUSE = self._settings.get(["pause"])
		self.PIN_STOP = self._settings.get(["stop"])
		self.BOUNCE = self._settings.get_int(["bounce"])

		if self.PIN_PAUSE != -1:
			self._logger.info("Pause button setup on GPIO [%s]..."%self.PIN_PAUSE)
			GPIO.setup(self.PIN_PAUSE, GPIO.IN, pull_up_down=GPIO.PUD_UP)

		if self.PIN_STOP != -1:
			self._logger.info("Stop button setup on GPIO [%s]..."%self.PIN_STOP)
			GPIO.setup(self.PIN_STOP, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	def get_settings_defaults(self):
		return dict(
			pause = -1,
			stop = -1,
			bounce = 300
		)

	@octoprint.plugin.BlueprintPlugin.route("/status", methods=["GET"])
	def check_status(self):
		status = "-1"
		if self.PIN_PAUSE != -1:
			status = "0" if GPIO.input(self.PIN_PAUSE) else "1"
		status2 = "-1"
		if self.PIN_STOP != -1:
			status2 = "0" if GPIO.input(self.PIN_STOP) else "1"
		return jsonify( pause = status, stop = status2 )
		
	def on_event(self, event, payload):
		if event == Events.PRINT_STARTED:
			self._logger.info("Printing started. Buttons enabled.")
			self.setup_gpio()
		elif event in (Events.PRINT_DONE, Events.PRINT_FAILED, Events.PRINT_CANCELLED):
			self._logger.info("Printing stopped. Buttons disabled.")
			try:
				GPIO.remove_event_detect(self.PIN_PAUSE)
				GPIO.remove_event_detect(self.PIN_STOP)
			except:
				pass

	def setup_gpio(self):
		try:
			GPIO.remove_event_detect(self.PIN_PAUSE)
			GPIO.remove_event_detect(self.PIN_STOP)
		except:
			pass
		if self.PIN_PAUSE != -1:
			GPIO.add_event_detect(self.PIN_PAUSE, GPIO.FALLING, callback=self.check_gpio, bouncetime=self.BOUNCE)
		if self.PIN_STOP != -1:
			GPIO.add_event_detect(self.PIN_STOP, GPIO.FALLING, callback=self.check_gpio, bouncetime=self.BOUNCE)

	def check_gpio(self, channel):
		state = GPIO.input(self.PIN_PAUSE)
		self._logger.debug("Detected button [%s] state [%s]? !"%(channel, state))
		if not state: 
			self._logger.debug("Pause button [%s]!"%state)
			if self._printer.is_printing():
				self._printer.toggle_pause_print()
			if self._printer.is_paused():
				self._printer.resume_print()

		state2 = GPIO.input(self.PIN_STOP)
		self._logger.debug("Detected button [%s] state [%s]? !"%(channel, state2))
		if not state2: 
			self._logger.debug("Stop button [%s]!"%state2)
			if self._printer.is_printing():
				self._printer.cancel_print()
			if self._printer.is_ready():
				self._printer.start_print()

				
	def get_version(self):
		return self._plugin_version

	def get_update_information(self):
		return dict(
			octoprint_physicalbuttons=dict(
				displayName="Physical Buttons",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="netlands",
				repo="Octoprint-Physical-Buttons",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/netlands/OctoPrint-Physical-Buttons/archive/{target_version}.zip"
			)
		)

__plugin_name__ = "Physical Buttons"
__plugin_version__ = "0.0.1"
__plugin_description__ = "Use physical buttons to start, stop and pause printing."

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = PhysicalButtonsPlugin()

