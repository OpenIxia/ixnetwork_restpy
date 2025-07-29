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


class IsisRouterKeyList(Base):
    """ISIS Keys to be used for Authentication by ISIS Router
    The IsisRouterKeyList class encapsulates a required isisRouterKeyList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "isisRouterKeyList"
    _SDM_ATT_MAP = {
        "Active": "active",
        "AreaKeyID": "areaKeyID",
        "AreaRecvEndTime": "areaRecvEndTime",
        "AreaRecvStartTime": "areaRecvStartTime",
        "AreaSecret": "areaSecret",
        "AreaTransmitEndTime": "areaTransmitEndTime",
        "AreaTransmitStartTime": "areaTransmitStartTime",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "DomainKeyID": "domainKeyID",
        "DomainRecvEndTime": "domainRecvEndTime",
        "DomainRecvStartTime": "domainRecvStartTime",
        "DomainSecret": "domainSecret",
        "DomainTransmitEndTime": "domainTransmitEndTime",
        "DomainTransmitStartTime": "domainTransmitStartTime",
        "Name": "name",
        "SameForAreaAndDomain": "sameForAreaAndDomain",
        "UseInfiniteAreaTimers": "useInfiniteAreaTimers",
        "UseInfiniteDomainTimers": "useInfiniteDomainTimers",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(IsisRouterKeyList, self).__init__(parent, list_op)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Active"]))

    @property
    def AreaKeyID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Area Key ID to be used for the key in the keychain
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AreaKeyID"]))

    @property
    def AreaRecvEndTime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Area Receive End time for the given Key- DD:MM:YYYY HH:MM:SS, need to match the chassis time, Infinite also accepted
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AreaRecvEndTime"])
        )

    @property
    def AreaRecvStartTime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Area Receive Start time for the given Key- DD:MM:YYYY HH:MM:SS, need to match the chassis time, Infinite also accepted
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AreaRecvStartTime"])
        )

    @property
    def AreaSecret(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Area Secret to be used with the key
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AreaSecret"]))

    @property
    def AreaTransmitEndTime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Area Transmit End time for the given Key- DD:MM:YYYY HH:MM:SS, need to match the chassis time, Infinite also accepted
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AreaTransmitEndTime"])
        )

    @property
    def AreaTransmitStartTime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Area Transmit Start time for the given Key- DD:MM:YYYY HH:MM:SS, need to match the chassis time, Infinite also accepted
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AreaTransmitStartTime"])
        )

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
    def DomainKeyID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Domain Key ID to be used for the key in the keychain
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DomainKeyID"]))

    @property
    def DomainRecvEndTime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Domain Receive End time for the given Key- DD:MM:YYYY HH:MM:SS, need to match the chassis time, Infinite also accepted
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DomainRecvEndTime"])
        )

    @property
    def DomainRecvStartTime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Domain Receive Start time for the given Key- DD:MM:YYYY HH:MM:SS, need to match the chassis time, Infinite also accepted
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DomainRecvStartTime"])
        )

    @property
    def DomainSecret(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Domain Secret to be used with the key
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DomainSecret"]))

    @property
    def DomainTransmitEndTime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Domain Transmit End time for the given Key- DD:MM:YYYY HH:MM:SS, need to match the chassis time, Infinite also accepted
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DomainTransmitEndTime"])
        )

    @property
    def DomainTransmitStartTime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Domain Transmit Start time for the given Key- DD:MM:YYYY HH:MM:SS, need to match the chassis time, Infinite also accepted
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DomainTransmitStartTime"])
        )

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
    def SameForAreaAndDomain(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Area Key to be applied for both Area and domain.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SameForAreaAndDomain"])
        )

    @property
    def UseInfiniteAreaTimers(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Infinite timers to be applied for all the Area timers
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UseInfiniteAreaTimers"])
        )

    @property
    def UseInfiniteDomainTimers(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Infinite timers to be applied for all the Domain timers
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UseInfiniteDomainTimers"])
        )

    def update(self, Name=None):
        # type: (str) -> IsisRouterKeyList
        """Updates isisRouterKeyList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, Name=None):
        # type: (int, str, str) -> IsisRouterKeyList
        """Finds and retrieves isisRouterKeyList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve isisRouterKeyList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all isisRouterKeyList resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching isisRouterKeyList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of isisRouterKeyList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the isisRouterKeyList resources from the server available through an iterator or index

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
        AreaKeyID=None,
        AreaRecvEndTime=None,
        AreaRecvStartTime=None,
        AreaSecret=None,
        AreaTransmitEndTime=None,
        AreaTransmitStartTime=None,
        DomainKeyID=None,
        DomainRecvEndTime=None,
        DomainRecvStartTime=None,
        DomainSecret=None,
        DomainTransmitEndTime=None,
        DomainTransmitStartTime=None,
        SameForAreaAndDomain=None,
        UseInfiniteAreaTimers=None,
        UseInfiniteDomainTimers=None,
    ):
        """Base class infrastructure that gets a list of isisRouterKeyList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AreaKeyID (str): optional regex of areaKeyID
        - AreaRecvEndTime (str): optional regex of areaRecvEndTime
        - AreaRecvStartTime (str): optional regex of areaRecvStartTime
        - AreaSecret (str): optional regex of areaSecret
        - AreaTransmitEndTime (str): optional regex of areaTransmitEndTime
        - AreaTransmitStartTime (str): optional regex of areaTransmitStartTime
        - DomainKeyID (str): optional regex of domainKeyID
        - DomainRecvEndTime (str): optional regex of domainRecvEndTime
        - DomainRecvStartTime (str): optional regex of domainRecvStartTime
        - DomainSecret (str): optional regex of domainSecret
        - DomainTransmitEndTime (str): optional regex of domainTransmitEndTime
        - DomainTransmitStartTime (str): optional regex of domainTransmitStartTime
        - SameForAreaAndDomain (str): optional regex of sameForAreaAndDomain
        - UseInfiniteAreaTimers (str): optional regex of useInfiniteAreaTimers
        - UseInfiniteDomainTimers (str): optional regex of useInfiniteDomainTimers

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
