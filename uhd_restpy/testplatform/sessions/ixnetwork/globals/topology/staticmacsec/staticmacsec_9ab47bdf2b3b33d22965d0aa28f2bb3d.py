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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
from typing import List, Any, Union


class StaticMacsec(Base):
    """Static MACsec Port Specific Data
    The StaticMacsec class encapsulates a required staticMacsec resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'staticMacsec'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'KeyGenerationMode': 'keyGenerationMode',
        'Name': 'name',
        'RowNames': 'rowNames',
    }
    _SDM_ENUM_MAP = {
        'keyGenerationMode': ['staticKeyGenerationMode', 'dynamicKeyGenerationMode'],
    }

    def __init__(self, parent, list_op=False):
        super(StaticMacsec, self).__init__(parent, list_op)

    @property
    def StartRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.startrate.startrate_2bc83a4fb9730935e8259bdb40af2dc0.StartRate): An instance of the StartRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.startrate.startrate_2bc83a4fb9730935e8259bdb40af2dc0 import StartRate
        if self._properties.get('StartRate', None) is not None:
            return self._properties.get('StartRate')
        else:
            return StartRate(self)._select()

    @property
    def StopRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.stoprate.stoprate_4ea9a1b38960d2b21012777131469a04.StopRate): An instance of the StopRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.stoprate.stoprate_4ea9a1b38960d2b21012777131469a04 import StopRate
        if self._properties.get('StopRate', None) is not None:
            return self._properties.get('StopRate')
        else:
            return StopRate(self)._select()

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def KeyGenerationMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(staticKeyGenerationMode | dynamicKeyGenerationMode): Encryption keys will be informed by MKA or configured statically in MACsec.
        """
        return self._get_attribute(self._SDM_ATT_MAP['KeyGenerationMode'])

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def RowNames(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Name of rows
        """
        return self._get_attribute(self._SDM_ATT_MAP['RowNames'])

    def update(self, Name=None):
        # type: (str) -> StaticMacsec
        """Updates staticMacsec resource on the server.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
