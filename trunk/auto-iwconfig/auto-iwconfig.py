#!/usr/bin/env python
# -*- coding: UTF8 -*-

import sys
import Profiles

def print_header():
	print """
auto-iwconfig %s Copyright (C) 2005 Henrik Ronellenfitsch
Licensed under the terms of the GPL.
	""" % Profiles.APP_VERSION

def print_help():
	print """
Usage: auto-iwconfig [profile-name]
"""

def main():
	print_header()
	
	profiles = Profiles.get_profiles()
	
	if len(sys.argv) > 1:
		try:
			blas = [z for z in profiles if z.name == sys.argv[1]]
			blas[0].apply()
			
		except KeyError:
			print "Profile not found."
	else:
		print "Not enough arguments."
		print_help()
		print "The following profiles are available:"

		for prf in profiles:
			print prf.name

if __name__ == '__main__':
	main()
