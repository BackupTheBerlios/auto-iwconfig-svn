#!/usr/bin/env python
# -*- coding: UTF8 -*-

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
