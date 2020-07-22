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


class SpbmNodeTopologyRange(Base):
    """The SPBM Node Topology Range.
    The SpbmNodeTopologyRange class encapsulates a list of spbmNodeTopologyRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the SpbmNodeTopologyRange.find() method.
    The list can be managed by using the SpbmNodeTopologyRange.add() and SpbmNodeTopologyRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'spbmNodeTopologyRange'
    _SDM_ATT_MAP = {
        'BridgePriority': 'bridgePriority',
        'CistExternalRootCost': 'cistExternalRootCost',
        'CistRootIdentifier': 'cistRootIdentifier',
        'EnableVbit': 'enableVbit',
        'Enabled': 'enabled',
        'InterNodeLinkMetricIncrement': 'interNodeLinkMetricIncrement',
        'InterNodeSpSourceIdIncrement': 'interNodeSpSourceIdIncrement',
        'LinkMetric': 'linkMetric',
        'NoOfPorts': 'noOfPorts',
        'PortIdentifier': 'portIdentifier',
        'SpSourceId': 'spSourceId',
    }

    def __init__(self, parent):
        super(SpbmNodeTopologyRange, self).__init__(parent)

    @property
    def SpbmNodeBaseVidRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbmnodebasevidrange_81d2c633816492894c7a12f8e3079130.SpbmNodeBaseVidRange): An instance of the SpbmNodeBaseVidRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbmnodebasevidrange_81d2c633816492894c7a12f8e3079130 import SpbmNodeBaseVidRange
        return SpbmNodeBaseVidRange(self)

    @property
    def BridgePriority(self):
        """
        Returns
        -------
        - number: The value assigned as the priority of the bridge. The default value is 32768. The maximum value is 65535. The minimum value is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BridgePriority'])
    @BridgePriority.setter
    def BridgePriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BridgePriority'], value)

    @property
    def CistExternalRootCost(self):
        """
        Returns
        -------
        - number: The Common and Internal Spanning Tree calculated cost to reach the root bridge from the bridge where the command is entered.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CistExternalRootCost'])
    @CistExternalRootCost.setter
    def CistExternalRootCost(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CistExternalRootCost'], value)

    @property
    def CistRootIdentifier(self):
        """
        Returns
        -------
        - str: Bridge identifier of the CIST root bridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CistRootIdentifier'])
    @CistRootIdentifier.setter
    def CistRootIdentifier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CistRootIdentifier'], value)

    @property
    def EnableVbit(self):
        """
        Returns
        -------
        - bool: If true, activates the V bit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableVbit'])
    @EnableVbit.setter
    def EnableVbit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableVbit'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, the topology range will be part of the simulated network.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def InterNodeLinkMetricIncrement(self):
        """
        Returns
        -------
        - number: The incremental value of the Inter Node link metric.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterNodeLinkMetricIncrement'])
    @InterNodeLinkMetricIncrement.setter
    def InterNodeLinkMetricIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterNodeLinkMetricIncrement'], value)

    @property
    def InterNodeSpSourceIdIncrement(self):
        """
        Returns
        -------
        - number: The inter node Shortest Path source identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterNodeSpSourceIdIncrement'])
    @InterNodeSpSourceIdIncrement.setter
    def InterNodeSpSourceIdIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterNodeSpSourceIdIncrement'], value)

    @property
    def LinkMetric(self):
        """
        Returns
        -------
        - number: The LSP metric related to the network. The default value is 10. The maximum value is 16777215. The minimum value is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkMetric'])
    @LinkMetric.setter
    def LinkMetric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkMetric'], value)

    @property
    def NoOfPorts(self):
        """
        Returns
        -------
        - number: The number of configured ports for the protocol. The default value is 1. The maximum value is 255. The minimum value is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfPorts'])
    @NoOfPorts.setter
    def NoOfPorts(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfPorts'], value)

    @property
    def PortIdentifier(self):
        """
        Returns
        -------
        - number: The identifier for the configured port. The default value is 1. The maximum value is 65535. The minimum value is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortIdentifier'])
    @PortIdentifier.setter
    def PortIdentifier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortIdentifier'], value)

    @property
    def SpSourceId(self):
        """
        Returns
        -------
        - number: The Shortest Path source identifier. The default value is 0. The maximum value is 1048575. The minimum value is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SpSourceId'])
    @SpSourceId.setter
    def SpSourceId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SpSourceId'], value)

    def update(self, BridgePriority=None, CistExternalRootCost=None, CistRootIdentifier=None, EnableVbit=None, Enabled=None, InterNodeLinkMetricIncrement=None, InterNodeSpSourceIdIncrement=None, LinkMetric=None, NoOfPorts=None, PortIdentifier=None, SpSourceId=None):
        """Updates spbmNodeTopologyRange resource on the server.

        Args
        ----
        - BridgePriority (number): The value assigned as the priority of the bridge. The default value is 32768. The maximum value is 65535. The minimum value is 0.
        - CistExternalRootCost (number): The Common and Internal Spanning Tree calculated cost to reach the root bridge from the bridge where the command is entered.
        - CistRootIdentifier (str): Bridge identifier of the CIST root bridge.
        - EnableVbit (bool): If true, activates the V bit.
        - Enabled (bool): If true, the topology range will be part of the simulated network.
        - InterNodeLinkMetricIncrement (number): The incremental value of the Inter Node link metric.
        - InterNodeSpSourceIdIncrement (number): The inter node Shortest Path source identifier.
        - LinkMetric (number): The LSP metric related to the network. The default value is 10. The maximum value is 16777215. The minimum value is 0.
        - NoOfPorts (number): The number of configured ports for the protocol. The default value is 1. The maximum value is 255. The minimum value is 0.
        - PortIdentifier (number): The identifier for the configured port. The default value is 1. The maximum value is 65535. The minimum value is 0.
        - SpSourceId (number): The Shortest Path source identifier. The default value is 0. The maximum value is 1048575. The minimum value is 0.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, BridgePriority=None, CistExternalRootCost=None, CistRootIdentifier=None, EnableVbit=None, Enabled=None, InterNodeLinkMetricIncrement=None, InterNodeSpSourceIdIncrement=None, LinkMetric=None, NoOfPorts=None, PortIdentifier=None, SpSourceId=None):
        """Adds a new spbmNodeTopologyRange resource on the server and adds it to the container.

        Args
        ----
        - BridgePriority (number): The value assigned as the priority of the bridge. The default value is 32768. The maximum value is 65535. The minimum value is 0.
        - CistExternalRootCost (number): The Common and Internal Spanning Tree calculated cost to reach the root bridge from the bridge where the command is entered.
        - CistRootIdentifier (str): Bridge identifier of the CIST root bridge.
        - EnableVbit (bool): If true, activates the V bit.
        - Enabled (bool): If true, the topology range will be part of the simulated network.
        - InterNodeLinkMetricIncrement (number): The incremental value of the Inter Node link metric.
        - InterNodeSpSourceIdIncrement (number): The inter node Shortest Path source identifier.
        - LinkMetric (number): The LSP metric related to the network. The default value is 10. The maximum value is 16777215. The minimum value is 0.
        - NoOfPorts (number): The number of configured ports for the protocol. The default value is 1. The maximum value is 255. The minimum value is 0.
        - PortIdentifier (number): The identifier for the configured port. The default value is 1. The maximum value is 65535. The minimum value is 0.
        - SpSourceId (number): The Shortest Path source identifier. The default value is 0. The maximum value is 1048575. The minimum value is 0.

        Returns
        -------
        - self: This instance with all currently retrieved spbmNodeTopologyRange resources using find and the newly added spbmNodeTopologyRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained spbmNodeTopologyRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, BridgePriority=None, CistExternalRootCost=None, CistRootIdentifier=None, EnableVbit=None, Enabled=None, InterNodeLinkMetricIncrement=None, InterNodeSpSourceIdIncrement=None, LinkMetric=None, NoOfPorts=None, PortIdentifier=None, SpSourceId=None):
        """Finds and retrieves spbmNodeTopologyRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve spbmNodeTopologyRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all spbmNodeTopologyRange resources from the server.

        Args
        ----
        - BridgePriority (number): The value assigned as the priority of the bridge. The default value is 32768. The maximum value is 65535. The minimum value is 0.
        - CistExternalRootCost (number): The Common and Internal Spanning Tree calculated cost to reach the root bridge from the bridge where the command is entered.
        - CistRootIdentifier (str): Bridge identifier of the CIST root bridge.
        - EnableVbit (bool): If true, activates the V bit.
        - Enabled (bool): If true, the topology range will be part of the simulated network.
        - InterNodeLinkMetricIncrement (number): The incremental value of the Inter Node link metric.
        - InterNodeSpSourceIdIncrement (number): The inter node Shortest Path source identifier.
        - LinkMetric (number): The LSP metric related to the network. The default value is 10. The maximum value is 16777215. The minimum value is 0.
        - NoOfPorts (number): The number of configured ports for the protocol. The default value is 1. The maximum value is 255. The minimum value is 0.
        - PortIdentifier (number): The identifier for the configured port. The default value is 1. The maximum value is 65535. The minimum value is 0.
        - SpSourceId (number): The Shortest Path source identifier. The default value is 0. The maximum value is 1048575. The minimum value is 0.

        Returns
        -------
        - self: This instance with matching spbmNodeTopologyRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of spbmNodeTopologyRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the spbmNodeTopologyRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
