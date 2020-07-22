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


class Modifier(Base):
    """Modify a field in incoming packets before sending them.
    The Modifier class encapsulates a list of modifier resources that are managed by the user.
    A list of resources can be retrieved from the server using the Modifier.find() method.
    The list can be managed by using the Modifier.add() and Modifier.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'modifier'
    _SDM_ATT_MAP = {
        'ClusterSize': 'clusterSize',
        'Enabled': 'enabled',
        'L3MatchEtherType': 'l3MatchEtherType',
        'L3MatchMode': 'l3MatchMode',
        'L3MatchMplsLabel': 'l3MatchMplsLabel',
        'L4MatchEncapsulation': 'l4MatchEncapsulation',
        'L4MatchMode': 'l4MatchMode',
        'L4MatchProtocolNumber': 'l4MatchProtocolNumber',
        'L5MatchEncapsulation': 'l5MatchEncapsulation',
        'L5MatchMode': 'l5MatchMode',
        'L5MatchPortNumber': 'l5MatchPortNumber',
        'Mask': 'mask',
        'MatchValue': 'matchValue',
        'MatchValueEnabled': 'matchValueEnabled',
        'Name': 'name',
        'Offset': 'offset',
        'OffsetStart': 'offsetStart',
        'PercentRate': 'percentRate',
        'ReplaceFixedValue': 'replaceFixedValue',
        'ReplaceMode': 'replaceMode',
        'ReplaceRangeCount': 'replaceRangeCount',
        'ReplaceRangeDecrement': 'replaceRangeDecrement',
        'ReplaceRangeFirst': 'replaceRangeFirst',
        'ReplaceRangeStep': 'replaceRangeStep',
    }

    def __init__(self, parent):
        super(Modifier, self).__init__(parent)

    @property
    def ClusterSize(self):
        """
        Returns
        -------
        - number: Number of packets to modify on each occurrence. Default: 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClusterSize'])
    @ClusterSize.setter
    def ClusterSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ClusterSize'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, modify incoming packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def L3MatchEtherType(self):
        """
        Returns
        -------
        - str: EtherType value to match.
        """
        return self._get_attribute(self._SDM_ATT_MAP['L3MatchEtherType'])
    @L3MatchEtherType.setter
    def L3MatchEtherType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['L3MatchEtherType'], value)

    @property
    def L3MatchMode(self):
        """
        Returns
        -------
        - str(matchAny | matchBottomMplsLabel | matchEtherType): For an L3 offset, specify whether to modify only packets with a specific EtherType or bottom MPLS label.
        """
        return self._get_attribute(self._SDM_ATT_MAP['L3MatchMode'])
    @L3MatchMode.setter
    def L3MatchMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['L3MatchMode'], value)

    @property
    def L3MatchMplsLabel(self):
        """
        Returns
        -------
        - number: MPLS label to match.
        """
        return self._get_attribute(self._SDM_ATT_MAP['L3MatchMplsLabel'])
    @L3MatchMplsLabel.setter
    def L3MatchMplsLabel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['L3MatchMplsLabel'], value)

    @property
    def L4MatchEncapsulation(self):
        """
        Returns
        -------
        - str(matchIpv4 | matchIpv4OrIpv6 | matchIpv6): For an L4 offset, specify whether to modify IPv4 packets, IPv6 packets, or both.
        """
        return self._get_attribute(self._SDM_ATT_MAP['L4MatchEncapsulation'])
    @L4MatchEncapsulation.setter
    def L4MatchEncapsulation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['L4MatchEncapsulation'], value)

    @property
    def L4MatchMode(self):
        """
        Returns
        -------
        - str(matchAny | matchProtocolNumber): For an L4 offset, specify whether to modify only packets with a specific protocol number.
        """
        return self._get_attribute(self._SDM_ATT_MAP['L4MatchMode'])
    @L4MatchMode.setter
    def L4MatchMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['L4MatchMode'], value)

    @property
    def L4MatchProtocolNumber(self):
        """
        Returns
        -------
        - number: Protocol number to match.
        """
        return self._get_attribute(self._SDM_ATT_MAP['L4MatchProtocolNumber'])
    @L4MatchProtocolNumber.setter
    def L4MatchProtocolNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['L4MatchProtocolNumber'], value)

    @property
    def L5MatchEncapsulation(self):
        """
        Returns
        -------
        - str(matchTcp | matchUdp): For an L5 offset, specify whether to modify TCP packets only or UDP packets only.
        """
        return self._get_attribute(self._SDM_ATT_MAP['L5MatchEncapsulation'])
    @L5MatchEncapsulation.setter
    def L5MatchEncapsulation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['L5MatchEncapsulation'], value)

    @property
    def L5MatchMode(self):
        """
        Returns
        -------
        - str(matchAny | matchDestinationPort | matchSourceOrDestinationPort | matchSourcePort): For an L5 offset, specify whether to modify only packets with a specific source or destination port number.
        """
        return self._get_attribute(self._SDM_ATT_MAP['L5MatchMode'])
    @L5MatchMode.setter
    def L5MatchMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['L5MatchMode'], value)

    @property
    def L5MatchPortNumber(self):
        """
        Returns
        -------
        - number: Port number to match.
        """
        return self._get_attribute(self._SDM_ATT_MAP['L5MatchPortNumber'])
    @L5MatchPortNumber.setter
    def L5MatchPortNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['L5MatchPortNumber'], value)

    @property
    def Mask(self):
        """
        Returns
        -------
        - str: Mask identifying the bits of the field to be modified, as a hex string with prefix 0x (e.g. 0xFF FF). The bits of the mask must be contiguous.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mask'])
    @Mask.setter
    def Mask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mask'], value)

    @property
    def MatchValue(self):
        """
        Returns
        -------
        - str: Value to be matched. Format: MAC address, IPv4 address, IPv6 address, decimal value, binary string with prefix 0b (e.g. 0b0100), or a hex string with prefix 0x (e.g. 0xFF FF).
        """
        return self._get_attribute(self._SDM_ATT_MAP['MatchValue'])
    @MatchValue.setter
    def MatchValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MatchValue'], value)

    @property
    def MatchValueEnabled(self):
        """
        Returns
        -------
        - bool: Only modify packets if the existing field value matches a specified value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MatchValueEnabled'])
    @MatchValueEnabled.setter
    def MatchValueEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MatchValueEnabled'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of the modifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def Offset(self):
        """
        Returns
        -------
        - number: The position of the field to be modified, as an offset in bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Offset'])
    @Offset.setter
    def Offset(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Offset'], value)

    @property
    def OffsetStart(self):
        """
        Returns
        -------
        - str(l2Offset | l3Offset | l4Offset | l5Offset): Define the position of the field to be modified, as an offset from a specified position. Default is from the start of the L2 header.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OffsetStart'])
    @OffsetStart.setter
    def OffsetStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OffsetStart'], value)

    @property
    def PercentRate(self):
        """
        Returns
        -------
        - number: How often to modify matching packets. Default: 100%.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PercentRate'])
    @PercentRate.setter
    def PercentRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PercentRate'], value)

    @property
    def ReplaceFixedValue(self):
        """
        Returns
        -------
        - str: Fixed replacement value. Format: MAC address, IPv4 address, IPv6 address, decimal value, binary string with prefix 0b (e.g. 0b0100), or a hex string with prefix 0x (e.g. 0xFF FF).
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReplaceFixedValue'])
    @ReplaceFixedValue.setter
    def ReplaceFixedValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReplaceFixedValue'], value)

    @property
    def ReplaceMode(self):
        """
        Returns
        -------
        - str(fixedValue | range): Replace field with a fixed value or a range of values.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReplaceMode'])
    @ReplaceMode.setter
    def ReplaceMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReplaceMode'], value)

    @property
    def ReplaceRangeCount(self):
        """
        Returns
        -------
        - str: Number of values in range. Can be any value up to ceiling(2^width / step), where width is the width of the field mask.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReplaceRangeCount'])
    @ReplaceRangeCount.setter
    def ReplaceRangeCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReplaceRangeCount'], value)

    @property
    def ReplaceRangeDecrement(self):
        """
        Returns
        -------
        - bool: Decrement instead of incrementing. Default: false.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReplaceRangeDecrement'])
    @ReplaceRangeDecrement.setter
    def ReplaceRangeDecrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReplaceRangeDecrement'], value)

    @property
    def ReplaceRangeFirst(self):
        """
        Returns
        -------
        - str: Start of range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReplaceRangeFirst'])
    @ReplaceRangeFirst.setter
    def ReplaceRangeFirst(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReplaceRangeFirst'], value)

    @property
    def ReplaceRangeStep(self):
        """
        Returns
        -------
        - str: Step to be added or subtracted for each modified packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReplaceRangeStep'])
    @ReplaceRangeStep.setter
    def ReplaceRangeStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReplaceRangeStep'], value)

    def update(self, ClusterSize=None, Enabled=None, L3MatchEtherType=None, L3MatchMode=None, L3MatchMplsLabel=None, L4MatchEncapsulation=None, L4MatchMode=None, L4MatchProtocolNumber=None, L5MatchEncapsulation=None, L5MatchMode=None, L5MatchPortNumber=None, Mask=None, MatchValue=None, MatchValueEnabled=None, Name=None, Offset=None, OffsetStart=None, PercentRate=None, ReplaceFixedValue=None, ReplaceMode=None, ReplaceRangeCount=None, ReplaceRangeDecrement=None, ReplaceRangeFirst=None, ReplaceRangeStep=None):
        """Updates modifier resource on the server.

        Args
        ----
        - ClusterSize (number): Number of packets to modify on each occurrence. Default: 1.
        - Enabled (bool): If true, modify incoming packets.
        - L3MatchEtherType (str): EtherType value to match.
        - L3MatchMode (str(matchAny | matchBottomMplsLabel | matchEtherType)): For an L3 offset, specify whether to modify only packets with a specific EtherType or bottom MPLS label.
        - L3MatchMplsLabel (number): MPLS label to match.
        - L4MatchEncapsulation (str(matchIpv4 | matchIpv4OrIpv6 | matchIpv6)): For an L4 offset, specify whether to modify IPv4 packets, IPv6 packets, or both.
        - L4MatchMode (str(matchAny | matchProtocolNumber)): For an L4 offset, specify whether to modify only packets with a specific protocol number.
        - L4MatchProtocolNumber (number): Protocol number to match.
        - L5MatchEncapsulation (str(matchTcp | matchUdp)): For an L5 offset, specify whether to modify TCP packets only or UDP packets only.
        - L5MatchMode (str(matchAny | matchDestinationPort | matchSourceOrDestinationPort | matchSourcePort)): For an L5 offset, specify whether to modify only packets with a specific source or destination port number.
        - L5MatchPortNumber (number): Port number to match.
        - Mask (str): Mask identifying the bits of the field to be modified, as a hex string with prefix 0x (e.g. 0xFF FF). The bits of the mask must be contiguous.
        - MatchValue (str): Value to be matched. Format: MAC address, IPv4 address, IPv6 address, decimal value, binary string with prefix 0b (e.g. 0b0100), or a hex string with prefix 0x (e.g. 0xFF FF).
        - MatchValueEnabled (bool): Only modify packets if the existing field value matches a specified value.
        - Name (str): Name of the modifier.
        - Offset (number): The position of the field to be modified, as an offset in bytes.
        - OffsetStart (str(l2Offset | l3Offset | l4Offset | l5Offset)): Define the position of the field to be modified, as an offset from a specified position. Default is from the start of the L2 header.
        - PercentRate (number): How often to modify matching packets. Default: 100%.
        - ReplaceFixedValue (str): Fixed replacement value. Format: MAC address, IPv4 address, IPv6 address, decimal value, binary string with prefix 0b (e.g. 0b0100), or a hex string with prefix 0x (e.g. 0xFF FF).
        - ReplaceMode (str(fixedValue | range)): Replace field with a fixed value or a range of values.
        - ReplaceRangeCount (str): Number of values in range. Can be any value up to ceiling(2^width / step), where width is the width of the field mask.
        - ReplaceRangeDecrement (bool): Decrement instead of incrementing. Default: false.
        - ReplaceRangeFirst (str): Start of range.
        - ReplaceRangeStep (str): Step to be added or subtracted for each modified packet.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ClusterSize=None, Enabled=None, L3MatchEtherType=None, L3MatchMode=None, L3MatchMplsLabel=None, L4MatchEncapsulation=None, L4MatchMode=None, L4MatchProtocolNumber=None, L5MatchEncapsulation=None, L5MatchMode=None, L5MatchPortNumber=None, Mask=None, MatchValue=None, MatchValueEnabled=None, Name=None, Offset=None, OffsetStart=None, PercentRate=None, ReplaceFixedValue=None, ReplaceMode=None, ReplaceRangeCount=None, ReplaceRangeDecrement=None, ReplaceRangeFirst=None, ReplaceRangeStep=None):
        """Adds a new modifier resource on the server and adds it to the container.

        Args
        ----
        - ClusterSize (number): Number of packets to modify on each occurrence. Default: 1.
        - Enabled (bool): If true, modify incoming packets.
        - L3MatchEtherType (str): EtherType value to match.
        - L3MatchMode (str(matchAny | matchBottomMplsLabel | matchEtherType)): For an L3 offset, specify whether to modify only packets with a specific EtherType or bottom MPLS label.
        - L3MatchMplsLabel (number): MPLS label to match.
        - L4MatchEncapsulation (str(matchIpv4 | matchIpv4OrIpv6 | matchIpv6)): For an L4 offset, specify whether to modify IPv4 packets, IPv6 packets, or both.
        - L4MatchMode (str(matchAny | matchProtocolNumber)): For an L4 offset, specify whether to modify only packets with a specific protocol number.
        - L4MatchProtocolNumber (number): Protocol number to match.
        - L5MatchEncapsulation (str(matchTcp | matchUdp)): For an L5 offset, specify whether to modify TCP packets only or UDP packets only.
        - L5MatchMode (str(matchAny | matchDestinationPort | matchSourceOrDestinationPort | matchSourcePort)): For an L5 offset, specify whether to modify only packets with a specific source or destination port number.
        - L5MatchPortNumber (number): Port number to match.
        - Mask (str): Mask identifying the bits of the field to be modified, as a hex string with prefix 0x (e.g. 0xFF FF). The bits of the mask must be contiguous.
        - MatchValue (str): Value to be matched. Format: MAC address, IPv4 address, IPv6 address, decimal value, binary string with prefix 0b (e.g. 0b0100), or a hex string with prefix 0x (e.g. 0xFF FF).
        - MatchValueEnabled (bool): Only modify packets if the existing field value matches a specified value.
        - Name (str): Name of the modifier.
        - Offset (number): The position of the field to be modified, as an offset in bytes.
        - OffsetStart (str(l2Offset | l3Offset | l4Offset | l5Offset)): Define the position of the field to be modified, as an offset from a specified position. Default is from the start of the L2 header.
        - PercentRate (number): How often to modify matching packets. Default: 100%.
        - ReplaceFixedValue (str): Fixed replacement value. Format: MAC address, IPv4 address, IPv6 address, decimal value, binary string with prefix 0b (e.g. 0b0100), or a hex string with prefix 0x (e.g. 0xFF FF).
        - ReplaceMode (str(fixedValue | range)): Replace field with a fixed value or a range of values.
        - ReplaceRangeCount (str): Number of values in range. Can be any value up to ceiling(2^width / step), where width is the width of the field mask.
        - ReplaceRangeDecrement (bool): Decrement instead of incrementing. Default: false.
        - ReplaceRangeFirst (str): Start of range.
        - ReplaceRangeStep (str): Step to be added or subtracted for each modified packet.

        Returns
        -------
        - self: This instance with all currently retrieved modifier resources using find and the newly added modifier resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained modifier resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ClusterSize=None, Enabled=None, L3MatchEtherType=None, L3MatchMode=None, L3MatchMplsLabel=None, L4MatchEncapsulation=None, L4MatchMode=None, L4MatchProtocolNumber=None, L5MatchEncapsulation=None, L5MatchMode=None, L5MatchPortNumber=None, Mask=None, MatchValue=None, MatchValueEnabled=None, Name=None, Offset=None, OffsetStart=None, PercentRate=None, ReplaceFixedValue=None, ReplaceMode=None, ReplaceRangeCount=None, ReplaceRangeDecrement=None, ReplaceRangeFirst=None, ReplaceRangeStep=None):
        """Finds and retrieves modifier resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve modifier resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all modifier resources from the server.

        Args
        ----
        - ClusterSize (number): Number of packets to modify on each occurrence. Default: 1.
        - Enabled (bool): If true, modify incoming packets.
        - L3MatchEtherType (str): EtherType value to match.
        - L3MatchMode (str(matchAny | matchBottomMplsLabel | matchEtherType)): For an L3 offset, specify whether to modify only packets with a specific EtherType or bottom MPLS label.
        - L3MatchMplsLabel (number): MPLS label to match.
        - L4MatchEncapsulation (str(matchIpv4 | matchIpv4OrIpv6 | matchIpv6)): For an L4 offset, specify whether to modify IPv4 packets, IPv6 packets, or both.
        - L4MatchMode (str(matchAny | matchProtocolNumber)): For an L4 offset, specify whether to modify only packets with a specific protocol number.
        - L4MatchProtocolNumber (number): Protocol number to match.
        - L5MatchEncapsulation (str(matchTcp | matchUdp)): For an L5 offset, specify whether to modify TCP packets only or UDP packets only.
        - L5MatchMode (str(matchAny | matchDestinationPort | matchSourceOrDestinationPort | matchSourcePort)): For an L5 offset, specify whether to modify only packets with a specific source or destination port number.
        - L5MatchPortNumber (number): Port number to match.
        - Mask (str): Mask identifying the bits of the field to be modified, as a hex string with prefix 0x (e.g. 0xFF FF). The bits of the mask must be contiguous.
        - MatchValue (str): Value to be matched. Format: MAC address, IPv4 address, IPv6 address, decimal value, binary string with prefix 0b (e.g. 0b0100), or a hex string with prefix 0x (e.g. 0xFF FF).
        - MatchValueEnabled (bool): Only modify packets if the existing field value matches a specified value.
        - Name (str): Name of the modifier.
        - Offset (number): The position of the field to be modified, as an offset in bytes.
        - OffsetStart (str(l2Offset | l3Offset | l4Offset | l5Offset)): Define the position of the field to be modified, as an offset from a specified position. Default is from the start of the L2 header.
        - PercentRate (number): How often to modify matching packets. Default: 100%.
        - ReplaceFixedValue (str): Fixed replacement value. Format: MAC address, IPv4 address, IPv6 address, decimal value, binary string with prefix 0b (e.g. 0b0100), or a hex string with prefix 0x (e.g. 0xFF FF).
        - ReplaceMode (str(fixedValue | range)): Replace field with a fixed value or a range of values.
        - ReplaceRangeCount (str): Number of values in range. Can be any value up to ceiling(2^width / step), where width is the width of the field mask.
        - ReplaceRangeDecrement (bool): Decrement instead of incrementing. Default: false.
        - ReplaceRangeFirst (str): Start of range.
        - ReplaceRangeStep (str): Step to be added or subtracted for each modified packet.

        Returns
        -------
        - self: This instance with matching modifier resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of modifier data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the modifier resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
