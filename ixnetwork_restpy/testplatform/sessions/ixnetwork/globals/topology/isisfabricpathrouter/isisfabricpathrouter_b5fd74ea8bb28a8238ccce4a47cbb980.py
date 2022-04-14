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


class IsisFabricPathRouter(Base):
    """Fabric-Path Port Configuration
    The IsisFabricPathRouter class encapsulates a list of isisFabricPathRouter resources that are managed by the system.
    A list of resources can be retrieved from the server using the IsisFabricPathRouter.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "isisFabricPathRouter"
    _SDM_ATT_MAP = {
        "AllL1RBridgesMAC": "allL1RBridgesMAC",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "HelloMulticastMAC": "helloMulticastMAC",
        "Name": "name",
        "NlpId": "nlpId",
        "NoOfLSPsOrMgroupPDUsPerInterval": "noOfLSPsOrMgroupPDUsPerInterval",
        "RateControlInterval": "rateControlInterval",
        "RowNames": "rowNames",
        "SendP2PHellosToUnicastMAC": "sendP2PHellosToUnicastMAC",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(IsisFabricPathRouter, self).__init__(parent, list_op)

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
    def AllL1RBridgesMAC(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Fabric-Path All L1 RBridges MAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AllL1RBridgesMAC"])
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
    def HelloMulticastMAC(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Fabric-Path Hello Multicast MAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HelloMulticastMAC"])
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
    def NlpId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Fabric-Path NLP ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NlpId"]))

    @property
    def NoOfLSPsOrMgroupPDUsPerInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LSPs/MGROUP-PDUs per Interval
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["NoOfLSPsOrMgroupPDUsPerInterval"]),
        )

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

    @property
    def SendP2PHellosToUnicastMAC(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TRILL/Fabric-Path Send P2P Hellos To Unicast MAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SendP2PHellosToUnicastMAC"])
        )

    def update(self, Name=None):
        # type: (str) -> IsisFabricPathRouter
        """Updates isisFabricPathRouter resource on the server.

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
        # type: (str) -> IsisFabricPathRouter
        """Adds a new isisFabricPathRouter resource on the json, only valid with batch add utility

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with all currently retrieved isisFabricPathRouter resources using find and the newly added isisFabricPathRouter resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, Name=None, RowNames=None):
        # type: (int, str, str, List[str]) -> IsisFabricPathRouter
        """Finds and retrieves isisFabricPathRouter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve isisFabricPathRouter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all isisFabricPathRouter resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - RowNames (list(str)): Name of rows

        Returns
        -------
        - self: This instance with matching isisFabricPathRouter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of isisFabricPathRouter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the isisFabricPathRouter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(
        self,
        PortNames=None,
        AllL1RBridgesMAC=None,
        HelloMulticastMAC=None,
        NlpId=None,
        NoOfLSPsOrMgroupPDUsPerInterval=None,
        RateControlInterval=None,
        SendP2PHellosToUnicastMAC=None,
    ):
        """Base class infrastructure that gets a list of isisFabricPathRouter device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AllL1RBridgesMAC (str): optional regex of allL1RBridgesMAC
        - HelloMulticastMAC (str): optional regex of helloMulticastMAC
        - NlpId (str): optional regex of nlpId
        - NoOfLSPsOrMgroupPDUsPerInterval (str): optional regex of noOfLSPsOrMgroupPDUsPerInterval
        - RateControlInterval (str): optional regex of rateControlInterval
        - SendP2PHellosToUnicastMAC (str): optional regex of sendP2PHellosToUnicastMAC

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
