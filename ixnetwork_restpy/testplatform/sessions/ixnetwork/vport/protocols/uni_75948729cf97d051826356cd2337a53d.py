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


class Uni(Base):
    """It signifies the user network interface.
    The Uni class encapsulates a list of uni resources that are managed by the user.
    A list of resources can be retrieved from the server using the Uni.find() method.
    The list can be managed by using the Uni.add() and Uni.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "uni"
    _SDM_ATT_MAP = {
        "DataInstance": "dataInstance",
        "EnablePollingVerificationTimer": "enablePollingVerificationTimer",
        "Enabled": "enabled",
        "IsEvcStatusLearnedInfoRefreshed": "isEvcStatusLearnedInfoRefreshed",
        "IsLmiStatusLearnedInfoRefreshed": "isLmiStatusLearnedInfoRefreshed",
        "IsUniStatusLearnedInfoRefreshed": "isUniStatusLearnedInfoRefreshed",
        "Mode": "mode",
        "OverrideDataInstance": "overrideDataInstance",
        "OverrideReceiveSequenceNumber": "overrideReceiveSequenceNumber",
        "OverrideSendSequenceNumber": "overrideSendSequenceNumber",
        "PollingCounter": "pollingCounter",
        "PollingTimer": "pollingTimer",
        "PollingVerificationTimer": "pollingVerificationTimer",
        "ProtocolInterface": "protocolInterface",
        "ProtocolVersion": "protocolVersion",
        "ReceiveSequenceNumber": "receiveSequenceNumber",
        "SendSequenceNumber": "sendSequenceNumber",
        "StatusCounter": "statusCounter",
    }
    _SDM_ENUM_MAP = {
        "mode": ["uniC", "uniN"],
    }

    def __init__(self, parent, list_op=False):
        super(Uni, self).__init__(parent, list_op)

    @property
    def Evc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evc_7500f87dab98e04d2ff46357ef4c0a19.Evc): An instance of the Evc class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evc_7500f87dab98e04d2ff46357ef4c0a19 import (
            Evc,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Evc", None) is not None:
                return self._properties.get("Evc")
        return Evc(self)

    @property
    def EvcStatusLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evcstatuslearnedinfo_c3b2e43e894cb8069d3a77cd8cf95e2c.EvcStatusLearnedInfo): An instance of the EvcStatusLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evcstatuslearnedinfo_c3b2e43e894cb8069d3a77cd8cf95e2c import (
            EvcStatusLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EvcStatusLearnedInfo", None) is not None:
                return self._properties.get("EvcStatusLearnedInfo")
        return EvcStatusLearnedInfo(self)

    @property
    def LmiStatusLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lmistatuslearnedinfo_eafb3fd4a42f8851d9c418f937223a26.LmiStatusLearnedInfo): An instance of the LmiStatusLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lmistatuslearnedinfo_eafb3fd4a42f8851d9c418f937223a26 import (
            LmiStatusLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LmiStatusLearnedInfo", None) is not None:
                return self._properties.get("LmiStatusLearnedInfo")
        return LmiStatusLearnedInfo(self)

    @property
    def UniStatus(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.unistatus_0096bbbaf5ab6dac178a8f65c71f8937.UniStatus): An instance of the UniStatus class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.unistatus_0096bbbaf5ab6dac178a8f65c71f8937 import (
            UniStatus,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("UniStatus", None) is not None:
                return self._properties.get("UniStatus")
        return UniStatus(self)

    @property
    def UniStatusLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.unistatuslearnedinfo_33a9891d20157d14ba19c5cd0bc4333e.UniStatusLearnedInfo): An instance of the UniStatusLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.unistatuslearnedinfo_33a9891d20157d14ba19c5cd0bc4333e import (
            UniStatusLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("UniStatusLearnedInfo", None) is not None:
                return self._properties.get("UniStatusLearnedInfo")
        return UniStatusLearnedInfo(self)

    @property
    def DataInstance(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This four-octet field indicates the Data Instance value to be sent in transmitted packet. It will be configurable only if Override Data Instance is enabled. By default it is grayed out with default value 0 for UNI-C and 1 for UNI-N. Max 4294967295, Min 0 for UNI-C and 1 for UNI- V. Change of value in this field takes effect when protocol is running.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataInstance"])

    @DataInstance.setter
    def DataInstance(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DataInstance"], value)

    @property
    def EnablePollingVerificationTimer(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, it shows the default value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePollingVerificationTimer"])

    @EnablePollingVerificationTimer.setter
    def EnablePollingVerificationTimer(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePollingVerificationTimer"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: It signifies whether the protocol is enabled or disabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def IsEvcStatusLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: It checks whether the EVC status learned info is refreshed or not.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsEvcStatusLearnedInfoRefreshed"])

    @property
    def IsLmiStatusLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: It checks whether the LMI status learned info is refreshed or not.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsLmiStatusLearnedInfoRefreshed"])

    @property
    def IsUniStatusLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: It checks whether the UNI status learned info is refreshed or not.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsUniStatusLearnedInfoRefreshed"])

    @property
    def Mode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(uniC | uniN): It is a type of UNI end point.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mode"])

    @Mode.setter
    def Mode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mode"], value)

    @property
    def OverrideDataInstance(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, it updates the Data Instance field of Data Instance Information Element (IE). Default is false. Change of value in this field takes effect when protocol is running.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OverrideDataInstance"])

    @OverrideDataInstance.setter
    def OverrideDataInstance(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OverrideDataInstance"], value)

    @property
    def OverrideReceiveSequenceNumber(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, it updates the receive sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OverrideReceiveSequenceNumber"])

    @OverrideReceiveSequenceNumber.setter
    def OverrideReceiveSequenceNumber(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OverrideReceiveSequenceNumber"], value)

    @property
    def OverrideSendSequenceNumber(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, it updates the send sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OverrideSendSequenceNumber"])

    @OverrideSendSequenceNumber.setter
    def OverrideSendSequenceNumber(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OverrideSendSequenceNumber"], value)

    @property
    def PollingCounter(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the full status (status of UNI and all EVCs) polling count. Range is 1- 65k. Default is 360. This is applicable only for UNI-C.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PollingCounter"])

    @PollingCounter.setter
    def PollingCounter(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PollingCounter"], value)

    @property
    def PollingTimer(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The range is 5-30 in seconds. Default is 10 seconds. This is applicable only for UNI-C.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PollingTimer"])

    @PollingTimer.setter
    def PollingTimer(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PollingTimer"], value)

    @property
    def PollingVerificationTimer(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This is applicable only for UNI-N. Range is 5-30 secs. Default is 15 seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PollingVerificationTimer"])

    @PollingVerificationTimer.setter
    def PollingVerificationTimer(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PollingVerificationTimer"], value)

    @property
    def ProtocolInterface(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/interface): It signifies the configured protocol interface. User has to select one interface to enable configuring UNI. Until and unless protocol interface is selected user will not be able to configure and enable UNI. Default is unassigned.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProtocolInterface"])

    @ProtocolInterface.setter
    def ProtocolInterface(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProtocolInterface"], value)

    @property
    def ProtocolVersion(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This one-octet field indicates the version supported by the sending entity (UNI-C or UNI-N). Default value is ox1. Max 255, Min - 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProtocolVersion"])

    @ProtocolVersion.setter
    def ProtocolVersion(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProtocolVersion"], value)

    @property
    def ReceiveSequenceNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This one-octet field indicates the sequence number to be sent in the 'Receive Sequence Number' in transmitted packet. It will be configurable only if Override Receive Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReceiveSequenceNumber"])

    @ReceiveSequenceNumber.setter
    def ReceiveSequenceNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReceiveSequenceNumber"], value)

    @property
    def SendSequenceNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This one-octet field indicates the sequence number to be sent in the 'Send Sequence Number' field in transmitted packet. It will be configurable only if Override Send Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SendSequenceNumber"])

    @SendSequenceNumber.setter
    def SendSequenceNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SendSequenceNumber"], value)

    @property
    def StatusCounter(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the count of consecutive errors. Range is 2 10. Default is 4.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StatusCounter"])

    @StatusCounter.setter
    def StatusCounter(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StatusCounter"], value)

    def update(
        self,
        DataInstance=None,
        EnablePollingVerificationTimer=None,
        Enabled=None,
        Mode=None,
        OverrideDataInstance=None,
        OverrideReceiveSequenceNumber=None,
        OverrideSendSequenceNumber=None,
        PollingCounter=None,
        PollingTimer=None,
        PollingVerificationTimer=None,
        ProtocolInterface=None,
        ProtocolVersion=None,
        ReceiveSequenceNumber=None,
        SendSequenceNumber=None,
        StatusCounter=None,
    ):
        # type: (int, bool, bool, str, bool, bool, bool, int, int, int, str, int, int, int, int) -> Uni
        """Updates uni resource on the server.

        Args
        ----
        - DataInstance (number): This four-octet field indicates the Data Instance value to be sent in transmitted packet. It will be configurable only if Override Data Instance is enabled. By default it is grayed out with default value 0 for UNI-C and 1 for UNI-N. Max 4294967295, Min 0 for UNI-C and 1 for UNI- V. Change of value in this field takes effect when protocol is running.
        - EnablePollingVerificationTimer (bool): If enabled, it shows the default value.
        - Enabled (bool): It signifies whether the protocol is enabled or disabled.
        - Mode (str(uniC | uniN)): It is a type of UNI end point.
        - OverrideDataInstance (bool): If enabled, it updates the Data Instance field of Data Instance Information Element (IE). Default is false. Change of value in this field takes effect when protocol is running.
        - OverrideReceiveSequenceNumber (bool): If enabled, it updates the receive sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.
        - OverrideSendSequenceNumber (bool): If enabled, it updates the send sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.
        - PollingCounter (number): It signifies the full status (status of UNI and all EVCs) polling count. Range is 1- 65k. Default is 360. This is applicable only for UNI-C.
        - PollingTimer (number): The range is 5-30 in seconds. Default is 10 seconds. This is applicable only for UNI-C.
        - PollingVerificationTimer (number): This is applicable only for UNI-N. Range is 5-30 secs. Default is 15 seconds.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): It signifies the configured protocol interface. User has to select one interface to enable configuring UNI. Until and unless protocol interface is selected user will not be able to configure and enable UNI. Default is unassigned.
        - ProtocolVersion (number): This one-octet field indicates the version supported by the sending entity (UNI-C or UNI-N). Default value is ox1. Max 255, Min - 1.
        - ReceiveSequenceNumber (number): This one-octet field indicates the sequence number to be sent in the 'Receive Sequence Number' in transmitted packet. It will be configurable only if Override Receive Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.
        - SendSequenceNumber (number): This one-octet field indicates the sequence number to be sent in the 'Send Sequence Number' field in transmitted packet. It will be configurable only if Override Send Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.
        - StatusCounter (number): It signifies the count of consecutive errors. Range is 2 10. Default is 4.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        DataInstance=None,
        EnablePollingVerificationTimer=None,
        Enabled=None,
        Mode=None,
        OverrideDataInstance=None,
        OverrideReceiveSequenceNumber=None,
        OverrideSendSequenceNumber=None,
        PollingCounter=None,
        PollingTimer=None,
        PollingVerificationTimer=None,
        ProtocolInterface=None,
        ProtocolVersion=None,
        ReceiveSequenceNumber=None,
        SendSequenceNumber=None,
        StatusCounter=None,
    ):
        # type: (int, bool, bool, str, bool, bool, bool, int, int, int, str, int, int, int, int) -> Uni
        """Adds a new uni resource on the server and adds it to the container.

        Args
        ----
        - DataInstance (number): This four-octet field indicates the Data Instance value to be sent in transmitted packet. It will be configurable only if Override Data Instance is enabled. By default it is grayed out with default value 0 for UNI-C and 1 for UNI-N. Max 4294967295, Min 0 for UNI-C and 1 for UNI- V. Change of value in this field takes effect when protocol is running.
        - EnablePollingVerificationTimer (bool): If enabled, it shows the default value.
        - Enabled (bool): It signifies whether the protocol is enabled or disabled.
        - Mode (str(uniC | uniN)): It is a type of UNI end point.
        - OverrideDataInstance (bool): If enabled, it updates the Data Instance field of Data Instance Information Element (IE). Default is false. Change of value in this field takes effect when protocol is running.
        - OverrideReceiveSequenceNumber (bool): If enabled, it updates the receive sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.
        - OverrideSendSequenceNumber (bool): If enabled, it updates the send sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.
        - PollingCounter (number): It signifies the full status (status of UNI and all EVCs) polling count. Range is 1- 65k. Default is 360. This is applicable only for UNI-C.
        - PollingTimer (number): The range is 5-30 in seconds. Default is 10 seconds. This is applicable only for UNI-C.
        - PollingVerificationTimer (number): This is applicable only for UNI-N. Range is 5-30 secs. Default is 15 seconds.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): It signifies the configured protocol interface. User has to select one interface to enable configuring UNI. Until and unless protocol interface is selected user will not be able to configure and enable UNI. Default is unassigned.
        - ProtocolVersion (number): This one-octet field indicates the version supported by the sending entity (UNI-C or UNI-N). Default value is ox1. Max 255, Min - 1.
        - ReceiveSequenceNumber (number): This one-octet field indicates the sequence number to be sent in the 'Receive Sequence Number' in transmitted packet. It will be configurable only if Override Receive Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.
        - SendSequenceNumber (number): This one-octet field indicates the sequence number to be sent in the 'Send Sequence Number' field in transmitted packet. It will be configurable only if Override Send Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.
        - StatusCounter (number): It signifies the count of consecutive errors. Range is 2 10. Default is 4.

        Returns
        -------
        - self: This instance with all currently retrieved uni resources using find and the newly added uni resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained uni resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        DataInstance=None,
        EnablePollingVerificationTimer=None,
        Enabled=None,
        IsEvcStatusLearnedInfoRefreshed=None,
        IsLmiStatusLearnedInfoRefreshed=None,
        IsUniStatusLearnedInfoRefreshed=None,
        Mode=None,
        OverrideDataInstance=None,
        OverrideReceiveSequenceNumber=None,
        OverrideSendSequenceNumber=None,
        PollingCounter=None,
        PollingTimer=None,
        PollingVerificationTimer=None,
        ProtocolInterface=None,
        ProtocolVersion=None,
        ReceiveSequenceNumber=None,
        SendSequenceNumber=None,
        StatusCounter=None,
    ):
        # type: (int, bool, bool, bool, bool, bool, str, bool, bool, bool, int, int, int, str, int, int, int, int) -> Uni
        """Finds and retrieves uni resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve uni resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all uni resources from the server.

        Args
        ----
        - DataInstance (number): This four-octet field indicates the Data Instance value to be sent in transmitted packet. It will be configurable only if Override Data Instance is enabled. By default it is grayed out with default value 0 for UNI-C and 1 for UNI-N. Max 4294967295, Min 0 for UNI-C and 1 for UNI- V. Change of value in this field takes effect when protocol is running.
        - EnablePollingVerificationTimer (bool): If enabled, it shows the default value.
        - Enabled (bool): It signifies whether the protocol is enabled or disabled.
        - IsEvcStatusLearnedInfoRefreshed (bool): It checks whether the EVC status learned info is refreshed or not.
        - IsLmiStatusLearnedInfoRefreshed (bool): It checks whether the LMI status learned info is refreshed or not.
        - IsUniStatusLearnedInfoRefreshed (bool): It checks whether the UNI status learned info is refreshed or not.
        - Mode (str(uniC | uniN)): It is a type of UNI end point.
        - OverrideDataInstance (bool): If enabled, it updates the Data Instance field of Data Instance Information Element (IE). Default is false. Change of value in this field takes effect when protocol is running.
        - OverrideReceiveSequenceNumber (bool): If enabled, it updates the receive sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.
        - OverrideSendSequenceNumber (bool): If enabled, it updates the send sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.
        - PollingCounter (number): It signifies the full status (status of UNI and all EVCs) polling count. Range is 1- 65k. Default is 360. This is applicable only for UNI-C.
        - PollingTimer (number): The range is 5-30 in seconds. Default is 10 seconds. This is applicable only for UNI-C.
        - PollingVerificationTimer (number): This is applicable only for UNI-N. Range is 5-30 secs. Default is 15 seconds.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): It signifies the configured protocol interface. User has to select one interface to enable configuring UNI. Until and unless protocol interface is selected user will not be able to configure and enable UNI. Default is unassigned.
        - ProtocolVersion (number): This one-octet field indicates the version supported by the sending entity (UNI-C or UNI-N). Default value is ox1. Max 255, Min - 1.
        - ReceiveSequenceNumber (number): This one-octet field indicates the sequence number to be sent in the 'Receive Sequence Number' in transmitted packet. It will be configurable only if Override Receive Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.
        - SendSequenceNumber (number): This one-octet field indicates the sequence number to be sent in the 'Send Sequence Number' field in transmitted packet. It will be configurable only if Override Send Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.
        - StatusCounter (number): It signifies the count of consecutive errors. Range is 2 10. Default is 4.

        Returns
        -------
        - self: This instance with matching uni resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of uni data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the uni resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def RefreshEvcStatusLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshEvcStatusLearnedInfo operation on the server.

        NOT DEFINED

        refreshEvcStatusLearnedInfo(async_operation=bool)bool
        -----------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
            "refreshEvcStatusLearnedInfo", payload=payload, response_object=None
        )

    def RefreshLmiStatusLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshLmiStatusLearnedInfo operation on the server.

        NOT DEFINED

        refreshLmiStatusLearnedInfo(async_operation=bool)bool
        -----------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
            "refreshLmiStatusLearnedInfo", payload=payload, response_object=None
        )

    def RefreshUniStatusLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshUniStatusLearnedInfo operation on the server.

        NOT DEFINED

        refreshUniStatusLearnedInfo(async_operation=bool)bool
        -----------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
            "refreshUniStatusLearnedInfo", payload=payload, response_object=None
        )
