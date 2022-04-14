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


class DcbxRange(Base):
    """
    The DcbxRange class encapsulates a required dcbxRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "dcbxRange"
    _SDM_ATT_MAP = {
        "ChassisId": "chassisId",
        "ControlTlvMaxVersion": "controlTlvMaxVersion",
        "DcbxEnable": "dcbxEnable",
        "DcbxSubtype": "dcbxSubtype",
        "DestMacAddress": "destMacAddress",
        "Enabled": "enabled",
        "FastInitEnable": "fastInitEnable",
        "HoldTime": "holdTime",
        "Name": "name",
        "ObjectId": "objectId",
        "Oui": "oui",
        "PortIdInterfaceName": "portIdInterfaceName",
        "PortIdMacAddress": "portIdMacAddress",
        "PortIdSubType": "portIdSubType",
        "TxDelay": "txDelay",
        "TxInterval": "txInterval",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(DcbxRange, self).__init__(parent, list_op)

    @property
    def DcbxTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlv_37d6aa3b470efb288cbc76a9c77c1804.DcbxTlv): An instance of the DcbxTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlv_37d6aa3b470efb288cbc76a9c77c1804 import (
            DcbxTlv,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlv", None) is not None:
                return self._properties.get("DcbxTlv")
        return DcbxTlv(self)

    @property
    def DcbxTlvQaz(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvqaz_208cf6f4022a5582a454a5c53e9a3b60.DcbxTlvQaz): An instance of the DcbxTlvQaz class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvqaz_208cf6f4022a5582a454a5c53e9a3b60 import (
            DcbxTlvQaz,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DcbxTlvQaz", None) is not None:
                return self._properties.get("DcbxTlvQaz")
        return DcbxTlvQaz(self)

    @property
    def LldpTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.lldptlv_d5fbeb9514995f839bf297520a09968a.LldpTlv): An instance of the LldpTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.lldptlv_d5fbeb9514995f839bf297520a09968a import (
            LldpTlv,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LldpTlv", None) is not None:
                return self._properties.get("LldpTlv")
        return LldpTlv(self)

    @property
    def ChassisId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Chassis identification for thedevice that transmitted the LLDP frame.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ChassisId"])

    @ChassisId.setter
    def ChassisId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ChassisId"], value)

    @property
    def ControlTlvMaxVersion(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Highest DCBX protocol version supported by the system.
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
        - bool: Enable DCBX TLVs.
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
        - number: Organizationally defined subtype.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DcbxSubtype"])

    @DcbxSubtype.setter
    def DcbxSubtype(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DcbxSubtype"], value)

    @property
    def DestMacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The destination MAC address value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestMacAddress"])

    @DestMacAddress.setter
    def DestMacAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DestMacAddress"], value)

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
    def FastInitEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable fast initial retransmission.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FastInitEnable"])

    @FastInitEnable.setter
    def FastInitEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FastInitEnable"], value)

    @property
    def HoldTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Multiplier to get actual TTL value used in an LLDPDU.
        """
        return self._get_attribute(self._SDM_ATT_MAP["HoldTime"])

    @HoldTime.setter
    def HoldTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["HoldTime"], value)

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
    def Oui(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The vendor identifier value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Oui"])

    @Oui.setter
    def Oui(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Oui"], value)

    @property
    def PortIdInterfaceName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Port identification for the device that sent the LLDP frame.
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
        - str:
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
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortIdSubType"])

    @PortIdSubType.setter
    def PortIdSubType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortIdSubType"], value)

    @property
    def TxDelay(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Minimum delay between successive LLDP packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxDelay"])

    @TxDelay.setter
    def TxDelay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxDelay"], value)

    @property
    def TxInterval(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This parameter indicates the interval at which LLDP frames are transmitted on behalf of this LLDP agent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxInterval"])

    @TxInterval.setter
    def TxInterval(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxInterval"], value)

    def update(
        self,
        ChassisId=None,
        ControlTlvMaxVersion=None,
        DcbxEnable=None,
        DcbxSubtype=None,
        DestMacAddress=None,
        Enabled=None,
        FastInitEnable=None,
        HoldTime=None,
        Name=None,
        Oui=None,
        PortIdInterfaceName=None,
        PortIdMacAddress=None,
        PortIdSubType=None,
        TxDelay=None,
        TxInterval=None,
    ):
        # type: (str, int, bool, int, str, bool, bool, int, str, str, str, str, int, int, int) -> DcbxRange
        """Updates dcbxRange resource on the server.

        Args
        ----
        - ChassisId (str): Chassis identification for thedevice that transmitted the LLDP frame.
        - ControlTlvMaxVersion (number): Highest DCBX protocol version supported by the system.
        - DcbxEnable (bool): Enable DCBX TLVs.
        - DcbxSubtype (number): Organizationally defined subtype.
        - DestMacAddress (str): The destination MAC address value.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - FastInitEnable (bool): Enable fast initial retransmission.
        - HoldTime (number): Multiplier to get actual TTL value used in an LLDPDU.
        - Name (str): Name of range
        - Oui (str): The vendor identifier value.
        - PortIdInterfaceName (str): Port identification for the device that sent the LLDP frame.
        - PortIdMacAddress (str):
        - PortIdSubType (number):
        - TxDelay (number): Minimum delay between successive LLDP packets.
        - TxInterval (number): This parameter indicates the interval at which LLDP frames are transmitted on behalf of this LLDP agent.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ChassisId=None,
        ControlTlvMaxVersion=None,
        DcbxEnable=None,
        DcbxSubtype=None,
        DestMacAddress=None,
        Enabled=None,
        FastInitEnable=None,
        HoldTime=None,
        Name=None,
        ObjectId=None,
        Oui=None,
        PortIdInterfaceName=None,
        PortIdMacAddress=None,
        PortIdSubType=None,
        TxDelay=None,
        TxInterval=None,
    ):
        # type: (str, int, bool, int, str, bool, bool, int, str, str, str, str, str, int, int, int) -> DcbxRange
        """Finds and retrieves dcbxRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dcbxRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dcbxRange resources from the server.

        Args
        ----
        - ChassisId (str): Chassis identification for thedevice that transmitted the LLDP frame.
        - ControlTlvMaxVersion (number): Highest DCBX protocol version supported by the system.
        - DcbxEnable (bool): Enable DCBX TLVs.
        - DcbxSubtype (number): Organizationally defined subtype.
        - DestMacAddress (str): The destination MAC address value.
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - FastInitEnable (bool): Enable fast initial retransmission.
        - HoldTime (number): Multiplier to get actual TTL value used in an LLDPDU.
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object
        - Oui (str): The vendor identifier value.
        - PortIdInterfaceName (str): Port identification for the device that sent the LLDP frame.
        - PortIdMacAddress (str):
        - PortIdSubType (number):
        - TxDelay (number): Minimum delay between successive LLDP packets.
        - TxInterval (number): This parameter indicates the interval at which LLDP frames are transmitted on behalf of this LLDP agent.

        Returns
        -------
        - self: This instance with matching dcbxRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dcbxRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dcbxRange resources from the server available through an iterator or index

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
