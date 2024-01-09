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


class BgpSRTEPoliciesSRv6BindingListV6(Base):
    """
    The BgpSRTEPoliciesSRv6BindingListV6 class encapsulates a required bgpSRTEPoliciesSRv6BindingListV6 resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "bgpSRTEPoliciesSRv6BindingListV6"
    _SDM_ATT_MAP = {
        "ArgLength": "argLength",
        "BflagSRv6": "bflagSRv6",
        "BindingListNumber": "bindingListNumber",
        "Count": "count",
        "CustomEndPointBehaviour": "customEndPointBehaviour",
        "DescriptiveName": "descriptiveName",
        "EnSRv6BindingTLV": "enSRv6BindingTLV",
        "EndPointBehaviour": "endPointBehaviour",
        "FunLength": "funLength",
        "IflagSRv6": "iflagSRv6",
        "LbLength": "lbLength",
        "LnLength": "lnLength",
        "Name": "name",
        "RemainingSRv6Bits": "remainingSRv6Bits",
        "SflagSRv6": "sflagSRv6",
        "SrtepolicyName": "srtepolicyName",
        "Srv6BindingSID": "srv6BindingSID",
        "Srv6SidEndpointBehaviourFlagReserved": "srv6SidEndpointBehaviourFlagReserved",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(BgpSRTEPoliciesSRv6BindingListV6, self).__init__(parent, list_op)

    @property
    def ArgLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Arguments length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ArgLength"]))

    @property
    def BflagSRv6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This flag indicates the presence of the SRv6 Endpoint Behaviour and SID Structure encoding.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BflagSRv6"]))

    @property
    def BindingListNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Binding List Number For Reference.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BindingListNumber"])
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
    def CustomEndPointBehaviour(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Custom End-Point Behaviour, applicable when Endpoint behaviour is 256-Custom End Point.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CustomEndPointBehaviour"])
        )

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
    def EnSRv6BindingTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Checkbox to enable SRv6 Binding Sub-TLV.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnSRv6BindingTLV"])
        )

    @property
    def EndPointBehaviour(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specifies the behaviour that can be associated with a SID.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndPointBehaviour"])
        )

    @property
    def FunLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Function length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FunLength"]))

    @property
    def IflagSRv6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This flag encodes the Drop Upon Invalid behaviour.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IflagSRv6"]))

    @property
    def LbLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Locator Block Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LbLength"]))

    @property
    def LnLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 SID Locator Node Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LnLength"]))

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
    def RemainingSRv6Bits(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Remaining Flag Bits takes the 8-bit flags value in Hex format. It ignores the bit position for flags exposed separately in GUI. For example, the 1st and 2nd bits and 3rd bits are ignored since they are set using the S Flag, I Flag and B flag settings.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RemainingSRv6Bits"])
        )

    @property
    def SflagSRv6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This flag encodes the Specified-BSID-only behaviour.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SflagSRv6"]))

    @property
    def SrtepolicyName(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Policy Name For Reference.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrtepolicyName"])

    @property
    def Srv6BindingSID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 Binding SID, a 16 octet IPv6 address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6BindingSID"])
        )

    @property
    def Srv6SidEndpointBehaviourFlagReserved(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): 16 bits Reserved for SRv6 Sid Endpoint Behaviour and Structure Flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Srv6SidEndpointBehaviourFlagReserved"]
            ),
        )

    def update(self, Name=None):
        # type: (str) -> BgpSRTEPoliciesSRv6BindingListV6
        """Updates bgpSRTEPoliciesSRv6BindingListV6 resource on the server.

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

    def find(self, Count=None, DescriptiveName=None, Name=None, SrtepolicyName=None):
        # type: (int, str, str, List[str]) -> BgpSRTEPoliciesSRv6BindingListV6
        """Finds and retrieves bgpSRTEPoliciesSRv6BindingListV6 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpSRTEPoliciesSRv6BindingListV6 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpSRTEPoliciesSRv6BindingListV6 resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SrtepolicyName (list(str)): Policy Name For Reference.

        Returns
        -------
        - self: This instance with matching bgpSRTEPoliciesSRv6BindingListV6 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpSRTEPoliciesSRv6BindingListV6 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpSRTEPoliciesSRv6BindingListV6 resources from the server available through an iterator or index

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
        ArgLength=None,
        BflagSRv6=None,
        BindingListNumber=None,
        CustomEndPointBehaviour=None,
        EnSRv6BindingTLV=None,
        EndPointBehaviour=None,
        FunLength=None,
        IflagSRv6=None,
        LbLength=None,
        LnLength=None,
        RemainingSRv6Bits=None,
        SflagSRv6=None,
        Srv6BindingSID=None,
        Srv6SidEndpointBehaviourFlagReserved=None,
    ):
        """Base class infrastructure that gets a list of bgpSRTEPoliciesSRv6BindingListV6 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ArgLength (str): optional regex of argLength
        - BflagSRv6 (str): optional regex of bflagSRv6
        - BindingListNumber (str): optional regex of bindingListNumber
        - CustomEndPointBehaviour (str): optional regex of customEndPointBehaviour
        - EnSRv6BindingTLV (str): optional regex of enSRv6BindingTLV
        - EndPointBehaviour (str): optional regex of endPointBehaviour
        - FunLength (str): optional regex of funLength
        - IflagSRv6 (str): optional regex of iflagSRv6
        - LbLength (str): optional regex of lbLength
        - LnLength (str): optional regex of lnLength
        - RemainingSRv6Bits (str): optional regex of remainingSRv6Bits
        - SflagSRv6 (str): optional regex of sflagSRv6
        - Srv6BindingSID (str): optional regex of srv6BindingSID
        - Srv6SidEndpointBehaviourFlagReserved (str): optional regex of srv6SidEndpointBehaviourFlagReserved

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
