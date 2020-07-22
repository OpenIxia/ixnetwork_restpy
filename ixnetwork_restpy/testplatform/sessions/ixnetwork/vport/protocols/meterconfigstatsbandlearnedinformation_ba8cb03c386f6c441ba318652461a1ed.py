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


class MeterConfigStatsBandLearnedInformation(Base):
    """NOT DEFINED
    The MeterConfigStatsBandLearnedInformation class encapsulates a list of meterConfigStatsBandLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the MeterConfigStatsBandLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'meterConfigStatsBandLearnedInformation'
    _SDM_ATT_MAP = {
        'BurstSize': 'burstSize',
        'DataPathId': 'dataPathId',
        'DataPathIdAsHex': 'dataPathIdAsHex',
        'Experimenter': 'experimenter',
        'LocalIp': 'localIp',
        'MeterId': 'meterId',
        'PrecedenceLevel': 'precedenceLevel',
        'Rate': 'rate',
        'RemoteIp': 'remoteIp',
        'Type': 'type',
    }

    def __init__(self, parent):
        super(MeterConfigStatsBandLearnedInformation, self).__init__(parent)

    @property
    def BurstSize(self):
        """
        Returns
        -------
        - number: Specifies the Burst Size
        """
        return self._get_attribute(self._SDM_ATT_MAP['BurstSize'])

    @property
    def DataPathId(self):
        """
        Returns
        -------
        - number: The Data Path identifier of the OpenFlow Controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathId'])

    @property
    def DataPathIdAsHex(self):
        """
        Returns
        -------
        - str: The Data Path identifier of the OpenFlow Controller in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathIdAsHex'])

    @property
    def Experimenter(self):
        """
        Returns
        -------
        - str: Specifies the Experimenter Value
        """
        return self._get_attribute(self._SDM_ATT_MAP['Experimenter'])

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - str: Indicates the local IP of the Controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIp'])

    @property
    def MeterId(self):
        """
        Returns
        -------
        - number: Specifies Meter Id
        """
        return self._get_attribute(self._SDM_ATT_MAP['MeterId'])

    @property
    def PrecedenceLevel(self):
        """
        Returns
        -------
        - str: Specifies the Precedence Level Value
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrecedenceLevel'])

    @property
    def Rate(self):
        """
        Returns
        -------
        - number: Specifies the rate
        """
        return self._get_attribute(self._SDM_ATT_MAP['Rate'])

    @property
    def RemoteIp(self):
        """
        Returns
        -------
        - str: The Remote IP address of the selected interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteIp'])

    @property
    def Type(self):
        """
        Returns
        -------
        - str: Specifies the Band Type
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])

    def find(self, BurstSize=None, DataPathId=None, DataPathIdAsHex=None, Experimenter=None, LocalIp=None, MeterId=None, PrecedenceLevel=None, Rate=None, RemoteIp=None, Type=None):
        """Finds and retrieves meterConfigStatsBandLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve meterConfigStatsBandLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all meterConfigStatsBandLearnedInformation resources from the server.

        Args
        ----
        - BurstSize (number): Specifies the Burst Size
        - DataPathId (number): The Data Path identifier of the OpenFlow Controller.
        - DataPathIdAsHex (str): The Data Path identifier of the OpenFlow Controller in hexadecimal format.
        - Experimenter (str): Specifies the Experimenter Value
        - LocalIp (str): Indicates the local IP of the Controller.
        - MeterId (number): Specifies Meter Id
        - PrecedenceLevel (str): Specifies the Precedence Level Value
        - Rate (number): Specifies the rate
        - RemoteIp (str): The Remote IP address of the selected interface.
        - Type (str): Specifies the Band Type

        Returns
        -------
        - self: This instance with matching meterConfigStatsBandLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of meterConfigStatsBandLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the meterConfigStatsBandLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
