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


class IsisAppSpecSrlgList(Base):
    """ISIS Application Specific SRLG
    The IsisAppSpecSrlgList class encapsulates a required isisAppSpecSrlgList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "isisAppSpecSrlgList"
    _SDM_ATT_MAP = {
        "Active": "active",
        "AppSpecificSrlgCount": "appSpecificSrlgCount",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "IpV4InterfaceAddr": "ipV4InterfaceAddr",
        "IpV4NeighborAddr": "ipV4NeighborAddr",
        "IpV6InterfaceAddr": "ipV6InterfaceAddr",
        "IpV6NeighborAddr": "ipV6NeighborAddr",
        "LFlag": "lFlag",
        "Name": "name",
        "StdAppType": "stdAppType",
        "UserDefAppBm": "userDefAppBm",
        "UserDefAppBmLen": "userDefAppBmLen",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(IsisAppSpecSrlgList, self).__init__(parent, list_op)

    @property
    def AppSpecificSrlgValueList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.appspecificsrlgvaluelist_04d0871fab9b2fb61fdfeb469179ed75.AppSpecificSrlgValueList): An instance of the AppSpecificSrlgValueList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.appspecificsrlgvaluelist_04d0871fab9b2fb61fdfeb469179ed75 import (
            AppSpecificSrlgValueList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AppSpecificSrlgValueList", None) is not None:
                return self._properties.get("AppSpecificSrlgValueList")
        return AppSpecificSrlgValueList(self)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Active"]))

    @property
    def AppSpecificSrlgCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Application Specific SRLGs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AppSpecificSrlgCount"])

    @AppSpecificSrlgCount.setter
    def AppSpecificSrlgCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AppSpecificSrlgCount"], value)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def IpV4InterfaceAddr(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Interface Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IpV4InterfaceAddr"])
        )

    @property
    def IpV4NeighborAddr(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Neighbor Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IpV4NeighborAddr"])
        )

    @property
    def IpV6InterfaceAddr(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Interface Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IpV6InterfaceAddr"])
        )

    @property
    def IpV6NeighborAddr(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Neighbor Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IpV6NeighborAddr"])
        )

    @property
    def LFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set to True, SRLG values should not be sent in 238 TLV.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LFlag"]))

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def StdAppType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Standard Application Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["StdAppType"]))

    @property
    def UserDefAppBm(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User Defined Application BM
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["UserDefAppBm"]))

    @property
    def UserDefAppBmLen(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User Defined Application BM Length
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserDefAppBmLen"])
        )

    def update(self, AppSpecificSrlgCount=None, Name=None):
        # type: (int, str) -> IsisAppSpecSrlgList
        """Updates isisAppSpecSrlgList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - AppSpecificSrlgCount (number): Number of Application Specific SRLGs.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self, AppSpecificSrlgCount=None, Count=None, DescriptiveName=None, Name=None
    ):
        # type: (int, int, str, str) -> IsisAppSpecSrlgList
        """Finds and retrieves isisAppSpecSrlgList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve isisAppSpecSrlgList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all isisAppSpecSrlgList resources from the server.

        Args
        ----
        - AppSpecificSrlgCount (number): Number of Application Specific SRLGs.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching isisAppSpecSrlgList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of isisAppSpecSrlgList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the isisAppSpecSrlgList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, Arg3=bool, async_operation=bool)
        ---------------------------------------------------------
        - Arg2 (bool):
        - Arg3 (bool):
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

    def PerformActionOnAllObjects(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the performActionOnAllObjects operation on the server.

        Action on All Objects

        performActionOnAllObjects(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------------
        - Arg2 (str): Action Name
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

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
            "performActionOnAllObjects", payload=payload, response_object=None
        )

    def get_device_ids(
        self,
        PortNames=None,
        Active=None,
        IpV4InterfaceAddr=None,
        IpV4NeighborAddr=None,
        IpV6InterfaceAddr=None,
        IpV6NeighborAddr=None,
        LFlag=None,
        StdAppType=None,
        UserDefAppBm=None,
        UserDefAppBmLen=None,
    ):
        """Base class infrastructure that gets a list of isisAppSpecSrlgList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - IpV4InterfaceAddr (str): optional regex of ipV4InterfaceAddr
        - IpV4NeighborAddr (str): optional regex of ipV4NeighborAddr
        - IpV6InterfaceAddr (str): optional regex of ipV6InterfaceAddr
        - IpV6NeighborAddr (str): optional regex of ipV6NeighborAddr
        - LFlag (str): optional regex of lFlag
        - StdAppType (str): optional regex of stdAppType
        - UserDefAppBm (str): optional regex of userDefAppBm
        - UserDefAppBmLen (str): optional regex of userDefAppBmLen

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
