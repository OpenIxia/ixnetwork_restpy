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


class TopologyLearnedInfo(Base):
    """This object allows to configure the Topology Learned Information parameters.
    The TopologyLearnedInfo class encapsulates a list of topologyLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the TopologyLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'topologyLearnedInfo'
    _SDM_ATT_MAP = {
        'InDataPathId': 'inDataPathId',
        'InDataPathIdAshex': 'inDataPathIdAshex',
        'InIp': 'inIp',
        'InPortEthernetAddress': 'inPortEthernetAddress',
        'InPortName': 'inPortName',
        'InPortNumber': 'inPortNumber',
        'OutDataPathId': 'outDataPathId',
        'OutDataPathIdAsHex': 'outDataPathIdAsHex',
        'OutIp': 'outIp',
        'OutPortEthernetAddress': 'outPortEthernetAddress',
        'OutPortName': 'outPortName',
        'OutPortNumber': 'outPortNumber',
    }

    def __init__(self, parent):
        super(TopologyLearnedInfo, self).__init__(parent)

    @property
    def InDataPathId(self):
        """
        Returns
        -------
        - str: Indicates the Datapath Id of Datapath for LLDP Packet-In Port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InDataPathId'])

    @property
    def InDataPathIdAshex(self):
        """
        Returns
        -------
        - str: Indicates the Datapath Id, in hexadecimal format, of Datapath for LLDP Packet-In Port
        """
        return self._get_attribute(self._SDM_ATT_MAP['InDataPathIdAshex'])

    @property
    def InIp(self):
        """
        Returns
        -------
        - str: Indicates the IP Address of Datapath for LLDP Packet-In Port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InIp'])

    @property
    def InPortEthernetAddress(self):
        """
        Returns
        -------
        - str: Indicates the Ethernet Address for LLDP Packet-In Port
        """
        return self._get_attribute(self._SDM_ATT_MAP['InPortEthernetAddress'])

    @property
    def InPortName(self):
        """
        Returns
        -------
        - str: Indicates the Port Name for LLDP Packet-In Port
        """
        return self._get_attribute(self._SDM_ATT_MAP['InPortName'])

    @property
    def InPortNumber(self):
        """
        Returns
        -------
        - number: Indicates the Port Number for LLDP Packet-In Port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InPortNumber'])

    @property
    def OutDataPathId(self):
        """
        Returns
        -------
        - str: Indicates the Datapath Id of Datapath for LLDP Packet Out Port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutDataPathId'])

    @property
    def OutDataPathIdAsHex(self):
        """
        Returns
        -------
        - str: Indicates the Datapath Id, in hexadecimal format, of Datapath for LLDP Packet Out Port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutDataPathIdAsHex'])

    @property
    def OutIp(self):
        """
        Returns
        -------
        - str: Indicates the IP Address of Datapath for LLDP Packet Out Port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutIp'])

    @property
    def OutPortEthernetAddress(self):
        """
        Returns
        -------
        - str: Indicates the Ethernet Address for LLDP Packet Out Port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutPortEthernetAddress'])

    @property
    def OutPortName(self):
        """
        Returns
        -------
        - str: Indicates the Port Name for LLDP Packet Out Port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutPortName'])

    @property
    def OutPortNumber(self):
        """
        Returns
        -------
        - number: Indicates the Port Number for LLDP Packet Out Port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutPortNumber'])

    def find(self, InDataPathId=None, InDataPathIdAshex=None, InIp=None, InPortEthernetAddress=None, InPortName=None, InPortNumber=None, OutDataPathId=None, OutDataPathIdAsHex=None, OutIp=None, OutPortEthernetAddress=None, OutPortName=None, OutPortNumber=None):
        """Finds and retrieves topologyLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve topologyLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all topologyLearnedInfo resources from the server.

        Args
        ----
        - InDataPathId (str): Indicates the Datapath Id of Datapath for LLDP Packet-In Port.
        - InDataPathIdAshex (str): Indicates the Datapath Id, in hexadecimal format, of Datapath for LLDP Packet-In Port
        - InIp (str): Indicates the IP Address of Datapath for LLDP Packet-In Port.
        - InPortEthernetAddress (str): Indicates the Ethernet Address for LLDP Packet-In Port
        - InPortName (str): Indicates the Port Name for LLDP Packet-In Port
        - InPortNumber (number): Indicates the Port Number for LLDP Packet-In Port.
        - OutDataPathId (str): Indicates the Datapath Id of Datapath for LLDP Packet Out Port.
        - OutDataPathIdAsHex (str): Indicates the Datapath Id, in hexadecimal format, of Datapath for LLDP Packet Out Port.
        - OutIp (str): Indicates the IP Address of Datapath for LLDP Packet Out Port.
        - OutPortEthernetAddress (str): Indicates the Ethernet Address for LLDP Packet Out Port.
        - OutPortName (str): Indicates the Port Name for LLDP Packet Out Port.
        - OutPortNumber (number): Indicates the Port Number for LLDP Packet Out Port.

        Returns
        -------
        - self: This instance with matching topologyLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of topologyLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the topologyLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
