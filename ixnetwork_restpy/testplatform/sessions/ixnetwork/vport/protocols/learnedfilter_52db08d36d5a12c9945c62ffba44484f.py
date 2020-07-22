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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LearnedFilter(Base):
    """This object controls the filter criteria for learned LDP information (from the DUT).
    The LearnedFilter class encapsulates a required learnedFilter resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedFilter'
    _SDM_ATT_MAP = {
        'EnableFilter': 'enableFilter',
        'EnableIpv4FecAddress': 'enableIpv4FecAddress',
        'EnableIpv4FecMask': 'enableIpv4FecMask',
        'EnableIpv4RootAddress': 'enableIpv4RootAddress',
        'EnableLabel': 'enableLabel',
        'EnableMartiniDescription': 'enableMartiniDescription',
        'EnableMartiniGroupId': 'enableMartiniGroupId',
        'EnableMartiniVcId': 'enableMartiniVcId',
        'EnableMartiniVcType': 'enableMartiniVcType',
        'EnablePeerAddress': 'enablePeerAddress',
        'EnablePeerMask': 'enablePeerMask',
        'Ipv4FecAddress': 'ipv4FecAddress',
        'Ipv4FecMask': 'ipv4FecMask',
        'Ipv4FecMaskMatch': 'ipv4FecMaskMatch',
        'Label': 'label',
        'MartiniDescription': 'martiniDescription',
        'MartiniGroupId': 'martiniGroupId',
        'MartiniVcId': 'martiniVcId',
        'MartiniVcType': 'martiniVcType',
        'PeerAddress': 'peerAddress',
        'PeerMask': 'peerMask',
        'RootAddress': 'rootAddress',
    }

    def __init__(self, parent):
        super(LearnedFilter, self).__init__(parent)

    @property
    def EnableFilter(self):
        """
        Returns
        -------
        - bool: Enables the use of the LDP learned labels filter.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableFilter'])
    @EnableFilter.setter
    def EnableFilter(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableFilter'], value)

    @property
    def EnableIpv4FecAddress(self):
        """
        Returns
        -------
        - bool: If enabled, uses the network address associated with the FEC.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableIpv4FecAddress'])
    @EnableIpv4FecAddress.setter
    def EnableIpv4FecAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableIpv4FecAddress'], value)

    @property
    def EnableIpv4FecMask(self):
        """
        Returns
        -------
        - bool: (FEC Mask Match must be enabled for this option to be active.)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableIpv4FecMask'])
    @EnableIpv4FecMask.setter
    def EnableIpv4FecMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableIpv4FecMask'], value)

    @property
    def EnableIpv4RootAddress(self):
        """
        Returns
        -------
        - bool: If enabled, it signifies the IP version 4 root address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableIpv4RootAddress'])
    @EnableIpv4RootAddress.setter
    def EnableIpv4RootAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableIpv4RootAddress'], value)

    @property
    def EnableLabel(self):
        """
        Returns
        -------
        - bool: If enabled, uses the label value added to the packet(s) by the upstream LDP peer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLabel'])
    @EnableLabel.setter
    def EnableLabel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLabel'], value)

    @property
    def EnableMartiniDescription(self):
        """
        Returns
        -------
        - bool: An optional user-defined interface description. It may be used with ALL VC types. Valid length is 0 to 80 octets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMartiniDescription'])
    @EnableMartiniDescription.setter
    def EnableMartiniDescription(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMartiniDescription'], value)

    @property
    def EnableMartiniGroupId(self):
        """
        Returns
        -------
        - bool: An arbitrary 32-bit value used to identify a group of VCs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMartiniGroupId'])
    @EnableMartiniGroupId.setter
    def EnableMartiniGroupId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMartiniGroupId'], value)

    @property
    def EnableMartiniVcId(self):
        """
        Returns
        -------
        - bool: The 32-bit VC connection identifier. Used with the VC type to identify a specific VC (for VC types 0x0001 to 0x000B).
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMartiniVcId'])
    @EnableMartiniVcId.setter
    def EnableMartiniVcId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMartiniVcId'], value)

    @property
    def EnableMartiniVcType(self):
        """
        Returns
        -------
        - bool: Enables the type of martini virtual circuit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMartiniVcType'])
    @EnableMartiniVcType.setter
    def EnableMartiniVcType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMartiniVcType'], value)

    @property
    def EnablePeerAddress(self):
        """
        Returns
        -------
        - bool: Uses the IP address of the LDP peer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePeerAddress'])
    @EnablePeerAddress.setter
    def EnablePeerAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePeerAddress'], value)

    @property
    def EnablePeerMask(self):
        """
        Returns
        -------
        - bool: (Peer address must be enabled for this option to be active.) If enabled, uses the number of bits in the mask for the peer's IP address for a loose match.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePeerMask'])
    @EnablePeerMask.setter
    def EnablePeerMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePeerMask'], value)

    @property
    def Ipv4FecAddress(self):
        """
        Returns
        -------
        - str: The IPv4 address component of the FEC. (default = 0.0.0.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4FecAddress'])
    @Ipv4FecAddress.setter
    def Ipv4FecAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4FecAddress'], value)

    @property
    def Ipv4FecMask(self):
        """
        Returns
        -------
        - number: The prefix length of the network IPv4 address. (default = 24)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4FecMask'])
    @Ipv4FecMask.setter
    def Ipv4FecMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4FecMask'], value)

    @property
    def Ipv4FecMaskMatch(self):
        """
        Returns
        -------
        - str(exactMatch | looseMatch): FEC Mask Match must be enabled for this option to be active.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4FecMaskMatch'])
    @Ipv4FecMaskMatch.setter
    def Ipv4FecMaskMatch(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv4FecMaskMatch'], value)

    @property
    def Label(self):
        """
        Returns
        -------
        - number: The first label to be assigned to the FEC.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Label'])
    @Label.setter
    def Label(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Label'], value)

    @property
    def MartiniDescription(self):
        """
        Returns
        -------
        - str: An optional user-defined interface description. It may be used with ALL VC types. Valid length is 0 to 80 octets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MartiniDescription'])
    @MartiniDescription.setter
    def MartiniDescription(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MartiniDescription'], value)

    @property
    def MartiniGroupId(self):
        """
        Returns
        -------
        - number: An arbitrary 32-bit value used to identify a group of VCs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MartiniGroupId'])
    @MartiniGroupId.setter
    def MartiniGroupId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MartiniGroupId'], value)

    @property
    def MartiniVcId(self):
        """
        Returns
        -------
        - number: The 32-bit VC connection identifier. Used with the VC type to identify a specific VC (for VC types 0x0001 to 0x000B).
        """
        return self._get_attribute(self._SDM_ATT_MAP['MartiniVcId'])
    @MartiniVcId.setter
    def MartiniVcId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MartiniVcId'], value)

    @property
    def MartiniVcType(self):
        """
        Returns
        -------
        - str(frameRelay | atmaal5 | atmxCell | vlan | ethernet | hdlc | ppp | cem | atmvcc | atmvpc | ip): The type of L2 VC depends on the Layer 2 protocol types.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MartiniVcType'])
    @MartiniVcType.setter
    def MartiniVcType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MartiniVcType'], value)

    @property
    def PeerAddress(self):
        """
        Returns
        -------
        - str: If enabled, uses the IP address of the LDP peer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeerAddress'])
    @PeerAddress.setter
    def PeerAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PeerAddress'], value)

    @property
    def PeerMask(self):
        """
        Returns
        -------
        - number: (Peer Address must be enabled for this option to be active.) If enabled, uses the number of bits in the mask for the peer's IP address for a loose match.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeerMask'])
    @PeerMask.setter
    def PeerMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PeerMask'], value)

    @property
    def RootAddress(self):
        """
        Returns
        -------
        - str: Indicates the root address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RootAddress'])
    @RootAddress.setter
    def RootAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RootAddress'], value)

    def update(self, EnableFilter=None, EnableIpv4FecAddress=None, EnableIpv4FecMask=None, EnableIpv4RootAddress=None, EnableLabel=None, EnableMartiniDescription=None, EnableMartiniGroupId=None, EnableMartiniVcId=None, EnableMartiniVcType=None, EnablePeerAddress=None, EnablePeerMask=None, Ipv4FecAddress=None, Ipv4FecMask=None, Ipv4FecMaskMatch=None, Label=None, MartiniDescription=None, MartiniGroupId=None, MartiniVcId=None, MartiniVcType=None, PeerAddress=None, PeerMask=None, RootAddress=None):
        """Updates learnedFilter resource on the server.

        Args
        ----
        - EnableFilter (bool): Enables the use of the LDP learned labels filter.
        - EnableIpv4FecAddress (bool): If enabled, uses the network address associated with the FEC.
        - EnableIpv4FecMask (bool): (FEC Mask Match must be enabled for this option to be active.)
        - EnableIpv4RootAddress (bool): If enabled, it signifies the IP version 4 root address.
        - EnableLabel (bool): If enabled, uses the label value added to the packet(s) by the upstream LDP peer.
        - EnableMartiniDescription (bool): An optional user-defined interface description. It may be used with ALL VC types. Valid length is 0 to 80 octets.
        - EnableMartiniGroupId (bool): An arbitrary 32-bit value used to identify a group of VCs.
        - EnableMartiniVcId (bool): The 32-bit VC connection identifier. Used with the VC type to identify a specific VC (for VC types 0x0001 to 0x000B).
        - EnableMartiniVcType (bool): Enables the type of martini virtual circuit.
        - EnablePeerAddress (bool): Uses the IP address of the LDP peer.
        - EnablePeerMask (bool): (Peer address must be enabled for this option to be active.) If enabled, uses the number of bits in the mask for the peer's IP address for a loose match.
        - Ipv4FecAddress (str): The IPv4 address component of the FEC. (default = 0.0.0.0)
        - Ipv4FecMask (number): The prefix length of the network IPv4 address. (default = 24)
        - Ipv4FecMaskMatch (str(exactMatch | looseMatch)): FEC Mask Match must be enabled for this option to be active.
        - Label (number): The first label to be assigned to the FEC.
        - MartiniDescription (str): An optional user-defined interface description. It may be used with ALL VC types. Valid length is 0 to 80 octets.
        - MartiniGroupId (number): An arbitrary 32-bit value used to identify a group of VCs.
        - MartiniVcId (number): The 32-bit VC connection identifier. Used with the VC type to identify a specific VC (for VC types 0x0001 to 0x000B).
        - MartiniVcType (str(frameRelay | atmaal5 | atmxCell | vlan | ethernet | hdlc | ppp | cem | atmvcc | atmvpc | ip)): The type of L2 VC depends on the Layer 2 protocol types.
        - PeerAddress (str): If enabled, uses the IP address of the LDP peer.
        - PeerMask (number): (Peer Address must be enabled for this option to be active.) If enabled, uses the number of bits in the mask for the peer's IP address for a loose match.
        - RootAddress (str): Indicates the root address.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
