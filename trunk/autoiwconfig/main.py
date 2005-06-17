#!/usr/bin/env python
# -*- coding: UTF8 -*-

# auto-iwconfig 0.1 - an automatic wireless profile tool
# Copyright (C) 2005 Henrik Ronellenfitsch

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

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
