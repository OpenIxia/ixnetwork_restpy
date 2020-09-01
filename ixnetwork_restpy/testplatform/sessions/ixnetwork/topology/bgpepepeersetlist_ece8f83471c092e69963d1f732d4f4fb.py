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


class BgpEpePeerSetList(Base):
    """EPE Peer Set
    The BgpEpePeerSetList class encapsulates a list of bgpEpePeerSetList resources that are managed by the system.
    A list of resources can be retrieved from the server using the BgpEpePeerSetList.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'bgpEpePeerSetList'
    _SDM_ATT_MAP = {
        'BBit': 'bBit',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'LBit': 'lBit',
        'Name': 'name',
        'PBit': 'pBit',
        'Reserved': 'reserved',
        'RsvdBits': 'rsvdBits',
        'SidIndex': 'sidIndex',
        'SidIndexValue': 'sidIndexValue',
        'VBit': 'vBit',
        'Weight': 'weight',
    }

    def __init__(self, parent):
        super(BgpEpePeerSetList, self).__init__(parent)

    @property
    def BBit(self):
        """
        Returns
        -------
        - bool: B-Flag:Backup Flag.If set, the SID refers to a path that is eligible for protection.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BBit'])
    @BBit.setter
    def BBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BBit'], value)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def LBit(self):
        """
        Returns
        -------
        - bool: L-Flag: Local Flag. If set, then the value/index carried by the SID has local significance.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LBit'])
    @LBit.setter
    def LBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LBit'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def PBit(self):
        """
        Returns
        -------
        - bool: P-Flag: Persistent Flag: If set, the SID is persistently allocated, i.e. the SID value remains consistent across router restart and session/interface flap
        """
        return self._get_attribute(self._SDM_ATT_MAP['PBit'])
    @PBit.setter
    def PBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PBit'], value)

    @property
    def Reserved(self):
        """
        Returns
        -------
        - number: Reserved
        """
        return self._get_attribute(self._SDM_ATT_MAP['Reserved'])
    @Reserved.setter
    def Reserved(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Reserved'], value)

    @property
    def RsvdBits(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reserved for future use and MUST be zero when originated and ignored when received
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RsvdBits']))

    @property
    def SidIndex(self):
        """
        Returns
        -------
        - str(sid | index): Local Label for Peer-Set
        """
        return self._get_attribute(self._SDM_ATT_MAP['SidIndex'])
    @SidIndex.setter
    def SidIndex(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SidIndex'], value)

    @property
    def SidIndexValue(self):
        """
        Returns
        -------
        - number: If Local Label type is SID, max value is 16777215 and for Index max value is 4294967295
        """
        return self._get_attribute(self._SDM_ATT_MAP['SidIndexValue'])
    @SidIndexValue.setter
    def SidIndexValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SidIndexValue'], value)

    @property
    def VBit(self):
        """
        Returns
        -------
        - bool: V-Flag: Value flag. If set, then the SID carries a label value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VBit'])
    @VBit.setter
    def VBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VBit'], value)

    @property
    def Weight(self):
        """
        Returns
        -------
        - number: Weight of SID for the purpose of load balancing
        """
        return self._get_attribute(self._SDM_ATT_MAP['Weight'])
    @Weight.setter
    def Weight(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Weight'], value)

    def update(self, BBit=None, LBit=None, Name=None, PBit=None, Reserved=None, SidIndex=None, SidIndexValue=None, VBit=None, Weight=None):
        """Updates bgpEpePeerSetList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - BBit (bool): B-Flag:Backup Flag.If set, the SID refers to a path that is eligible for protection.
        - LBit (bool): L-Flag: Local Flag. If set, then the value/index carried by the SID has local significance.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PBit (bool): P-Flag: Persistent Flag: If set, the SID is persistently allocated, i.e. the SID value remains consistent across router restart and session/interface flap
        - Reserved (number): Reserved
        - SidIndex (str(sid | index)): Local Label for Peer-Set
        - SidIndexValue (number): If Local Label type is SID, max value is 16777215 and for Index max value is 4294967295
        - VBit (bool): V-Flag: Value flag. If set, then the SID carries a label value.
        - Weight (number): Weight of SID for the purpose of load balancing

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, BBit=None, Count=None, DescriptiveName=None, LBit=None, Name=None, PBit=None, Reserved=None, SidIndex=None, SidIndexValue=None, VBit=None, Weight=None):
        """Finds and retrieves bgpEpePeerSetList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpEpePeerSetList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpEpePeerSetList resources from the server.

        Args
        ----
        - BBit (bool): B-Flag:Backup Flag.If set, the SID refers to a path that is eligible for protection.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - LBit (bool): L-Flag: Local Flag. If set, then the value/index carried by the SID has local significance.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PBit (bool): P-Flag: Persistent Flag: If set, the SID is persistently allocated, i.e. the SID value remains consistent across router restart and session/interface flap
        - Reserved (number): Reserved
        - SidIndex (str(sid | index)): Local Label for Peer-Set
        - SidIndexValue (number): If Local Label type is SID, max value is 16777215 and for Index max value is 4294967295
        - VBit (bool): V-Flag: Value flag. If set, then the SID carries a label value.
        - Weight (number): Weight of SID for the purpose of load balancing

        Returns
        -------
        - self: This instance with matching bgpEpePeerSetList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpEpePeerSetList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpEpePeerSetList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, RsvdBits=None):
        """Base class infrastructure that gets a list of bgpEpePeerSetList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - RsvdBits (str): optional regex of rsvdBits

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
