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


class BgpEvpnSpmsiV4(Base):
    """
    The BgpEvpnSpmsiV4 class encapsulates a required bgpEvpnSpmsiV4 resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "bgpEvpnSpmsiV4"
    _SDM_ATT_MAP = {
        "Active": "active",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "EnableSpmsiTraffic": "enableSpmsiTraffic",
        "GroupAddress": "groupAddress",
        "GroupAddressCountSPMSI": "groupAddressCountSPMSI",
        "GroupAddressStep": "groupAddressStep",
        "Mode": "mode",
        "MulticastTunnelType": "multicastTunnelType",
        "Name": "name",
        "SPmsiTunnelCount": "sPmsiTunnelCount",
        "SenderAddress": "senderAddress",
        "SenderAddressStep": "senderAddressStep",
        "SourceAddressCountSPMSI": "sourceAddressCountSPMSI",
        "SourceGroupMappingSPMSI": "sourceGroupMappingSPMSI",
        "StartGroupAddressSPMSI": "startGroupAddressSPMSI",
        "StartSourceAddressIpv4": "startSourceAddressIpv4",
        "UpstreamAssignedLabel": "upstreamAssignedLabel",
        "UpstreamAssignedLabelStep": "upstreamAssignedLabelStep",
        "UseUpstreamAssignedLabel": "useUpstreamAssignedLabel",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(BgpEvpnSpmsiV4, self).__init__(parent, list_op)

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
    def EnableSpmsiTraffic(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable SPMSI Traffic
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableSpmsiTraffic"])

    @EnableSpmsiTraffic.setter
    def EnableSpmsiTraffic(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableSpmsiTraffic"], value)

    @property
    def GroupAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Group Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["GroupAddress"]))

    @property
    def GroupAddressCountSPMSI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): C-Group Address Count
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupAddressCountSPMSI"])
        )

    @property
    def GroupAddressStep(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Group Address Step
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupAddressStep"])
        )

    @property
    def Mode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mode"]))

    @property
    def MulticastTunnelType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multicast Tunnel Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MulticastTunnelType"])
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
    def SPmsiTunnelCount(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): S-PMSI Tunnel Count
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SPmsiTunnelCount"])
        )

    @property
    def SenderAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sender Address/P-Root Node Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SenderAddress"]))

    @property
    def SenderAddressStep(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sender Address/P-Root Node Address Step
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SenderAddressStep"])
        )

    @property
    def SourceAddressCountSPMSI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): C-Source Address Count
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SourceAddressCountSPMSI"])
        )

    @property
    def SourceGroupMappingSPMSI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source Group Mapping
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SourceGroupMappingSPMSI"])
        )

    @property
    def StartGroupAddressSPMSI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Start C-Group Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StartGroupAddressSPMSI"])
        )

    @property
    def StartSourceAddressIpv4(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Start C-Source Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StartSourceAddressIpv4"])
        )

    @property
    def UpstreamAssignedLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Upstream Assigned Label
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UpstreamAssignedLabel"])
        )

    @property
    def UpstreamAssignedLabelStep(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Upstream Assigned Label Step
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UpstreamAssignedLabelStep"])
        )

    @property
    def UseUpstreamAssignedLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use Upstream Assigned Label
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UseUpstreamAssignedLabel"])
        )

    def update(self, EnableSpmsiTraffic=None, Name=None):
        # type: (bool, str) -> BgpEvpnSpmsiV4
        """Updates bgpEvpnSpmsiV4 resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - EnableSpmsiTraffic (bool): Enable SPMSI Traffic
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self, Count=None, DescriptiveName=None, EnableSpmsiTraffic=None, Name=None
    ):
        # type: (int, str, bool, str) -> BgpEvpnSpmsiV4
        """Finds and retrieves bgpEvpnSpmsiV4 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpEvpnSpmsiV4 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpEvpnSpmsiV4 resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - EnableSpmsiTraffic (bool): Enable SPMSI Traffic
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching bgpEvpnSpmsiV4 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpEvpnSpmsiV4 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpEvpnSpmsiV4 resources from the server available through an iterator or index

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
        GroupAddress=None,
        GroupAddressCountSPMSI=None,
        GroupAddressStep=None,
        Mode=None,
        MulticastTunnelType=None,
        SPmsiTunnelCount=None,
        SenderAddress=None,
        SenderAddressStep=None,
        SourceAddressCountSPMSI=None,
        SourceGroupMappingSPMSI=None,
        StartGroupAddressSPMSI=None,
        StartSourceAddressIpv4=None,
        UpstreamAssignedLabel=None,
        UpstreamAssignedLabelStep=None,
        UseUpstreamAssignedLabel=None,
    ):
        """Base class infrastructure that gets a list of bgpEvpnSpmsiV4 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - GroupAddress (str): optional regex of groupAddress
        - GroupAddressCountSPMSI (str): optional regex of groupAddressCountSPMSI
        - GroupAddressStep (str): optional regex of groupAddressStep
        - Mode (str): optional regex of mode
        - MulticastTunnelType (str): optional regex of multicastTunnelType
        - SPmsiTunnelCount (str): optional regex of sPmsiTunnelCount
        - SenderAddress (str): optional regex of senderAddress
        - SenderAddressStep (str): optional regex of senderAddressStep
        - SourceAddressCountSPMSI (str): optional regex of sourceAddressCountSPMSI
        - SourceGroupMappingSPMSI (str): optional regex of sourceGroupMappingSPMSI
        - StartGroupAddressSPMSI (str): optional regex of startGroupAddressSPMSI
        - StartSourceAddressIpv4 (str): optional regex of startSourceAddressIpv4
        - UpstreamAssignedLabel (str): optional regex of upstreamAssignedLabel
        - UpstreamAssignedLabelStep (str): optional regex of upstreamAssignedLabelStep
        - UseUpstreamAssignedLabel (str): optional regex of useUpstreamAssignedLabel

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
