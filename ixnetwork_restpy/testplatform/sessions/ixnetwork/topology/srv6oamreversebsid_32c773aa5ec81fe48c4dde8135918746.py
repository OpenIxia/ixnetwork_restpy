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


class Srv6OamReverseBsid(Base):
    """SRv6 Reverse Binding SID Address
    The Srv6OamReverseBsid class encapsulates a required srv6OamReverseBsid resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "srv6OamReverseBsid"
    _SDM_ATT_MAP = {
        "Active": "active",
        "AutoGenSegmentLeftValue": "autoGenSegmentLeftValue",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "HopLimit": "hopLimit",
        "Name": "name",
        "NumSegments": "numSegments",
        "RemoveOuterHeader": "removeOuterHeader",
        "SegmentLeftValue": "segmentLeftValue",
        "SiIndex": "siIndex",
        "SrcAddress": "srcAddress",
        "SrcSameAsIncoming": "srcSameAsIncoming",
        "Srv6ReverseBsid": "srv6ReverseBsid",
        "UseGSRv6SI": "useGSRv6SI",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Srv6OamReverseBsid, self).__init__(parent, list_op)

    @property
    def Srv6oamSegmentNode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.srv6oamsegmentnode_4504116c9d97fb3485d94c3ced1752bc.Srv6oamSegmentNode): An instance of the Srv6oamSegmentNode class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.srv6oamsegmentnode_4504116c9d97fb3485d94c3ced1752bc import (
            Srv6oamSegmentNode,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Srv6oamSegmentNode", None) is not None:
                return self._properties.get("Srv6oamSegmentNode")
        return Srv6oamSegmentNode(self)._select()

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
    def AutoGenSegmentLeftValue(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled then Segment Left field value will be auto generated.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AutoGenSegmentLeftValue"])
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
    def HopLimit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Hop Limit to be used in IPv6 Header of backhaul packet.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HopLimit"]))

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
    def NumSegments(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Total Number Segments/Trasit addresses present to reach destination. This count is excluding the actual Destination Address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumSegments"])

    @NumSegments.setter
    def NumSegments(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumSegments"], value)

    @property
    def RemoveOuterHeader(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If Enabled, Outer IPv6 header will be removed in backhaul packet. If Disabled, all incoming headers will be present in backhaul packet.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RemoveOuterHeader"])
        )

    @property
    def SegmentLeftValue(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Segment Left value to be used in SRH.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentLeftValue"])
        )

    @property
    def SiIndex(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Segment Index to be filled in argument field of IPv6 Destination Address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SiIndex"]))

    @property
    def SrcAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Source address to be used in backhaul packet.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SrcAddress"]))

    @property
    def SrcSameAsIncoming(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, Source Address will be copied from Source Address of incoming packet. If Disabled, Source Address of will be taken from input configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrcSameAsIncoming"])
        )

    @property
    def Srv6ReverseBsid(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reverse Binding SID address to be used for backhaul detection.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6ReverseBsid"])
        )

    @property
    def UseGSRv6SI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use G SRv6 SI in SRH.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["UseGSRv6SI"]))

    def update(self, Name=None, NumSegments=None):
        # type: (str, int) -> Srv6OamReverseBsid
        """Updates srv6OamReverseBsid resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumSegments (number): Total Number Segments/Trasit addresses present to reach destination. This count is excluding the actual Destination Address.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, Name=None, NumSegments=None):
        # type: (int, str, str, int) -> Srv6OamReverseBsid
        """Finds and retrieves srv6OamReverseBsid resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve srv6OamReverseBsid resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all srv6OamReverseBsid resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumSegments (number): Total Number Segments/Trasit addresses present to reach destination. This count is excluding the actual Destination Address.

        Returns
        -------
        - self: This instance with matching srv6OamReverseBsid resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of srv6OamReverseBsid data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the srv6OamReverseBsid resources from the server available through an iterator or index

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
        Active=None,
        AutoGenSegmentLeftValue=None,
        HopLimit=None,
        RemoveOuterHeader=None,
        SegmentLeftValue=None,
        SiIndex=None,
        SrcAddress=None,
        SrcSameAsIncoming=None,
        Srv6ReverseBsid=None,
        UseGSRv6SI=None,
    ):
        """Base class infrastructure that gets a list of srv6OamReverseBsid device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AutoGenSegmentLeftValue (str): optional regex of autoGenSegmentLeftValue
        - HopLimit (str): optional regex of hopLimit
        - RemoveOuterHeader (str): optional regex of removeOuterHeader
        - SegmentLeftValue (str): optional regex of segmentLeftValue
        - SiIndex (str): optional regex of siIndex
        - SrcAddress (str): optional regex of srcAddress
        - SrcSameAsIncoming (str): optional regex of srcSameAsIncoming
        - Srv6ReverseBsid (str): optional regex of srv6ReverseBsid
        - UseGSRv6SI (str): optional regex of useGSRv6SI

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
