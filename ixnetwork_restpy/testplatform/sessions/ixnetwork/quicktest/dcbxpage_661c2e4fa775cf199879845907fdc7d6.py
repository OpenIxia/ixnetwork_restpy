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


class DcbxPage(Base):
    """This object specifies the attributes for DCBX Range specific options that are available when the DCBX stack is enabled on the FCoE configuration.
    The DcbxPage class encapsulates a list of dcbxPage resources that are managed by the system.
    A list of resources can be retrieved from the server using the DcbxPage.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "dcbxPage"
    _SDM_ATT_MAP = {
        "ChassisId": "chassisId",
        "ChassisIdIncrement": "chassisIdIncrement",
        "ControlTlvMaxVersion": "controlTlvMaxVersion",
        "DcbxEnable": "dcbxEnable",
        "DcbxSubtype": "dcbxSubtype",
        "FailOnMismatch": "failOnMismatch",
        "FlapLinkOnStart": "flapLinkOnStart",
        "HoldTime": "holdTime",
        "IsInnerWizard": "isInnerWizard",
        "LldpEnable": "lldpEnable",
        "Oui": "oui",
        "PortIdIncrement": "portIdIncrement",
        "PortIdInterfaceName": "portIdInterfaceName",
        "PortIdMacAddress": "portIdMacAddress",
        "PortIdSubType": "portIdSubType",
        "TxInterval": "txInterval",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(DcbxPage, self).__init__(parent, list_op)

    @property
    def ChassisId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The chassis identification of the device that transmits the LLDP frame. Thereceiving LLDP agent combines the Chassis ID and Port ID to represent theentity connected to the port that receives the frame.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ChassisId"])

    @ChassisId.setter
    def ChassisId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ChassisId"], value)

    @property
    def ChassisIdIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Chassis ID increment value. If more than one port group is selected forconfiguration, the wizard uses this increment value to create a unique Chassis IDfor each port group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ChassisIdIncrement"])

    @ChassisIdIncrement.setter
    def ChassisIdIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ChassisIdIncrement"], value)

    @property
    def ControlTlvMaxVersion(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The highest DCBX protocol version supported by the system. Version numbersrange from 0 to 255.The default value is 255.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControlTlvMaxVersion"])

    @ControlTlvMaxVersion.setter
    def ControlTlvMaxVersion(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ControlTlvMaxVersion"], value)

    @property
    def DcbxEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, the emulated DCB device includes the DCBX Control TLV as well assupported feature TLVs in the LLDPDUs.If cleared, the emulated DCB device does not include any DCBX TLVs in theLLDPDUs that it transmits from its LLDP-enabled ports.By default it is selected.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DcbxEnable"])

    @DcbxEnable.setter
    def DcbxEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DcbxEnable"], value)

    @property
    def DcbxSubtype(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The organizationally-defined DCBX subtype:Intel 1.0IEEE 1.01Each subtype has a unique TLV structure.The default value is IEEE 1.01.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DcbxSubtype"])

    @DcbxSubtype.setter
    def DcbxSubtype(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DcbxSubtype"], value)

    @property
    def FailOnMismatch(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This signifies the DCBX 802.1Qaz Priority-based Flow Control and Application Priority TLVs negotiation will be declared as failed if the configurations at both ends do not match.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FailOnMismatch"])

    @FailOnMismatch.setter
    def FailOnMismatch(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FailOnMismatch"], value)

    @property
    def FlapLinkOnStart(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Change the interface status (DOWN, then UP) to notify the switch that DCBX isabout to restart the negotiation.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlapLinkOnStart"])

    @FlapLinkOnStart.setter
    def FlapLinkOnStart(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlapLinkOnStart"], value)

    @property
    def HoldTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The multiplier used to calculate the actual TTL value that is sent in the LLDP message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["HoldTime"])

    @HoldTime.setter
    def HoldTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["HoldTime"], value)

    @property
    def IsInnerWizard(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsInnerWizard"])

    @IsInnerWizard.setter
    def IsInnerWizard(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsInnerWizard"], value)

    @property
    def LldpEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When enabled, the emulated DCB device includes the optional LLDP TLVs thatyou select and configure for the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LldpEnable"])

    @LldpEnable.setter
    def LldpEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LldpEnable"], value)

    @property
    def Oui(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The three-byte Organizationally Unique Identifier (OUI) to use in the DCBX TLV.The default OUI is 00.1B.21 (the Intel OUI).
        """
        return self._get_attribute(self._SDM_ATT_MAP["Oui"])

    @Oui.setter
    def Oui(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Oui"], value)

    @property
    def PortIdIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Port ID increment value. If more than one port group is selected forconfiguration, and you are using MAC addresses for Port IDs, the wizard usesthis increment value to create a unique Port ID for each port group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortIdIncrement"])

    @PortIdIncrement.setter
    def PortIdIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortIdIncrement"], value)

    @property
    def PortIdInterfaceName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the port ID interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortIdInterfaceName"])

    @PortIdInterfaceName.setter
    def PortIdInterfaceName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortIdInterfaceName"], value)

    @property
    def PortIdMacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The value to use when MAC addresses are used for the Port IDs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortIdMacAddress"])

    @PortIdMacAddress.setter
    def PortIdMacAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortIdMacAddress"], value)

    @property
    def PortIdSubType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The type of identifier used for the Port ID. The default is MAC Address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortIdSubType"])

    @PortIdSubType.setter
    def PortIdSubType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortIdSubType"], value)

    @property
    def TxInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The interval at which LLDP frames are transmitted on behalf of this LLDP agent.The default value is 30, the minimum is 5, and the maximum is 32768.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxInterval"])

    @TxInterval.setter
    def TxInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxInterval"], value)

    def update(
        self,
        ChassisId=None,
        ChassisIdIncrement=None,
        ControlTlvMaxVersion=None,
        DcbxEnable=None,
        DcbxSubtype=None,
        FailOnMismatch=None,
        FlapLinkOnStart=None,
        HoldTime=None,
        IsInnerWizard=None,
        LldpEnable=None,
        Oui=None,
        PortIdIncrement=None,
        PortIdInterfaceName=None,
        PortIdMacAddress=None,
        PortIdSubType=None,
        TxInterval=None,
    ):
        # type: (str, str, int, bool, int, bool, bool, int, bool, bool, str, str, str, str, int, int) -> DcbxPage
        """Updates dcbxPage resource on the server.

        Args
        ----
        - ChassisId (str): The chassis identification of the device that transmits the LLDP frame. Thereceiving LLDP agent combines the Chassis ID and Port ID to represent theentity connected to the port that receives the frame.
        - ChassisIdIncrement (str): The Chassis ID increment value. If more than one port group is selected forconfiguration, the wizard uses this increment value to create a unique Chassis IDfor each port group.
        - ControlTlvMaxVersion (number): The highest DCBX protocol version supported by the system. Version numbersrange from 0 to 255.The default value is 255.
        - DcbxEnable (bool): If selected, the emulated DCB device includes the DCBX Control TLV as well assupported feature TLVs in the LLDPDUs.If cleared, the emulated DCB device does not include any DCBX TLVs in theLLDPDUs that it transmits from its LLDP-enabled ports.By default it is selected.
        - DcbxSubtype (number): The organizationally-defined DCBX subtype:Intel 1.0IEEE 1.01Each subtype has a unique TLV structure.The default value is IEEE 1.01.
        - FailOnMismatch (bool): This signifies the DCBX 802.1Qaz Priority-based Flow Control and Application Priority TLVs negotiation will be declared as failed if the configurations at both ends do not match.
        - FlapLinkOnStart (bool): Change the interface status (DOWN, then UP) to notify the switch that DCBX isabout to restart the negotiation.
        - HoldTime (number): The multiplier used to calculate the actual TTL value that is sent in the LLDP message.
        - IsInnerWizard (bool): NOT DEFINED
        - LldpEnable (bool): When enabled, the emulated DCB device includes the optional LLDP TLVs thatyou select and configure for the test.
        - Oui (str): The three-byte Organizationally Unique Identifier (OUI) to use in the DCBX TLV.The default OUI is 00.1B.21 (the Intel OUI).
        - PortIdIncrement (str): The Port ID increment value. If more than one port group is selected forconfiguration, and you are using MAC addresses for Port IDs, the wizard usesthis increment value to create a unique Port ID for each port group.
        - PortIdInterfaceName (str): The name of the port ID interface.
        - PortIdMacAddress (str): The value to use when MAC addresses are used for the Port IDs.
        - PortIdSubType (number): The type of identifier used for the Port ID. The default is MAC Address.
        - TxInterval (number): The interval at which LLDP frames are transmitted on behalf of this LLDP agent.The default value is 30, the minimum is 5, and the maximum is 32768.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ChassisId=None,
        ChassisIdIncrement=None,
        ControlTlvMaxVersion=None,
        DcbxEnable=None,
        DcbxSubtype=None,
        FailOnMismatch=None,
        FlapLinkOnStart=None,
        HoldTime=None,
        IsInnerWizard=None,
        LldpEnable=None,
        Oui=None,
        PortIdIncrement=None,
        PortIdInterfaceName=None,
        PortIdMacAddress=None,
        PortIdSubType=None,
        TxInterval=None,
    ):
        # type: (str, str, int, bool, int, bool, bool, int, bool, bool, str, str, str, str, int, int) -> DcbxPage
        """Adds a new dcbxPage resource on the json, only valid with batch add utility

        Args
        ----
        - ChassisId (str): The chassis identification of the device that transmits the LLDP frame. Thereceiving LLDP agent combines the Chassis ID and Port ID to represent theentity connected to the port that receives the frame.
        - ChassisIdIncrement (str): The Chassis ID increment value. If more than one port group is selected forconfiguration, the wizard uses this increment value to create a unique Chassis IDfor each port group.
        - ControlTlvMaxVersion (number): The highest DCBX protocol version supported by the system. Version numbersrange from 0 to 255.The default value is 255.
        - DcbxEnable (bool): If selected, the emulated DCB device includes the DCBX Control TLV as well assupported feature TLVs in the LLDPDUs.If cleared, the emulated DCB device does not include any DCBX TLVs in theLLDPDUs that it transmits from its LLDP-enabled ports.By default it is selected.
        - DcbxSubtype (number): The organizationally-defined DCBX subtype:Intel 1.0IEEE 1.01Each subtype has a unique TLV structure.The default value is IEEE 1.01.
        - FailOnMismatch (bool): This signifies the DCBX 802.1Qaz Priority-based Flow Control and Application Priority TLVs negotiation will be declared as failed if the configurations at both ends do not match.
        - FlapLinkOnStart (bool): Change the interface status (DOWN, then UP) to notify the switch that DCBX isabout to restart the negotiation.
        - HoldTime (number): The multiplier used to calculate the actual TTL value that is sent in the LLDP message.
        - IsInnerWizard (bool): NOT DEFINED
        - LldpEnable (bool): When enabled, the emulated DCB device includes the optional LLDP TLVs thatyou select and configure for the test.
        - Oui (str): The three-byte Organizationally Unique Identifier (OUI) to use in the DCBX TLV.The default OUI is 00.1B.21 (the Intel OUI).
        - PortIdIncrement (str): The Port ID increment value. If more than one port group is selected forconfiguration, and you are using MAC addresses for Port IDs, the wizard usesthis increment value to create a unique Port ID for each port group.
        - PortIdInterfaceName (str): The name of the port ID interface.
        - PortIdMacAddress (str): The value to use when MAC addresses are used for the Port IDs.
        - PortIdSubType (number): The type of identifier used for the Port ID. The default is MAC Address.
        - TxInterval (number): The interval at which LLDP frames are transmitted on behalf of this LLDP agent.The default value is 30, the minimum is 5, and the maximum is 32768.

        Returns
        -------
        - self: This instance with all currently retrieved dcbxPage resources using find and the newly added dcbxPage resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ChassisId=None,
        ChassisIdIncrement=None,
        ControlTlvMaxVersion=None,
        DcbxEnable=None,
        DcbxSubtype=None,
        FailOnMismatch=None,
        FlapLinkOnStart=None,
        HoldTime=None,
        IsInnerWizard=None,
        LldpEnable=None,
        Oui=None,
        PortIdIncrement=None,
        PortIdInterfaceName=None,
        PortIdMacAddress=None,
        PortIdSubType=None,
        TxInterval=None,
    ):
        # type: (str, str, int, bool, int, bool, bool, int, bool, bool, str, str, str, str, int, int) -> DcbxPage
        """Finds and retrieves dcbxPage resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dcbxPage resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dcbxPage resources from the server.

        Args
        ----
        - ChassisId (str): The chassis identification of the device that transmits the LLDP frame. Thereceiving LLDP agent combines the Chassis ID and Port ID to represent theentity connected to the port that receives the frame.
        - ChassisIdIncrement (str): The Chassis ID increment value. If more than one port group is selected forconfiguration, the wizard uses this increment value to create a unique Chassis IDfor each port group.
        - ControlTlvMaxVersion (number): The highest DCBX protocol version supported by the system. Version numbersrange from 0 to 255.The default value is 255.
        - DcbxEnable (bool): If selected, the emulated DCB device includes the DCBX Control TLV as well assupported feature TLVs in the LLDPDUs.If cleared, the emulated DCB device does not include any DCBX TLVs in theLLDPDUs that it transmits from its LLDP-enabled ports.By default it is selected.
        - DcbxSubtype (number): The organizationally-defined DCBX subtype:Intel 1.0IEEE 1.01Each subtype has a unique TLV structure.The default value is IEEE 1.01.
        - FailOnMismatch (bool): This signifies the DCBX 802.1Qaz Priority-based Flow Control and Application Priority TLVs negotiation will be declared as failed if the configurations at both ends do not match.
        - FlapLinkOnStart (bool): Change the interface status (DOWN, then UP) to notify the switch that DCBX isabout to restart the negotiation.
        - HoldTime (number): The multiplier used to calculate the actual TTL value that is sent in the LLDP message.
        - IsInnerWizard (bool): NOT DEFINED
        - LldpEnable (bool): When enabled, the emulated DCB device includes the optional LLDP TLVs thatyou select and configure for the test.
        - Oui (str): The three-byte Organizationally Unique Identifier (OUI) to use in the DCBX TLV.The default OUI is 00.1B.21 (the Intel OUI).
        - PortIdIncrement (str): The Port ID increment value. If more than one port group is selected forconfiguration, and you are using MAC addresses for Port IDs, the wizard usesthis increment value to create a unique Port ID for each port group.
        - PortIdInterfaceName (str): The name of the port ID interface.
        - PortIdMacAddress (str): The value to use when MAC addresses are used for the Port IDs.
        - PortIdSubType (number): The type of identifier used for the Port ID. The default is MAC Address.
        - TxInterval (number): The interval at which LLDP frames are transmitted on behalf of this LLDP agent.The default value is 30, the minimum is 5, and the maximum is 32768.

        Returns
        -------
        - self: This instance with matching dcbxPage resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dcbxPage data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dcbxPage resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the apply operation on the server.

        Applies the specified Quick Test.

        apply(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        return self._execute("apply", payload=payload, response_object=None)

    def ApplyAsync(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyAsync operation on the server.

        applyAsync(async_operation=bool)
        --------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        return self._execute("applyAsync", payload=payload, response_object=None)

    def ApplyAsyncResult(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the applyAsyncResult operation on the server.

        applyAsyncResult(async_operation=bool)bool
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool:

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
        return self._execute("applyAsyncResult", payload=payload, response_object=None)

    def ApplyITWizardConfiguration(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the specified Quick Test.

        applyITWizardConfiguration(async_operation=bool)
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
            "applyITWizardConfiguration", payload=payload, response_object=None
        )

    def GenerateReport(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the generateReport operation on the server.

        Generate a PDF report for the last succesfull test run.

        generateReport(async_operation=bool)string
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: This method is asynchronous and has no return value.

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
        return self._execute("generateReport", payload=payload, response_object=None)

    def Run(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the run operation on the server.

        Starts the specified Quick Test and waits for its execution to finish.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        run(async_operation=bool)list
        -----------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        run(InputParameters=string, async_operation=bool)list
        -----------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

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
        return self._execute("run", payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the specified Quick Test.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(InputParameters=string, async_operation=bool)
        ---------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        return self._execute("start", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stops the currently running Quick Test.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        return self._execute("stop", payload=payload, response_object=None)

    def WaitForTest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the waitForTest operation on the server.

        Waits for the execution of the specified Quick Test to be completed.

        waitForTest(async_operation=bool)list
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

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
        return self._execute("waitForTest", payload=payload, response_object=None)
