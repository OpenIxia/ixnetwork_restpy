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


class LearnedMartiniLabel(Base):
    """A single Martini label from the list maintained by the LDP interface object.
    The LearnedMartiniLabel class encapsulates a list of learnedMartiniLabel resources that are managed by the system.
    A list of resources can be retrieved from the server using the LearnedMartiniLabel.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedMartiniLabel'
    _SDM_ATT_MAP = {
        'CBit': 'cBit',
        'Cas': 'cas',
        'CemOption': 'cemOption',
        'CemPayloadBytes': 'cemPayloadBytes',
        'Description': 'description',
        'DisCeAddress': 'disCeAddress',
        'Frequency': 'frequency',
        'GroupId': 'groupId',
        'IncludeRtpHeader': 'includeRtpHeader',
        'Label': 'label',
        'LabelSpaceId': 'labelSpaceId',
        'LocalPwSubStatus': 'localPwSubStatus',
        'MaxAtmCell': 'maxAtmCell',
        'Mtu': 'mtu',
        'PayloadSize': 'payloadSize',
        'PayloadType': 'payloadType',
        'Peer': 'peer',
        'PeerPwSubStatus': 'peerPwSubStatus',
        'PwState': 'pwState',
        'Sp': 'sp',
        'Ssrc': 'ssrc',
        'TdmBitrate': 'tdmBitrate',
        'TimestampMode': 'timestampMode',
        'VcId': 'vcId',
        'VcType': 'vcType',
    }

    def __init__(self, parent):
        super(LearnedMartiniLabel, self).__init__(parent)

    @property
    def CBit(self):
        """
        Returns
        -------
        - bool: If enabled, sets the C-Bit (flag). It is the highest order bit in the VC Type field. If the bit is set, it indicates the presence of a control word on this VC.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CBit'])

    @property
    def Cas(self):
        """
        Returns
        -------
        - str(e1Trunk | t1EsfTrunk | t1SfTrunk): Indicates the CAS value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Cas'])

    @property
    def CemOption(self):
        """
        Returns
        -------
        - number: The value of the CEM option.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CemOption'])

    @property
    def CemPayloadBytes(self):
        """
        Returns
        -------
        - number: (For Circuit Emulation Service over MPLS/CEM). The length of the CEM payload (in bytes).
        """
        return self._get_attribute(self._SDM_ATT_MAP['CemPayloadBytes'])

    @property
    def Description(self):
        """
        Returns
        -------
        - str: An optional user-defined interface description. It may be used with ALL VC types. Valid length is 0 to 80 octets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])

    @property
    def DisCeAddress(self):
        """
        Returns
        -------
        - str: If the L2 interface type for the VC whose learned information is seen is IP, this field indicates the learned IP address of the remote end CE of the IP vrtual circuit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DisCeAddress'])

    @property
    def Frequency(self):
        """
        Returns
        -------
        - number: Indicates the frequency.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Frequency'])

    @property
    def GroupId(self):
        """
        Returns
        -------
        - number: An arbitrary 32-bit value used to identify a group of VCs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupId'])

    @property
    def IncludeRtpHeader(self):
        """
        Returns
        -------
        - bool: If enables, includes the RTP information in the header.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeRtpHeader'])

    @property
    def Label(self):
        """
        Returns
        -------
        - number: The label value added to the packet(s) by the upstream LDP peer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Label'])

    @property
    def LabelSpaceId(self):
        """
        Returns
        -------
        - number: (2 octets) Identifies the set of labels that will be used. Part of the LDP identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LabelSpaceId'])

    @property
    def LocalPwSubStatus(self):
        """
        Returns
        -------
        - number: It reflects the status carried in the PW status notification received from the peer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalPwSubStatus'])

    @property
    def MaxAtmCell(self):
        """
        Returns
        -------
        - number: The maximum number of ATM Cells which may be concatenated and sent in a single MPLS frame. This parameter is part of the FEC element.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxAtmCell'])

    @property
    def Mtu(self):
        """
        Returns
        -------
        - number: (in octets) The 2-octet value for the maximum Transmission Unit (MTU).
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mtu'])

    @property
    def PayloadSize(self):
        """
        Returns
        -------
        - number: Indicates the payload size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PayloadSize'])

    @property
    def PayloadType(self):
        """
        Returns
        -------
        - number: The payload type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PayloadType'])

    @property
    def Peer(self):
        """
        Returns
        -------
        - str: The RID of the upstream LDP peer. Part of the LSR ID. It must be globally unique. It forms the first 4 octets of the 6-octet LDP identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Peer'])

    @property
    def PeerPwSubStatus(self):
        """
        Returns
        -------
        - number: It reflects the status carried in the PW status last sent to the peer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeerPwSubStatus'])

    @property
    def PwState(self):
        """
        Returns
        -------
        - bool: The PseudoWire State - either Up or Down. For the PseudoWire to be Up (Up status), the VC ID, VC Type, and Peer must match.If the Enable VC Group Matching (on PseudoWire Status) option is enabled for the router, the VC Group ID must also be matched for the PseudoWire State to be Up.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PwState'])

    @property
    def Sp(self):
        """
        Returns
        -------
        - str(hexVal1 | hexVal2 | hexVal3 | hexVal4): Indicates the SP value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Sp'])

    @property
    def Ssrc(self):
        """
        Returns
        -------
        - number: Indicates the SSRC value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ssrc'])

    @property
    def TdmBitrate(self):
        """
        Returns
        -------
        - number: The tdm bit rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TdmBitrate'])

    @property
    def TimestampMode(self):
        """
        Returns
        -------
        - str(absolute | differential): Indicates the timestamp mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimestampMode'])

    @property
    def VcId(self):
        """
        Returns
        -------
        - number: The 32-bit VC connection identifier. Used with the VC type to identify a specific VC (for VC types 0x0001 to 0x000B).
        """
        return self._get_attribute(self._SDM_ATT_MAP['VcId'])

    @property
    def VcType(self):
        """
        Returns
        -------
        - str(frameRelay | atmaal5 | atmxCell | vlan | ethernet | hdlc | ppp | cem | atmvcc | atmvpc | ip | satopE1 | satopT1 | satopE3 | satopT3 | cesoPsnBasic | cesoPsnCas | frameRelayRfc4619): The type of L2 VC depends on the Layer 2 protocol types.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VcType'])

    def find(self, CBit=None, Cas=None, CemOption=None, CemPayloadBytes=None, Description=None, DisCeAddress=None, Frequency=None, GroupId=None, IncludeRtpHeader=None, Label=None, LabelSpaceId=None, LocalPwSubStatus=None, MaxAtmCell=None, Mtu=None, PayloadSize=None, PayloadType=None, Peer=None, PeerPwSubStatus=None, PwState=None, Sp=None, Ssrc=None, TdmBitrate=None, TimestampMode=None, VcId=None, VcType=None):
        """Finds and retrieves learnedMartiniLabel resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedMartiniLabel resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedMartiniLabel resources from the server.

        Args
        ----
        - CBit (bool): If enabled, sets the C-Bit (flag). It is the highest order bit in the VC Type field. If the bit is set, it indicates the presence of a control word on this VC.
        - Cas (str(e1Trunk | t1EsfTrunk | t1SfTrunk)): Indicates the CAS value.
        - CemOption (number): The value of the CEM option.
        - CemPayloadBytes (number): (For Circuit Emulation Service over MPLS/CEM). The length of the CEM payload (in bytes).
        - Description (str): An optional user-defined interface description. It may be used with ALL VC types. Valid length is 0 to 80 octets.
        - DisCeAddress (str): If the L2 interface type for the VC whose learned information is seen is IP, this field indicates the learned IP address of the remote end CE of the IP vrtual circuit.
        - Frequency (number): Indicates the frequency.
        - GroupId (number): An arbitrary 32-bit value used to identify a group of VCs.
        - IncludeRtpHeader (bool): If enables, includes the RTP information in the header.
        - Label (number): The label value added to the packet(s) by the upstream LDP peer.
        - LabelSpaceId (number): (2 octets) Identifies the set of labels that will be used. Part of the LDP identifier.
        - LocalPwSubStatus (number): It reflects the status carried in the PW status notification received from the peer.
        - MaxAtmCell (number): The maximum number of ATM Cells which may be concatenated and sent in a single MPLS frame. This parameter is part of the FEC element.
        - Mtu (number): (in octets) The 2-octet value for the maximum Transmission Unit (MTU).
        - PayloadSize (number): Indicates the payload size.
        - PayloadType (number): The payload type.
        - Peer (str): The RID of the upstream LDP peer. Part of the LSR ID. It must be globally unique. It forms the first 4 octets of the 6-octet LDP identifier.
        - PeerPwSubStatus (number): It reflects the status carried in the PW status last sent to the peer.
        - PwState (bool): The PseudoWire State - either Up or Down. For the PseudoWire to be Up (Up status), the VC ID, VC Type, and Peer must match.If the Enable VC Group Matching (on PseudoWire Status) option is enabled for the router, the VC Group ID must also be matched for the PseudoWire State to be Up.
        - Sp (str(hexVal1 | hexVal2 | hexVal3 | hexVal4)): Indicates the SP value.
        - Ssrc (number): Indicates the SSRC value.
        - TdmBitrate (number): The tdm bit rate.
        - TimestampMode (str(absolute | differential)): Indicates the timestamp mode.
        - VcId (number): The 32-bit VC connection identifier. Used with the VC type to identify a specific VC (for VC types 0x0001 to 0x000B).
        - VcType (str(frameRelay | atmaal5 | atmxCell | vlan | ethernet | hdlc | ppp | cem | atmvcc | atmvpc | ip | satopE1 | satopT1 | satopE3 | satopT3 | cesoPsnBasic | cesoPsnCas | frameRelayRfc4619)): The type of L2 VC depends on the Layer 2 protocol types.

        Returns
        -------
        - self: This instance with matching learnedMartiniLabel resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedMartiniLabel data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedMartiniLabel resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
