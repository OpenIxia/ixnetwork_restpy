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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class BgpEpePeerLinkList(Base):
    """EPE Peer Links
    The BgpEpePeerLinkList class encapsulates a required bgpEpePeerLinkList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'bgpEpePeerLinkList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'BBit': 'bBit',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnableLinkAddress': 'enableLinkAddress',
        'EnableLinkIdentifier': 'enableLinkIdentifier',
        'EnablePeerAdjSid': 'enablePeerAdjSid',
        'LBit': 'lBit',
        'LinkAddressType': 'linkAddressType',
        'LinkLocalIdentifier': 'linkLocalIdentifier',
        'LinkNumber': 'linkNumber',
        'LinkRemoteIdentifier': 'linkRemoteIdentifier',
        'LocalIpv4LinkAddress': 'localIpv4LinkAddress',
        'LocalIpv6LinkAddress': 'localIpv6LinkAddress',
        'Name': 'name',
        'PBit': 'pBit',
        'PeerName': 'peerName',
        'RemoteIpv4LinkAddress': 'remoteIpv4LinkAddress',
        'RemoteIpv6LinkAddress': 'remoteIpv6LinkAddress',
        'Reserved': 'reserved',
        'RsvdBits': 'rsvdBits',
        'SidIndex': 'sidIndex',
        'SidIndexValue': 'sidIndexValue',
        'VBit': 'vBit',
        'Weight': 'weight',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(BgpEpePeerLinkList, self).__init__(parent, list_op)

    @property
    def TlvProfile(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile_421be1db953efaf826fe146cf9700e26.TlvProfile): An instance of the TlvProfile class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile_421be1db953efaf826fe146cf9700e26 import TlvProfile
        if len(self._object_properties) > 0:
            if self._properties.get('TlvProfile', None) is not None:
                return self._properties.get('TlvProfile')
        return TlvProfile(self)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def BBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): B-Flag:Backup Flag.If set, the SID refers to a path that is eligible for protection.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BBit']))

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def EnableLinkAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Link Addresses
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableLinkAddress']))

    @property
    def EnableLinkIdentifier(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Link Identifier
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableLinkIdentifier']))

    @property
    def EnablePeerAdjSid(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable Peer-Adj-SID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnablePeerAdjSid']))

    @property
    def LBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): L-Flag: Local Flag. If set, then the value/index carried by the SID has local significance.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LBit']))

    @property
    def LinkAddressType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Link Address Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LinkAddressType']))

    @property
    def LinkLocalIdentifier(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Link Local Identifier
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LinkLocalIdentifier']))

    @property
    def LinkNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): EPE Link Number For Reference
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LinkNumber']))

    @property
    def LinkRemoteIdentifier(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Link Remote Identifier
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LinkRemoteIdentifier']))

    @property
    def LocalIpv4LinkAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Local IPv4 Link Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocalIpv4LinkAddress']))

    @property
    def LocalIpv6LinkAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Local IPv6 Link Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocalIpv6LinkAddress']))

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def PBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): P-Flag: Persistent Flag: If set, the SID is persistently allocated, i.e. the SID value remains consistent across router restart and session/interface flap
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PBit']))

    @property
    def PeerName(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Peer Name For Reference
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeerName'])

    @property
    def RemoteIpv4LinkAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Remote IPv4 Link Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RemoteIpv4LinkAddress']))

    @property
    def RemoteIpv6LinkAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Remote IPv6 Link Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RemoteIpv6LinkAddress']))

    @property
    def Reserved(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Reserved
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def RsvdBits(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Reserved for future use and MUST be zero when originated and ignored when received
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RsvdBits']))

    @property
    def SidIndex(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Local Label for Peer-Adj
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SidIndex']))

    @property
    def SidIndexValue(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If Local Label type is SID, max value is 16777215 and for Index max value is 4294967295
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SidIndexValue']))

    @property
    def VBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): V-Flag: Value flag. If set, then the SID carries a label value.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VBit']))

    @property
    def Weight(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Weight of the SID for the purpose of load balancing
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Weight']))

    def update(self, Name=None):
        # type: (str) -> BgpEpePeerLinkList
        """Updates bgpEpePeerLinkList resource on the server.

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

    def find(self, Count=None, DescriptiveName=None, Name=None, PeerName=None):
        # type: (int, str, str, List[str]) -> BgpEpePeerLinkList
        """Finds and retrieves bgpEpePeerLinkList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpEpePeerLinkList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpEpePeerLinkList resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PeerName (list(str)): Peer Name For Reference

        Returns
        -------
        - self: This instance with matching bgpEpePeerLinkList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpEpePeerLinkList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpEpePeerLinkList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, BBit=None, EnableLinkAddress=None, EnableLinkIdentifier=None, EnablePeerAdjSid=None, LBit=None, LinkAddressType=None, LinkLocalIdentifier=None, LinkNumber=None, LinkRemoteIdentifier=None, LocalIpv4LinkAddress=None, LocalIpv6LinkAddress=None, PBit=None, RemoteIpv4LinkAddress=None, RemoteIpv6LinkAddress=None, Reserved=None, RsvdBits=None, SidIndex=None, SidIndexValue=None, VBit=None, Weight=None):
        """Base class infrastructure that gets a list of bgpEpePeerLinkList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - BBit (str): optional regex of bBit
        - EnableLinkAddress (str): optional regex of enableLinkAddress
        - EnableLinkIdentifier (str): optional regex of enableLinkIdentifier
        - EnablePeerAdjSid (str): optional regex of enablePeerAdjSid
        - LBit (str): optional regex of lBit
        - LinkAddressType (str): optional regex of linkAddressType
        - LinkLocalIdentifier (str): optional regex of linkLocalIdentifier
        - LinkNumber (str): optional regex of linkNumber
        - LinkRemoteIdentifier (str): optional regex of linkRemoteIdentifier
        - LocalIpv4LinkAddress (str): optional regex of localIpv4LinkAddress
        - LocalIpv6LinkAddress (str): optional regex of localIpv6LinkAddress
        - PBit (str): optional regex of pBit
        - RemoteIpv4LinkAddress (str): optional regex of remoteIpv4LinkAddress
        - RemoteIpv6LinkAddress (str): optional regex of remoteIpv6LinkAddress
        - Reserved (str): optional regex of reserved
        - RsvdBits (str): optional regex of rsvdBits
        - SidIndex (str): optional regex of sidIndex
        - SidIndexValue (str): optional regex of sidIndexValue
        - VBit (str): optional regex of vBit
        - Weight (str): optional regex of weight

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
