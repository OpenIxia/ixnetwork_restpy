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


class PppoxServerSessions(Base):
    """PPPoX Server Sessions.
    The PppoxServerSessions class encapsulates a required pppoxServerSessions resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "pppoxServerSessions"
    _SDM_ATT_MAP = {
        "ChapName": "chapName",
        "ChapSecret": "chapSecret",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "DiscoveredClientsMacs": "discoveredClientsMacs",
        "DiscoveredRemoteSessionIds": "discoveredRemoteSessionIds",
        "DiscoveredRemoteTunnelIds": "discoveredRemoteTunnelIds",
        "DiscoveredSessionIds": "discoveredSessionIds",
        "DiscoveredTunnelIPs": "discoveredTunnelIPs",
        "DiscoveredTunnelIds": "discoveredTunnelIds",
        "DomainList": "domainList",
        "EnableDomainGroups": "enableDomainGroups",
        "Name": "name",
        "PapPassword": "papPassword",
        "PapUser": "papUser",
        "ServerIpv4Addresses": "serverIpv4Addresses",
        "ServerIpv6Addresses": "serverIpv6Addresses",
        "SessionInfo": "sessionInfo",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PppoxServerSessions, self).__init__(parent, list_op)

    @property
    def Tag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d.Tag): An instance of the Tag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d import (
            Tag,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Tag", None) is not None:
                return self._properties.get("Tag")
        return Tag(self)

    @property
    def ChapName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User name when CHAP Authentication is being used
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ChapName"]))

    @property
    def ChapSecret(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Secret when CHAP Authentication is being used
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ChapSecret"]))

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
    def DiscoveredClientsMacs(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The discovered remote MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DiscoveredClientsMacs"])

    @property
    def DiscoveredRemoteSessionIds(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): The negotiated session ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DiscoveredRemoteSessionIds"])

    @property
    def DiscoveredRemoteTunnelIds(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): The negotiated tunnel ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DiscoveredRemoteTunnelIds"])

    @property
    def DiscoveredSessionIds(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): The negotiated session ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DiscoveredSessionIds"])

    @property
    def DiscoveredTunnelIPs(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The discovered remote tunnel IP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DiscoveredTunnelIPs"])

    @property
    def DiscoveredTunnelIds(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): The negotiated tunnel ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DiscoveredTunnelIds"])

    @property
    def DomainList(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure domain group settings
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DomainList"]))

    @property
    def EnableDomainGroups(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable domain groups
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableDomainGroups"])
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
    def PapPassword(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Password when PAP Authentication is being used
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PapPassword"]))

    @property
    def PapUser(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User name when PAP Authentication is being used
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PapUser"]))

    @property
    def ServerIpv4Addresses(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): IPv4 Server Address. Each PPPoX Server Session will display the v4 address from the PPPoX Server it belongs to.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerIpv4Addresses"])

    @property
    def ServerIpv6Addresses(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): IPv6 Server Address. Each PPPoX Server Session will display the v6 address from the PPPoX Server it belongs to.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ServerIpv6Addresses"])

    @property
    def SessionInfo(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[cLS_CFG_REJ_AUTH | cLS_CHAP_PEER_DET_FAIL | cLS_CHAP_PEER_RESP_BAD | cLS_CODE_REJ_IPCP | cLS_CODE_REJ_IPV6CP | cLS_CODE_REJ_LCP | cLS_ERR_PPP_NO_BUF | cLS_ERR_PPP_SEND_PKT | cLS_LINK_DISABLE | cLS_LOC_IPADDR_BROADCAST | cLS_LOC_IPADDR_CLASS_E | cLS_LOC_IPADDR_INVAL_ACKS_0 | cLS_LOC_IPADDR_INVAL_ACKS_DIFF | cLS_LOC_IPADDR_LOOPBACK | cLS_LOC_IPADDR_PEER_MATCH_LOC | cLS_LOC_IPADDR_PEER_NO_GIVE | cLS_LOC_IPADDR_PEER_NO_HELP | cLS_LOC_IPADDR_PEER_NO_TAKE | cLS_LOC_IPADDR_PEER_REJ | cLS_LOOPBACK_DETECT | cLS_NO_NCP | cLS_NONE | cLS_PAP_BAD_PASSWD | cLS_PEER_DISCONNECTED | cLS_PEER_IPADDR_MATCH_LOC | cLS_PEER_IPADDR_PEER_NO_SET | cLS_PPOE_AC_SYSTEM_ERROR | cLS_PPOE_GENERIC_ERROR | cLS_PPP_DISABLE | cLS_PPPOE_PADI_TIMEOUT | cLS_PPPOE_PADO_TIMEOUT | cLS_PPPOE_PADR_TIMEOUT | cLS_PROTO_REJ_IPCP | cLS_PROTO_REJ_IPv6CP | cLS_TIMEOUT_CHAP_CHAL | cLS_TIMEOUT_CHAP_RESP | cLS_TIMEOUT_IPCP_CFG_REQ | cLS_TIMEOUT_IPV6CP_CFG_REQ | cLS_TIMEOUT_IPV6CP_RA | cLS_TIMEOUT_LCP_CFG_REQ | cLS_TIMEOUT_LCP_ECHO_REQ | cLS_TIMEOUT_PAP_AUTH_REQ]): Logs additional information about the session state
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionInfo"])

    def update(self, Name=None):
        # type: (str) -> PppoxServerSessions
        """Updates pppoxServerSessions resource on the server.

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

    def find(
        self,
        Count=None,
        DescriptiveName=None,
        DiscoveredClientsMacs=None,
        DiscoveredRemoteSessionIds=None,
        DiscoveredRemoteTunnelIds=None,
        DiscoveredSessionIds=None,
        DiscoveredTunnelIPs=None,
        DiscoveredTunnelIds=None,
        Name=None,
        ServerIpv4Addresses=None,
        ServerIpv6Addresses=None,
        SessionInfo=None,
    ):
        # type: (int, str, List[str], List[int], List[int], List[int], List[str], List[int], str, List[str], List[str], List[str]) -> PppoxServerSessions
        """Finds and retrieves pppoxServerSessions resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pppoxServerSessions resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pppoxServerSessions resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - DiscoveredClientsMacs (list(str)): The discovered remote MAC address.
        - DiscoveredRemoteSessionIds (list(number)): The negotiated session ID.
        - DiscoveredRemoteTunnelIds (list(number)): The negotiated tunnel ID.
        - DiscoveredSessionIds (list(number)): The negotiated session ID.
        - DiscoveredTunnelIPs (list(str)): The discovered remote tunnel IP.
        - DiscoveredTunnelIds (list(number)): The negotiated tunnel ID.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - ServerIpv4Addresses (list(str)): IPv4 Server Address. Each PPPoX Server Session will display the v4 address from the PPPoX Server it belongs to.
        - ServerIpv6Addresses (list(str)): IPv6 Server Address. Each PPPoX Server Session will display the v6 address from the PPPoX Server it belongs to.
        - SessionInfo (list(str[cLS_CFG_REJ_AUTH | cLS_CHAP_PEER_DET_FAIL | cLS_CHAP_PEER_RESP_BAD | cLS_CODE_REJ_IPCP | cLS_CODE_REJ_IPV6CP | cLS_CODE_REJ_LCP | cLS_ERR_PPP_NO_BUF | cLS_ERR_PPP_SEND_PKT | cLS_LINK_DISABLE | cLS_LOC_IPADDR_BROADCAST | cLS_LOC_IPADDR_CLASS_E | cLS_LOC_IPADDR_INVAL_ACKS_0 | cLS_LOC_IPADDR_INVAL_ACKS_DIFF | cLS_LOC_IPADDR_LOOPBACK | cLS_LOC_IPADDR_PEER_MATCH_LOC | cLS_LOC_IPADDR_PEER_NO_GIVE | cLS_LOC_IPADDR_PEER_NO_HELP | cLS_LOC_IPADDR_PEER_NO_TAKE | cLS_LOC_IPADDR_PEER_REJ | cLS_LOOPBACK_DETECT | cLS_NO_NCP | cLS_NONE | cLS_PAP_BAD_PASSWD | cLS_PEER_DISCONNECTED | cLS_PEER_IPADDR_MATCH_LOC | cLS_PEER_IPADDR_PEER_NO_SET | cLS_PPOE_AC_SYSTEM_ERROR | cLS_PPOE_GENERIC_ERROR | cLS_PPP_DISABLE | cLS_PPPOE_PADI_TIMEOUT | cLS_PPPOE_PADO_TIMEOUT | cLS_PPPOE_PADR_TIMEOUT | cLS_PROTO_REJ_IPCP | cLS_PROTO_REJ_IPv6CP | cLS_TIMEOUT_CHAP_CHAL | cLS_TIMEOUT_CHAP_RESP | cLS_TIMEOUT_IPCP_CFG_REQ | cLS_TIMEOUT_IPV6CP_CFG_REQ | cLS_TIMEOUT_IPV6CP_RA | cLS_TIMEOUT_LCP_CFG_REQ | cLS_TIMEOUT_LCP_ECHO_REQ | cLS_TIMEOUT_PAP_AUTH_REQ])): Logs additional information about the session state

        Returns
        -------
        - self: This instance with matching pppoxServerSessions resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pppoxServerSessions data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pppoxServerSessions resources from the server available through an iterator or index

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

    def CloseIpcp(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the closeIpcp operation on the server.

        Close IPCP for selected PPPoX Server Sessions items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        closeIpcp(async_operation=bool)
        -------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        closeIpcp(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        closeIpcp(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("closeIpcp", payload=payload, response_object=None)

    def CloseIpv6cp(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the closeIpv6cp operation on the server.

        Close IPv6CP for selected PPPoX Severs Sessions items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        closeIpv6cp(async_operation=bool)
        ---------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        closeIpv6cp(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        closeIpv6cp(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("closeIpv6cp", payload=payload, response_object=None)

    def get_device_ids(
        self,
        PortNames=None,
        ChapName=None,
        ChapSecret=None,
        DomainList=None,
        EnableDomainGroups=None,
        PapPassword=None,
        PapUser=None,
    ):
        """Base class infrastructure that gets a list of pppoxServerSessions device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ChapName (str): optional regex of chapName
        - ChapSecret (str): optional regex of chapSecret
        - DomainList (str): optional regex of domainList
        - EnableDomainGroups (str): optional regex of enableDomainGroups
        - PapPassword (str): optional regex of papPassword
        - PapUser (str): optional regex of papUser

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
