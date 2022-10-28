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


class Interface(Base):
    """This object holds the information for a single interface on the LDP router.
    The Interface class encapsulates a list of interface resources that are managed by the user.
    A list of resources can be retrieved from the server using the Interface.find() method.
    The list can be managed by using the Interface.add() and Interface.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "interface"
    _SDM_ATT_MAP = {
        "AdvertisingMode": "advertisingMode",
        "AtmVcDirection": "atmVcDirection",
        "Authentication": "authentication",
        "BfdOperationMode": "bfdOperationMode",
        "DiscoveryMode": "discoveryMode",
        "EnableAtmSession": "enableAtmSession",
        "EnableBfdRegistration": "enableBfdRegistration",
        "Enabled": "enabled",
        "IsLdpLearnedInfoRefreshed": "isLdpLearnedInfoRefreshed",
        "LabelSpaceId": "labelSpaceId",
        "Md5Key": "md5Key",
        "ProtocolInterface": "protocolInterface",
    }
    _SDM_ENUM_MAP = {
        "advertisingMode": ["unsolicited", "onDemand"],
        "atmVcDirection": ["unidirectional", "bidirectional"],
        "authentication": ["null", "md5"],
        "bfdOperationMode": ["singleHop", "multiHop"],
        "discoveryMode": ["basic", "extended", "extendedMartini"],
    }

    def __init__(self, parent, list_op=False):
        super(Interface, self).__init__(parent, list_op)

    @property
    def AtmLabelRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.atmlabelrange_ebe9434fea7d160a4f5a4fca69d81dcf.AtmLabelRange): An instance of the AtmLabelRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.atmlabelrange_ebe9434fea7d160a4f5a4fca69d81dcf import (
            AtmLabelRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AtmLabelRange", None) is not None:
                return self._properties.get("AtmLabelRange")
        return AtmLabelRange(self)

    @property
    def LearnedFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedfilter_df33d6e2936a15d8a0c3082383d4e700.LearnedFilter): An instance of the LearnedFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedfilter_df33d6e2936a15d8a0c3082383d4e700 import (
            LearnedFilter,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedFilter", None) is not None:
                return self._properties.get("LearnedFilter")
        return LearnedFilter(self)._select()

    @property
    def LearnedIpv4Label(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedipv4label_fd641bf6fc1fc77c6a919b5699bdcbe0.LearnedIpv4Label): An instance of the LearnedIpv4Label class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedipv4label_fd641bf6fc1fc77c6a919b5699bdcbe0 import (
            LearnedIpv4Label,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedIpv4Label", None) is not None:
                return self._properties.get("LearnedIpv4Label")
        return LearnedIpv4Label(self)

    @property
    def LearnedIpv4P2mpLables(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedipv4p2mplables_7da643070755e8b965ca7f53c9a8250a.LearnedIpv4P2mpLables): An instance of the LearnedIpv4P2mpLables class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedipv4p2mplables_7da643070755e8b965ca7f53c9a8250a import (
            LearnedIpv4P2mpLables,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedIpv4P2mpLables", None) is not None:
                return self._properties.get("LearnedIpv4P2mpLables")
        return LearnedIpv4P2mpLables(self)

    @property
    def LearnedMartiniLabel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedmartinilabel_cc6a3b5bae90ffc430db92d0f71136a1.LearnedMartiniLabel): An instance of the LearnedMartiniLabel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedmartinilabel_cc6a3b5bae90ffc430db92d0f71136a1 import (
            LearnedMartiniLabel,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedMartiniLabel", None) is not None:
                return self._properties.get("LearnedMartiniLabel")
        return LearnedMartiniLabel(self)

    @property
    def TargetPeer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.targetpeer_d7cc221539f0f14696e2588a1ed5bda7.TargetPeer): An instance of the TargetPeer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.targetpeer_d7cc221539f0f14696e2588a1ed5bda7 import (
            TargetPeer,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TargetPeer", None) is not None:
                return self._properties.get("TargetPeer")
        return TargetPeer(self)

    @property
    def AdvertisingMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(unsolicited | onDemand): The mode by which labels are advertised, either downstream unsolicited or downstream on demand.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AdvertisingMode"])

    @AdvertisingMode.setter
    def AdvertisingMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AdvertisingMode"], value)

    @property
    def AtmVcDirection(self):
        # type: () -> str
        """
        Returns
        -------
        - str(unidirectional | bidirectional): Whether a virtual circuit (VC) may be used one way or both ways as an LSP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AtmVcDirection"])

    @AtmVcDirection.setter
    def AtmVcDirection(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AtmVcDirection"], value)

    @property
    def Authentication(self):
        # type: () -> str
        """
        Returns
        -------
        - str(null | md5): The cryptographic authentication type used by the interface; one of: NULL (no authentication) or MD5. When MD5 is used, an md5Key must be configured by the user.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Authentication"])

    @Authentication.setter
    def Authentication(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Authentication"], value)

    @property
    def BfdOperationMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(singleHop | multiHop): Helps to set the BFD session in terms of hops, one of Single and Multi.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BfdOperationMode"])

    @BfdOperationMode.setter
    def BfdOperationMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["BfdOperationMode"], value)

    @property
    def DiscoveryMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(basic | extended | extendedMartini): The discovery mode used for the interface: basic, extended, or extended Martini.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DiscoveryMode"])

    @DiscoveryMode.setter
    def DiscoveryMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DiscoveryMode"], value)

    @property
    def EnableAtmSession(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the establishment of ATM sessions.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAtmSession"])

    @EnableAtmSession.setter
    def EnableAtmSession(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAtmSession"], value)

    @property
    def EnableBfdRegistration(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables BFD registration with LDP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableBfdRegistration"])

    @EnableBfdRegistration.setter
    def EnableBfdRegistration(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableBfdRegistration"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the use of this interface for the simulated router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def IsLdpLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When enabled, automatically refreshes the LDP learned info (from the DUT).
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsLdpLearnedInfoRefreshed"])

    @property
    def LabelSpaceId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The LDP label space used by this interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LabelSpaceId"])

    @LabelSpaceId.setter
    def LabelSpaceId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LabelSpaceId"], value)

    @property
    def Md5Key(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Used with MD5 authentication. A user-defined string; maximum = 255 characters.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Md5Key"])

    @Md5Key.setter
    def Md5Key(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Md5Key"], value)

    @property
    def ProtocolInterface(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/interface): The protocol interface associated with this LDP interface. There may be more than one protocol interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProtocolInterface"])

    @ProtocolInterface.setter
    def ProtocolInterface(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProtocolInterface"], value)

    def update(
        self,
        AdvertisingMode=None,
        AtmVcDirection=None,
        Authentication=None,
        BfdOperationMode=None,
        DiscoveryMode=None,
        EnableAtmSession=None,
        EnableBfdRegistration=None,
        Enabled=None,
        LabelSpaceId=None,
        Md5Key=None,
        ProtocolInterface=None,
    ):
        # type: (str, str, str, str, str, bool, bool, bool, int, str, str) -> Interface
        """Updates interface resource on the server.

        Args
        ----
        - AdvertisingMode (str(unsolicited | onDemand)): The mode by which labels are advertised, either downstream unsolicited or downstream on demand.
        - AtmVcDirection (str(unidirectional | bidirectional)): Whether a virtual circuit (VC) may be used one way or both ways as an LSP.
        - Authentication (str(null | md5)): The cryptographic authentication type used by the interface; one of: NULL (no authentication) or MD5. When MD5 is used, an md5Key must be configured by the user.
        - BfdOperationMode (str(singleHop | multiHop)): Helps to set the BFD session in terms of hops, one of Single and Multi.
        - DiscoveryMode (str(basic | extended | extendedMartini)): The discovery mode used for the interface: basic, extended, or extended Martini.
        - EnableAtmSession (bool): Enables the establishment of ATM sessions.
        - EnableBfdRegistration (bool): If true, enables BFD registration with LDP.
        - Enabled (bool): Enables the use of this interface for the simulated router.
        - LabelSpaceId (number): The LDP label space used by this interface.
        - Md5Key (str): Used with MD5 authentication. A user-defined string; maximum = 255 characters.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): The protocol interface associated with this LDP interface. There may be more than one protocol interface.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        AdvertisingMode=None,
        AtmVcDirection=None,
        Authentication=None,
        BfdOperationMode=None,
        DiscoveryMode=None,
        EnableAtmSession=None,
        EnableBfdRegistration=None,
        Enabled=None,
        LabelSpaceId=None,
        Md5Key=None,
        ProtocolInterface=None,
    ):
        # type: (str, str, str, str, str, bool, bool, bool, int, str, str) -> Interface
        """Adds a new interface resource on the server and adds it to the container.

        Args
        ----
        - AdvertisingMode (str(unsolicited | onDemand)): The mode by which labels are advertised, either downstream unsolicited or downstream on demand.
        - AtmVcDirection (str(unidirectional | bidirectional)): Whether a virtual circuit (VC) may be used one way or both ways as an LSP.
        - Authentication (str(null | md5)): The cryptographic authentication type used by the interface; one of: NULL (no authentication) or MD5. When MD5 is used, an md5Key must be configured by the user.
        - BfdOperationMode (str(singleHop | multiHop)): Helps to set the BFD session in terms of hops, one of Single and Multi.
        - DiscoveryMode (str(basic | extended | extendedMartini)): The discovery mode used for the interface: basic, extended, or extended Martini.
        - EnableAtmSession (bool): Enables the establishment of ATM sessions.
        - EnableBfdRegistration (bool): If true, enables BFD registration with LDP.
        - Enabled (bool): Enables the use of this interface for the simulated router.
        - LabelSpaceId (number): The LDP label space used by this interface.
        - Md5Key (str): Used with MD5 authentication. A user-defined string; maximum = 255 characters.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): The protocol interface associated with this LDP interface. There may be more than one protocol interface.

        Returns
        -------
        - self: This instance with all currently retrieved interface resources using find and the newly added interface resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained interface resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        AdvertisingMode=None,
        AtmVcDirection=None,
        Authentication=None,
        BfdOperationMode=None,
        DiscoveryMode=None,
        EnableAtmSession=None,
        EnableBfdRegistration=None,
        Enabled=None,
        IsLdpLearnedInfoRefreshed=None,
        LabelSpaceId=None,
        Md5Key=None,
        ProtocolInterface=None,
    ):
        # type: (str, str, str, str, str, bool, bool, bool, bool, int, str, str) -> Interface
        """Finds and retrieves interface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve interface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all interface resources from the server.

        Args
        ----
        - AdvertisingMode (str(unsolicited | onDemand)): The mode by which labels are advertised, either downstream unsolicited or downstream on demand.
        - AtmVcDirection (str(unidirectional | bidirectional)): Whether a virtual circuit (VC) may be used one way or both ways as an LSP.
        - Authentication (str(null | md5)): The cryptographic authentication type used by the interface; one of: NULL (no authentication) or MD5. When MD5 is used, an md5Key must be configured by the user.
        - BfdOperationMode (str(singleHop | multiHop)): Helps to set the BFD session in terms of hops, one of Single and Multi.
        - DiscoveryMode (str(basic | extended | extendedMartini)): The discovery mode used for the interface: basic, extended, or extended Martini.
        - EnableAtmSession (bool): Enables the establishment of ATM sessions.
        - EnableBfdRegistration (bool): If true, enables BFD registration with LDP.
        - Enabled (bool): Enables the use of this interface for the simulated router.
        - IsLdpLearnedInfoRefreshed (bool): When enabled, automatically refreshes the LDP learned info (from the DUT).
        - LabelSpaceId (number): The LDP label space used by this interface.
        - Md5Key (str): Used with MD5 authentication. A user-defined string; maximum = 255 characters.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): The protocol interface associated with this LDP interface. There may be more than one protocol interface.

        Returns
        -------
        - self: This instance with matching interface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of interface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the interface resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def RefreshLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshLearnedInfo operation on the server.

        This exec refreshes the LDP learned information from the DUT.

        refreshLearnedInfo(async_operation=bool)bool
        --------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
            "refreshLearnedInfo", payload=payload, response_object=None
        )
