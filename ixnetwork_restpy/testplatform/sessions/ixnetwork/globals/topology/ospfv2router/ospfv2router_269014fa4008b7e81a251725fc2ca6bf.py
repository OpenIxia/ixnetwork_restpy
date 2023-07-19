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


class Ospfv2Router(Base):
    """Ospf Port Specific Data
    The Ospfv2Router class encapsulates a list of ospfv2Router resources that are managed by the system.
    A list of resources can be retrieved from the server using the Ospfv2Router.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "ospfv2Router"
    _SDM_ATT_MAP = {
        "AppSpecLinkAttrSubTlvType": "appSpecLinkAttrSubTlvType",
        "BierMplsEncapSubTlvType": "bierMplsEncapSubTlvType",
        "BierSubTlvType": "bierSubTlvType",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "EnableDrBdr": "enableDrBdr",
        "EnableSingleAdjSIDTLV": "enableSingleAdjSIDTLV",
        "FaEagSubTlvType": "faEagSubTlvType",
        "FadSubTlvType": "fadSubTlvType",
        "FadfSubTlvType": "fadfSubTlvType",
        "FaeSrlgSubTlvType": "faeSrlgSubTlvType",
        "FaiAllAgSubTlvType": "faiAllAgSubTlvType",
        "FaiAnyAgSubTlvType": "faiAnyAgSubTlvType",
        "FapmPrefixMetricSubTlvType": "fapmPrefixMetricSubTlvType",
        "FloodLsUpdatesPerInterval": "floodLsUpdatesPerInterval",
        "Name": "name",
        "RateControlInterval": "rateControlInterval",
        "RowNames": "rowNames",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Ospfv2Router, self).__init__(parent, list_op)

    @property
    def StartRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.startrate.startrate_2bc83a4fb9730935e8259bdb40af2dc0.StartRate): An instance of the StartRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.startrate.startrate_2bc83a4fb9730935e8259bdb40af2dc0 import (
            StartRate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("StartRate", None) is not None:
                return self._properties.get("StartRate")
        return StartRate(self)._select()

    @property
    def StopRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.stoprate.stoprate_4ea9a1b38960d2b21012777131469a04.StopRate): An instance of the StopRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.stoprate.stoprate_4ea9a1b38960d2b21012777131469a04 import (
            StopRate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("StopRate", None) is not None:
                return self._properties.get("StopRate")
        return StopRate(self)._select()

    @property
    def AppSpecLinkAttrSubTlvType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): App Specific Link Attr Sub-TLV Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AppSpecLinkAttrSubTlvType"])
        )

    @property
    def BierMplsEncapSubTlvType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BIER MPLS Encapsulation Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BierMplsEncapSubTlvType"])
        )

    @property
    def BierSubTlvType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BIER Sub-TLV Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BierSubTlvType"])
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
    def EnableDrBdr(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable DR/BDR
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableDrBdr"]))

    @property
    def EnableSingleAdjSIDTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): When there are multiple links of a router then send one Extended Link TLV per Extended Link Opaque LSA for each link. This is expected behavior as per RFC7684. If this checkbox is disabled then multiple link TLVs are combined in one single Extended Link Opaque LSA.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableSingleAdjSIDTLV"])
        )

    @property
    def FaEagSubTlvType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): FAEAG Sub-TLV Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FaEagSubTlvType"])
        )

    @property
    def FadSubTlvType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): FAD Sub-TLV Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FadSubTlvType"]))

    @property
    def FadfSubTlvType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): FADF Sub-TLV Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FadfSubTlvType"])
        )

    @property
    def FaeSrlgSubTlvType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): FAESRLG Sub-TLV type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FaeSrlgSubTlvType"])
        )

    @property
    def FaiAllAgSubTlvType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): FAIAllAG Sub-TLV Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FaiAllAgSubTlvType"])
        )

    @property
    def FaiAnyAgSubTlvType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): FAIAnyAG Sub-TLV Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FaiAnyAgSubTlvType"])
        )

    @property
    def FapmPrefixMetricSubTlvType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): FAPM Prefix Metric Sub-TLV type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FapmPrefixMetricSubTlvType"])
        )

    @property
    def FloodLsUpdatesPerInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Flood Link State Updates per Interval
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FloodLsUpdatesPerInterval"])
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
    def RateControlInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Rate Control Interval (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RateControlInterval"])
        )

    @property
    def RowNames(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Name of rows
        """
        return self._get_attribute(self._SDM_ATT_MAP["RowNames"])

    def update(self, Name=None):
        # type: (str) -> Ospfv2Router
        """Updates ospfv2Router resource on the server.

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

    def add(self, Name=None):
        # type: (str) -> Ospfv2Router
        """Adds a new ospfv2Router resource on the json, only valid with batch add utility

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with all currently retrieved ospfv2Router resources using find and the newly added ospfv2Router resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, Name=None, RowNames=None):
        # type: (int, str, str, List[str]) -> Ospfv2Router
        """Finds and retrieves ospfv2Router resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ospfv2Router resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ospfv2Router resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - RowNames (list(str)): Name of rows

        Returns
        -------
        - self: This instance with matching ospfv2Router resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ospfv2Router data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ospfv2Router resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(
        self,
        PortNames=None,
        AppSpecLinkAttrSubTlvType=None,
        BierMplsEncapSubTlvType=None,
        BierSubTlvType=None,
        EnableDrBdr=None,
        EnableSingleAdjSIDTLV=None,
        FaEagSubTlvType=None,
        FadSubTlvType=None,
        FadfSubTlvType=None,
        FaeSrlgSubTlvType=None,
        FaiAllAgSubTlvType=None,
        FaiAnyAgSubTlvType=None,
        FapmPrefixMetricSubTlvType=None,
        FloodLsUpdatesPerInterval=None,
        RateControlInterval=None,
    ):
        """Base class infrastructure that gets a list of ospfv2Router device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AppSpecLinkAttrSubTlvType (str): optional regex of appSpecLinkAttrSubTlvType
        - BierMplsEncapSubTlvType (str): optional regex of bierMplsEncapSubTlvType
        - BierSubTlvType (str): optional regex of bierSubTlvType
        - EnableDrBdr (str): optional regex of enableDrBdr
        - EnableSingleAdjSIDTLV (str): optional regex of enableSingleAdjSIDTLV
        - FaEagSubTlvType (str): optional regex of faEagSubTlvType
        - FadSubTlvType (str): optional regex of fadSubTlvType
        - FadfSubTlvType (str): optional regex of fadfSubTlvType
        - FaeSrlgSubTlvType (str): optional regex of faeSrlgSubTlvType
        - FaiAllAgSubTlvType (str): optional regex of faiAllAgSubTlvType
        - FaiAnyAgSubTlvType (str): optional regex of faiAnyAgSubTlvType
        - FapmPrefixMetricSubTlvType (str): optional regex of fapmPrefixMetricSubTlvType
        - FloodLsUpdatesPerInterval (str): optional regex of floodLsUpdatesPerInterval
        - RateControlInterval (str): optional regex of rateControlInterval

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
