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


class TunnelHeadToLeaf(Base):
    """It is introduced for the enhanced functionality of ERO and SERO configuration for the head range.
    The TunnelHeadToLeaf class encapsulates a list of tunnelHeadToLeaf resources that are managed by the user.
    A list of resources can be retrieved from the server using the TunnelHeadToLeaf.find() method.
    The list can be managed by using the TunnelHeadToLeaf.add() and TunnelHeadToLeaf.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'tunnelHeadToLeaf'
    _SDM_ATT_MAP = {
        'DutHopType': 'dutHopType',
        'DutPrefixLength': 'dutPrefixLength',
        'Enabled': 'enabled',
        'HeadIpStart': 'headIpStart',
        'IsAppendTunnelLeaf': 'isAppendTunnelLeaf',
        'IsPrependDut': 'isPrependDut',
        'IsSendingAsEro': 'isSendingAsEro',
        'IsSendingAsSero': 'isSendingAsSero',
        'SubObjectList': 'subObjectList',
        'TunnelLeafCount': 'tunnelLeafCount',
        'TunnelLeafHopType': 'tunnelLeafHopType',
        'TunnelLeafIpStart': 'tunnelLeafIpStart',
        'TunnelLeafPrefixLength': 'tunnelLeafPrefixLength',
    }

    def __init__(self, parent):
        super(TunnelHeadToLeaf, self).__init__(parent)

    @property
    def DutHopType(self):
        """
        Returns
        -------
        - str(strict | loose): Based on the input, the corresponding L bit in the packet is set.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DutHopType'])
    @DutHopType.setter
    def DutHopType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DutHopType'], value)

    @property
    def DutPrefixLength(self):
        """
        Returns
        -------
        - number: Prefix length of DUT.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DutPrefixLength'])
    @DutPrefixLength.setter
    def DutPrefixLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DutPrefixLength'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: It enables or disables the ERO/SERO specific configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def HeadIpStart(self):
        """
        Returns
        -------
        - str: It is the tunnel head IP address for which the ERO/SERO is being configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HeadIpStart'])

    @property
    def IsAppendTunnelLeaf(self):
        """
        Returns
        -------
        - bool: If enabled, this appends the tunnel leaf at the end of the ERO/SERO list in the packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsAppendTunnelLeaf'])
    @IsAppendTunnelLeaf.setter
    def IsAppendTunnelLeaf(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsAppendTunnelLeaf'], value)

    @property
    def IsPrependDut(self):
        """
        Returns
        -------
        - bool: Enables prepend DUT to the ERO/SERO list.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsPrependDut'])
    @IsPrependDut.setter
    def IsPrependDut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsPrependDut'], value)

    @property
    def IsSendingAsEro(self):
        """
        Returns
        -------
        - bool: If enabled, the entire configuration would go as ERO.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsSendingAsEro'])
    @IsSendingAsEro.setter
    def IsSendingAsEro(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsSendingAsEro'], value)

    @property
    def IsSendingAsSero(self):
        """
        Returns
        -------
        - bool: If enabled, the entire configuration would go as SERO.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsSendingAsSero'])
    @IsSendingAsSero.setter
    def IsSendingAsSero(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsSendingAsSero'], value)

    @property
    def SubObjectList(self):
        """
        Returns
        -------
        - str: The sub-object list for this ERO/SERO can be configured by typing it as a string. Input String: = NULL| [<Subobject> ;< Subobject list>] Subobject: = <AS :< 1-65535> :< S|L>| <IP :< IP Addr>/<1-32> :< S|L> IP Addr: = <0-255>.<0-255>.<0-255>.<0-255> NULL: =Example. IP:2.2.2.2/24:S;AS:100:L;IP:33.33.33.33/32:S
        """
        return self._get_attribute(self._SDM_ATT_MAP['SubObjectList'])
    @SubObjectList.setter
    def SubObjectList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SubObjectList'], value)

    @property
    def TunnelLeafCount(self):
        """
        Returns
        -------
        - number: The count of tunnel leaf.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelLeafCount'])
    @TunnelLeafCount.setter
    def TunnelLeafCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TunnelLeafCount'], value)

    @property
    def TunnelLeafHopType(self):
        """
        Returns
        -------
        - str(strict | loose): It is enabled if Append Leaf is enabled. Based on the input, corresponding L bit in the packet is set.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelLeafHopType'])
    @TunnelLeafHopType.setter
    def TunnelLeafHopType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TunnelLeafHopType'], value)

    @property
    def TunnelLeafIpStart(self):
        """
        Returns
        -------
        - str: It contains the start IP address of leaf for which the ERO/SERO will be configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelLeafIpStart'])
    @TunnelLeafIpStart.setter
    def TunnelLeafIpStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TunnelLeafIpStart'], value)

    @property
    def TunnelLeafPrefixLength(self):
        """
        Returns
        -------
        - number: Prefix length of tunnel leaf.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelLeafPrefixLength'])
    @TunnelLeafPrefixLength.setter
    def TunnelLeafPrefixLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TunnelLeafPrefixLength'], value)

    def update(self, DutHopType=None, DutPrefixLength=None, Enabled=None, IsAppendTunnelLeaf=None, IsPrependDut=None, IsSendingAsEro=None, IsSendingAsSero=None, SubObjectList=None, TunnelLeafCount=None, TunnelLeafHopType=None, TunnelLeafIpStart=None, TunnelLeafPrefixLength=None):
        """Updates tunnelHeadToLeaf resource on the server.

        Args
        ----
        - DutHopType (str(strict | loose)): Based on the input, the corresponding L bit in the packet is set.
        - DutPrefixLength (number): Prefix length of DUT.
        - Enabled (bool): It enables or disables the ERO/SERO specific configuration.
        - IsAppendTunnelLeaf (bool): If enabled, this appends the tunnel leaf at the end of the ERO/SERO list in the packet.
        - IsPrependDut (bool): Enables prepend DUT to the ERO/SERO list.
        - IsSendingAsEro (bool): If enabled, the entire configuration would go as ERO.
        - IsSendingAsSero (bool): If enabled, the entire configuration would go as SERO.
        - SubObjectList (str): The sub-object list for this ERO/SERO can be configured by typing it as a string. Input String: = NULL| [<Subobject> ;< Subobject list>] Subobject: = <AS :< 1-65535> :< S|L>| <IP :< IP Addr>/<1-32> :< S|L> IP Addr: = <0-255>.<0-255>.<0-255>.<0-255> NULL: =Example. IP:2.2.2.2/24:S;AS:100:L;IP:33.33.33.33/32:S
        - TunnelLeafCount (number): The count of tunnel leaf.
        - TunnelLeafHopType (str(strict | loose)): It is enabled if Append Leaf is enabled. Based on the input, corresponding L bit in the packet is set.
        - TunnelLeafIpStart (str): It contains the start IP address of leaf for which the ERO/SERO will be configured.
        - TunnelLeafPrefixLength (number): Prefix length of tunnel leaf.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, DutHopType=None, DutPrefixLength=None, Enabled=None, IsAppendTunnelLeaf=None, IsPrependDut=None, IsSendingAsEro=None, IsSendingAsSero=None, SubObjectList=None, TunnelLeafCount=None, TunnelLeafHopType=None, TunnelLeafIpStart=None, TunnelLeafPrefixLength=None):
        """Adds a new tunnelHeadToLeaf resource on the server and adds it to the container.

        Args
        ----
        - DutHopType (str(strict | loose)): Based on the input, the corresponding L bit in the packet is set.
        - DutPrefixLength (number): Prefix length of DUT.
        - Enabled (bool): It enables or disables the ERO/SERO specific configuration.
        - IsAppendTunnelLeaf (bool): If enabled, this appends the tunnel leaf at the end of the ERO/SERO list in the packet.
        - IsPrependDut (bool): Enables prepend DUT to the ERO/SERO list.
        - IsSendingAsEro (bool): If enabled, the entire configuration would go as ERO.
        - IsSendingAsSero (bool): If enabled, the entire configuration would go as SERO.
        - SubObjectList (str): The sub-object list for this ERO/SERO can be configured by typing it as a string. Input String: = NULL| [<Subobject> ;< Subobject list>] Subobject: = <AS :< 1-65535> :< S|L>| <IP :< IP Addr>/<1-32> :< S|L> IP Addr: = <0-255>.<0-255>.<0-255>.<0-255> NULL: =Example. IP:2.2.2.2/24:S;AS:100:L;IP:33.33.33.33/32:S
        - TunnelLeafCount (number): The count of tunnel leaf.
        - TunnelLeafHopType (str(strict | loose)): It is enabled if Append Leaf is enabled. Based on the input, corresponding L bit in the packet is set.
        - TunnelLeafIpStart (str): It contains the start IP address of leaf for which the ERO/SERO will be configured.
        - TunnelLeafPrefixLength (number): Prefix length of tunnel leaf.

        Returns
        -------
        - self: This instance with all currently retrieved tunnelHeadToLeaf resources using find and the newly added tunnelHeadToLeaf resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained tunnelHeadToLeaf resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DutHopType=None, DutPrefixLength=None, Enabled=None, HeadIpStart=None, IsAppendTunnelLeaf=None, IsPrependDut=None, IsSendingAsEro=None, IsSendingAsSero=None, SubObjectList=None, TunnelLeafCount=None, TunnelLeafHopType=None, TunnelLeafIpStart=None, TunnelLeafPrefixLength=None):
        """Finds and retrieves tunnelHeadToLeaf resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve tunnelHeadToLeaf resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all tunnelHeadToLeaf resources from the server.

        Args
        ----
        - DutHopType (str(strict | loose)): Based on the input, the corresponding L bit in the packet is set.
        - DutPrefixLength (number): Prefix length of DUT.
        - Enabled (bool): It enables or disables the ERO/SERO specific configuration.
        - HeadIpStart (str): It is the tunnel head IP address for which the ERO/SERO is being configured.
        - IsAppendTunnelLeaf (bool): If enabled, this appends the tunnel leaf at the end of the ERO/SERO list in the packet.
        - IsPrependDut (bool): Enables prepend DUT to the ERO/SERO list.
        - IsSendingAsEro (bool): If enabled, the entire configuration would go as ERO.
        - IsSendingAsSero (bool): If enabled, the entire configuration would go as SERO.
        - SubObjectList (str): The sub-object list for this ERO/SERO can be configured by typing it as a string. Input String: = NULL| [<Subobject> ;< Subobject list>] Subobject: = <AS :< 1-65535> :< S|L>| <IP :< IP Addr>/<1-32> :< S|L> IP Addr: = <0-255>.<0-255>.<0-255>.<0-255> NULL: =Example. IP:2.2.2.2/24:S;AS:100:L;IP:33.33.33.33/32:S
        - TunnelLeafCount (number): The count of tunnel leaf.
        - TunnelLeafHopType (str(strict | loose)): It is enabled if Append Leaf is enabled. Based on the input, corresponding L bit in the packet is set.
        - TunnelLeafIpStart (str): It contains the start IP address of leaf for which the ERO/SERO will be configured.
        - TunnelLeafPrefixLength (number): Prefix length of tunnel leaf.

        Returns
        -------
        - self: This instance with matching tunnelHeadToLeaf resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of tunnelHeadToLeaf data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the tunnelHeadToLeaf resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
