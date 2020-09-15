# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE. 
import os
import sys
import time
import argparse
from setuptools import setup


base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir, 'README.md')) as fid:
    long_description = fid.read()
if '--internal' in sys.argv:
    version_number = time.strftime('%Y%m%d.%H.%M', time.gmtime())
    sys.argv.remove('--internal')
else:
    with open(os.path.join(base_dir, 'version.txt')) as fid:
        version_number = fid.read()


setup(
    name='ixnetwork_restpy',
    version=version_number,
    description='The IxNetwork Python Client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/OpenIxia/ixnetwork_restpy',
    author='Keysight ISG IxNetwork team',
    author_email='andy.balogh@keysight.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    keywords='ixnetwork performance traffic generator real world ixia automation',
    packages=['ixnetwork_restpy', 'uhd_restpy'],
    include_package_data=True,
    python_requires='>=2.7, <4',
    install_requires=['requests', 'websocket-client'],
    tests_require=['mock'],
    test_suite='ixnetwork_restpy.tests'
)
