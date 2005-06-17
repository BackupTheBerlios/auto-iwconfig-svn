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

from distutils.core import setup

setup(name='auto-iwconfig',
		version='0.1',
		description='Wireless profile management tool',
		author='Henrik Ronellenfitsch',
		author_email='searinox@web.de',
		url='http://auto-iwconfig.berlios.de',
		packages=['autoiwconfig'],
		package_dir={'autoiwconfig': 'autoiwconfig'},
		scripts=['bin/auto-iwconfig']
		)
