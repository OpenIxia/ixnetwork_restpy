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


class Bridge(Base):
    """This object represents a simulated STP bridge which holds a list of interfaces associated with the simulated bridge.
    The Bridge class encapsulates a list of bridge resources that are managed by the user.
    A list of resources can be retrieved from the server using the Bridge.find() method.
    The list can be managed by using the Bridge.add() and Bridge.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'bridge'
    _SDM_ATT_MAP = {
        'AutoPickBridgeMac': 'autoPickBridgeMac',
        'BridgeMac': 'bridgeMac',
        'BridgePriority': 'bridgePriority',
        'BridgeSystemId': 'bridgeSystemId',
        'BridgeType': 'bridgeType',
        'CistRegRootCost': 'cistRegRootCost',
        'CistRegRootMac': 'cistRegRootMac',
        'CistRegRootPriority': 'cistRegRootPriority',
        'CistRemainingHop': 'cistRemainingHop',
        'Enabled': 'enabled',
        'ExternalRootCost': 'externalRootCost',
        'ExternalRootMac': 'externalRootMac',
        'ExternalRootPriority': 'externalRootPriority',
        'ForwardDelay': 'forwardDelay',
        'HelloInterval': 'helloInterval',
        'IsRefreshComplete': 'isRefreshComplete',
        'MaxAge': 'maxAge',
        'MessageAge': 'messageAge',
        'Mode': 'mode',
        'MstcName': 'mstcName',
        'MstcRevisionNumber': 'mstcRevisionNumber',
        'PortPriority': 'portPriority',
        'PvstpMode': 'pvstpMode',
        'RootCost': 'rootCost',
        'RootMac': 'rootMac',
        'RootPriority': 'rootPriority',
        'RootSystemId': 'rootSystemId',
        'UpdateRequired': 'updateRequired',
        'VlanPortPriority': 'vlanPortPriority',
        'VlanRootMac': 'vlanRootMac',
        'VlanRootPathCost': 'vlanRootPathCost',
        'VlanRootPriority': 'vlanRootPriority',
    }

    def __init__(self, parent):
        super(Bridge, self).__init__(parent)

    @property
    def Cist(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cist_5125ef3dd560263f3c06cf84445f600c.Cist): An instance of the Cist class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cist_5125ef3dd560263f3c06cf84445f600c import Cist
        return Cist(self)._select()

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_d26d04ed3c9249181ab014c22140816e.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_d26d04ed3c9249181ab014c22140816e import Interface
        return Interface(self)

    @property
    def LearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinfo_d1b9dcdde0ad5595e3e505fa55ba6552.LearnedInfo): An instance of the LearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinfo_d1b9dcdde0ad5595e3e505fa55ba6552 import LearnedInfo
        return LearnedInfo(self)._select()

    @property
    def Msti(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.msti_1a0d87ce8de6a704d21d743b57844116.Msti): An instance of the Msti class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.msti_1a0d87ce8de6a704d21d743b57844116 import Msti
        return Msti(self)

    @property
    def Vlan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vlan_346cf815cbe7a05d0d162263098c4b42.Vlan): An instance of the Vlan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vlan_346cf815cbe7a05d0d162263098c4b42 import Vlan
        return Vlan(self)

    @property
    def AutoPickBridgeMac(self):
        """
        Returns
        -------
        - bool: If enabled, the MAC address for one of the STP interfaces will be automatically assigned as the MAC address for this bridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoPickBridgeMac'])
    @AutoPickBridgeMac.setter
    def AutoPickBridgeMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AutoPickBridgeMac'], value)

    @property
    def BridgeMac(self):
        """
        Returns
        -------
        - str: The 6-byte MAC address assigned to this bridge. Part of the bridge identifier (bridge ID).
        """
        return self._get_attribute(self._SDM_ATT_MAP['BridgeMac'])
    @BridgeMac.setter
    def BridgeMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BridgeMac'], value)

    @property
    def BridgePriority(self):
        """
        Returns
        -------
        - str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440): The Bridge Priority for this bridge.The valid range is 0 to 61,440, in multiples of 4,096. (default = 32,768)
        """
        return self._get_attribute(self._SDM_ATT_MAP['BridgePriority'])
    @BridgePriority.setter
    def BridgePriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BridgePriority'], value)

    @property
    def BridgeSystemId(self):
        """
        Returns
        -------
        - number: The System ID for the bridge. The valid range is 0 to 4,095. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['BridgeSystemId'])
    @BridgeSystemId.setter
    def BridgeSystemId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BridgeSystemId'], value)

    @property
    def BridgeType(self):
        """
        Returns
        -------
        - str(bridges | providerBridges): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['BridgeType'])
    @BridgeType.setter
    def BridgeType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BridgeType'], value)

    @property
    def CistRegRootCost(self):
        """
        Returns
        -------
        - number: (For use with PVST+ and RPVST+ only) The Common Spanning Tree (CST) root path cost. The valid range is 0 to 4294967295. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['CistRegRootCost'])
    @CistRegRootCost.setter
    def CistRegRootCost(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CistRegRootCost'], value)

    @property
    def CistRegRootMac(self):
        """
        Returns
        -------
        - str: (For use with PVST+ and RPVST+ only) The Common Spanning Tree (CST) 6-byte root MAC address. (default = 00:00:00:00:00:00)
        """
        return self._get_attribute(self._SDM_ATT_MAP['CistRegRootMac'])
    @CistRegRootMac.setter
    def CistRegRootMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CistRegRootMac'], value)

    @property
    def CistRegRootPriority(self):
        """
        Returns
        -------
        - str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440): (For use with PVST+ and RPVST+ only) The Common Spanning Tree (CST) priority of the root. The valid range is 0 to 61,440, in increments of 4,096. (default = 32,768)
        """
        return self._get_attribute(self._SDM_ATT_MAP['CistRegRootPriority'])
    @CistRegRootPriority.setter
    def CistRegRootPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CistRegRootPriority'], value)

    @property
    def CistRemainingHop(self):
        """
        Returns
        -------
        - number: (For use with MSTP only) The number of additional bridge-to-bridge hops that will be allowed for the MSTP BPDUs. The root sets the maximum hop count, and each subsequent bridge decrements this value by 1. The valid range is 1 to 255. (default = 20)
        """
        return self._get_attribute(self._SDM_ATT_MAP['CistRemainingHop'])
    @CistRemainingHop.setter
    def CistRemainingHop(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CistRemainingHop'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables or disables the bridge's simulation. (default = disabled)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def ExternalRootCost(self):
        """
        Returns
        -------
        - number: Common and Internal Spanning Tree (CIST) external root path cost. A 4-byte unsigned integer. The default is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExternalRootCost'])
    @ExternalRootCost.setter
    def ExternalRootCost(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExternalRootCost'], value)

    @property
    def ExternalRootMac(self):
        """
        Returns
        -------
        - str: Common and Internal Spanning Tree (CIST) external root MAC address. A 6-byte MAC address.The default is 00 00 00 00 00 00.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExternalRootMac'])
    @ExternalRootMac.setter
    def ExternalRootMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExternalRootMac'], value)

    @property
    def ExternalRootPriority(self):
        """
        Returns
        -------
        - str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440): (For use with MSTP only) The priority value of the root bridge for the CIST/MSTP region (external). Part of the CIST External Root Identifier. The valid range is 0 to 61,440, in increments of 4096. (default = 32,768)
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExternalRootPriority'])
    @ExternalRootPriority.setter
    def ExternalRootPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExternalRootPriority'], value)

    @property
    def ForwardDelay(self):
        """
        Returns
        -------
        - number: The delay used for a port's change to the Forwarding state. (in milliseconds) The valid range is 500 msec to 255 sec. (default = 15,000 msec (15 sec)
        """
        return self._get_attribute(self._SDM_ATT_MAP['ForwardDelay'])
    @ForwardDelay.setter
    def ForwardDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ForwardDelay'], value)

    @property
    def HelloInterval(self):
        """
        Returns
        -------
        - number: The length of time between transmission of Hello messages from the root bridge (in milliseconds). The valid range is 500 msec to 255 sec. (default = 2,000 msec (2 sec)
        """
        return self._get_attribute(self._SDM_ATT_MAP['HelloInterval'])
    @HelloInterval.setter
    def HelloInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HelloInterval'], value)

    @property
    def IsRefreshComplete(self):
        """
        Returns
        -------
        - bool: If true, this causes the STP bridge to update.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsRefreshComplete'])

    @property
    def MaxAge(self):
        """
        Returns
        -------
        - number: The maximum Configuration message aging time. (in milliseconds) The valid range is 500 msec to 255 sec. (default = 20,000 msec (20 sec)
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxAge'])
    @MaxAge.setter
    def MaxAge(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxAge'], value)

    @property
    def MessageAge(self):
        """
        Returns
        -------
        - number: The message age time parameter in the BPDU (in milliseconds). (It should be less than the Max. Age.) The valid range is 500 msec to 255 sec. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['MessageAge'])
    @MessageAge.setter
    def MessageAge(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MessageAge'], value)

    @property
    def Mode(self):
        """
        Returns
        -------
        - str(stp | rstp | mstp | pvst | rpvst | pvstp): The version of the STP protocol that is being used on the Bridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mode'])
    @Mode.setter
    def Mode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mode'], value)

    @property
    def MstcName(self):
        """
        Returns
        -------
        - str: (For use with MSTP only) The name of the Multiple Spanning Tree Configuration being used. Format = MSTC ID-n (editable by user).
        """
        return self._get_attribute(self._SDM_ATT_MAP['MstcName'])
    @MstcName.setter
    def MstcName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MstcName'], value)

    @property
    def MstcRevisionNumber(self):
        """
        Returns
        -------
        - number: (For use with MSTP only) The Revision Number of the Multiple Spanning Tree Configuration being used. A 2-byte unsigned integer. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['MstcRevisionNumber'])
    @MstcRevisionNumber.setter
    def MstcRevisionNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MstcRevisionNumber'], value)

    @property
    def PortPriority(self):
        """
        Returns
        -------
        - str(0 | 16 | 32 | 48 | 64 | 80 | 96 | 112 | 128 | 144 | 160 | 176 | 192 | 208 | 224 | 240): The port priority. The valid range is to 240, in multiples of 16. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortPriority'])
    @PortPriority.setter
    def PortPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortPriority'], value)

    @property
    def PvstpMode(self):
        """
        Returns
        -------
        - str(stp | rstp): The version of the pvSTP protocol that is being used on the Bridge.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PvstpMode'])
    @PvstpMode.setter
    def PvstpMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PvstpMode'], value)

    @property
    def RootCost(self):
        """
        Returns
        -------
        - number: (For STP and RSTP) The administrative cost for the shortest path from this bridge to the Root Bridge. The valid range is 0 to 4294967295. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['RootCost'])
    @RootCost.setter
    def RootCost(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RootCost'], value)

    @property
    def RootMac(self):
        """
        Returns
        -------
        - str: (For STP and RSTP) The 6-byte MAC Address for the Root Bridge. (default = 00:00:00:00:00:00)
        """
        return self._get_attribute(self._SDM_ATT_MAP['RootMac'])
    @RootMac.setter
    def RootMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RootMac'], value)

    @property
    def RootPriority(self):
        """
        Returns
        -------
        - str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440): (For STP and RSTP) The Bridge Priority for the root bridge. The valid range is 0 to 61,440, in increments of 4096. (default = 32,768)
        """
        return self._get_attribute(self._SDM_ATT_MAP['RootPriority'])
    @RootPriority.setter
    def RootPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RootPriority'], value)

    @property
    def RootSystemId(self):
        """
        Returns
        -------
        - number: (For STP and RSTP) The System ID for the root bridge. The valid range is 0 to 4,095. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['RootSystemId'])
    @RootSystemId.setter
    def RootSystemId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RootSystemId'], value)

    @property
    def UpdateRequired(self):
        """
        Returns
        -------
        - number: Indicates that an updated is required.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpdateRequired'])
    @UpdateRequired.setter
    def UpdateRequired(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpdateRequired'], value)

    @property
    def VlanPortPriority(self):
        """
        Returns
        -------
        - number: (For use with PVST+ and RPVST+ only) The Common Spanning Tree (CST) VLAN port priority. The valid range is 0 to 63. (default = 32)
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanPortPriority'])
    @VlanPortPriority.setter
    def VlanPortPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanPortPriority'], value)

    @property
    def VlanRootMac(self):
        """
        Returns
        -------
        - str: Common and Internal Spanning Tree (CIST) Regional (external) MAC address. Part of the CIST External Root Identifier. A 6-byte MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanRootMac'])
    @VlanRootMac.setter
    def VlanRootMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanRootMac'], value)

    @property
    def VlanRootPathCost(self):
        """
        Returns
        -------
        - number: Common and Internal Spanning Tree (CIST) regional (external) root path cost.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanRootPathCost'])
    @VlanRootPathCost.setter
    def VlanRootPathCost(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanRootPathCost'], value)

    @property
    def VlanRootPriority(self):
        """
        Returns
        -------
        - str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440): The priority value of the root bridge for the Common Spanning Tree (CST).
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanRootPriority'])
    @VlanRootPriority.setter
    def VlanRootPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanRootPriority'], value)

    def update(self, AutoPickBridgeMac=None, BridgeMac=None, BridgePriority=None, BridgeSystemId=None, BridgeType=None, CistRegRootCost=None, CistRegRootMac=None, CistRegRootPriority=None, CistRemainingHop=None, Enabled=None, ExternalRootCost=None, ExternalRootMac=None, ExternalRootPriority=None, ForwardDelay=None, HelloInterval=None, MaxAge=None, MessageAge=None, Mode=None, MstcName=None, MstcRevisionNumber=None, PortPriority=None, PvstpMode=None, RootCost=None, RootMac=None, RootPriority=None, RootSystemId=None, UpdateRequired=None, VlanPortPriority=None, VlanRootMac=None, VlanRootPathCost=None, VlanRootPriority=None):
        """Updates bridge resource on the server.

        Args
        ----
        - AutoPickBridgeMac (bool): If enabled, the MAC address for one of the STP interfaces will be automatically assigned as the MAC address for this bridge.
        - BridgeMac (str): The 6-byte MAC address assigned to this bridge. Part of the bridge identifier (bridge ID).
        - BridgePriority (str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440)): The Bridge Priority for this bridge.The valid range is 0 to 61,440, in multiples of 4,096. (default = 32,768)
        - BridgeSystemId (number): The System ID for the bridge. The valid range is 0 to 4,095. (default = 0)
        - BridgeType (str(bridges | providerBridges)): NOT DEFINED
        - CistRegRootCost (number): (For use with PVST+ and RPVST+ only) The Common Spanning Tree (CST) root path cost. The valid range is 0 to 4294967295. (default = 0)
        - CistRegRootMac (str): (For use with PVST+ and RPVST+ only) The Common Spanning Tree (CST) 6-byte root MAC address. (default = 00:00:00:00:00:00)
        - CistRegRootPriority (str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440)): (For use with PVST+ and RPVST+ only) The Common Spanning Tree (CST) priority of the root. The valid range is 0 to 61,440, in increments of 4,096. (default = 32,768)
        - CistRemainingHop (number): (For use with MSTP only) The number of additional bridge-to-bridge hops that will be allowed for the MSTP BPDUs. The root sets the maximum hop count, and each subsequent bridge decrements this value by 1. The valid range is 1 to 255. (default = 20)
        - Enabled (bool): Enables or disables the bridge's simulation. (default = disabled)
        - ExternalRootCost (number): Common and Internal Spanning Tree (CIST) external root path cost. A 4-byte unsigned integer. The default is 0.
        - ExternalRootMac (str): Common and Internal Spanning Tree (CIST) external root MAC address. A 6-byte MAC address.The default is 00 00 00 00 00 00.
        - ExternalRootPriority (str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440)): (For use with MSTP only) The priority value of the root bridge for the CIST/MSTP region (external). Part of the CIST External Root Identifier. The valid range is 0 to 61,440, in increments of 4096. (default = 32,768)
        - ForwardDelay (number): The delay used for a port's change to the Forwarding state. (in milliseconds) The valid range is 500 msec to 255 sec. (default = 15,000 msec (15 sec)
        - HelloInterval (number): The length of time between transmission of Hello messages from the root bridge (in milliseconds). The valid range is 500 msec to 255 sec. (default = 2,000 msec (2 sec)
        - MaxAge (number): The maximum Configuration message aging time. (in milliseconds) The valid range is 500 msec to 255 sec. (default = 20,000 msec (20 sec)
        - MessageAge (number): The message age time parameter in the BPDU (in milliseconds). (It should be less than the Max. Age.) The valid range is 500 msec to 255 sec. (default = 0)
        - Mode (str(stp | rstp | mstp | pvst | rpvst | pvstp)): The version of the STP protocol that is being used on the Bridge.
        - MstcName (str): (For use with MSTP only) The name of the Multiple Spanning Tree Configuration being used. Format = MSTC ID-n (editable by user).
        - MstcRevisionNumber (number): (For use with MSTP only) The Revision Number of the Multiple Spanning Tree Configuration being used. A 2-byte unsigned integer. (default = 0)
        - PortPriority (str(0 | 16 | 32 | 48 | 64 | 80 | 96 | 112 | 128 | 144 | 160 | 176 | 192 | 208 | 224 | 240)): The port priority. The valid range is to 240, in multiples of 16. (default = 0)
        - PvstpMode (str(stp | rstp)): The version of the pvSTP protocol that is being used on the Bridge.
        - RootCost (number): (For STP and RSTP) The administrative cost for the shortest path from this bridge to the Root Bridge. The valid range is 0 to 4294967295. (default = 0)
        - RootMac (str): (For STP and RSTP) The 6-byte MAC Address for the Root Bridge. (default = 00:00:00:00:00:00)
        - RootPriority (str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440)): (For STP and RSTP) The Bridge Priority for the root bridge. The valid range is 0 to 61,440, in increments of 4096. (default = 32,768)
        - RootSystemId (number): (For STP and RSTP) The System ID for the root bridge. The valid range is 0 to 4,095. (default = 0)
        - UpdateRequired (number): Indicates that an updated is required.
        - VlanPortPriority (number): (For use with PVST+ and RPVST+ only) The Common Spanning Tree (CST) VLAN port priority. The valid range is 0 to 63. (default = 32)
        - VlanRootMac (str): Common and Internal Spanning Tree (CIST) Regional (external) MAC address. Part of the CIST External Root Identifier. A 6-byte MAC address.
        - VlanRootPathCost (number): Common and Internal Spanning Tree (CIST) regional (external) root path cost.
        - VlanRootPriority (str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440)): The priority value of the root bridge for the Common Spanning Tree (CST).

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AutoPickBridgeMac=None, BridgeMac=None, BridgePriority=None, BridgeSystemId=None, BridgeType=None, CistRegRootCost=None, CistRegRootMac=None, CistRegRootPriority=None, CistRemainingHop=None, Enabled=None, ExternalRootCost=None, ExternalRootMac=None, ExternalRootPriority=None, ForwardDelay=None, HelloInterval=None, MaxAge=None, MessageAge=None, Mode=None, MstcName=None, MstcRevisionNumber=None, PortPriority=None, PvstpMode=None, RootCost=None, RootMac=None, RootPriority=None, RootSystemId=None, UpdateRequired=None, VlanPortPriority=None, VlanRootMac=None, VlanRootPathCost=None, VlanRootPriority=None):
        """Adds a new bridge resource on the server and adds it to the container.

        Args
        ----
        - AutoPickBridgeMac (bool): If enabled, the MAC address for one of the STP interfaces will be automatically assigned as the MAC address for this bridge.
        - BridgeMac (str): The 6-byte MAC address assigned to this bridge. Part of the bridge identifier (bridge ID).
        - BridgePriority (str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440)): The Bridge Priority for this bridge.The valid range is 0 to 61,440, in multiples of 4,096. (default = 32,768)
        - BridgeSystemId (number): The System ID for the bridge. The valid range is 0 to 4,095. (default = 0)
        - BridgeType (str(bridges | providerBridges)): NOT DEFINED
        - CistRegRootCost (number): (For use with PVST+ and RPVST+ only) The Common Spanning Tree (CST) root path cost. The valid range is 0 to 4294967295. (default = 0)
        - CistRegRootMac (str): (For use with PVST+ and RPVST+ only) The Common Spanning Tree (CST) 6-byte root MAC address. (default = 00:00:00:00:00:00)
        - CistRegRootPriority (str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440)): (For use with PVST+ and RPVST+ only) The Common Spanning Tree (CST) priority of the root. The valid range is 0 to 61,440, in increments of 4,096. (default = 32,768)
        - CistRemainingHop (number): (For use with MSTP only) The number of additional bridge-to-bridge hops that will be allowed for the MSTP BPDUs. The root sets the maximum hop count, and each subsequent bridge decrements this value by 1. The valid range is 1 to 255. (default = 20)
        - Enabled (bool): Enables or disables the bridge's simulation. (default = disabled)
        - ExternalRootCost (number): Common and Internal Spanning Tree (CIST) external root path cost. A 4-byte unsigned integer. The default is 0.
        - ExternalRootMac (str): Common and Internal Spanning Tree (CIST) external root MAC address. A 6-byte MAC address.The default is 00 00 00 00 00 00.
        - ExternalRootPriority (str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440)): (For use with MSTP only) The priority value of the root bridge for the CIST/MSTP region (external). Part of the CIST External Root Identifier. The valid range is 0 to 61,440, in increments of 4096. (default = 32,768)
        - ForwardDelay (number): The delay used for a port's change to the Forwarding state. (in milliseconds) The valid range is 500 msec to 255 sec. (default = 15,000 msec (15 sec)
        - HelloInterval (number): The length of time between transmission of Hello messages from the root bridge (in milliseconds). The valid range is 500 msec to 255 sec. (default = 2,000 msec (2 sec)
        - MaxAge (number): The maximum Configuration message aging time. (in milliseconds) The valid range is 500 msec to 255 sec. (default = 20,000 msec (20 sec)
        - MessageAge (number): The message age time parameter in the BPDU (in milliseconds). (It should be less than the Max. Age.) The valid range is 500 msec to 255 sec. (default = 0)
        - Mode (str(stp | rstp | mstp | pvst | rpvst | pvstp)): The version of the STP protocol that is being used on the Bridge.
        - MstcName (str): (For use with MSTP only) The name of the Multiple Spanning Tree Configuration being used. Format = MSTC ID-n (editable by user).
        - MstcRevisionNumber (number): (For use with MSTP only) The Revision Number of the Multiple Spanning Tree Configuration being used. A 2-byte unsigned integer. (default = 0)
        - PortPriority (str(0 | 16 | 32 | 48 | 64 | 80 | 96 | 112 | 128 | 144 | 160 | 176 | 192 | 208 | 224 | 240)): The port priority. The valid range is to 240, in multiples of 16. (default = 0)
        - PvstpMode (str(stp | rstp)): The version of the pvSTP protocol that is being used on the Bridge.
        - RootCost (number): (For STP and RSTP) The administrative cost for the shortest path from this bridge to the Root Bridge. The valid range is 0 to 4294967295. (default = 0)
        - RootMac (str): (For STP and RSTP) The 6-byte MAC Address for the Root Bridge. (default = 00:00:00:00:00:00)
        - RootPriority (str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440)): (For STP and RSTP) The Bridge Priority for the root bridge. The valid range is 0 to 61,440, in increments of 4096. (default = 32,768)
        - RootSystemId (number): (For STP and RSTP) The System ID for the root bridge. The valid range is 0 to 4,095. (default = 0)
        - UpdateRequired (number): Indicates that an updated is required.
        - VlanPortPriority (number): (For use with PVST+ and RPVST+ only) The Common Spanning Tree (CST) VLAN port priority. The valid range is 0 to 63. (default = 32)
        - VlanRootMac (str): Common and Internal Spanning Tree (CIST) Regional (external) MAC address. Part of the CIST External Root Identifier. A 6-byte MAC address.
        - VlanRootPathCost (number): Common and Internal Spanning Tree (CIST) regional (external) root path cost.
        - VlanRootPriority (str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440)): The priority value of the root bridge for the Common Spanning Tree (CST).

        Returns
        -------
        - self: This instance with all currently retrieved bridge resources using find and the newly added bridge resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained bridge resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AutoPickBridgeMac=None, BridgeMac=None, BridgePriority=None, BridgeSystemId=None, BridgeType=None, CistRegRootCost=None, CistRegRootMac=None, CistRegRootPriority=None, CistRemainingHop=None, Enabled=None, ExternalRootCost=None, ExternalRootMac=None, ExternalRootPriority=None, ForwardDelay=None, HelloInterval=None, IsRefreshComplete=None, MaxAge=None, MessageAge=None, Mode=None, MstcName=None, MstcRevisionNumber=None, PortPriority=None, PvstpMode=None, RootCost=None, RootMac=None, RootPriority=None, RootSystemId=None, UpdateRequired=None, VlanPortPriority=None, VlanRootMac=None, VlanRootPathCost=None, VlanRootPriority=None):
        """Finds and retrieves bridge resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bridge resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bridge resources from the server.

        Args
        ----
        - AutoPickBridgeMac (bool): If enabled, the MAC address for one of the STP interfaces will be automatically assigned as the MAC address for this bridge.
        - BridgeMac (str): The 6-byte MAC address assigned to this bridge. Part of the bridge identifier (bridge ID).
        - BridgePriority (str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440)): The Bridge Priority for this bridge.The valid range is 0 to 61,440, in multiples of 4,096. (default = 32,768)
        - BridgeSystemId (number): The System ID for the bridge. The valid range is 0 to 4,095. (default = 0)
        - BridgeType (str(bridges | providerBridges)): NOT DEFINED
        - CistRegRootCost (number): (For use with PVST+ and RPVST+ only) The Common Spanning Tree (CST) root path cost. The valid range is 0 to 4294967295. (default = 0)
        - CistRegRootMac (str): (For use with PVST+ and RPVST+ only) The Common Spanning Tree (CST) 6-byte root MAC address. (default = 00:00:00:00:00:00)
        - CistRegRootPriority (str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440)): (For use with PVST+ and RPVST+ only) The Common Spanning Tree (CST) priority of the root. The valid range is 0 to 61,440, in increments of 4,096. (default = 32,768)
        - CistRemainingHop (number): (For use with MSTP only) The number of additional bridge-to-bridge hops that will be allowed for the MSTP BPDUs. The root sets the maximum hop count, and each subsequent bridge decrements this value by 1. The valid range is 1 to 255. (default = 20)
        - Enabled (bool): Enables or disables the bridge's simulation. (default = disabled)
        - ExternalRootCost (number): Common and Internal Spanning Tree (CIST) external root path cost. A 4-byte unsigned integer. The default is 0.
        - ExternalRootMac (str): Common and Internal Spanning Tree (CIST) external root MAC address. A 6-byte MAC address.The default is 00 00 00 00 00 00.
        - ExternalRootPriority (str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440)): (For use with MSTP only) The priority value of the root bridge for the CIST/MSTP region (external). Part of the CIST External Root Identifier. The valid range is 0 to 61,440, in increments of 4096. (default = 32,768)
        - ForwardDelay (number): The delay used for a port's change to the Forwarding state. (in milliseconds) The valid range is 500 msec to 255 sec. (default = 15,000 msec (15 sec)
        - HelloInterval (number): The length of time between transmission of Hello messages from the root bridge (in milliseconds). The valid range is 500 msec to 255 sec. (default = 2,000 msec (2 sec)
        - IsRefreshComplete (bool): If true, this causes the STP bridge to update.
        - MaxAge (number): The maximum Configuration message aging time. (in milliseconds) The valid range is 500 msec to 255 sec. (default = 20,000 msec (20 sec)
        - MessageAge (number): The message age time parameter in the BPDU (in milliseconds). (It should be less than the Max. Age.) The valid range is 500 msec to 255 sec. (default = 0)
        - Mode (str(stp | rstp | mstp | pvst | rpvst | pvstp)): The version of the STP protocol that is being used on the Bridge.
        - MstcName (str): (For use with MSTP only) The name of the Multiple Spanning Tree Configuration being used. Format = MSTC ID-n (editable by user).
        - MstcRevisionNumber (number): (For use with MSTP only) The Revision Number of the Multiple Spanning Tree Configuration being used. A 2-byte unsigned integer. (default = 0)
        - PortPriority (str(0 | 16 | 32 | 48 | 64 | 80 | 96 | 112 | 128 | 144 | 160 | 176 | 192 | 208 | 224 | 240)): The port priority. The valid range is to 240, in multiples of 16. (default = 0)
        - PvstpMode (str(stp | rstp)): The version of the pvSTP protocol that is being used on the Bridge.
        - RootCost (number): (For STP and RSTP) The administrative cost for the shortest path from this bridge to the Root Bridge. The valid range is 0 to 4294967295. (default = 0)
        - RootMac (str): (For STP and RSTP) The 6-byte MAC Address for the Root Bridge. (default = 00:00:00:00:00:00)
        - RootPriority (str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440)): (For STP and RSTP) The Bridge Priority for the root bridge. The valid range is 0 to 61,440, in increments of 4096. (default = 32,768)
        - RootSystemId (number): (For STP and RSTP) The System ID for the root bridge. The valid range is 0 to 4,095. (default = 0)
        - UpdateRequired (number): Indicates that an updated is required.
        - VlanPortPriority (number): (For use with PVST+ and RPVST+ only) The Common Spanning Tree (CST) VLAN port priority. The valid range is 0 to 63. (default = 32)
        - VlanRootMac (str): Common and Internal Spanning Tree (CIST) Regional (external) MAC address. Part of the CIST External Root Identifier. A 6-byte MAC address.
        - VlanRootPathCost (number): Common and Internal Spanning Tree (CIST) regional (external) root path cost.
        - VlanRootPriority (str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440)): The priority value of the root bridge for the Common Spanning Tree (CST).

        Returns
        -------
        - self: This instance with matching bridge resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bridge data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bridge resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def BridgeTopologyChange(self):
        """Executes the bridgeTopologyChange operation on the server.

        This commands checks to see if there has been a topology change in the specified STP bridge.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('bridgeTopologyChange', payload=payload, response_object=None)

    def CistTopologyChange(self):
        """Executes the cistTopologyChange operation on the server.

        This command checks to see if a topology change has occurred on the specified STP bridge CIST.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('cistTopologyChange', payload=payload, response_object=None)

    def RefreshLearnedInfo(self):
        """Executes the refreshLearnedInfo operation on the server.

        This exec refreshes the STP learned information from the DUT.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshLearnedInfo', payload=payload, response_object=None)

    def UpdateParameters(self):
        """Executes the updateParameters operation on the server.

        Updates the current STP parameters for the STP bridge.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('updateParameters', payload=payload, response_object=None)
