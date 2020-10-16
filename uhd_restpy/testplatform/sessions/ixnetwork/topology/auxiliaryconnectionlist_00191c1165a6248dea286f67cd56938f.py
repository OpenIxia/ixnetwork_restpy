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


class AuxiliaryConnectionList(Base):
    """Openflow Switch Auxiliary Connections level Configuration
    The AuxiliaryConnectionList class encapsulates a list of auxiliaryConnectionList resources that are managed by the system.
    A list of resources can be retrieved from the server using the AuxiliaryConnectionList.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'auxiliaryConnectionList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AuxId': 'auxId',
        'ChannelName': 'channelName',
        'ConnectionType': 'connectionType',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'Name': 'name',
        'UDPSrcPortNum': 'uDPSrcPortNum',
    }

    def __init__(self, parent):
        super(AuxiliaryConnectionList, self).__init__(parent)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def AuxId(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Specify the Auxiliary Id, {0 - 255}
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AuxId']))

    @property
    def ChannelName(self):
        """
        Returns
        -------
        - str: Parent Channel Name
        """
        return self._get_attribute(self._SDM_ATT_MAP['ChannelName'])

    @property
    def ConnectionType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): The type of connection used for the Interface. Options include: 1) TCP 2) TLS 3) UDP
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConnectionType']))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def UDPSrcPortNum(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): UDP Source Port Number
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UDPSrcPortNum']))

    def update(self, Name=None):
        """Updates auxiliaryConnectionList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, ChannelName=None, Count=None, DescriptiveName=None, Name=None):
        """Finds and retrieves auxiliaryConnectionList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve auxiliaryConnectionList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all auxiliaryConnectionList resources from the server.

        Args
        ----
        - ChannelName (str): Parent Channel Name
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching auxiliaryConnectionList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of auxiliaryConnectionList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the auxiliaryConnectionList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, AuxId=None, ConnectionType=None, UDPSrcPortNum=None):
        """Base class infrastructure that gets a list of auxiliaryConnectionList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AuxId (str): optional regex of auxId
        - ConnectionType (str): optional regex of connectionType
        - UDPSrcPortNum (str): optional regex of uDPSrcPortNum

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
