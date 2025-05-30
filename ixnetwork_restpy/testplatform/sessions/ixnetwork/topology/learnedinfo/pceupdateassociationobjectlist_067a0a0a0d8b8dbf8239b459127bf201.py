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


class PceUpdateAssociationObjectList(Base):
    """
    The PceUpdateAssociationObjectList class encapsulates a list of pceUpdateAssociationObjectList resources that are managed by the system.
    A list of resources can be retrieved from the server using the PceUpdateAssociationObjectList.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "pceUpdateAssociationObjectList"
    _SDM_ATT_MAP = {
        "ActiveThisAssociation": "activeThisAssociation",
        "AssocType": "assocType",
        "AssociationId": "associationId",
        "AssociationObjectType": "associationObjectType",
        "Color": "color",
        "Discriminator": "discriminator",
        "EndpointIPv4Address": "endpointIPv4Address",
        "EndpointIPv6Address": "endpointIPv6Address",
        "IncludeExtAssocIDTLV": "includeExtAssocIDTLV",
        "IncludePPAGTLV": "includePPAGTLV",
        "IncludeSRPolicyCPathIDTLV": "includeSRPolicyCPathIDTLV",
        "IncludeSRPolicyCPathNameTLV": "includeSRPolicyCPathNameTLV",
        "IncludeSRPolicyCPathPrefTLV": "includeSRPolicyCPathPrefTLV",
        "IncludeSRPolicyPolNameTLV": "includeSRPolicyPolNameTLV",
        "Ipv4AssociationSrc": "ipv4AssociationSrc",
        "Ipv6AssociationSrc": "ipv6AssociationSrc",
        "OriginatorASN": "originatorASN",
        "OriginatorIPVersion": "originatorIPVersion",
        "OriginatorIPv4Address": "originatorIPv4Address",
        "OriginatorIPv6Address": "originatorIPv6Address",
        "PolicyEndpointType": "policyEndpointType",
        "Preference": "preference",
        "ProtectionLspBit": "protectionLspBit",
        "ProtocolOrigin": "protocolOrigin",
        "RemoveAssociation": "removeAssociation",
        "SrPolicyCPathName": "srPolicyCPathName",
        "SrPolicyName": "srPolicyName",
        "StandbyLspBit": "standbyLspBit",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PceUpdateAssociationObjectList, self).__init__(parent, list_op)

    @property
    def ActiveThisAssociation(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Controls whether the Association object will be sent in the pcep message.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ActiveThisAssociation"])
        )

    @property
    def AssocType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Association Type code point identifier.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AssocType"]))

    @property
    def AssociationId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Association ID of this LSP.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AssociationId"]))

    @property
    def AssociationObjectType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the Association Object Type.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AssociationObjectType"])
        )

    @property
    def Color(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the SR Policy color value.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Color"]))

    @property
    def Discriminator(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Discriminator of the candidate path.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Discriminator"]))

    @property
    def EndpointIPv4Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the SR Policy endpoint IPv4 address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointIPv4Address"])
        )

    @property
    def EndpointIPv6Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the SR Policy endpoint IPv6 address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointIPv6Address"])
        )

    @property
    def IncludeExtAssocIDTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates if Extended Association ID TLV is to be included in PCC Sync LSP.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeExtAssocIDTLV"])
        )

    @property
    def IncludePPAGTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates if Path Protection Association TLV is to be included in PCEP message.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludePPAGTLV"])
        )

    @property
    def IncludeSRPolicyCPathIDTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates if SRPOLICY-CPATH-ID TLV is to be included in PCC Sync LSP.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeSRPolicyCPathIDTLV"])
        )

    @property
    def IncludeSRPolicyCPathNameTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates if SRPOLICY-CPATH-NAME TLV is to be included in PCC Sync LSP.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeSRPolicyCPathNameTLV"])
        )

    @property
    def IncludeSRPolicyCPathPrefTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates if SRPOLICY-CPATH-PREFERENCE TLV is to be included in PCC Sync LSP.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeSRPolicyCPathPrefTLV"])
        )

    @property
    def IncludeSRPolicyPolNameTLV(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates if SRPOLICY-POL-NAME TLV is to be included in PCC Sync LSP.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeSRPolicyPolNameTLV"])
        )

    @property
    def Ipv4AssociationSrc(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Association Source IPv4 address that will be set to the headend IPv4 address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4AssociationSrc"])
        )

    @property
    def Ipv6AssociationSrc(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Association Source IPv6 address that will be set to the headend IPv6 address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6AssociationSrc"])
        )

    @property
    def OriginatorASN(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the 4 byte Originator ASN.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["OriginatorASN"]))

    @property
    def OriginatorIPVersion(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the Originator IP Version.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OriginatorIPVersion"])
        )

    @property
    def OriginatorIPv4Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the Originator IPv4 address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OriginatorIPv4Address"])
        )

    @property
    def OriginatorIPv6Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the Originator IPv6 address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OriginatorIPv6Address"])
        )

    @property
    def PolicyEndpointType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the Policy Endpoint Type.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PolicyEndpointType"])
        )

    @property
    def Preference(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the Preference of the candidate path.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Preference"]))

    @property
    def ProtectionLspBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether Protection LSP Bit is On.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ProtectionLspBit"])
        )

    @property
    def ProtocolOrigin(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the protocol origin.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ProtocolOrigin"])
        )

    @property
    def RemoveAssociation(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Removes the Association.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RemoveAssociation"])
        )

    @property
    def SrPolicyCPathName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the SR Policy Candidate Path Name. It SHOULD be a string of printable ASCII characters, without a NULL terminator.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrPolicyCPathName"])
        )

    @property
    def SrPolicyName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denote sthe SR Policy Name. It SHOULD be a string of printable ASCII characters, without a NULL terminator.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SrPolicyName"]))

    @property
    def StandbyLspBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether Standby LSP Bit is On.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["StandbyLspBit"]))

    def add(self):
        """Adds a new pceUpdateAssociationObjectList resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved pceUpdateAssociationObjectList resources using find and the newly added pceUpdateAssociationObjectList resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self):
        """Finds and retrieves pceUpdateAssociationObjectList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pceUpdateAssociationObjectList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pceUpdateAssociationObjectList resources from the server.

        Returns
        -------
        - self: This instance with matching pceUpdateAssociationObjectList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pceUpdateAssociationObjectList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pceUpdateAssociationObjectList resources from the server available through an iterator or index

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
        ActiveThisAssociation=None,
        AssocType=None,
        AssociationId=None,
        AssociationObjectType=None,
        Color=None,
        Discriminator=None,
        EndpointIPv4Address=None,
        EndpointIPv6Address=None,
        IncludeExtAssocIDTLV=None,
        IncludePPAGTLV=None,
        IncludeSRPolicyCPathIDTLV=None,
        IncludeSRPolicyCPathNameTLV=None,
        IncludeSRPolicyCPathPrefTLV=None,
        IncludeSRPolicyPolNameTLV=None,
        Ipv4AssociationSrc=None,
        Ipv6AssociationSrc=None,
        OriginatorASN=None,
        OriginatorIPVersion=None,
        OriginatorIPv4Address=None,
        OriginatorIPv6Address=None,
        PolicyEndpointType=None,
        Preference=None,
        ProtectionLspBit=None,
        ProtocolOrigin=None,
        RemoveAssociation=None,
        SrPolicyCPathName=None,
        SrPolicyName=None,
        StandbyLspBit=None,
    ):
        """Base class infrastructure that gets a list of pceUpdateAssociationObjectList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ActiveThisAssociation (str): optional regex of activeThisAssociation
        - AssocType (str): optional regex of assocType
        - AssociationId (str): optional regex of associationId
        - AssociationObjectType (str): optional regex of associationObjectType
        - Color (str): optional regex of color
        - Discriminator (str): optional regex of discriminator
        - EndpointIPv4Address (str): optional regex of endpointIPv4Address
        - EndpointIPv6Address (str): optional regex of endpointIPv6Address
        - IncludeExtAssocIDTLV (str): optional regex of includeExtAssocIDTLV
        - IncludePPAGTLV (str): optional regex of includePPAGTLV
        - IncludeSRPolicyCPathIDTLV (str): optional regex of includeSRPolicyCPathIDTLV
        - IncludeSRPolicyCPathNameTLV (str): optional regex of includeSRPolicyCPathNameTLV
        - IncludeSRPolicyCPathPrefTLV (str): optional regex of includeSRPolicyCPathPrefTLV
        - IncludeSRPolicyPolNameTLV (str): optional regex of includeSRPolicyPolNameTLV
        - Ipv4AssociationSrc (str): optional regex of ipv4AssociationSrc
        - Ipv6AssociationSrc (str): optional regex of ipv6AssociationSrc
        - OriginatorASN (str): optional regex of originatorASN
        - OriginatorIPVersion (str): optional regex of originatorIPVersion
        - OriginatorIPv4Address (str): optional regex of originatorIPv4Address
        - OriginatorIPv6Address (str): optional regex of originatorIPv6Address
        - PolicyEndpointType (str): optional regex of policyEndpointType
        - Preference (str): optional regex of preference
        - ProtectionLspBit (str): optional regex of protectionLspBit
        - ProtocolOrigin (str): optional regex of protocolOrigin
        - RemoveAssociation (str): optional regex of removeAssociation
        - SrPolicyCPathName (str): optional regex of srPolicyCPathName
        - SrPolicyName (str): optional regex of srPolicyName
        - StandbyLspBit (str): optional regex of standbyLspBit

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
