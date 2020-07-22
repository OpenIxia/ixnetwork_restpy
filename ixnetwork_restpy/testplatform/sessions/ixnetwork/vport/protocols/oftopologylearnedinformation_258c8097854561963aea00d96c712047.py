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


class OfTopologyLearnedInformation(Base):
    """This object allows to configure the OF Toplogy Learned Information parameters.
    The OfTopologyLearnedInformation class encapsulates a required ofTopologyLearnedInformation resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ofTopologyLearnedInformation'
    _SDM_ATT_MAP = {
        'EnableInstallLldpFlow': 'enableInstallLldpFlow',
        'EnableRefreshLldpLearnedInformation': 'enableRefreshLldpLearnedInformation',
        'IsOfTopologyLearnedInformationRefreshed': 'isOfTopologyLearnedInformationRefreshed',
        'LldpDestinationMac': 'lldpDestinationMac',
        'LldpResponseTimeOut': 'lldpResponseTimeOut',
    }

    def __init__(self, parent):
        super(OfTopologyLearnedInformation, self).__init__(parent)

    @property
    def TopologyLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.topologylearnedinfo_c88c6312d724f74dc23e3d2634e6484a.TopologyLearnedInfo): An instance of the TopologyLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.topologylearnedinfo_c88c6312d724f74dc23e3d2634e6484a import TopologyLearnedInfo
        return TopologyLearnedInfo(self)

    @property
    def EnableInstallLldpFlow(self):
        """
        Returns
        -------
        - bool: If true, Install Flow in Switch for LLDP Packets to explicitly send to Controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableInstallLldpFlow'])
    @EnableInstallLldpFlow.setter
    def EnableInstallLldpFlow(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableInstallLldpFlow'], value)

    @property
    def EnableRefreshLldpLearnedInformation(self):
        """
        Returns
        -------
        - bool: If true, the LLDP trigger configuration parameters are available.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableRefreshLldpLearnedInformation'])
    @EnableRefreshLldpLearnedInformation.setter
    def EnableRefreshLldpLearnedInformation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableRefreshLldpLearnedInformation'], value)

    @property
    def IsOfTopologyLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: If true, it denotes that the Topology Learned Info is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsOfTopologyLearnedInformationRefreshed'])

    @property
    def LldpDestinationMac(self):
        """
        Returns
        -------
        - str: Indicates the Destination MAC Address for LLDP PacketOut.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LldpDestinationMac'])
    @LldpDestinationMac.setter
    def LldpDestinationMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LldpDestinationMac'], value)

    @property
    def LldpResponseTimeOut(self):
        """
        Returns
        -------
        - number: Indicates the duration in milliseconds after which the trigger request times out if no Topology learned info response is received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LldpResponseTimeOut'])
    @LldpResponseTimeOut.setter
    def LldpResponseTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LldpResponseTimeOut'], value)

    def update(self, EnableInstallLldpFlow=None, EnableRefreshLldpLearnedInformation=None, LldpDestinationMac=None, LldpResponseTimeOut=None):
        """Updates ofTopologyLearnedInformation resource on the server.

        Args
        ----
        - EnableInstallLldpFlow (bool): If true, Install Flow in Switch for LLDP Packets to explicitly send to Controller.
        - EnableRefreshLldpLearnedInformation (bool): If true, the LLDP trigger configuration parameters are available.
        - LldpDestinationMac (str): Indicates the Destination MAC Address for LLDP PacketOut.
        - LldpResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no Topology learned info response is received.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def RefreshOfTopology(self):
        """Executes the refreshOfTopology operation on the server.

        Exec to refresh ofChannel topology.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshOfTopology', payload=payload, response_object=None)
