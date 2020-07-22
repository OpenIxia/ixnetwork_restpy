# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class InterfaceDiscoveredAddress(Base):
    """The tab that shows description and ip of interface configured on this port.
    The InterfaceDiscoveredAddress class encapsulates a required interfaceDiscoveredAddress resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'interfaceDiscoveredAddress'
    _SDM_ATT_MAP = {
        'Description': 'description',
        'IpAddress': 'ipAddress',
    }

    def __init__(self, parent):
        super(InterfaceDiscoveredAddress, self).__init__(parent)

    @property
    def Description(self):
        """
        Returns
        -------
        - str: Shows description of the interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])

    @property
    def IpAddress(self):
        """
        Returns
        -------
        - str: Shows IP address of the interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpAddress'])
