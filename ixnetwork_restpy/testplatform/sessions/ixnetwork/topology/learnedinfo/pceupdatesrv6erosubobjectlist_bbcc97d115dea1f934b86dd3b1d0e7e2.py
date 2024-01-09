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


class PceUpdateSrv6EroSubObjectList(Base):
    """
    The PceUpdateSrv6EroSubObjectList class encapsulates a list of pceUpdateSrv6EroSubObjectList resources that are managed by the system.
    A list of resources can be retrieved from the server using the PceUpdateSrv6EroSubObjectList.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "pceUpdateSrv6EroSubObjectList"
    _SDM_ATT_MAP = {
        "LooseHop": "looseHop",
        "Srv6ActiveThisEro": "srv6ActiveThisEro",
        "Srv6Identifier": "srv6Identifier",
        "Srv6LocalIPv6address": "srv6LocalIPv6address",
        "Srv6LocalInterfaceId": "srv6LocalInterfaceId",
        "Srv6NaiType": "srv6NaiType",
        "Srv6RemoteIPv6address": "srv6RemoteIPv6address",
        "Srv6RemoteInterfaceId": "srv6RemoteInterfaceId",
        "Srv6endpointBehavior": "srv6endpointBehavior",
        "Srv6fBit": "srv6fBit",
        "Srv6ipv6NodeId": "srv6ipv6NodeId",
        "Srv6locatorBlockLength": "srv6locatorBlockLength",
        "Srv6locatorNodeLength": "srv6locatorNodeLength",
        "Srv6sBit": "srv6sBit",
        "Srv6sidArgumentLength": "srv6sidArgumentLength",
        "Srv6sidFunctionLength": "srv6sidFunctionLength",
        "Srv6tBit": "srv6tBit",
        "Srv6vBit": "srv6vBit",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PceUpdateSrv6EroSubObjectList, self).__init__(parent, list_op)

    @property
    def LooseHop(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates if user wants to represent a loose-hop sub object in the LSP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LooseHop"]))

    @property
    def Srv6ActiveThisEro(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Controls whether the ERO sub-object will be sent in the PCInitiate message.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6ActiveThisEro"])
        )

    @property
    def Srv6Identifier(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 Identifier is the 128 bit IPv6 addresses representing SRv6 segment.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6Identifier"])
        )

    @property
    def Srv6LocalIPv6address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This Control can be configured if NAI Type is set to IPv6 Adjacency and F bit is disabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6LocalIPv6address"])
        )

    @property
    def Srv6LocalInterfaceId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the Local Interface ID of the IPv6 adjacency with link-local IPv6 addresses which is specified as a pair of Node ID / Interface ID tuples.This Control can be configured if NAI Type is set to IPv6 adjacency with link-local IPv6 addresses and F bit is disabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6LocalInterfaceId"])
        )

    @property
    def Srv6NaiType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The SRv6 NAI Type which indicates the interpretation for NAI (Node or Adjacency Identifier).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Srv6NaiType"]))

    @property
    def Srv6RemoteIPv6address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This Control can be configured if NAI Type is set to IPv6 Adjacency and F bit is disabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6RemoteIPv6address"])
        )

    @property
    def Srv6RemoteInterfaceId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the Remote Interface ID of the IPv6 adjacency with link-local IPv6 addresses which is specified as a pair of Node ID / Interface ID tuples.This Control can be configured if NAI Type is set to IPv6 adjacency with link-local IPv6 addresses and F bit is disabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6RemoteInterfaceId"])
        )

    @property
    def Srv6endpointBehavior(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A 16 bit field representing the behavior associated with the SRv6 SIDs. This information is optional andplays no role in the fields in SRH imposed on the packet. It could be used for maintainability and diagnostic purpose.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6endpointBehavior"])
        )

    @property
    def Srv6fBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A Flag which is used to carry additional information pertaining to SID. When this bit is set, the NAI value in the subobject body is null.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Srv6fBit"]))

    @property
    def Srv6ipv6NodeId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Node ID is specified as an IPv6 address. This control can be configured if NAI Type is set to IPv6 Node ID and F bit is disabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6ipv6NodeId"])
        )

    @property
    def Srv6locatorBlockLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Locator Block length in bits.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6locatorBlockLength"])
        )

    @property
    def Srv6locatorNodeLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Locator Node length in bits.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6locatorNodeLength"])
        )

    @property
    def Srv6sBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A Flag which is used to carry additional information pertaining to SID. When this bit is set, the NAI value in the subobject body is null.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Srv6sBit"]))

    @property
    def Srv6sidArgumentLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Arguments length in bits.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6sidArgumentLength"])
        )

    @property
    def Srv6sidFunctionLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Function length in bits.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6sidFunctionLength"])
        )

    @property
    def Srv6tBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A Flag which is used to carry additional information pertaining to SID. When this bit is set, the NAI value in the subobject body is null.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Srv6tBit"]))

    @property
    def Srv6vBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A Flag which is used to carry additional information pertaining to SID. When this bit is set, the NAI value in the subobject body is null.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Srv6vBit"]))

    def add(self):
        """Adds a new pceUpdateSrv6EroSubObjectList resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved pceUpdateSrv6EroSubObjectList resources using find and the newly added pceUpdateSrv6EroSubObjectList resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self):
        """Finds and retrieves pceUpdateSrv6EroSubObjectList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pceUpdateSrv6EroSubObjectList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pceUpdateSrv6EroSubObjectList resources from the server.

        Returns
        -------
        - self: This instance with matching pceUpdateSrv6EroSubObjectList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pceUpdateSrv6EroSubObjectList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pceUpdateSrv6EroSubObjectList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, async_operation=bool)
        ----------------------------------------------
        - Arg2 (bool):
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
        return self._execute("addDeleteTags", payload=payload, response_object=None)

    def get_device_ids(
        self,
        PortNames=None,
        LooseHop=None,
        Srv6ActiveThisEro=None,
        Srv6Identifier=None,
        Srv6LocalIPv6address=None,
        Srv6LocalInterfaceId=None,
        Srv6NaiType=None,
        Srv6RemoteIPv6address=None,
        Srv6RemoteInterfaceId=None,
        Srv6endpointBehavior=None,
        Srv6fBit=None,
        Srv6ipv6NodeId=None,
        Srv6locatorBlockLength=None,
        Srv6locatorNodeLength=None,
        Srv6sBit=None,
        Srv6sidArgumentLength=None,
        Srv6sidFunctionLength=None,
        Srv6tBit=None,
        Srv6vBit=None,
    ):
        """Base class infrastructure that gets a list of pceUpdateSrv6EroSubObjectList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - LooseHop (str): optional regex of looseHop
        - Srv6ActiveThisEro (str): optional regex of srv6ActiveThisEro
        - Srv6Identifier (str): optional regex of srv6Identifier
        - Srv6LocalIPv6address (str): optional regex of srv6LocalIPv6address
        - Srv6LocalInterfaceId (str): optional regex of srv6LocalInterfaceId
        - Srv6NaiType (str): optional regex of srv6NaiType
        - Srv6RemoteIPv6address (str): optional regex of srv6RemoteIPv6address
        - Srv6RemoteInterfaceId (str): optional regex of srv6RemoteInterfaceId
        - Srv6endpointBehavior (str): optional regex of srv6endpointBehavior
        - Srv6fBit (str): optional regex of srv6fBit
        - Srv6ipv6NodeId (str): optional regex of srv6ipv6NodeId
        - Srv6locatorBlockLength (str): optional regex of srv6locatorBlockLength
        - Srv6locatorNodeLength (str): optional regex of srv6locatorNodeLength
        - Srv6sBit (str): optional regex of srv6sBit
        - Srv6sidArgumentLength (str): optional regex of srv6sidArgumentLength
        - Srv6sidFunctionLength (str): optional regex of srv6sidFunctionLength
        - Srv6tBit (str): optional regex of srv6tBit
        - Srv6vBit (str): optional regex of srv6vBit

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
