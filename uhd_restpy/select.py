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


class Select(object):
    """ Select infrastructure

    e.g.,
    POST .../operations/select
    {
        "selects": [
            {
                "from": "/",
                "properties": [],
                "children": [
                    {
                        "child": "(?i)^(topology|deviceGroup|ethernet|ipv4|ipv6|bgpIpv4Peer)$",
                        "properties": ["*"],
                        "filters": []
                    }
                ],
                "inlines": [
                    {
                        "child": "multivalue",
                        "properties": ["format", "pattern"]
                    },	
                    {
                        "child": "^(singleValue)$",
                        "properties": ["*"]
                    }	
                ]
            }
        ]
    }
    """

    def __init__(self, connection, from_url, from_properties=['*'], children=[], inlines=[]):
        self._connection = connection
        self._url = '%s/operations/select?xpath=true' % from_url[0:from_url.index('ixnetwork') + len('ixnetwork')]
        self._payload = {
            'selects': [
                {
                    'from': from_url,
                    'properties': from_properties,
                    'children': children,
                    'inlines': inlines
                }
            ]
        }

    def go(self):
        return self._connection._execute(self._url, self._payload)
