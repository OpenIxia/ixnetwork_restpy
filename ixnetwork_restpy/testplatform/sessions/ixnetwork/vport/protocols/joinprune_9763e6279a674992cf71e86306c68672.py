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


class JoinPrune(Base):
    """A set of multicast addresses to be included in this interface.
    The JoinPrune class encapsulates a list of joinPrune resources that are managed by the user.
    A list of resources can be retrieved from the server using the JoinPrune.find() method.
    The list can be managed by using the JoinPrune.add() and JoinPrune.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "joinPrune"
    _SDM_ATT_MAP = {
        "DiscardRegisterStates": "discardRegisterStates",
        "Enabled": "enabled",
        "EnabledDataMdt": "enabledDataMdt",
        "FlapEnabled": "flapEnabled",
        "FlapInterval": "flapInterval",
        "GroupAddress": "groupAddress",
        "GroupCount": "groupCount",
        "GroupMappingMode": "groupMappingMode",
        "GroupMaskWidth": "groupMaskWidth",
        "GroupRange": "groupRange",
        "NumRegToReceivePerSg": "numRegToReceivePerSg",
        "PackGroupsEnabled": "packGroupsEnabled",
        "PruneSourceAddress": "pruneSourceAddress",
        "PruneSourceCount": "pruneSourceCount",
        "PruneSourceMaskWidth": "pruneSourceMaskWidth",
        "RpAddress": "rpAddress",
        "SourceAddress": "sourceAddress",
        "SourceCount": "sourceCount",
        "SourceMaskWidth": "sourceMaskWidth",
        "SptSwitchoverInterval": "sptSwitchoverInterval",
    }
    _SDM_ENUM_MAP = {
        "groupMappingMode": ["fullyMeshed", "oneToOne"],
        "groupRange": ["rp", "g", "sg", "sptSwitchOver", "registerTriggeredSg"],
    }

    def __init__(self, parent, list_op=False):
        super(JoinPrune, self).__init__(parent, list_op)

    @property
    def LearnedMgrState(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedmgrstate_d7919072a223792ffde967c8d24af004.LearnedMgrState): An instance of the LearnedMgrState class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedmgrstate_d7919072a223792ffde967c8d24af004 import (
            LearnedMgrState,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedMgrState", None) is not None:
                return self._properties.get("LearnedMgrState")
        return LearnedMgrState(self)

    @property
    def DiscardRegisterStates(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If checked, the Learned Join States sent by the RP (DUT) in response to this specific Register Message will be discarded - and will not be displayed in the table of the Register Range window.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DiscardRegisterStates"])

    @DiscardRegisterStates.setter
    def DiscardRegisterStates(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DiscardRegisterStates"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the use of this join/prune.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def EnabledDataMdt(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, pimsmLearnedDataMdt will be available. (default = disabled)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnabledDataMdt"])

    @EnabledDataMdt.setter
    def EnabledDataMdt(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnabledDataMdt"], value)

    @property
    def FlapEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables emulated flapping of this multicast group range. NOTE: Flapping is not supported for the Switchover (*, G) -> (S, G) range type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlapEnabled"])

    @FlapEnabled.setter
    def FlapEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlapEnabled"], value)

    @property
    def FlapInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Defines the join/prune flapping interval.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlapInterval"])

    @FlapInterval.setter
    def FlapInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlapInterval"], value)

    @property
    def GroupAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: An IPv4 or IPv6 address used with the group mask to create a range of multicast addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupAddress"])

    @GroupAddress.setter
    def GroupAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupAddress"], value)

    @property
    def GroupCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of multicast group addresses to be included in the multicast group range. The maximum number of valid possible addresses depends on the values for the group address and the group mask width.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupCount"])

    @GroupCount.setter
    def GroupCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupCount"], value)

    @property
    def GroupMappingMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fullyMeshed | oneToOne): Sets the type of mapping that occurs when routes are advertised. This only applies for (S, G) and switchover types for MGR and is meaningful for RR.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupMappingMode"])

    @GroupMappingMode.setter
    def GroupMappingMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupMappingMode"], value)

    @property
    def GroupMaskWidth(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of bits in the mask applied to the group address. (The masked bits in the group address form the address prefix.)The default value is 32. The valid range is 1 to 128, depending on address family type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupMaskWidth"])

    @GroupMaskWidth.setter
    def GroupMaskWidth(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupMaskWidth"], value)

    @property
    def GroupRange(self):
        # type: () -> str
        """
        Returns
        -------
        - str(rp | g | sg | sptSwitchOver | registerTriggeredSg): The multicast group range type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupRange"])

    @GroupRange.setter
    def GroupRange(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupRange"], value)

    @property
    def NumRegToReceivePerSg(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If rangeType is set to pimsmJoinsPrunesTypeRegisterTriggeredSG, then this is the count of register messages received that will trigger transmission of a (S,G) message. (default = 10)
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumRegToReceivePerSg"])

    @NumRegToReceivePerSg.setter
    def NumRegToReceivePerSg(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumRegToReceivePerSg"], value)

    @property
    def PackGroupsEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, multiple groups can be included within a single packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PackGroupsEnabled"])

    @PackGroupsEnabled.setter
    def PackGroupsEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PackGroupsEnabled"], value)

    @property
    def PruneSourceAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: ONLY used for (*,G) Type to send (S,G,rpt) Prune Messages. (Multicast addresses are invalid.)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PruneSourceAddress"])

    @PruneSourceAddress.setter
    def PruneSourceAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PruneSourceAddress"], value)

    @property
    def PruneSourceCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of prune source addresses to be included. The maximum number of valid possible addresses depends on the values for the source address and the source mask width. The default value is 0. ONLY used for (*,G) type to send (S,G,rpt) prune messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PruneSourceCount"])

    @PruneSourceCount.setter
    def PruneSourceCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PruneSourceCount"], value)

    @property
    def PruneSourceMaskWidth(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of bits in the mask applied to the prune source address. (The masked bits in the prune source address form the address prefix.)
        """
        return self._get_attribute(self._SDM_ATT_MAP["PruneSourceMaskWidth"])

    @PruneSourceMaskWidth.setter
    def PruneSourceMaskWidth(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PruneSourceMaskWidth"], value)

    @property
    def RpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IP address of the Rendezvous Point (RP) router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RpAddress"])

    @RpAddress.setter
    def RpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RpAddress"], value)

    @property
    def SourceAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Multicast Source Address. Used for (S,G) Type and (S,G, rpt) only. (Multicast addresses are invalid.)
        """
        return self._get_attribute(self._SDM_ATT_MAP["SourceAddress"])

    @SourceAddress.setter
    def SourceAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SourceAddress"], value)

    @property
    def SourceCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of multicast source addresses to be included. The maximum number of valid possible addresses depends on the values for the source address and the source mask width.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SourceCount"])

    @SourceCount.setter
    def SourceCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SourceCount"], value)

    @property
    def SourceMaskWidth(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of bits in the mask applied to the source address. (The masked bits in the source address form the address prefix.)The default value is 32. The valid range is 1 to 128, depending on address family type. Used for (S,G) Type and (S,G, rpt) only.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SourceMaskWidth"])

    @SourceMaskWidth.setter
    def SourceMaskWidth(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SourceMaskWidth"], value)

    @property
    def SptSwitchoverInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time interval (in seconds) allowed for the switch from using the RP tree to using a Source-specific tree - from (*,G) to (S,G). The default value is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SptSwitchoverInterval"])

    @SptSwitchoverInterval.setter
    def SptSwitchoverInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SptSwitchoverInterval"], value)

    def update(
        self,
        DiscardRegisterStates=None,
        Enabled=None,
        EnabledDataMdt=None,
        FlapEnabled=None,
        FlapInterval=None,
        GroupAddress=None,
        GroupCount=None,
        GroupMappingMode=None,
        GroupMaskWidth=None,
        GroupRange=None,
        NumRegToReceivePerSg=None,
        PackGroupsEnabled=None,
        PruneSourceAddress=None,
        PruneSourceCount=None,
        PruneSourceMaskWidth=None,
        RpAddress=None,
        SourceAddress=None,
        SourceCount=None,
        SourceMaskWidth=None,
        SptSwitchoverInterval=None,
    ):
        # type: (bool, bool, bool, bool, int, str, int, str, int, str, int, bool, str, int, int, str, str, int, int, int) -> JoinPrune
        """Updates joinPrune resource on the server.

        Args
        ----
        - DiscardRegisterStates (bool): If checked, the Learned Join States sent by the RP (DUT) in response to this specific Register Message will be discarded - and will not be displayed in the table of the Register Range window.
        - Enabled (bool): Enables the use of this join/prune.
        - EnabledDataMdt (bool): If enabled, pimsmLearnedDataMdt will be available. (default = disabled)
        - FlapEnabled (bool): Enables emulated flapping of this multicast group range. NOTE: Flapping is not supported for the Switchover (*, G) -> (S, G) range type.
        - FlapInterval (number): Defines the join/prune flapping interval.
        - GroupAddress (str): An IPv4 or IPv6 address used with the group mask to create a range of multicast addresses.
        - GroupCount (number): The number of multicast group addresses to be included in the multicast group range. The maximum number of valid possible addresses depends on the values for the group address and the group mask width.
        - GroupMappingMode (str(fullyMeshed | oneToOne)): Sets the type of mapping that occurs when routes are advertised. This only applies for (S, G) and switchover types for MGR and is meaningful for RR.
        - GroupMaskWidth (number): The number of bits in the mask applied to the group address. (The masked bits in the group address form the address prefix.)The default value is 32. The valid range is 1 to 128, depending on address family type.
        - GroupRange (str(rp | g | sg | sptSwitchOver | registerTriggeredSg)): The multicast group range type.
        - NumRegToReceivePerSg (number): If rangeType is set to pimsmJoinsPrunesTypeRegisterTriggeredSG, then this is the count of register messages received that will trigger transmission of a (S,G) message. (default = 10)
        - PackGroupsEnabled (bool): If enabled, multiple groups can be included within a single packet.
        - PruneSourceAddress (str): ONLY used for (*,G) Type to send (S,G,rpt) Prune Messages. (Multicast addresses are invalid.)
        - PruneSourceCount (number): The number of prune source addresses to be included. The maximum number of valid possible addresses depends on the values for the source address and the source mask width. The default value is 0. ONLY used for (*,G) type to send (S,G,rpt) prune messages.
        - PruneSourceMaskWidth (number): The number of bits in the mask applied to the prune source address. (The masked bits in the prune source address form the address prefix.)
        - RpAddress (str): The IP address of the Rendezvous Point (RP) router.
        - SourceAddress (str): The Multicast Source Address. Used for (S,G) Type and (S,G, rpt) only. (Multicast addresses are invalid.)
        - SourceCount (number): The number of multicast source addresses to be included. The maximum number of valid possible addresses depends on the values for the source address and the source mask width.
        - SourceMaskWidth (number): The number of bits in the mask applied to the source address. (The masked bits in the source address form the address prefix.)The default value is 32. The valid range is 1 to 128, depending on address family type. Used for (S,G) Type and (S,G, rpt) only.
        - SptSwitchoverInterval (number): The time interval (in seconds) allowed for the switch from using the RP tree to using a Source-specific tree - from (*,G) to (S,G). The default value is 0.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        DiscardRegisterStates=None,
        Enabled=None,
        EnabledDataMdt=None,
        FlapEnabled=None,
        FlapInterval=None,
        GroupAddress=None,
        GroupCount=None,
        GroupMappingMode=None,
        GroupMaskWidth=None,
        GroupRange=None,
        NumRegToReceivePerSg=None,
        PackGroupsEnabled=None,
        PruneSourceAddress=None,
        PruneSourceCount=None,
        PruneSourceMaskWidth=None,
        RpAddress=None,
        SourceAddress=None,
        SourceCount=None,
        SourceMaskWidth=None,
        SptSwitchoverInterval=None,
    ):
        # type: (bool, bool, bool, bool, int, str, int, str, int, str, int, bool, str, int, int, str, str, int, int, int) -> JoinPrune
        """Adds a new joinPrune resource on the server and adds it to the container.

        Args
        ----
        - DiscardRegisterStates (bool): If checked, the Learned Join States sent by the RP (DUT) in response to this specific Register Message will be discarded - and will not be displayed in the table of the Register Range window.
        - Enabled (bool): Enables the use of this join/prune.
        - EnabledDataMdt (bool): If enabled, pimsmLearnedDataMdt will be available. (default = disabled)
        - FlapEnabled (bool): Enables emulated flapping of this multicast group range. NOTE: Flapping is not supported for the Switchover (*, G) -> (S, G) range type.
        - FlapInterval (number): Defines the join/prune flapping interval.
        - GroupAddress (str): An IPv4 or IPv6 address used with the group mask to create a range of multicast addresses.
        - GroupCount (number): The number of multicast group addresses to be included in the multicast group range. The maximum number of valid possible addresses depends on the values for the group address and the group mask width.
        - GroupMappingMode (str(fullyMeshed | oneToOne)): Sets the type of mapping that occurs when routes are advertised. This only applies for (S, G) and switchover types for MGR and is meaningful for RR.
        - GroupMaskWidth (number): The number of bits in the mask applied to the group address. (The masked bits in the group address form the address prefix.)The default value is 32. The valid range is 1 to 128, depending on address family type.
        - GroupRange (str(rp | g | sg | sptSwitchOver | registerTriggeredSg)): The multicast group range type.
        - NumRegToReceivePerSg (number): If rangeType is set to pimsmJoinsPrunesTypeRegisterTriggeredSG, then this is the count of register messages received that will trigger transmission of a (S,G) message. (default = 10)
        - PackGroupsEnabled (bool): If enabled, multiple groups can be included within a single packet.
        - PruneSourceAddress (str): ONLY used for (*,G) Type to send (S,G,rpt) Prune Messages. (Multicast addresses are invalid.)
        - PruneSourceCount (number): The number of prune source addresses to be included. The maximum number of valid possible addresses depends on the values for the source address and the source mask width. The default value is 0. ONLY used for (*,G) type to send (S,G,rpt) prune messages.
        - PruneSourceMaskWidth (number): The number of bits in the mask applied to the prune source address. (The masked bits in the prune source address form the address prefix.)
        - RpAddress (str): The IP address of the Rendezvous Point (RP) router.
        - SourceAddress (str): The Multicast Source Address. Used for (S,G) Type and (S,G, rpt) only. (Multicast addresses are invalid.)
        - SourceCount (number): The number of multicast source addresses to be included. The maximum number of valid possible addresses depends on the values for the source address and the source mask width.
        - SourceMaskWidth (number): The number of bits in the mask applied to the source address. (The masked bits in the source address form the address prefix.)The default value is 32. The valid range is 1 to 128, depending on address family type. Used for (S,G) Type and (S,G, rpt) only.
        - SptSwitchoverInterval (number): The time interval (in seconds) allowed for the switch from using the RP tree to using a Source-specific tree - from (*,G) to (S,G). The default value is 0.

        Returns
        -------
        - self: This instance with all currently retrieved joinPrune resources using find and the newly added joinPrune resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained joinPrune resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        DiscardRegisterStates=None,
        Enabled=None,
        EnabledDataMdt=None,
        FlapEnabled=None,
        FlapInterval=None,
        GroupAddress=None,
        GroupCount=None,
        GroupMappingMode=None,
        GroupMaskWidth=None,
        GroupRange=None,
        NumRegToReceivePerSg=None,
        PackGroupsEnabled=None,
        PruneSourceAddress=None,
        PruneSourceCount=None,
        PruneSourceMaskWidth=None,
        RpAddress=None,
        SourceAddress=None,
        SourceCount=None,
        SourceMaskWidth=None,
        SptSwitchoverInterval=None,
    ):
        # type: (bool, bool, bool, bool, int, str, int, str, int, str, int, bool, str, int, int, str, str, int, int, int) -> JoinPrune
        """Finds and retrieves joinPrune resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve joinPrune resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all joinPrune resources from the server.

        Args
        ----
        - DiscardRegisterStates (bool): If checked, the Learned Join States sent by the RP (DUT) in response to this specific Register Message will be discarded - and will not be displayed in the table of the Register Range window.
        - Enabled (bool): Enables the use of this join/prune.
        - EnabledDataMdt (bool): If enabled, pimsmLearnedDataMdt will be available. (default = disabled)
        - FlapEnabled (bool): Enables emulated flapping of this multicast group range. NOTE: Flapping is not supported for the Switchover (*, G) -> (S, G) range type.
        - FlapInterval (number): Defines the join/prune flapping interval.
        - GroupAddress (str): An IPv4 or IPv6 address used with the group mask to create a range of multicast addresses.
        - GroupCount (number): The number of multicast group addresses to be included in the multicast group range. The maximum number of valid possible addresses depends on the values for the group address and the group mask width.
        - GroupMappingMode (str(fullyMeshed | oneToOne)): Sets the type of mapping that occurs when routes are advertised. This only applies for (S, G) and switchover types for MGR and is meaningful for RR.
        - GroupMaskWidth (number): The number of bits in the mask applied to the group address. (The masked bits in the group address form the address prefix.)The default value is 32. The valid range is 1 to 128, depending on address family type.
        - GroupRange (str(rp | g | sg | sptSwitchOver | registerTriggeredSg)): The multicast group range type.
        - NumRegToReceivePerSg (number): If rangeType is set to pimsmJoinsPrunesTypeRegisterTriggeredSG, then this is the count of register messages received that will trigger transmission of a (S,G) message. (default = 10)
        - PackGroupsEnabled (bool): If enabled, multiple groups can be included within a single packet.
        - PruneSourceAddress (str): ONLY used for (*,G) Type to send (S,G,rpt) Prune Messages. (Multicast addresses are invalid.)
        - PruneSourceCount (number): The number of prune source addresses to be included. The maximum number of valid possible addresses depends on the values for the source address and the source mask width. The default value is 0. ONLY used for (*,G) type to send (S,G,rpt) prune messages.
        - PruneSourceMaskWidth (number): The number of bits in the mask applied to the prune source address. (The masked bits in the prune source address form the address prefix.)
        - RpAddress (str): The IP address of the Rendezvous Point (RP) router.
        - SourceAddress (str): The Multicast Source Address. Used for (S,G) Type and (S,G, rpt) only. (Multicast addresses are invalid.)
        - SourceCount (number): The number of multicast source addresses to be included. The maximum number of valid possible addresses depends on the values for the source address and the source mask width.
        - SourceMaskWidth (number): The number of bits in the mask applied to the source address. (The masked bits in the source address form the address prefix.)The default value is 32. The valid range is 1 to 128, depending on address family type. Used for (S,G) Type and (S,G, rpt) only.
        - SptSwitchoverInterval (number): The time interval (in seconds) allowed for the switch from using the RP tree to using a Source-specific tree - from (*,G) to (S,G). The default value is 0.

        Returns
        -------
        - self: This instance with matching joinPrune resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of joinPrune data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the joinPrune resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
