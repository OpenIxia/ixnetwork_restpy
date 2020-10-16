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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class IsisL3Router(Base):
    """ISIS-L3 Port Configuration
    The IsisL3Router class encapsulates a list of isisL3Router resources that are managed by the system.
    A list of resources can be retrieved from the server using the IsisL3Router.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'isisL3Router'
    _SDM_ATT_MAP = {
        'BIERInfoSubTLVType': 'bIERInfoSubTLVType',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'FaAppSpecfLinkAttrSubTlvType': 'faAppSpecfLinkAttrSubTlvType',
        'FaEagSubTlvType': 'faEagSubTlvType',
        'FadSubTlvType': 'fadSubTlvType',
        'FadfSubTlvType': 'fadfSubTlvType',
        'FaiAllAgSubTlvType': 'faiAllAgSubTlvType',
        'FaiAnyAgSubTlvType': 'faiAnyAgSubTlvType',
        'LinkMsdSubTlvType': 'linkMsdSubTlvType',
        'MaxEndDMsdType': 'maxEndDMsdType',
        'MaxEndPopMsdType': 'maxEndPopMsdType',
        'MaxSegmentsLeftMsdType': 'maxSegmentsLeftMsdType',
        'MaxTEncapMsdType': 'maxTEncapMsdType',
        'MaxTInsertMsdType': 'maxTInsertMsdType',
        'Name': 'name',
        'NoOfLSPsOrMgroupPDUsPerInterval': 'noOfLSPsOrMgroupPDUsPerInterval',
        'NodeMsdSubTlvType': 'nodeMsdSubTlvType',
        'RateControlInterval': 'rateControlInterval',
        'RowNames': 'rowNames',
        'SendP2PHellosToUnicastMAC': 'sendP2PHellosToUnicastMAC',
        'SrDraftExtension': 'srDraftExtension',
        'SrlbSubTlvType': 'srlbSubTlvType',
        'SrmsPreferenceSubTlvType': 'srmsPreferenceSubTlvType',
        'Srv6AdjSIDSubTlvType': 'srv6AdjSIDSubTlvType',
        'Srv6CapabilitiesSubTlvType': 'srv6CapabilitiesSubTlvType',
        'Srv6EndSidSubTlvType': 'srv6EndSidSubTlvType',
        'Srv6EndXSidSubTlvType': 'srv6EndXSidSubTlvType',
        'Srv6LANAdjSIDSubTlvType': 'srv6LANAdjSIDSubTlvType',
        'Srv6LanEndXSidSubTlvType': 'srv6LanEndXSidSubTlvType',
        'Srv6NodeSIDTlvType': 'srv6NodeSIDTlvType',
        'Srv6SidLocatorTlvType': 'srv6SidLocatorTlvType',
    }

    def __init__(self, parent):
        super(IsisL3Router, self).__init__(parent)

    @property
    def StartRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.startrate.startrate_2bc83a4fb9730935e8259bdb40af2dc0.StartRate): An instance of the StartRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.startrate.startrate_2bc83a4fb9730935e8259bdb40af2dc0 import StartRate
        return StartRate(self)._select()

    @property
    def StopRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.stoprate.stoprate_4ea9a1b38960d2b21012777131469a04.StopRate): An instance of the StopRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.stoprate.stoprate_4ea9a1b38960d2b21012777131469a04 import StopRate
        return StopRate(self)._select()

    @property
    def BIERInfoSubTLVType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): BIER Info Sub-TLV Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BIERInfoSubTLVType']))

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
    def FaAppSpecfLinkAttrSubTlvType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): App Specific Link Attr Sub-TLV Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FaAppSpecfLinkAttrSubTlvType']))

    @property
    def FaEagSubTlvType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): FAEAG Sub-TLV Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FaEagSubTlvType']))

    @property
    def FadSubTlvType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): FAD Sub-TLV Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FadSubTlvType']))

    @property
    def FadfSubTlvType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): FADF Sub-TLV Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FadfSubTlvType']))

    @property
    def FaiAllAgSubTlvType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): FAIAllAG Sub-TLV Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FaiAllAgSubTlvType']))

    @property
    def FaiAnyAgSubTlvType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): FAIAnyAG Sub-TLV Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FaiAnyAgSubTlvType']))

    @property
    def LinkMsdSubTlvType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This specifies the type of Link MSD sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LinkMsdSubTlvType']))

    @property
    def MaxEndDMsdType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This specifies the type of Max End D MSD
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxEndDMsdType']))

    @property
    def MaxEndPopMsdType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This specifies the type of Max End Pop MSD
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxEndPopMsdType']))

    @property
    def MaxSegmentsLeftMsdType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This specifies the type of Max Segments Left MSD
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxSegmentsLeftMsdType']))

    @property
    def MaxTEncapMsdType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This specifies the type of Max T Encap MSD
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxTEncapMsdType']))

    @property
    def MaxTInsertMsdType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This specifies the type of Max T Insert MSD
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxTInsertMsdType']))

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
    def NoOfLSPsOrMgroupPDUsPerInterval(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): LSPs/MGROUP-PDUs per Interval
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NoOfLSPsOrMgroupPDUsPerInterval']))

    @property
    def NodeMsdSubTlvType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This specifies the type of Node MSD sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NodeMsdSubTlvType']))

    @property
    def RateControlInterval(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Rate Control Interval (ms)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RateControlInterval']))

    @property
    def RowNames(self):
        """
        Returns
        -------
        - list(str): Name of rows
        """
        return self._get_attribute(self._SDM_ATT_MAP['RowNames'])

    @property
    def SendP2PHellosToUnicastMAC(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Send P2P Hellos To Unicast MAC
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SendP2PHellosToUnicastMAC']))

    @property
    def SrDraftExtension(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This refers to the TLV structure of SRGB as per the Segment Routing draft version
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SrDraftExtension']))

    @property
    def SrlbSubTlvType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This specifies the type of Segment Routing Local Block sub tlv, suggested value is 22.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SrlbSubTlvType']))

    @property
    def SrmsPreferenceSubTlvType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This specifies the type of SRMS Preference sub tlv, suggested value is 23.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SrmsPreferenceSubTlvType']))

    @property
    def Srv6AdjSIDSubTlvType(self):
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This specifies the type of SRv6 Adjacency-SID sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6AdjSIDSubTlvType']))

    @property
    def Srv6CapabilitiesSubTlvType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This specifies the type of SRv6 Capabilities sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6CapabilitiesSubTlvType']))

    @property
    def Srv6EndSidSubTlvType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This specifies the type of SRv6 End SID sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6EndSidSubTlvType']))

    @property
    def Srv6EndXSidSubTlvType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This specifies the type of SRv6 End.X SID sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6EndXSidSubTlvType']))

    @property
    def Srv6LANAdjSIDSubTlvType(self):
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This specifies the type of SRv6 LAN Adjacency-SID sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6LANAdjSIDSubTlvType']))

    @property
    def Srv6LanEndXSidSubTlvType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This specifies the type of SRv6 LAN End.X SID sub-TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6LanEndXSidSubTlvType']))

    @property
    def Srv6NodeSIDTlvType(self):
        """DEPRECATED 
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This specifies the type of SRv6 Node SID TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6NodeSIDTlvType']))

    @property
    def Srv6SidLocatorTlvType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): SRv6 SID Locator Tlv Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidLocatorTlvType']))

    def update(self, Name=None):
        """Updates isisL3Router resource on the server.

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

    def find(self, Count=None, DescriptiveName=None, Name=None, RowNames=None):
        """Finds and retrieves isisL3Router resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve isisL3Router resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all isisL3Router resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - RowNames (list(str)): Name of rows

        Returns
        -------
        - self: This instance with matching isisL3Router resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of isisL3Router data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the isisL3Router resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, BIERInfoSubTLVType=None, FaAppSpecfLinkAttrSubTlvType=None, FaEagSubTlvType=None, FadSubTlvType=None, FadfSubTlvType=None, FaiAllAgSubTlvType=None, FaiAnyAgSubTlvType=None, LinkMsdSubTlvType=None, MaxEndDMsdType=None, MaxEndPopMsdType=None, MaxSegmentsLeftMsdType=None, MaxTEncapMsdType=None, MaxTInsertMsdType=None, NoOfLSPsOrMgroupPDUsPerInterval=None, NodeMsdSubTlvType=None, RateControlInterval=None, SendP2PHellosToUnicastMAC=None, SrDraftExtension=None, SrlbSubTlvType=None, SrmsPreferenceSubTlvType=None, Srv6AdjSIDSubTlvType=None, Srv6CapabilitiesSubTlvType=None, Srv6EndSidSubTlvType=None, Srv6EndXSidSubTlvType=None, Srv6LANAdjSIDSubTlvType=None, Srv6LanEndXSidSubTlvType=None, Srv6NodeSIDTlvType=None, Srv6SidLocatorTlvType=None):
        """Base class infrastructure that gets a list of isisL3Router device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - BIERInfoSubTLVType (str): optional regex of bIERInfoSubTLVType
        - FaAppSpecfLinkAttrSubTlvType (str): optional regex of faAppSpecfLinkAttrSubTlvType
        - FaEagSubTlvType (str): optional regex of faEagSubTlvType
        - FadSubTlvType (str): optional regex of fadSubTlvType
        - FadfSubTlvType (str): optional regex of fadfSubTlvType
        - FaiAllAgSubTlvType (str): optional regex of faiAllAgSubTlvType
        - FaiAnyAgSubTlvType (str): optional regex of faiAnyAgSubTlvType
        - LinkMsdSubTlvType (str): optional regex of linkMsdSubTlvType
        - MaxEndDMsdType (str): optional regex of maxEndDMsdType
        - MaxEndPopMsdType (str): optional regex of maxEndPopMsdType
        - MaxSegmentsLeftMsdType (str): optional regex of maxSegmentsLeftMsdType
        - MaxTEncapMsdType (str): optional regex of maxTEncapMsdType
        - MaxTInsertMsdType (str): optional regex of maxTInsertMsdType
        - NoOfLSPsOrMgroupPDUsPerInterval (str): optional regex of noOfLSPsOrMgroupPDUsPerInterval
        - NodeMsdSubTlvType (str): optional regex of nodeMsdSubTlvType
        - RateControlInterval (str): optional regex of rateControlInterval
        - SendP2PHellosToUnicastMAC (str): optional regex of sendP2PHellosToUnicastMAC
        - SrDraftExtension (str): optional regex of srDraftExtension
        - SrlbSubTlvType (str): optional regex of srlbSubTlvType
        - SrmsPreferenceSubTlvType (str): optional regex of srmsPreferenceSubTlvType
        - Srv6AdjSIDSubTlvType (str): optional regex of srv6AdjSIDSubTlvType
        - Srv6CapabilitiesSubTlvType (str): optional regex of srv6CapabilitiesSubTlvType
        - Srv6EndSidSubTlvType (str): optional regex of srv6EndSidSubTlvType
        - Srv6EndXSidSubTlvType (str): optional regex of srv6EndXSidSubTlvType
        - Srv6LANAdjSIDSubTlvType (str): optional regex of srv6LANAdjSIDSubTlvType
        - Srv6LanEndXSidSubTlvType (str): optional regex of srv6LanEndXSidSubTlvType
        - Srv6NodeSIDTlvType (str): optional regex of srv6NodeSIDTlvType
        - Srv6SidLocatorTlvType (str): optional regex of srv6SidLocatorTlvType

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
