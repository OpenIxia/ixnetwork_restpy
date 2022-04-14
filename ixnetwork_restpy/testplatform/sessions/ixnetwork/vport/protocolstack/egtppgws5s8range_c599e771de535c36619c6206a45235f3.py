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


class EgtpPgwS5S8Range(Base):
    """
    The EgtpPgwS5S8Range class encapsulates a required egtpPgwS5S8Range resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "egtpPgwS5S8Range"
    _SDM_ATT_MAP = {
        "ChangeReportingMode": "changeReportingMode",
        "EnableEchoRequest": "enableEchoRequest",
        "Enabled": "enabled",
        "IpType": "ipType",
        "N3CreateBearerReq": "n3CreateBearerReq",
        "N3DeleteBearerReq": "n3DeleteBearerReq",
        "N3EchoReq": "n3EchoReq",
        "N3UpdateBearerReq": "n3UpdateBearerReq",
        "Name": "name",
        "ObjectId": "objectId",
        "T3CreateBearerReq": "t3CreateBearerReq",
        "T3DeleteBearerReq": "t3DeleteBearerReq",
        "T3EchoReq": "t3EchoReq",
        "T3UpdateBearerReq": "t3UpdateBearerReq",
        "UseCpIp": "useCpIp",
        "UseUpIp": "useUpIp",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(EgtpPgwS5S8Range, self).__init__(parent, list_op)

    @property
    def CpIpRangeS5S8(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.cpipranges5s8_0d5eafc48bf1d7f3baa6571c32484a76.CpIpRangeS5S8): An instance of the CpIpRangeS5S8 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.cpipranges5s8_0d5eafc48bf1d7f3baa6571c32484a76 import (
            CpIpRangeS5S8,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CpIpRangeS5S8", None) is not None:
                return self._properties.get("CpIpRangeS5S8")
        return CpIpRangeS5S8(self)._select()

    @property
    def CpMacRangeS5S8(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.cpmacranges5s8_c1127e40be0516e70ad4b0a915df0ec4.CpMacRangeS5S8): An instance of the CpMacRangeS5S8 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.cpmacranges5s8_c1127e40be0516e70ad4b0a915df0ec4 import (
            CpMacRangeS5S8,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CpMacRangeS5S8", None) is not None:
                return self._properties.get("CpMacRangeS5S8")
        return CpMacRangeS5S8(self)._select()

    @property
    def CpVlanRangeS5S8(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.cpvlanranges5s8_0ae52b7b51bf4ddbc60a0931d41f0c37.CpVlanRangeS5S8): An instance of the CpVlanRangeS5S8 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.cpvlanranges5s8_0ae52b7b51bf4ddbc60a0931d41f0c37 import (
            CpVlanRangeS5S8,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CpVlanRangeS5S8", None) is not None:
                return self._properties.get("CpVlanRangeS5S8")
        return CpVlanRangeS5S8(self)._select()

    @property
    def UpIpRangeS5S8(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.upipranges5s8_2da47e1741846868f2d8c1e7a10bd8d1.UpIpRangeS5S8): An instance of the UpIpRangeS5S8 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.upipranges5s8_2da47e1741846868f2d8c1e7a10bd8d1 import (
            UpIpRangeS5S8,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("UpIpRangeS5S8", None) is not None:
                return self._properties.get("UpIpRangeS5S8")
        return UpIpRangeS5S8(self)._select()

    @property
    def UpMacRangeS5S8(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.upmacranges5s8_4cbfbb717f1f9bc1e3d83068d62e3839.UpMacRangeS5S8): An instance of the UpMacRangeS5S8 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.upmacranges5s8_4cbfbb717f1f9bc1e3d83068d62e3839 import (
            UpMacRangeS5S8,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("UpMacRangeS5S8", None) is not None:
                return self._properties.get("UpMacRangeS5S8")
        return UpMacRangeS5S8(self)._select()

    @property
    def UpVlanRangeS5S8(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.upvlanranges5s8_770654fa18df114bc2fffbff8a3919a1.UpVlanRangeS5S8): An instance of the UpVlanRangeS5S8 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.upvlanranges5s8_770654fa18df114bc2fffbff8a3919a1 import (
            UpVlanRangeS5S8,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("UpVlanRangeS5S8", None) is not None:
                return self._properties.get("UpVlanRangeS5S8")
        return UpVlanRangeS5S8(self)._select()

    @property
    def ChangeReportingMode(self):
        # type: () -> int
        """
        Returns
        -------
        - number: OBSOLETE: Use changeReportingList instead.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ChangeReportingMode"])

    @ChangeReportingMode.setter
    def ChangeReportingMode(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ChangeReportingMode"], value)

    @property
    def EnableEchoRequest(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Set to true to send echo request
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableEchoRequest"])

    @EnableEchoRequest.setter
    def EnableEchoRequest(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableEchoRequest"], value)

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
    def IpType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IP type of the address(es) that will be assigned to the UEs. When choosing IPv4v6 both an IPv4 address and an IPv6 address will be assigned to the UE.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpType"])

    @IpType.setter
    def IpType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpType"], value)

    @property
    def N3CreateBearerReq(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of retransmissions for Create Bearer request
        """
        return self._get_attribute(self._SDM_ATT_MAP["N3CreateBearerReq"])

    @N3CreateBearerReq.setter
    def N3CreateBearerReq(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["N3CreateBearerReq"], value)

    @property
    def N3DeleteBearerReq(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of retransmissions for Delete Bearer request
        """
        return self._get_attribute(self._SDM_ATT_MAP["N3DeleteBearerReq"])

    @N3DeleteBearerReq.setter
    def N3DeleteBearerReq(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["N3DeleteBearerReq"], value)

    @property
    def N3EchoReq(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of retransmissions for Echo request
        """
        return self._get_attribute(self._SDM_ATT_MAP["N3EchoReq"])

    @N3EchoReq.setter
    def N3EchoReq(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["N3EchoReq"], value)

    @property
    def N3UpdateBearerReq(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of retransmissions for Update Bearer request
        """
        return self._get_attribute(self._SDM_ATT_MAP["N3UpdateBearerReq"])

    @N3UpdateBearerReq.setter
    def N3UpdateBearerReq(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["N3UpdateBearerReq"], value)

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
    def T3CreateBearerReq(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Response timeout for a Create Bearer request (seconds)
        """
        return self._get_attribute(self._SDM_ATT_MAP["T3CreateBearerReq"])

    @T3CreateBearerReq.setter
    def T3CreateBearerReq(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["T3CreateBearerReq"], value)

    @property
    def T3DeleteBearerReq(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Response timeout for a Delete Bearer request (seconds)
        """
        return self._get_attribute(self._SDM_ATT_MAP["T3DeleteBearerReq"])

    @T3DeleteBearerReq.setter
    def T3DeleteBearerReq(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["T3DeleteBearerReq"], value)

    @property
    def T3EchoReq(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Response timeout for a Echo request (seconds).
        """
        return self._get_attribute(self._SDM_ATT_MAP["T3EchoReq"])

    @T3EchoReq.setter
    def T3EchoReq(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["T3EchoReq"], value)

    @property
    def T3UpdateBearerReq(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Response timeout for a Update Bearer request (seconds)
        """
        return self._get_attribute(self._SDM_ATT_MAP["T3UpdateBearerReq"])

    @T3UpdateBearerReq.setter
    def T3UpdateBearerReq(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["T3UpdateBearerReq"], value)

    @property
    def UseCpIp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Use Control Plane Load Balancer
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseCpIp"])

    @UseCpIp.setter
    def UseCpIp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseCpIp"], value)

    @property
    def UseUpIp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Use User Plane Load Balancer
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseUpIp"])

    @UseUpIp.setter
    def UseUpIp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseUpIp"], value)

    def update(
        self,
        ChangeReportingMode=None,
        EnableEchoRequest=None,
        Enabled=None,
        IpType=None,
        N3CreateBearerReq=None,
        N3DeleteBearerReq=None,
        N3EchoReq=None,
        N3UpdateBearerReq=None,
        Name=None,
        T3CreateBearerReq=None,
        T3DeleteBearerReq=None,
        T3EchoReq=None,
        T3UpdateBearerReq=None,
        UseCpIp=None,
        UseUpIp=None,
    ):
        # type: (int, bool, bool, str, int, int, int, int, str, int, int, int, int, bool, bool) -> EgtpPgwS5S8Range
        """Updates egtpPgwS5S8Range resource on the server.

        Args
        ----
        - ChangeReportingMode (number): OBSOLETE: Use changeReportingList instead.
        - EnableEchoRequest (bool): Set to true to send echo request
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - IpType (str): The IP type of the address(es) that will be assigned to the UEs. When choosing IPv4v6 both an IPv4 address and an IPv6 address will be assigned to the UE.
        - N3CreateBearerReq (number): Number of retransmissions for Create Bearer request
        - N3DeleteBearerReq (number): Number of retransmissions for Delete Bearer request
        - N3EchoReq (number): Number of retransmissions for Echo request
        - N3UpdateBearerReq (number): Number of retransmissions for Update Bearer request
        - Name (str): Name of range
        - T3CreateBearerReq (number): Response timeout for a Create Bearer request (seconds)
        - T3DeleteBearerReq (number): Response timeout for a Delete Bearer request (seconds)
        - T3EchoReq (number): Response timeout for a Echo request (seconds).
        - T3UpdateBearerReq (number): Response timeout for a Update Bearer request (seconds)
        - UseCpIp (bool): Use Control Plane Load Balancer
        - UseUpIp (bool): Use User Plane Load Balancer

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ChangeReportingMode=None,
        EnableEchoRequest=None,
        Enabled=None,
        IpType=None,
        N3CreateBearerReq=None,
        N3DeleteBearerReq=None,
        N3EchoReq=None,
        N3UpdateBearerReq=None,
        Name=None,
        ObjectId=None,
        T3CreateBearerReq=None,
        T3DeleteBearerReq=None,
        T3EchoReq=None,
        T3UpdateBearerReq=None,
        UseCpIp=None,
        UseUpIp=None,
    ):
        # type: (int, bool, bool, str, int, int, int, int, str, str, int, int, int, int, bool, bool) -> EgtpPgwS5S8Range
        """Finds and retrieves egtpPgwS5S8Range resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve egtpPgwS5S8Range resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all egtpPgwS5S8Range resources from the server.

        Args
        ----
        - ChangeReportingMode (number): OBSOLETE: Use changeReportingList instead.
        - EnableEchoRequest (bool): Set to true to send echo request
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - IpType (str): The IP type of the address(es) that will be assigned to the UEs. When choosing IPv4v6 both an IPv4 address and an IPv6 address will be assigned to the UE.
        - N3CreateBearerReq (number): Number of retransmissions for Create Bearer request
        - N3DeleteBearerReq (number): Number of retransmissions for Delete Bearer request
        - N3EchoReq (number): Number of retransmissions for Echo request
        - N3UpdateBearerReq (number): Number of retransmissions for Update Bearer request
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object
        - T3CreateBearerReq (number): Response timeout for a Create Bearer request (seconds)
        - T3DeleteBearerReq (number): Response timeout for a Delete Bearer request (seconds)
        - T3EchoReq (number): Response timeout for a Echo request (seconds).
        - T3UpdateBearerReq (number): Response timeout for a Update Bearer request (seconds)
        - UseCpIp (bool): Use Control Plane Load Balancer
        - UseUpIp (bool): Use User Plane Load Balancer

        Returns
        -------
        - self: This instance with matching egtpPgwS5S8Range resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of egtpPgwS5S8Range data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the egtpPgwS5S8Range resources from the server available through an iterator or index

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
