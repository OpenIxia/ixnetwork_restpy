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


class LdpRootRangeV6(Base):
    """Ldp Targeted RootRange V6 Configuration
    The LdpRootRangeV6 class encapsulates a required ldpRootRangeV6 resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "ldpRootRangeV6"
    _SDM_ATT_MAP = {
        "ContinuousIncrementOVAcrossRoot": "continuousIncrementOVAcrossRoot",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "FilterOnGroupAddress": "filterOnGroupAddress",
        "GroupCountPerLSP": "groupCountPerLSP",
        "LspCountPerRoot": "lspCountPerRoot",
        "Name": "name",
        "NumberOfTLVs": "numberOfTLVs",
        "RootAddress": "rootAddress",
        "RootAddressCount": "rootAddressCount",
        "RootAddressStep": "rootAddressStep",
        "SourceAddressV4": "sourceAddressV4",
        "SourceAddressV6": "sourceAddressV6",
        "SourceCountPerLSP": "sourceCountPerLSP",
        "StartGroupAddressV4": "startGroupAddressV4",
        "StartGroupAddressV6": "startGroupAddressV6",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(LdpRootRangeV6, self).__init__(parent, list_op)

    @property
    def LdpTLVList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptlvlist_30bf84fe9b838fe1c5800e633f13cff2.LdpTLVList): An instance of the LdpTLVList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptlvlist_30bf84fe9b838fe1c5800e633f13cff2 import (
            LdpTLVList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LdpTLVList", None) is not None:
                return self._properties.get("LdpTLVList")
        return LdpTLVList(self)

    @property
    def ContinuousIncrementOVAcrossRoot(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Continuous Increment Opaque Value Across Root
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ContinuousIncrementOVAcrossRoot"]),
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
    def FilterOnGroupAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, all the LSPs will belong to the same set of groups
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FilterOnGroupAddress"])
        )

    @property
    def GroupCountPerLSP(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Group Count Per LSP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupCountPerLSP"])
        )

    @property
    def LspCountPerRoot(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LSP Count Per Root
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LspCountPerRoot"])
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
    def NumberOfTLVs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number Of TLVs
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfTLVs"])

    @NumberOfTLVs.setter
    def NumberOfTLVs(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfTLVs"], value)

    @property
    def RootAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Root Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RootAddress"]))

    @property
    def RootAddressCount(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Root Address Count
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RootAddressCount"])
        )

    @property
    def RootAddressStep(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Root Address Step
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RootAddressStep"])
        )

    @property
    def SourceAddressV4(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Source Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SourceAddressV4"])
        )

    @property
    def SourceAddressV6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Source Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SourceAddressV6"])
        )

    @property
    def SourceCountPerLSP(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source Count Per LSP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SourceCountPerLSP"])
        )

    @property
    def StartGroupAddressV4(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Start Group Address(V4)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StartGroupAddressV4"])
        )

    @property
    def StartGroupAddressV6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Start Group Address(V6)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StartGroupAddressV6"])
        )

    def update(self, Name=None, NumberOfTLVs=None):
        # type: (str, int) -> LdpRootRangeV6
        """Updates ldpRootRangeV6 resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfTLVs (number): Number Of TLVs

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, Name=None, NumberOfTLVs=None):
        # type: (int, str, str, int) -> LdpRootRangeV6
        """Finds and retrieves ldpRootRangeV6 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ldpRootRangeV6 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ldpRootRangeV6 resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfTLVs (number): Number Of TLVs

        Returns
        -------
        - self: This instance with matching ldpRootRangeV6 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ldpRootRangeV6 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ldpRootRangeV6 resources from the server available through an iterator or index

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
        ContinuousIncrementOVAcrossRoot=None,
        FilterOnGroupAddress=None,
        GroupCountPerLSP=None,
        LspCountPerRoot=None,
        RootAddress=None,
        RootAddressCount=None,
        RootAddressStep=None,
        SourceAddressV4=None,
        SourceAddressV6=None,
        SourceCountPerLSP=None,
        StartGroupAddressV4=None,
        StartGroupAddressV6=None,
    ):
        """Base class infrastructure that gets a list of ldpRootRangeV6 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ContinuousIncrementOVAcrossRoot (str): optional regex of continuousIncrementOVAcrossRoot
        - FilterOnGroupAddress (str): optional regex of filterOnGroupAddress
        - GroupCountPerLSP (str): optional regex of groupCountPerLSP
        - LspCountPerRoot (str): optional regex of lspCountPerRoot
        - RootAddress (str): optional regex of rootAddress
        - RootAddressCount (str): optional regex of rootAddressCount
        - RootAddressStep (str): optional regex of rootAddressStep
        - SourceAddressV4 (str): optional regex of sourceAddressV4
        - SourceAddressV6 (str): optional regex of sourceAddressV6
        - SourceCountPerLSP (str): optional regex of sourceCountPerLSP
        - StartGroupAddressV4 (str): optional regex of startGroupAddressV4
        - StartGroupAddressV6 (str): optional regex of startGroupAddressV6

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
