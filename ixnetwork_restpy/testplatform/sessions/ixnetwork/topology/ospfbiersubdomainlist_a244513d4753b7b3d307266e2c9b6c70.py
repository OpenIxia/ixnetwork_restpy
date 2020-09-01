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


class OspfBierSubDomainList(Base):
    """OSPFv2 BIER Sub Domain
    The OspfBierSubDomainList class encapsulates a required ospfBierSubDomainList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ospfBierSubDomainList'
    _SDM_ATT_MAP = {
        'BFRId': 'BFRId',
        'Bar': 'Bar',
        'Active': 'active',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'Ipa': 'ipa',
        'MtId': 'mtId',
        'Name': 'name',
        'NumberOfBSLen': 'numberOfBSLen',
        'SubDomainId': 'subDomainId',
    }

    def __init__(self, parent):
        super(OspfBierSubDomainList, self).__init__(parent)

    @property
    def OspfBierBSObjectList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfbierbsobjectlist_d963618a7e3bb458722a4ffc379ac86a.OspfBierBSObjectList): An instance of the OspfBierBSObjectList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfbierbsobjectlist_d963618a7e3bb458722a4ffc379ac86a import OspfBierBSObjectList
        return OspfBierBSObjectList(self)

    @property
    def BFRId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A BFR Identifier (BFR-id) is a number within a given sub-domain. Every BFR that may need to function as a BFIR or BFER MUST have a single BFR-id, which identifies it uniquely within that sub-domain
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BFRId']))

    @property
    def Bar(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): It is a single octet BIER specific algorithm used to calculate underlay paths to reach other BFRs
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Bar']))

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

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
    def Ipa(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): It is a single octet IGP algorithm to either modify, enhance or replace the calculation of underlay paths to reach other BFRs as defined by the BAR value.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipa']))

    @property
    def MtId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multi-Topology ID - It identifies the topology that is associated with the BIER sub-domain
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MtId']))

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
    def NumberOfBSLen(self):
        """
        Returns
        -------
        - number: Number of Supported Bit String Length
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfBSLen'])
    @NumberOfBSLen.setter
    def NumberOfBSLen(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfBSLen'], value)

    @property
    def SubDomainId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): It is a unique value which identifies the BIER sub-domain within the BIER domain
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SubDomainId']))

    def update(self, Name=None, NumberOfBSLen=None):
        """Updates ospfBierSubDomainList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfBSLen (number): Number of Supported Bit String Length

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, BFRId=None, Bar=None, Active=None, Ipa=None, MtId=None, SubDomainId=None):
        """Base class infrastructure that gets a list of ospfBierSubDomainList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - BFRId (str): optional regex of BFRId
        - Bar (str): optional regex of Bar
        - Active (str): optional regex of active
        - Ipa (str): optional regex of ipa
        - MtId (str): optional regex of mtId
        - SubDomainId (str): optional regex of subDomainId

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
