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


class SpbRbridges(Base):
    """The DCE ISIS Learned Information option fetches the learned information for the RBridges of a particular DCE ISIS Router on SPB topology range.
    The SpbRbridges class encapsulates a list of spbRbridges resources that are managed by the system.
    A list of resources can be retrieved from the server using the SpbRbridges.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'spbRbridges'
    _SDM_ATT_MAP = {
        'Age': 'age',
        'AuxillaryMcidConfigName': 'auxillaryMcidConfigName',
        'BaseVid': 'baseVid',
        'BridgeMacAddress': 'bridgeMacAddress',
        'BridgePriority': 'bridgePriority',
        'EctAlgorithm': 'ectAlgorithm',
        'HostName': 'hostName',
        'IsId': 'isId',
        'LinkMetric': 'linkMetric',
        'MBit': 'mBit',
        'McidConfigName': 'mcidConfigName',
        'RBit': 'rBit',
        'SequenceNumber': 'sequenceNumber',
        'SystemId': 'systemId',
        'TBit': 'tBit',
        'UseFlagBit': 'useFlagBit',
    }

    def __init__(self, parent):
        super(SpbRbridges, self).__init__(parent)

    @property
    def Age(self):
        """
        Returns
        -------
        - number: (read only) This indicates the age in time in seconds, since it was last refreshed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Age'])

    @property
    def AuxillaryMcidConfigName(self):
        """
        Returns
        -------
        - str: The auxiliary MCID configuration name.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AuxillaryMcidConfigName'])

    @property
    def BaseVid(self):
        """
        Returns
        -------
        - number: The Base VLAN ID. The default value is 1. The maximum value is 4095. The minimum value is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BaseVid'])

    @property
    def BridgeMacAddress(self):
        """
        Returns
        -------
        - str: The 6-byte MAC address assigned to this bridge. Part of the bridge identifier (bridge ID).
        """
        return self._get_attribute(self._SDM_ATT_MAP['BridgeMacAddress'])

    @property
    def BridgePriority(self):
        """
        Returns
        -------
        - number: The Bridge Priority for this bridge.The valid range is 0 to 61,440, in multiples of 4,096. (default = 32,768).
        """
        return self._get_attribute(self._SDM_ATT_MAP['BridgePriority'])

    @property
    def EctAlgorithm(self):
        """
        Returns
        -------
        - number: The SPB Equal Cost Tree (ECT) algorithm. The default algorithm is 01-80-C2-01.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EctAlgorithm'])

    @property
    def HostName(self):
        """
        Returns
        -------
        - str: (read only) The host name as retrieved from the related packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HostName'])

    @property
    def IsId(self):
        """
        Returns
        -------
        - number: The I-component service identifier. The maximum value is 16777215. The minimum value is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsId'])

    @property
    def LinkMetric(self):
        """
        Returns
        -------
        - number: The LSP metric related to the network. The default value is 10. The maximum value is 16777215. The minimum value is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkMetric'])

    @property
    def MBit(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MBit'])

    @property
    def McidConfigName(self):
        """
        Returns
        -------
        - str: The MCID configuration name.
        """
        return self._get_attribute(self._SDM_ATT_MAP['McidConfigName'])

    @property
    def RBit(self):
        """
        Returns
        -------
        - bool: The Restart State bit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RBit'])

    @property
    def SequenceNumber(self):
        """
        Returns
        -------
        - number: (read only) This indicates the sequence number of the LSP containing the route.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SequenceNumber'])

    @property
    def SystemId(self):
        """
        Returns
        -------
        - str: (read only) This indicates the ISIS System ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SystemId'])

    @property
    def TBit(self):
        """
        Returns
        -------
        - bool: The external route tag bit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TBit'])

    @property
    def UseFlagBit(self):
        """
        Returns
        -------
        - bool: Allows to use flag bit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseFlagBit'])

    def find(self, Age=None, AuxillaryMcidConfigName=None, BaseVid=None, BridgeMacAddress=None, BridgePriority=None, EctAlgorithm=None, HostName=None, IsId=None, LinkMetric=None, MBit=None, McidConfigName=None, RBit=None, SequenceNumber=None, SystemId=None, TBit=None, UseFlagBit=None):
        """Finds and retrieves spbRbridges resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve spbRbridges resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all spbRbridges resources from the server.

        Args
        ----
        - Age (number): (read only) This indicates the age in time in seconds, since it was last refreshed.
        - AuxillaryMcidConfigName (str): The auxiliary MCID configuration name.
        - BaseVid (number): The Base VLAN ID. The default value is 1. The maximum value is 4095. The minimum value is 0.
        - BridgeMacAddress (str): The 6-byte MAC address assigned to this bridge. Part of the bridge identifier (bridge ID).
        - BridgePriority (number): The Bridge Priority for this bridge.The valid range is 0 to 61,440, in multiples of 4,096. (default = 32,768).
        - EctAlgorithm (number): The SPB Equal Cost Tree (ECT) algorithm. The default algorithm is 01-80-C2-01.
        - HostName (str): (read only) The host name as retrieved from the related packets.
        - IsId (number): The I-component service identifier. The maximum value is 16777215. The minimum value is 0.
        - LinkMetric (number): The LSP metric related to the network. The default value is 10. The maximum value is 16777215. The minimum value is 0.
        - MBit (bool): NOT DEFINED
        - McidConfigName (str): The MCID configuration name.
        - RBit (bool): The Restart State bit.
        - SequenceNumber (number): (read only) This indicates the sequence number of the LSP containing the route.
        - SystemId (str): (read only) This indicates the ISIS System ID.
        - TBit (bool): The external route tag bit.
        - UseFlagBit (bool): Allows to use flag bit.

        Returns
        -------
        - self: This instance with matching spbRbridges resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of spbRbridges data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the spbRbridges resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
