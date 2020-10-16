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


class ConfigMANamesParams(Base):
    """Import IPv6 routes from standard route file. Supported format - Cisco IOS, Juniper JUNOS, Classis Ixia (.csv) and standard CSV.
    The ConfigMANamesParams class encapsulates a required configMANamesParams resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'configMANamesParams'
    _SDM_ATT_MAP = {
        'IncrementMaName': 'incrementMaName',
        'MaName': 'maName',
        'SmaFormat': 'smaFormat',
    }

    def __init__(self, parent):
        super(ConfigMANamesParams, self).__init__(parent)

    @property
    def IncrementMaName(self):
        """
        Returns
        -------
        - bool: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementMaName'])
    @IncrementMaName.setter
    def IncrementMaName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrementMaName'], value)

    @property
    def MaName(self):
        """
        Returns
        -------
        - str: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaName'])
    @MaName.setter
    def MaName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaName'], value)

    @property
    def SmaFormat(self):
        """
        Returns
        -------
        - str(megIdFormatTypeIccBasedFormat | megIdFormatTypePrimaryVid | megIdFormatTypeCharStr | megIdFormatTypeTwoOctetInt | megIdFormatTypeRfc2685VpnId): Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['SmaFormat'])
    @SmaFormat.setter
    def SmaFormat(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SmaFormat'], value)

    def update(self, IncrementMaName=None, MaName=None, SmaFormat=None):
        """Updates configMANamesParams resource on the server.

        Args
        ----
        - IncrementMaName (bool): Import only the best routes (provided route file has this information).
        - MaName (str): Import only the best routes (provided route file has this information).
        - SmaFormat (str(megIdFormatTypeIccBasedFormat | megIdFormatTypePrimaryVid | megIdFormatTypeCharStr | megIdFormatTypeTwoOctetInt | megIdFormatTypeRfc2685VpnId)): Import only the best routes (provided route file has this information).

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def ConfigMANames(self):
        """Executes the configMANames operation on the server.

        Import IPv6 routes from standard route file. Supported format - Cisco IOS, Juniper JUNOS, Classis Ixia (.csv) and standard CSV.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('configMANames', payload=payload, response_object=None)
