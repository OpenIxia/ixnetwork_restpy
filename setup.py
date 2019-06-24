import io
import os
import sys
from shutil import rmtree
from setuptools import setup


base_dir = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
with open(os.path.join(base_dir, 'README.md'), 'rb') as fid:
	long_description = '\n' + fid.read()

# Import the README and use it as the long-description.
with open(os.path.join(base_dir, 'version.txt'), 'rb') as fid:
	version_number = fid.read()

setup(
	name='ixnetwork_restpy',
	version=version_number,
	description='IxNetwork REST API Python Client',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/OpenIxia/ixnetwork_restpy',
	author='Keysight ISG IxNetwork team',
	author_email='ixnetwork@keysight.com',
	license='MIT',
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Topic :: Software Development',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
	],
	keywords='ixnetwork l2l3 test tool ixia automation',
	packages=['ixnetwork_restpy'],
	include_package_data=True,
	python_requires='>=2.7, <4',
	install_requires=['requests'])
