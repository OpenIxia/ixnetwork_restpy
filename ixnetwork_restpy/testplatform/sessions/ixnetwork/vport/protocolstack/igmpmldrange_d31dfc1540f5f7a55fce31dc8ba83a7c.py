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
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class IgmpMldRange(Base):
    """
    The IgmpMldRange class encapsulates a list of igmpMldRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the IgmpMldRange.find() method.
    The list can be managed by using the IgmpMldRange.add() and IgmpMldRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "igmpMldRange"
    _SDM_ATT_MAP = {
        "Enabled": "enabled",
        "GeneralQueryResponseMode": "generalQueryResponseMode",
        "ImmediateResponse": "immediateResponse",
        "JoinLeaveMultiplier": "joinLeaveMultiplier",
        "MeshingMode": "meshingMode",
        "Name": "name",
        "ObjectId": "objectId",
        "ReportFrequency": "reportFrequency",
        "RouterAlert": "routerAlert",
        "SpecificQueryResponseMode": "specificQueryResponseMode",
        "UnsolicitedResponseMode": "unsolicitedResponseMode",
        "Version": "version",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(IgmpMldRange, self).__init__(parent, list_op)

    @property
    def JoinLeaveMulticastGroupRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.joinleavemulticastgrouprange_4a42d2a6d2f94961430440a0c5e2cf02.JoinLeaveMulticastGroupRange): An instance of the JoinLeaveMulticastGroupRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.joinleavemulticastgrouprange_4a42d2a6d2f94961430440a0c5e2cf02 import (
            JoinLeaveMulticastGroupRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("JoinLeaveMulticastGroupRange", None) is not None:
                return self._properties.get("JoinLeaveMulticastGroupRange")
        return JoinLeaveMulticastGroupRange(self)

    @property
    def MulticastGroupRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.multicastgrouprange_992efde580b0afb1313e376da7fe0b33.MulticastGroupRange): An instance of the MulticastGroupRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.multicastgrouprange_992efde580b0afb1313e376da7fe0b33 import (
            MulticastGroupRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MulticastGroupRange", None) is not None:
                return self._properties.get("MulticastGroupRange")
        return MulticastGroupRange(self)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Disabled ranges won't be configured nor validated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def GeneralQueryResponseMode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, responds to General Query messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GeneralQueryResponseMode"])

    @GeneralQueryResponseMode.setter
    def GeneralQueryResponseMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GeneralQueryResponseMode"], value)

    @property
    def ImmediateResponse(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, it will ignore the value specified in the Maximum Response Delay in the Membership Query message, assume that the Delay is always = 0 seconds and immediately respond to the Query by sending a Report.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ImmediateResponse"])

    @ImmediateResponse.setter
    def ImmediateResponse(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ImmediateResponse"], value)

    @property
    def JoinLeaveMultiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of times a host sends every Join or Leave message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["JoinLeaveMultiplier"])

    @JoinLeaveMultiplier.setter
    def JoinLeaveMultiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["JoinLeaveMultiplier"], value)

    @property
    def MeshingMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Defines how the hosts in a range join the selected multicast group ranges.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MeshingMode"])

    @MeshingMode.setter
    def MeshingMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MeshingMode"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of range
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def ObjectId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP["ObjectId"])

    @property
    def ReportFrequency(self):
        # type: () -> int
        """
        Returns
        -------
        - number: When Send Unsolicited Response is enabled, specifies the frequency, in seconds, with which unsolicited messages are generated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReportFrequency"])

    @ReportFrequency.setter
    def ReportFrequency(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReportFrequency"], value)

    @property
    def RouterAlert(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, sets the Send Router Alert bit in the IP header.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouterAlert"])

    @RouterAlert.setter
    def RouterAlert(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouterAlert"], value)

    @property
    def SpecificQueryResponseMode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, responds to Group-Specific Query messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SpecificQueryResponseMode"])

    @SpecificQueryResponseMode.setter
    def SpecificQueryResponseMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SpecificQueryResponseMode"], value)

    @property
    def UnsolicitedResponseMode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, causes the emulated IGMP host to automatically send full membership messages at regular intervals, without waiting for a query message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UnsolicitedResponseMode"])

    @UnsolicitedResponseMode.setter
    def UnsolicitedResponseMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UnsolicitedResponseMode"], value)

    @property
    def Version(self):
        # type: () -> str
        """
        Returns
        -------
        - str: IGMP/MLD protocol version.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Version"])

    @Version.setter
    def Version(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Version"], value)

    def update(
        self,
        Enabled=None,
        GeneralQueryResponseMode=None,
        ImmediateResponse=None,
        JoinLeaveMultiplier=None,
        MeshingMode=None,
        Name=None,
        ReportFrequency=None,
        RouterAlert=None,
        SpecificQueryResponseMode=None,
        UnsolicitedResponseMode=None,
        Version=None,
    ):
        # type: (bool, bool, bool, int, str, str, int, bool, bool, bool, str) -> IgmpMldRange
        """Updates igmpMldRange resource on the server.

        Args
        ----
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - GeneralQueryResponseMode (bool): If selected, responds to General Query messages.
        - ImmediateResponse (bool): If selected, it will ignore the value specified in the Maximum Response Delay in the Membership Query message, assume that the Delay is always = 0 seconds and immediately respond to the Query by sending a Report.
        - JoinLeaveMultiplier (number): The number of times a host sends every Join or Leave message.
        - MeshingMode (str): Defines how the hosts in a range join the selected multicast group ranges.
        - Name (str): Name of range
        - ReportFrequency (number): When Send Unsolicited Response is enabled, specifies the frequency, in seconds, with which unsolicited messages are generated.
        - RouterAlert (bool): If selected, sets the Send Router Alert bit in the IP header.
        - SpecificQueryResponseMode (bool): If selected, responds to Group-Specific Query messages.
        - UnsolicitedResponseMode (bool): If selected, causes the emulated IGMP host to automatically send full membership messages at regular intervals, without waiting for a query message.
        - Version (str): IGMP/MLD protocol version.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Enabled=None,
        GeneralQueryResponseMode=None,
        ImmediateResponse=None,
        JoinLeaveMultiplier=None,
        MeshingMode=None,
        Name=None,
        ReportFrequency=None,
        RouterAlert=None,
        SpecificQueryResponseMode=None,
        UnsolicitedResponseMode=None,
        Version=None,
    ):
        # type: (bool, bool, bool, int, str, str, int, bool, bool, bool, str) -> IgmpMldRange
        """Adds a new igmpMldRange resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - GeneralQueryResponseMode (bool): If selected, responds to General Query messages.
        - ImmediateResponse (bool): If selected, it will ignore the value specified in the Maximum Response Delay in the Membership Query message, assume that the Delay is always = 0 seconds and immediately respond to the Query by sending a Report.
        - JoinLeaveMultiplier (number): The number of times a host sends every Join or Leave message.
        - MeshingMode (str): Defines how the hosts in a range join the selected multicast group ranges.
        - Name (str): Name of range
        - ReportFrequency (number): When Send Unsolicited Response is enabled, specifies the frequency, in seconds, with which unsolicited messages are generated.
        - RouterAlert (bool): If selected, sets the Send Router Alert bit in the IP header.
        - SpecificQueryResponseMode (bool): If selected, responds to Group-Specific Query messages.
        - UnsolicitedResponseMode (bool): If selected, causes the emulated IGMP host to automatically send full membership messages at regular intervals, without waiting for a query message.
        - Version (str): IGMP/MLD protocol version.

        Returns
        -------
        - self: This instance with all currently retrieved igmpMldRange resources using find and the newly added igmpMldRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained igmpMldRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        Enabled=None,
        GeneralQueryResponseMode=None,
        ImmediateResponse=None,
        JoinLeaveMultiplier=None,
        MeshingMode=None,
        Name=None,
        ObjectId=None,
        ReportFrequency=None,
        RouterAlert=None,
        SpecificQueryResponseMode=None,
        UnsolicitedResponseMode=None,
        Version=None,
    ):
        # type: (bool, bool, bool, int, str, str, str, int, bool, bool, bool, str) -> IgmpMldRange
        """Finds and retrieves igmpMldRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve igmpMldRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all igmpMldRange resources from the server.

        Args
        ----
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - GeneralQueryResponseMode (bool): If selected, responds to General Query messages.
        - ImmediateResponse (bool): If selected, it will ignore the value specified in the Maximum Response Delay in the Membership Query message, assume that the Delay is always = 0 seconds and immediately respond to the Query by sending a Report.
        - JoinLeaveMultiplier (number): The number of times a host sends every Join or Leave message.
        - MeshingMode (str): Defines how the hosts in a range join the selected multicast group ranges.
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object
        - ReportFrequency (number): When Send Unsolicited Response is enabled, specifies the frequency, in seconds, with which unsolicited messages are generated.
        - RouterAlert (bool): If selected, sets the Send Router Alert bit in the IP header.
        - SpecificQueryResponseMode (bool): If selected, responds to Group-Specific Query messages.
        - UnsolicitedResponseMode (bool): If selected, causes the emulated IGMP host to automatically send full membership messages at regular intervals, without waiting for a query message.
        - Version (str): IGMP/MLD protocol version.

        Returns
        -------
        - self: This instance with matching igmpMldRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of igmpMldRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the igmpMldRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the apply operation on the server.

        Apply changes for on the fly configuration support.

        apply(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("apply", payload=payload, response_object=None)

    def CustomProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum, async_operation=bool)
        ---------------------------------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "customProtocolStack", payload=payload, response_object=None
        )

    def DisableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string, async_operation=bool)string
        -------------------------------------------------------------
        - Arg2 (str): Protocol class name to disable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "disableProtocolStack", payload=payload, response_object=None
        )

    def EnableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------
        - Arg2 (str): Protocol class name to enable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "enableProtocolStack", payload=payload, response_object=None
        )

    def IgmpMldJoin(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the igmpMldJoin operation on the server.

        Join IGMP/MLD multicast group ranges on the fly

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        igmpMldJoin(async_operation=bool)
        ---------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        igmpMldJoin(Arg2=enum, async_operation=bool)
        --------------------------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/igmpMld,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/igmpMld,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ipEndpoint/igmpMld,/vport/protocolStack/atm/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/igmpMld,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/range/igmpMldRange]
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("igmpMldJoin", payload=payload, response_object=None)

    def IgmpMldLeave(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the igmpMldLeave operation on the server.

        Leave IGMP/MLD multicast group ranges on the fly

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        igmpMldLeave(async_operation=bool)
        ----------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        igmpMldLeave(Arg2=enum, async_operation=bool)
        ---------------------------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/igmpMld,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/igmpMld,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ipEndpoint/igmpMld,/vport/protocolStack/atm/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/igmpMld,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/range/igmpMldRange]
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("igmpMldLeave", payload=payload, response_object=None)

    def IgmpMldStart(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the igmpMldStart operation on the server.

        Start IGMP/MLD on selected plugins and ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        igmpMldStart(async_operation=bool)
        ----------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        igmpMldStart(Arg2=enum, async_operation=bool)
        ---------------------------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/igmpMld,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/igmpMld,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ipEndpoint/igmpMld,/vport/protocolStack/atm/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/igmpMld,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/range/igmpMldRange]
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("igmpMldStart", payload=payload, response_object=None)

    def IgmpMldStop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the igmpMldStop operation on the server.

        Stop IGMP/MLD on selected plugins and ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        igmpMldStop(async_operation=bool)
        ---------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        igmpMldStop(Arg2=enum, async_operation=bool)
        --------------------------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/igmpMld,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/igmpMld,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/atm/ipEndpoint/igmpMld,/vport/protocolStack/atm/ipEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/atm/pppox/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/igmpMld,/vport/protocolStack/atm/pppoxEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/igmpMld,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/ipEndpoint/igmpMld,/vport/protocolStack/ethernet/ipEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/igmpMldRange,/vport/protocolStack/ethernet/pppox/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/igmpMld,/vport/protocolStack/ethernet/pppoxEndpoint/range/igmpMldRange]
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("igmpMldStop", payload=payload, response_object=None)
