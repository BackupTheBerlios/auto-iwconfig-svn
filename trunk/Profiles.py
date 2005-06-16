#!/usr/bin/env python
# -*- coding: UTF8 -*-

import os, subprocess, ConfigParser, sys, tempfile

CONFIG_FILE = '~/.auto-iwconfig.conf'
APP_VERSION = '0.1'

class ProfileError(Exception):
	pass

class Profile:
	"""Holds information about exactly one Profile and allows to apply it."""
	def __init__(self, name, interface, options):
		self.name, self.interface, self.options = name, interface, options

	def apply(self, gui=False):
		"""Applies the profile option by calling "sudo iwconfig %ifc %option %value" on each option."""

		# generate commandfile
		cmdf = open(os.path.join(tempfile.gettempdir(), 'auto-iwconfig'), 'w')
		os.chmod(cmdf.name, 0777)

		cmdf.write('#!/bin/sh\n')
		
		for k in self.options:
			cmdf.write("%s %s %s %s\n" % ('iwconfig', self.interface, k, self.options[k]))
		
		cmdf.close()
		
		try:
			if gui:
				subprocess.call(['gksu', '-S', cmdf.name])
			else:
				subprocess.call(['sudo', cmdf.name])
		except OSError:
			print "gksu/sudo/iwconfig not found"

def __make_dict(self, list):
	"""Convert a list of (name, value) tuples into a dictionary."""
	ret = {}
	for i in list:
		ret[i[0]] = i[1]

	return ret

def get_profiles(self):
	"""Read the configuration file.
	Return a list of profiles"""
	c = ConfigParser.ConfigParser()
	c.read(os.path.expanduser(CONFIG_FILE))
	
	profiles = []
	
	for sec in c.sections():
		# remove the 'interface'-option
		if not c.has_option(sec, 'interface'):
			raise ProfileError, "No interface name given for profile '%s'" % sec
		
		ifc = c.get(sec, 'interface')
		c.remove_option(sec, 'interface')

		profiles.append(Profile(sec, ifc, __make_dict(c.items(sec))))

	return profiles
