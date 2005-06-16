#!/usr/bin/env python

from distutils.core import setup

setup(name='auto-iwconfig',
		version='0.1',
		description='Wireless profile management tool',
		author='Henrik Ronellenfitsch',
		author_email='searinox@web.de',
		url='http://auto-iwconfig.berlios.de',
		packages=['auto-iwconfig'],
		package_dir={'auto-iwconfig': 'auto-iwconfig'},
		scripts=['auto-iwconfig/auto-iwconfig']
		)
