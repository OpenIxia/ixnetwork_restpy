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


class DedicatedBearer(Base):
    """Bearer
    The DedicatedBearer class encapsulates a list of dedicatedBearer resources that are managed by the user.
    A list of resources can be retrieved from the server using the DedicatedBearer.find() method.
    The list can be managed by using the DedicatedBearer.add() and DedicatedBearer.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "dedicatedBearer"
    _SDM_ATT_MAP = {
        "ApnAmbrUpdateValue": "apnAmbrUpdateValue",
        "Arp": "arp",
        "CustomTft": "customTft",
        "EnableLifetime": "enableLifetime",
        "Enabled": "enabled",
        "Gbrd": "gbrd",
        "Gbru": "gbru",
        "Lifetime": "lifetime",
        "Mbrd": "mbrd",
        "Mbru": "mbru",
        "Mode": "mode",
        "Name": "name",
        "ObjectId": "objectId",
        "PreemptionCapability": "preemptionCapability",
        "PreemptionVulnerability": "preemptionVulnerability",
        "PriorityLevel": "priorityLevel",
        "Qci": "qci",
        "QosLabel": "qosLabel",
        "QosUpdateValue": "qosUpdateValue",
        "Tft": "tft",
        "TimeoutAction": "timeoutAction",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(DedicatedBearer, self).__init__(parent, list_op)

    @property
    def ApnAmbrUpdateValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: APN_AMBR update value (in %).
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApnAmbrUpdateValue"])

    @ApnAmbrUpdateValue.setter
    def ApnAmbrUpdateValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ApnAmbrUpdateValue"], value)

    @property
    def Arp(self):
        # type: () -> int
        """
        Returns
        -------
        - number: OBSOLETE - Please use preemptionCapability, preemptionVulnerability and priorityLevel.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Arp"])

    @Arp.setter
    def Arp(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Arp"], value)

    @property
    def CustomTft(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomTft"])

    @CustomTft.setter
    def CustomTft(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomTft"], value)

    @property
    def EnableLifetime(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable bearer lifetime control
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLifetime"])

    @EnableLifetime.setter
    def EnableLifetime(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLifetime"], value)

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
    def Gbrd(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Guaranteed bitrate for downlink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Gbrd"])

    @Gbrd.setter
    def Gbrd(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Gbrd"], value)

    @property
    def Gbru(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Guaranteed bitrate for uplink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Gbru"])

    @Gbru.setter
    def Gbru(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Gbru"], value)

    @property
    def Lifetime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Bearer lifetime (seconds)
        """
        return self._get_attribute(self._SDM_ATT_MAP["Lifetime"])

    @Lifetime.setter
    def Lifetime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Lifetime"], value)

    @property
    def Mbrd(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum bitrate for downlink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mbrd"])

    @Mbrd.setter
    def Mbrd(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mbrd"], value)

    @property
    def Mbru(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum bitrate for uplink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mbru"])

    @Mbru.setter
    def Mbru(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mbru"], value)

    @property
    def Mode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: A dedicated bearer can be requested by the UE (UE requested) or created by the core network without a previous request (Network initiared). If the UE requested mode is selected the dedicated bearer will be activated only if the UE requests it using the UE requested bearer resource modification procedure
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mode"])

    @Mode.setter
    def Mode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mode"], value)

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
    def PreemptionCapability(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true preemption capability is enabled
        """
        return self._get_attribute(self._SDM_ATT_MAP["PreemptionCapability"])

    @PreemptionCapability.setter
    def PreemptionCapability(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PreemptionCapability"], value)

    @property
    def PreemptionVulnerability(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true preemption vulnerability is enabled
        """
        return self._get_attribute(self._SDM_ATT_MAP["PreemptionVulnerability"])

    @PreemptionVulnerability.setter
    def PreemptionVulnerability(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PreemptionVulnerability"], value)

    @property
    def PriorityLevel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Priority Level 1=highest 15=lowest
        """
        return self._get_attribute(self._SDM_ATT_MAP["PriorityLevel"])

    @PriorityLevel.setter
    def PriorityLevel(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PriorityLevel"], value)

    @property
    def Qci(self):
        # type: () -> int
        """
        Returns
        -------
        - number: QoS Class Identifier
        """
        return self._get_attribute(self._SDM_ATT_MAP["Qci"])

    @Qci.setter
    def Qci(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Qci"], value)

    @property
    def QosLabel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Quality of Service characteristics requested by the SGSN for the primary PDP contexts.
        """
        return self._get_attribute(self._SDM_ATT_MAP["QosLabel"])

    @QosLabel.setter
    def QosLabel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["QosLabel"], value)

    @property
    def QosUpdateValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: QoS update value (in %).
        """
        return self._get_attribute(self._SDM_ATT_MAP["QosUpdateValue"])

    @QosUpdateValue.setter
    def QosUpdateValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["QosUpdateValue"], value)

    @property
    def Tft(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Traffic Flow Template
        """
        return self._get_attribute(self._SDM_ATT_MAP["Tft"])

    @Tft.setter
    def Tft(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Tft"], value)

    @property
    def TimeoutAction(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Action to be execute when a bearer lifetime expires
        """
        return self._get_attribute(self._SDM_ATT_MAP["TimeoutAction"])

    @TimeoutAction.setter
    def TimeoutAction(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TimeoutAction"], value)

    def update(
        self,
        ApnAmbrUpdateValue=None,
        Arp=None,
        CustomTft=None,
        EnableLifetime=None,
        Enabled=None,
        Gbrd=None,
        Gbru=None,
        Lifetime=None,
        Mbrd=None,
        Mbru=None,
        Mode=None,
        Name=None,
        PreemptionCapability=None,
        PreemptionVulnerability=None,
        PriorityLevel=None,
        Qci=None,
        QosLabel=None,
        QosUpdateValue=None,
        Tft=None,
        TimeoutAction=None,
    ):
        # type: (int, int, str, bool, bool, int, int, int, int, int, str, str, bool, bool, int, int, str, int, str, str) -> DedicatedBearer
        """Updates dedicatedBearer resource on the server.

        Args
        ----
        - ApnAmbrUpdateValue (number): APN_AMBR update value (in %).
        - Arp (number): OBSOLETE - Please use preemptionCapability, preemptionVulnerability and priorityLevel.
        - CustomTft (str):
        - EnableLifetime (bool): Enable bearer lifetime control
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Gbrd (number): Guaranteed bitrate for downlink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Gbru (number): Guaranteed bitrate for uplink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Lifetime (number): Bearer lifetime (seconds)
        - Mbrd (number): Maximum bitrate for downlink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Mbru (number): Maximum bitrate for uplink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Mode (str): A dedicated bearer can be requested by the UE (UE requested) or created by the core network without a previous request (Network initiared). If the UE requested mode is selected the dedicated bearer will be activated only if the UE requests it using the UE requested bearer resource modification procedure
        - Name (str): Name of range
        - PreemptionCapability (bool): If true preemption capability is enabled
        - PreemptionVulnerability (bool): If true preemption vulnerability is enabled
        - PriorityLevel (number): Priority Level 1=highest 15=lowest
        - Qci (number): QoS Class Identifier
        - QosLabel (str): Quality of Service characteristics requested by the SGSN for the primary PDP contexts.
        - QosUpdateValue (number): QoS update value (in %).
        - Tft (str): Traffic Flow Template
        - TimeoutAction (str): Action to be execute when a bearer lifetime expires

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ApnAmbrUpdateValue=None,
        Arp=None,
        CustomTft=None,
        EnableLifetime=None,
        Enabled=None,
        Gbrd=None,
        Gbru=None,
        Lifetime=None,
        Mbrd=None,
        Mbru=None,
        Mode=None,
        Name=None,
        PreemptionCapability=None,
        PreemptionVulnerability=None,
        PriorityLevel=None,
        Qci=None,
        QosLabel=None,
        QosUpdateValue=None,
        Tft=None,
        TimeoutAction=None,
    ):
        # type: (int, int, str, bool, bool, int, int, int, int, int, str, str, bool, bool, int, int, str, int, str, str) -> DedicatedBearer
        """Adds a new dedicatedBearer resource on the server and adds it to the container.

        Args
        ----
        - ApnAmbrUpdateValue (number): APN_AMBR update value (in %).
        - Arp (number): OBSOLETE - Please use preemptionCapability, preemptionVulnerability and priorityLevel.
        - CustomTft (str):
        - EnableLifetime (bool): Enable bearer lifetime control
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Gbrd (number): Guaranteed bitrate for downlink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Gbru (number): Guaranteed bitrate for uplink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Lifetime (number): Bearer lifetime (seconds)
        - Mbrd (number): Maximum bitrate for downlink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Mbru (number): Maximum bitrate for uplink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Mode (str): A dedicated bearer can be requested by the UE (UE requested) or created by the core network without a previous request (Network initiared). If the UE requested mode is selected the dedicated bearer will be activated only if the UE requests it using the UE requested bearer resource modification procedure
        - Name (str): Name of range
        - PreemptionCapability (bool): If true preemption capability is enabled
        - PreemptionVulnerability (bool): If true preemption vulnerability is enabled
        - PriorityLevel (number): Priority Level 1=highest 15=lowest
        - Qci (number): QoS Class Identifier
        - QosLabel (str): Quality of Service characteristics requested by the SGSN for the primary PDP contexts.
        - QosUpdateValue (number): QoS update value (in %).
        - Tft (str): Traffic Flow Template
        - TimeoutAction (str): Action to be execute when a bearer lifetime expires

        Returns
        -------
        - self: This instance with all currently retrieved dedicatedBearer resources using find and the newly added dedicatedBearer resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dedicatedBearer resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        ApnAmbrUpdateValue=None,
        Arp=None,
        CustomTft=None,
        EnableLifetime=None,
        Enabled=None,
        Gbrd=None,
        Gbru=None,
        Lifetime=None,
        Mbrd=None,
        Mbru=None,
        Mode=None,
        Name=None,
        ObjectId=None,
        PreemptionCapability=None,
        PreemptionVulnerability=None,
        PriorityLevel=None,
        Qci=None,
        QosLabel=None,
        QosUpdateValue=None,
        Tft=None,
        TimeoutAction=None,
    ):
        # type: (int, int, str, bool, bool, int, int, int, int, int, str, str, str, bool, bool, int, int, str, int, str, str) -> DedicatedBearer
        """Finds and retrieves dedicatedBearer resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dedicatedBearer resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dedicatedBearer resources from the server.

        Args
        ----
        - ApnAmbrUpdateValue (number): APN_AMBR update value (in %).
        - Arp (number): OBSOLETE - Please use preemptionCapability, preemptionVulnerability and priorityLevel.
        - CustomTft (str):
        - EnableLifetime (bool): Enable bearer lifetime control
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Gbrd (number): Guaranteed bitrate for downlink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Gbru (number): Guaranteed bitrate for uplink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Lifetime (number): Bearer lifetime (seconds)
        - Mbrd (number): Maximum bitrate for downlink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Mbru (number): Maximum bitrate for uplink. Maximum bitrate for uplink. For December '09 and December '10 spec versions the maximum value that can be encoded is 1,099,511,627,775 kbps.
        - Mode (str): A dedicated bearer can be requested by the UE (UE requested) or created by the core network without a previous request (Network initiared). If the UE requested mode is selected the dedicated bearer will be activated only if the UE requests it using the UE requested bearer resource modification procedure
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object
        - PreemptionCapability (bool): If true preemption capability is enabled
        - PreemptionVulnerability (bool): If true preemption vulnerability is enabled
        - PriorityLevel (number): Priority Level 1=highest 15=lowest
        - Qci (number): QoS Class Identifier
        - QosLabel (str): Quality of Service characteristics requested by the SGSN for the primary PDP contexts.
        - QosUpdateValue (number): QoS update value (in %).
        - Tft (str): Traffic Flow Template
        - TimeoutAction (str): Action to be execute when a bearer lifetime expires

        Returns
        -------
        - self: This instance with matching dedicatedBearer resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dedicatedBearer data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dedicatedBearer resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

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
