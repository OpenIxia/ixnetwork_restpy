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


class Router(Base):
    """This object is used to hold three lists associate with the router: route ranges, interfaces, and link state advertisements (LSA).
    The Router class encapsulates a list of router resources that are managed by the user.
    A list of resources can be retrieved from the server using the Router.find() method.
    The list can be managed by using the Router.add() and Router.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'router'
    _SDM_ATT_MAP = {
        'DiscardLearnedLsa': 'discardLearnedLsa',
        'Enabled': 'enabled',
        'GenerateRouterLsa': 'generateRouterLsa',
        'GracefulRestart': 'gracefulRestart',
        'InterFloodLsUpdateBurstGap': 'interFloodLsUpdateBurstGap',
        'LsaRefreshTime': 'lsaRefreshTime',
        'LsaRetransmitTime': 'lsaRetransmitTime',
        'MaxFloodLsUpdatesPerBurst': 'maxFloodLsUpdatesPerBurst',
        'RebuildAdjForLsdbChange': 'rebuildAdjForLsdbChange',
        'RouterId': 'routerId',
        'StrictLsaChecking': 'strictLsaChecking',
        'SupportForRfc3623': 'supportForRfc3623',
        'SupportReasonSoftReloadUpgrade': 'supportReasonSoftReloadUpgrade',
        'SupportReasonSoftRestart': 'supportReasonSoftRestart',
        'SupportReasonSwotchRedundantCntrlProcessor': 'supportReasonSwotchRedundantCntrlProcessor',
        'SupportReasonUnknown': 'supportReasonUnknown',
        'TrafficGroupId': 'trafficGroupId',
    }

    def __init__(self, parent):
        super(Router, self).__init__(parent)

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_7ae4a7abfbf3ddadcc20bd5c0e92cc02.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_7ae4a7abfbf3ddadcc20bd5c0e92cc02 import Interface
        return Interface(self)

    @property
    def RouteRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_2c9ff03ab2e44705c6af83f3c7265f53.RouteRange): An instance of the RouteRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_2c9ff03ab2e44705c6af83f3c7265f53 import RouteRange
        return RouteRange(self)

    @property
    def UserLsaGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.userlsagroup_7795cb447526ddc4b75100787366e015.UserLsaGroup): An instance of the UserLsaGroup class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.userlsagroup_7795cb447526ddc4b75100787366e015 import UserLsaGroup
        return UserLsaGroup(self)

    @property
    def DiscardLearnedLsa(self):
        """
        Returns
        -------
        - bool: When this option is true, this simulated OSPF router (RID) will not learn any LSAs from the neighbor. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP['DiscardLearnedLsa'])
    @DiscardLearnedLsa.setter
    def DiscardLearnedLsa(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DiscardLearnedLsa'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables or disables the use of this emulated OSPF router in the emulated OSPF network. (default = disabled)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def GenerateRouterLsa(self):
        """
        Returns
        -------
        - bool: If enabled, the router will automatically generate a router LSA including all of the interfaces added with the ospfRouter addInterface command. This should be turned off if you are building OSPF topologies with ospfUserLsa commands. (default = true)
        """
        return self._get_attribute(self._SDM_ATT_MAP['GenerateRouterLsa'])
    @GenerateRouterLsa.setter
    def GenerateRouterLsa(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GenerateRouterLsa'], value)

    @property
    def GracefulRestart(self):
        """
        Returns
        -------
        - bool: Enables the graceful restart Helper Mode function, per the IETF drafts, for the emulated OSPF router. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP['GracefulRestart'])
    @GracefulRestart.setter
    def GracefulRestart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GracefulRestart'], value)

    @property
    def InterFloodLsUpdateBurstGap(self):
        """
        Returns
        -------
        - number: The number of FloodlsUpdates sent between each Burst gap.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterFloodLsUpdateBurstGap'])
    @InterFloodLsUpdateBurstGap.setter
    def InterFloodLsUpdateBurstGap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterFloodLsUpdateBurstGap'], value)

    @property
    def LsaRefreshTime(self):
        """
        Returns
        -------
        - number: The time taken for LSA refresh.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LsaRefreshTime'])
    @LsaRefreshTime.setter
    def LsaRefreshTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LsaRefreshTime'], value)

    @property
    def LsaRetransmitTime(self):
        """
        Returns
        -------
        - number: The time taken to retransmit LSA.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LsaRetransmitTime'])
    @LsaRetransmitTime.setter
    def LsaRetransmitTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LsaRetransmitTime'], value)

    @property
    def MaxFloodLsUpdatesPerBurst(self):
        """
        Returns
        -------
        - number: The maximum number of FloodLsUpdates sent for each Burst.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxFloodLsUpdatesPerBurst'])
    @MaxFloodLsUpdatesPerBurst.setter
    def MaxFloodLsUpdatesPerBurst(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxFloodLsUpdatesPerBurst'], value)

    @property
    def RebuildAdjForLsdbChange(self):
        """
        Returns
        -------
        - bool: The enableGracefulRestart option must be true. If this option is true, Database Description (DBD) packets will have the R bit set - and the DBD packets will also have the LR (LSDB Resynchronization) bit set in the LLS Extended Options TLV. Out-of-Band Link State Database (OOB LSDB) resynchronization will be used instead of normal LSDB resynchronization, in order to preserve the OSPF adjacency with the neighbor router across OSPF Graceful Restart. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP['RebuildAdjForLsdbChange'])
    @RebuildAdjForLsdbChange.setter
    def RebuildAdjForLsdbChange(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RebuildAdjForLsdbChange'], value)

    @property
    def RouterId(self):
        """
        Returns
        -------
        - str: The router ID for this emulated OSPF router, in IPv4 format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouterId'])
    @RouterId.setter
    def RouterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouterId'], value)

    @property
    def StrictLsaChecking(self):
        """
        Returns
        -------
        - bool: If enabled, the OSPFv2 Restart Helper will terminate Graceful Restart when there are changes to an LSA that would be flooded to, or retransmitted by, the restarting router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StrictLsaChecking'])
    @StrictLsaChecking.setter
    def StrictLsaChecking(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StrictLsaChecking'], value)

    @property
    def SupportForRfc3623(self):
        """
        Returns
        -------
        - bool: Enables Graceful Restart Helper Mode per RFC 3623 on the emulated OSPF router. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportForRfc3623'])
    @SupportForRfc3623.setter
    def SupportForRfc3623(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportForRfc3623'], value)

    @property
    def SupportReasonSoftReloadUpgrade(self):
        """
        Returns
        -------
        - bool: If enabled, Graceful Restart Helper Mode will be supported on this emulated OSPFv2 Router when the restart reason is a Software Reload or Upgrade on the restarting router. (Planned outage) The default is checked/enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportReasonSoftReloadUpgrade'])
    @SupportReasonSoftReloadUpgrade.setter
    def SupportReasonSoftReloadUpgrade(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportReasonSoftReloadUpgrade'], value)

    @property
    def SupportReasonSoftRestart(self):
        """
        Returns
        -------
        - bool: If enabled, Graceful Restart Helper Mode will be supported on this emulated OSPFv2 Router when the restart reason is an OSPFv2 software restart (on the restarting router). (Planned or unplanned outage) The default is checked/enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportReasonSoftRestart'])
    @SupportReasonSoftRestart.setter
    def SupportReasonSoftRestart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportReasonSoftRestart'], value)

    @property
    def SupportReasonSwotchRedundantCntrlProcessor(self):
        """
        Returns
        -------
        - bool: If enabled, Graceful Restart Helper Mode will be supported on this emulated OSPFv2 Router when the restart reason is a unplanned switchover to a redundant control processor on the restarting router. (Unplanned outage)
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportReasonSwotchRedundantCntrlProcessor'])
    @SupportReasonSwotchRedundantCntrlProcessor.setter
    def SupportReasonSwotchRedundantCntrlProcessor(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportReasonSwotchRedundantCntrlProcessor'], value)

    @property
    def SupportReasonUnknown(self):
        """
        Returns
        -------
        - bool: If enabled, Graceful Restart Helper Mode will be supported on this emulated OSPFv2 Router when the restart reason is unknown and unplanned. (Unplanned outage) The default is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportReasonUnknown'])
    @SupportReasonUnknown.setter
    def SupportReasonUnknown(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportReasonUnknown'], value)

    @property
    def TrafficGroupId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup): The name of the group to which this emulated OSPF router is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficGroupId'])
    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficGroupId'], value)

    def update(self, DiscardLearnedLsa=None, Enabled=None, GenerateRouterLsa=None, GracefulRestart=None, InterFloodLsUpdateBurstGap=None, LsaRefreshTime=None, LsaRetransmitTime=None, MaxFloodLsUpdatesPerBurst=None, RebuildAdjForLsdbChange=None, RouterId=None, StrictLsaChecking=None, SupportForRfc3623=None, SupportReasonSoftReloadUpgrade=None, SupportReasonSoftRestart=None, SupportReasonSwotchRedundantCntrlProcessor=None, SupportReasonUnknown=None, TrafficGroupId=None):
        """Updates router resource on the server.

        Args
        ----
        - DiscardLearnedLsa (bool): When this option is true, this simulated OSPF router (RID) will not learn any LSAs from the neighbor. (default = false)
        - Enabled (bool): Enables or disables the use of this emulated OSPF router in the emulated OSPF network. (default = disabled)
        - GenerateRouterLsa (bool): If enabled, the router will automatically generate a router LSA including all of the interfaces added with the ospfRouter addInterface command. This should be turned off if you are building OSPF topologies with ospfUserLsa commands. (default = true)
        - GracefulRestart (bool): Enables the graceful restart Helper Mode function, per the IETF drafts, for the emulated OSPF router. (default = false)
        - InterFloodLsUpdateBurstGap (number): The number of FloodlsUpdates sent between each Burst gap.
        - LsaRefreshTime (number): The time taken for LSA refresh.
        - LsaRetransmitTime (number): The time taken to retransmit LSA.
        - MaxFloodLsUpdatesPerBurst (number): The maximum number of FloodLsUpdates sent for each Burst.
        - RebuildAdjForLsdbChange (bool): The enableGracefulRestart option must be true. If this option is true, Database Description (DBD) packets will have the R bit set - and the DBD packets will also have the LR (LSDB Resynchronization) bit set in the LLS Extended Options TLV. Out-of-Band Link State Database (OOB LSDB) resynchronization will be used instead of normal LSDB resynchronization, in order to preserve the OSPF adjacency with the neighbor router across OSPF Graceful Restart. (default = false)
        - RouterId (str): The router ID for this emulated OSPF router, in IPv4 format.
        - StrictLsaChecking (bool): If enabled, the OSPFv2 Restart Helper will terminate Graceful Restart when there are changes to an LSA that would be flooded to, or retransmitted by, the restarting router.
        - SupportForRfc3623 (bool): Enables Graceful Restart Helper Mode per RFC 3623 on the emulated OSPF router. (default = false)
        - SupportReasonSoftReloadUpgrade (bool): If enabled, Graceful Restart Helper Mode will be supported on this emulated OSPFv2 Router when the restart reason is a Software Reload or Upgrade on the restarting router. (Planned outage) The default is checked/enabled.
        - SupportReasonSoftRestart (bool): If enabled, Graceful Restart Helper Mode will be supported on this emulated OSPFv2 Router when the restart reason is an OSPFv2 software restart (on the restarting router). (Planned or unplanned outage) The default is checked/enabled.
        - SupportReasonSwotchRedundantCntrlProcessor (bool): If enabled, Graceful Restart Helper Mode will be supported on this emulated OSPFv2 Router when the restart reason is a unplanned switchover to a redundant control processor on the restarting router. (Unplanned outage)
        - SupportReasonUnknown (bool): If enabled, Graceful Restart Helper Mode will be supported on this emulated OSPFv2 Router when the restart reason is unknown and unplanned. (Unplanned outage) The default is enabled.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this emulated OSPF router is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, DiscardLearnedLsa=None, Enabled=None, GenerateRouterLsa=None, GracefulRestart=None, InterFloodLsUpdateBurstGap=None, LsaRefreshTime=None, LsaRetransmitTime=None, MaxFloodLsUpdatesPerBurst=None, RebuildAdjForLsdbChange=None, RouterId=None, StrictLsaChecking=None, SupportForRfc3623=None, SupportReasonSoftReloadUpgrade=None, SupportReasonSoftRestart=None, SupportReasonSwotchRedundantCntrlProcessor=None, SupportReasonUnknown=None, TrafficGroupId=None):
        """Adds a new router resource on the server and adds it to the container.

        Args
        ----
        - DiscardLearnedLsa (bool): When this option is true, this simulated OSPF router (RID) will not learn any LSAs from the neighbor. (default = false)
        - Enabled (bool): Enables or disables the use of this emulated OSPF router in the emulated OSPF network. (default = disabled)
        - GenerateRouterLsa (bool): If enabled, the router will automatically generate a router LSA including all of the interfaces added with the ospfRouter addInterface command. This should be turned off if you are building OSPF topologies with ospfUserLsa commands. (default = true)
        - GracefulRestart (bool): Enables the graceful restart Helper Mode function, per the IETF drafts, for the emulated OSPF router. (default = false)
        - InterFloodLsUpdateBurstGap (number): The number of FloodlsUpdates sent between each Burst gap.
        - LsaRefreshTime (number): The time taken for LSA refresh.
        - LsaRetransmitTime (number): The time taken to retransmit LSA.
        - MaxFloodLsUpdatesPerBurst (number): The maximum number of FloodLsUpdates sent for each Burst.
        - RebuildAdjForLsdbChange (bool): The enableGracefulRestart option must be true. If this option is true, Database Description (DBD) packets will have the R bit set - and the DBD packets will also have the LR (LSDB Resynchronization) bit set in the LLS Extended Options TLV. Out-of-Band Link State Database (OOB LSDB) resynchronization will be used instead of normal LSDB resynchronization, in order to preserve the OSPF adjacency with the neighbor router across OSPF Graceful Restart. (default = false)
        - RouterId (str): The router ID for this emulated OSPF router, in IPv4 format.
        - StrictLsaChecking (bool): If enabled, the OSPFv2 Restart Helper will terminate Graceful Restart when there are changes to an LSA that would be flooded to, or retransmitted by, the restarting router.
        - SupportForRfc3623 (bool): Enables Graceful Restart Helper Mode per RFC 3623 on the emulated OSPF router. (default = false)
        - SupportReasonSoftReloadUpgrade (bool): If enabled, Graceful Restart Helper Mode will be supported on this emulated OSPFv2 Router when the restart reason is a Software Reload or Upgrade on the restarting router. (Planned outage) The default is checked/enabled.
        - SupportReasonSoftRestart (bool): If enabled, Graceful Restart Helper Mode will be supported on this emulated OSPFv2 Router when the restart reason is an OSPFv2 software restart (on the restarting router). (Planned or unplanned outage) The default is checked/enabled.
        - SupportReasonSwotchRedundantCntrlProcessor (bool): If enabled, Graceful Restart Helper Mode will be supported on this emulated OSPFv2 Router when the restart reason is a unplanned switchover to a redundant control processor on the restarting router. (Unplanned outage)
        - SupportReasonUnknown (bool): If enabled, Graceful Restart Helper Mode will be supported on this emulated OSPFv2 Router when the restart reason is unknown and unplanned. (Unplanned outage) The default is enabled.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this emulated OSPF router is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Returns
        -------
        - self: This instance with all currently retrieved router resources using find and the newly added router resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained router resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DiscardLearnedLsa=None, Enabled=None, GenerateRouterLsa=None, GracefulRestart=None, InterFloodLsUpdateBurstGap=None, LsaRefreshTime=None, LsaRetransmitTime=None, MaxFloodLsUpdatesPerBurst=None, RebuildAdjForLsdbChange=None, RouterId=None, StrictLsaChecking=None, SupportForRfc3623=None, SupportReasonSoftReloadUpgrade=None, SupportReasonSoftRestart=None, SupportReasonSwotchRedundantCntrlProcessor=None, SupportReasonUnknown=None, TrafficGroupId=None):
        """Finds and retrieves router resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve router resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all router resources from the server.

        Args
        ----
        - DiscardLearnedLsa (bool): When this option is true, this simulated OSPF router (RID) will not learn any LSAs from the neighbor. (default = false)
        - Enabled (bool): Enables or disables the use of this emulated OSPF router in the emulated OSPF network. (default = disabled)
        - GenerateRouterLsa (bool): If enabled, the router will automatically generate a router LSA including all of the interfaces added with the ospfRouter addInterface command. This should be turned off if you are building OSPF topologies with ospfUserLsa commands. (default = true)
        - GracefulRestart (bool): Enables the graceful restart Helper Mode function, per the IETF drafts, for the emulated OSPF router. (default = false)
        - InterFloodLsUpdateBurstGap (number): The number of FloodlsUpdates sent between each Burst gap.
        - LsaRefreshTime (number): The time taken for LSA refresh.
        - LsaRetransmitTime (number): The time taken to retransmit LSA.
        - MaxFloodLsUpdatesPerBurst (number): The maximum number of FloodLsUpdates sent for each Burst.
        - RebuildAdjForLsdbChange (bool): The enableGracefulRestart option must be true. If this option is true, Database Description (DBD) packets will have the R bit set - and the DBD packets will also have the LR (LSDB Resynchronization) bit set in the LLS Extended Options TLV. Out-of-Band Link State Database (OOB LSDB) resynchronization will be used instead of normal LSDB resynchronization, in order to preserve the OSPF adjacency with the neighbor router across OSPF Graceful Restart. (default = false)
        - RouterId (str): The router ID for this emulated OSPF router, in IPv4 format.
        - StrictLsaChecking (bool): If enabled, the OSPFv2 Restart Helper will terminate Graceful Restart when there are changes to an LSA that would be flooded to, or retransmitted by, the restarting router.
        - SupportForRfc3623 (bool): Enables Graceful Restart Helper Mode per RFC 3623 on the emulated OSPF router. (default = false)
        - SupportReasonSoftReloadUpgrade (bool): If enabled, Graceful Restart Helper Mode will be supported on this emulated OSPFv2 Router when the restart reason is a Software Reload or Upgrade on the restarting router. (Planned outage) The default is checked/enabled.
        - SupportReasonSoftRestart (bool): If enabled, Graceful Restart Helper Mode will be supported on this emulated OSPFv2 Router when the restart reason is an OSPFv2 software restart (on the restarting router). (Planned or unplanned outage) The default is checked/enabled.
        - SupportReasonSwotchRedundantCntrlProcessor (bool): If enabled, Graceful Restart Helper Mode will be supported on this emulated OSPFv2 Router when the restart reason is a unplanned switchover to a redundant control processor on the restarting router. (Unplanned outage)
        - SupportReasonUnknown (bool): If enabled, Graceful Restart Helper Mode will be supported on this emulated OSPFv2 Router when the restart reason is unknown and unplanned. (Unplanned outage) The default is enabled.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this emulated OSPF router is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Returns
        -------
        - self: This instance with matching router resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of router data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the router resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
