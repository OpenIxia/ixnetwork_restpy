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


class RBridges(Base):
    """The DCE ISIS Learned Information option fetches the learned information for the RBridges of a particular DCE ISIS Router.
    The RBridges class encapsulates a list of rBridges resources that are managed by the system.
    A list of resources can be retrieved from the server using the RBridges.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'rBridges'
    _SDM_ATT_MAP = {
        'Age': 'age',
        'EnableCommonMtId': 'enableCommonMtId',
        'ExtendedCircuitId': 'extendedCircuitId',
        'GraphId': 'graphId',
        'HostName': 'hostName',
        'LinkMetric': 'linkMetric',
        'MtId': 'mtId',
        'PrimaryFtag': 'primaryFtag',
        'Priority': 'priority',
        'Role': 'role',
        'SecondaryFtag': 'secondaryFtag',
        'SequenceNumber': 'sequenceNumber',
        'SwitchId': 'switchId',
        'SystemId': 'systemId',
    }

    def __init__(self, parent):
        super(RBridges, self).__init__(parent)

    @property
    def Age(self):
        """
        Returns
        -------
        - number: This indicates the age in time in seconds, since it was last refreshed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Age'])

    @property
    def EnableCommonMtId(self):
        """
        Returns
        -------
        - bool: If true, common Mt ld is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableCommonMtId'])

    @property
    def ExtendedCircuitId(self):
        """
        Returns
        -------
        - number: The hexadecimal format of the extended circuit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExtendedCircuitId'])

    @property
    def GraphId(self):
        """
        Returns
        -------
        - number: This indicates the Graph ID value if FTAG is present.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GraphId'])

    @property
    def HostName(self):
        """
        Returns
        -------
        - str: The host name as retrieved from the related packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HostName'])

    @property
    def LinkMetric(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkMetric'])

    @property
    def MtId(self):
        """
        Returns
        -------
        - number: This indicates the MT ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MtId'])

    @property
    def PrimaryFtag(self):
        """
        Returns
        -------
        - number: This indicates the Primary FTAG value if FTAG is present.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrimaryFtag'])

    @property
    def Priority(self):
        """
        Returns
        -------
        - number: This indicates the Broadcast Root Priority as advertised by this RBridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Priority'])

    @property
    def Role(self):
        """
        Returns
        -------
        - str: This indicates the role of the RBridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Role'])

    @property
    def SecondaryFtag(self):
        """
        Returns
        -------
        - number: This indicates the Secondary FTAG value if FTAG is present.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SecondaryFtag'])

    @property
    def SequenceNumber(self):
        """
        Returns
        -------
        - number: This indicates the sequence number of the LSP containing the route.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SequenceNumber'])

    @property
    def SwitchId(self):
        """
        Returns
        -------
        - number: This indicates the Switch ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SwitchId'])

    @property
    def SystemId(self):
        """
        Returns
        -------
        - str: This indicates the ISIS System ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SystemId'])

    def find(self, Age=None, EnableCommonMtId=None, ExtendedCircuitId=None, GraphId=None, HostName=None, LinkMetric=None, MtId=None, PrimaryFtag=None, Priority=None, Role=None, SecondaryFtag=None, SequenceNumber=None, SwitchId=None, SystemId=None):
        """Finds and retrieves rBridges resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve rBridges resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all rBridges resources from the server.

        Args
        ----
        - Age (number): This indicates the age in time in seconds, since it was last refreshed.
        - EnableCommonMtId (bool): If true, common Mt ld is enabled.
        - ExtendedCircuitId (number): The hexadecimal format of the extended circuit.
        - GraphId (number): This indicates the Graph ID value if FTAG is present.
        - HostName (str): The host name as retrieved from the related packets.
        - LinkMetric (number): NOT DEFINED
        - MtId (number): This indicates the MT ID.
        - PrimaryFtag (number): This indicates the Primary FTAG value if FTAG is present.
        - Priority (number): This indicates the Broadcast Root Priority as advertised by this RBridge.
        - Role (str): This indicates the role of the RBridge.
        - SecondaryFtag (number): This indicates the Secondary FTAG value if FTAG is present.
        - SequenceNumber (number): This indicates the sequence number of the LSP containing the route.
        - SwitchId (number): This indicates the Switch ID.
        - SystemId (str): This indicates the ISIS System ID.

        Returns
        -------
        - self: This instance with matching rBridges resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of rBridges data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the rBridges resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
