# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class AdvancedLearnedInfoOptions(Base):
    """CFM Learned Info Filters
    The AdvancedLearnedInfoOptions class encapsulates a required advancedLearnedInfoOptions resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'advancedLearnedInfoOptions'

    def __init__(self, parent):
        super(AdvancedLearnedInfoOptions, self).__init__(parent)

    @property
    def AllCVlanCCM(self):
        """Include All C-VLAN

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('allCVlanCCM')

    @property
    def AllCVlanFilterDM(self):
        """Show All C-VLAN

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('allCVlanFilterDM')

    @property
    def AllCVlanFilterLM(self):
        """Show All C-VLAN

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('allCVlanFilterLM')

    @property
    def AllDstMEPDM(self):
        """Use All Configured MEPs as Destination

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('allDstMEPDM')

    @property
    def AllDstMEPLM(self):
        """Use All Configured MEPs as Destination

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('allDstMEPLM')

    @property
    def AllDstMEPLT(self):
        """Use All Configured MEPs as Destination

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('allDstMEPLT')

    @property
    def AllDstMEPLb(self):
        """Use All Configured MEPs as Destination

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('allDstMEPLb')

    @property
    def AllSVlanCCM(self):
        """Include All S-VLAN

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('allSVlanCCM')

    @property
    def AllSVlanFilterDM(self):
        """Show All S-VLAN

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('allSVlanFilterDM')

    @property
    def AllSVlanFilterLM(self):
        """Show All S-VLAN

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('allSVlanFilterLM')

    @property
    def AllSrcMEPDM(self):
        """Use All Configured MEPs as Source

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('allSrcMEPDM')

    @property
    def AllSrcMEPLM(self):
        """Use All Configured MEPs as Source

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('allSrcMEPLM')

    @property
    def AllSrcMEPLT(self):
        """Use All Configured MEPs as Source

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('allSrcMEPLT')

    @property
    def AllSrcMEPLb(self):
        """Use All Configured MEPs as Source

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('allSrcMEPLb')

    @property
    def AllVlanCCM(self):
        """Include All VLAN

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('allVlanCCM')

    @property
    def AutoVLANLT(self):
        """Use/Don't use VLAN in LT from configured source MEP

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('autoVLANLT')

    @property
    def AutoVLANLb(self):
        """Use/Don't use VLAN in LB from configured source MEP

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('autoVLANLb')

    @property
    def CVlanIdFilterCCM(self):
        """C-VLAN ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('cVlanIdFilterCCM')

    @property
    def CVlanIdFilterDM(self):
        """C-VLAN ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('cVlanIdFilterDM')

    @property
    def CVlanIdFilterLM(self):
        """C-VLAN ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('cVlanIdFilterLM')

    @property
    def CVlanIdFilterLT(self):
        """C-VLAN ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('cVlanIdFilterLT')

    @property
    def CVlanIdFilterLb(self):
        """C-VLAN ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('cVlanIdFilterLb')

    @property
    def CVlanPriorityFilterCCM(self):
        """C-VLAN Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('cVlanPriorityFilterCCM')

    @property
    def CVlanPriorityFilterDM(self):
        """C-VLAN Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('cVlanPriorityFilterDM')

    @property
    def CVlanPriorityFilterLM(self):
        """C-VLAN Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('cVlanPriorityFilterLM')

    @property
    def CVlanPriorityFilterLT(self):
        """C-VLAN Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('cVlanPriorityFilterLT')

    @property
    def CVlanPriorityFilterLb(self):
        """C-VLAN Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('cVlanPriorityFilterLb')

    @property
    def CVlanTpidFilterCCM(self):
        """C-VLAN TPID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('cVlanTpidFilterCCM')

    @property
    def CVlanTpidFilterDM(self):
        """C-VLAN TPID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('cVlanTpidFilterDM')

    @property
    def CVlanTpidFilterLM(self):
        """C-VLAN TPID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('cVlanTpidFilterLM')

    @property
    def CVlanTpidFilterLT(self):
        """C-VLAN TPID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('cVlanTpidFilterLT')

    @property
    def CVlanTpidFilterLb(self):
        """C-VLAN TPID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('cVlanTpidFilterLb')

    @property
    def Count(self):
        """Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

        Returns:
            number
        """
        return self._get_attribute('count')

    @property
    def DescriptiveName(self):
        """Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context

        Returns:
            str
        """
        return self._get_attribute('descriptiveName')

    @property
    def DestinationMpMacDM(self):
        """Destination MP MAC Filters Use All Destination MAC to fetch all Or use any other value

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('destinationMpMacDM')

    @property
    def DestinationMpMacLM(self):
        """Destination MP MAC Filters Use All Destination MAC to fetch all Or use any other value

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('destinationMpMacLM')

    @property
    def DestinationMpMacLT(self):
        """Destination MP MAC Filters Use All Destination MEP to fetch all Or use any other value

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('destinationMpMacLT')

    @property
    def DestinationMpMacLb(self):
        """Destination MP MAC Filters Use All Destination MAC to fetch all Or use any other value

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('destinationMpMacLb')

    @property
    def EnVLANFilterCCM(self):
        """Enable VLAN Filter

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enVLANFilterCCM')

    @property
    def MdOrMegLevelCCM(self):
        """MD/MEG Level Filters Use All MD Levels to fetch all Or use any other value

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('mdOrMegLevelCCM')

    @property
    def MdOrMegLevelDM(self):
        """MD/MEG Level Filters Use All MD Levels to fetch all Or use any other value

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('mdOrMegLevelDM')

    @property
    def MdOrMegLevelLM(self):
        """MD/MEG Level Filters Use All MD Levels to fetch all Or use any other value

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('mdOrMegLevelLM')

    @property
    def MdlevelLT(self):
        """MD/MEG Level Filters Use All MD Levels to fetch all Or use any other value

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('mdlevelLT')

    @property
    def MdlevelLb(self):
        """MD/MEG Level Filters Use All MD Levels to fetch all Or use any other value

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('mdlevelLb')

    @property
    def MethodDM(self):
        """Choose a Delay Measurement Method

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('methodDM')

    @property
    def Name(self):
        """Name of NGPF element, guaranteed to be unique in Scenario

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def NoCVlanFilterDM(self):
        """Use C-VLAN Filter

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('noCVlanFilterDM')

    @property
    def NoCVlanFilterLM(self):
        """Use C-VLAN Filter

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('noCVlanFilterLM')

    @property
    def NoSVlanFilterDM(self):
        """Use S-VLAN Filter

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('noSVlanFilterDM')

    @property
    def NoSVlanFilterLM(self):
        """Use S-VLAN Filter

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('noSVlanFilterLM')

    @property
    def SVlanIdFilterCCM(self):
        """S-VLAN ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sVlanIdFilterCCM')

    @property
    def SVlanIdFilterDM(self):
        """S-VLAN ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sVlanIdFilterDM')

    @property
    def SVlanIdFilterLM(self):
        """S-VLAN ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sVlanIdFilterLM')

    @property
    def SVlanIdFilterLT(self):
        """S-VLAN ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sVlanIdFilterLT')

    @property
    def SVlanIdFilterLb(self):
        """S-VLAN ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sVlanIdFilterLb')

    @property
    def SVlanPriorityFilterCCM(self):
        """S-VLAN Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sVlanPriorityFilterCCM')

    @property
    def SVlanPriorityFilterDM(self):
        """S-VLAN Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sVlanPriorityFilterDM')

    @property
    def SVlanPriorityFilterLM(self):
        """S-VLAN Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sVlanPriorityFilterLM')

    @property
    def SVlanPriorityFilterLT(self):
        """S-VLAN Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sVlanPriorityFilterLT')

    @property
    def SVlanPriorityFilterLb(self):
        """S-VLAN Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sVlanPriorityFilterLb')

    @property
    def SVlanTpidFilterCCM(self):
        """S-VLAN TPID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sVlanTpidFilterCCM')

    @property
    def SVlanTpidFilterDM(self):
        """S-VLAN TPID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sVlanTpidFilterDM')

    @property
    def SVlanTpidFilterLM(self):
        """S-VLAN TPID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sVlanTpidFilterLM')

    @property
    def SVlanTpidFilterLT(self):
        """S-VLAN TPID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sVlanTpidFilterLT')

    @property
    def SVlanTpidFilterLb(self):
        """S-VLAN TPID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sVlanTpidFilterLb')

    @property
    def SourceMpMacDM(self):
        """Source MP MAC Filters Use All Source MAC to fetch all Or use any other value

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sourceMpMacDM')

    @property
    def SourceMpMacLM(self):
        """Source MP MAC Filters Use All Source MAC to fetch all Or use any other value

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sourceMpMacLM')

    @property
    def SourceMpMacLT(self):
        """Source MP MAC Filters Use All Source MEP to fetch all Or use any other value

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sourceMpMacLT')

    @property
    def SourceMpMacLb(self):
        """Source MP MAC Filters Use All Source MAC to fetch all Or use any other value

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sourceMpMacLb')

    @property
    def TimeoutDM(self):
        """Timeout (ms)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('timeoutDM')

    @property
    def TimeoutLM(self):
        """Timeout (ms)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('timeoutLM')

    @property
    def TimeoutLT(self):
        """Timeout

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('timeoutLT')

    @property
    def TimeoutLb(self):
        """Timeout (ms)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('timeoutLb')

    @property
    def TransactionId(self):
        """Transaction ID (Unconfigured MEP)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('transactionId')

    @property
    def TransactionIdLT(self):
        """Transaction ID for Unconfigured Source MEP

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('transactionIdLT')

    @property
    def TtlLT(self):
        """TTL

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ttlLT')

    @property
    def TypeDM(self):
        """Type (DM/DVM)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('typeDM')

    @property
    def VlanIdFilterCCM(self):
        """VLAN ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('vlanIdFilterCCM')

    @property
    def VlanIdFilterLT(self):
        """VLAN ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('vlanIdFilterLT')

    @property
    def VlanIdFilterLb(self):
        """VLAN ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('vlanIdFilterLb')

    @property
    def VlanPriorityFilterCCM(self):
        """VLAN Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('vlanPriorityFilterCCM')

    @property
    def VlanPriorityFilterLT(self):
        """VLAN Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('vlanPriorityFilterLT')

    @property
    def VlanPriorityFilterLb(self):
        """VLAN Priority

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('vlanPriorityFilterLb')

    @property
    def VlanStackingCCM(self):
        """VLAN Stacking

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('vlanStackingCCM')

    @property
    def VlanStackingLT(self):
        """VLAN Stacking

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('vlanStackingLT')

    @property
    def VlanStackingLb(self):
        """VLAN Stacking

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('vlanStackingLb')

    @property
    def VlanTpidFilterCCM(self):
        """VLAN TPID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('vlanTpidFilterCCM')

    @property
    def VlanTpidFilterLT(self):
        """VLAN TPID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('vlanTpidFilterLT')

    @property
    def VlanTpidFilterLb(self):
        """VLAN TPID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('vlanTpidFilterLb')

    def update(self, Name=None):
        """Updates a child instance of advancedLearnedInfoOptions on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args:
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def get_device_ids(self, PortNames=None, AllCVlanCCM=None, AllCVlanFilterDM=None, AllCVlanFilterLM=None, AllDstMEPDM=None, AllDstMEPLM=None, AllDstMEPLT=None, AllDstMEPLb=None, AllSVlanCCM=None, AllSVlanFilterDM=None, AllSVlanFilterLM=None, AllSrcMEPDM=None, AllSrcMEPLM=None, AllSrcMEPLT=None, AllSrcMEPLb=None, AllVlanCCM=None, AutoVLANLT=None, AutoVLANLb=None, CVlanIdFilterCCM=None, CVlanIdFilterDM=None, CVlanIdFilterLM=None, CVlanIdFilterLT=None, CVlanIdFilterLb=None, CVlanPriorityFilterCCM=None, CVlanPriorityFilterDM=None, CVlanPriorityFilterLM=None, CVlanPriorityFilterLT=None, CVlanPriorityFilterLb=None, CVlanTpidFilterCCM=None, CVlanTpidFilterDM=None, CVlanTpidFilterLM=None, CVlanTpidFilterLT=None, CVlanTpidFilterLb=None, DestinationMpMacDM=None, DestinationMpMacLM=None, DestinationMpMacLT=None, DestinationMpMacLb=None, EnVLANFilterCCM=None, MdOrMegLevelCCM=None, MdOrMegLevelDM=None, MdOrMegLevelLM=None, MdlevelLT=None, MdlevelLb=None, MethodDM=None, NoCVlanFilterDM=None, NoCVlanFilterLM=None, NoSVlanFilterDM=None, NoSVlanFilterLM=None, SVlanIdFilterCCM=None, SVlanIdFilterDM=None, SVlanIdFilterLM=None, SVlanIdFilterLT=None, SVlanIdFilterLb=None, SVlanPriorityFilterCCM=None, SVlanPriorityFilterDM=None, SVlanPriorityFilterLM=None, SVlanPriorityFilterLT=None, SVlanPriorityFilterLb=None, SVlanTpidFilterCCM=None, SVlanTpidFilterDM=None, SVlanTpidFilterLM=None, SVlanTpidFilterLT=None, SVlanTpidFilterLb=None, SourceMpMacDM=None, SourceMpMacLM=None, SourceMpMacLT=None, SourceMpMacLb=None, TimeoutDM=None, TimeoutLM=None, TimeoutLT=None, TimeoutLb=None, TransactionId=None, TransactionIdLT=None, TtlLT=None, TypeDM=None, VlanIdFilterCCM=None, VlanIdFilterLT=None, VlanIdFilterLb=None, VlanPriorityFilterCCM=None, VlanPriorityFilterLT=None, VlanPriorityFilterLb=None, VlanStackingCCM=None, VlanStackingLT=None, VlanStackingLb=None, VlanTpidFilterCCM=None, VlanTpidFilterLT=None, VlanTpidFilterLb=None):
        """Base class infrastructure that gets a list of advancedLearnedInfoOptions device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args:
            PortNames (str): optional regex of port names
            AllCVlanCCM (str): optional regex of allCVlanCCM
            AllCVlanFilterDM (str): optional regex of allCVlanFilterDM
            AllCVlanFilterLM (str): optional regex of allCVlanFilterLM
            AllDstMEPDM (str): optional regex of allDstMEPDM
            AllDstMEPLM (str): optional regex of allDstMEPLM
            AllDstMEPLT (str): optional regex of allDstMEPLT
            AllDstMEPLb (str): optional regex of allDstMEPLb
            AllSVlanCCM (str): optional regex of allSVlanCCM
            AllSVlanFilterDM (str): optional regex of allSVlanFilterDM
            AllSVlanFilterLM (str): optional regex of allSVlanFilterLM
            AllSrcMEPDM (str): optional regex of allSrcMEPDM
            AllSrcMEPLM (str): optional regex of allSrcMEPLM
            AllSrcMEPLT (str): optional regex of allSrcMEPLT
            AllSrcMEPLb (str): optional regex of allSrcMEPLb
            AllVlanCCM (str): optional regex of allVlanCCM
            AutoVLANLT (str): optional regex of autoVLANLT
            AutoVLANLb (str): optional regex of autoVLANLb
            CVlanIdFilterCCM (str): optional regex of cVlanIdFilterCCM
            CVlanIdFilterDM (str): optional regex of cVlanIdFilterDM
            CVlanIdFilterLM (str): optional regex of cVlanIdFilterLM
            CVlanIdFilterLT (str): optional regex of cVlanIdFilterLT
            CVlanIdFilterLb (str): optional regex of cVlanIdFilterLb
            CVlanPriorityFilterCCM (str): optional regex of cVlanPriorityFilterCCM
            CVlanPriorityFilterDM (str): optional regex of cVlanPriorityFilterDM
            CVlanPriorityFilterLM (str): optional regex of cVlanPriorityFilterLM
            CVlanPriorityFilterLT (str): optional regex of cVlanPriorityFilterLT
            CVlanPriorityFilterLb (str): optional regex of cVlanPriorityFilterLb
            CVlanTpidFilterCCM (str): optional regex of cVlanTpidFilterCCM
            CVlanTpidFilterDM (str): optional regex of cVlanTpidFilterDM
            CVlanTpidFilterLM (str): optional regex of cVlanTpidFilterLM
            CVlanTpidFilterLT (str): optional regex of cVlanTpidFilterLT
            CVlanTpidFilterLb (str): optional regex of cVlanTpidFilterLb
            DestinationMpMacDM (str): optional regex of destinationMpMacDM
            DestinationMpMacLM (str): optional regex of destinationMpMacLM
            DestinationMpMacLT (str): optional regex of destinationMpMacLT
            DestinationMpMacLb (str): optional regex of destinationMpMacLb
            EnVLANFilterCCM (str): optional regex of enVLANFilterCCM
            MdOrMegLevelCCM (str): optional regex of mdOrMegLevelCCM
            MdOrMegLevelDM (str): optional regex of mdOrMegLevelDM
            MdOrMegLevelLM (str): optional regex of mdOrMegLevelLM
            MdlevelLT (str): optional regex of mdlevelLT
            MdlevelLb (str): optional regex of mdlevelLb
            MethodDM (str): optional regex of methodDM
            NoCVlanFilterDM (str): optional regex of noCVlanFilterDM
            NoCVlanFilterLM (str): optional regex of noCVlanFilterLM
            NoSVlanFilterDM (str): optional regex of noSVlanFilterDM
            NoSVlanFilterLM (str): optional regex of noSVlanFilterLM
            SVlanIdFilterCCM (str): optional regex of sVlanIdFilterCCM
            SVlanIdFilterDM (str): optional regex of sVlanIdFilterDM
            SVlanIdFilterLM (str): optional regex of sVlanIdFilterLM
            SVlanIdFilterLT (str): optional regex of sVlanIdFilterLT
            SVlanIdFilterLb (str): optional regex of sVlanIdFilterLb
            SVlanPriorityFilterCCM (str): optional regex of sVlanPriorityFilterCCM
            SVlanPriorityFilterDM (str): optional regex of sVlanPriorityFilterDM
            SVlanPriorityFilterLM (str): optional regex of sVlanPriorityFilterLM
            SVlanPriorityFilterLT (str): optional regex of sVlanPriorityFilterLT
            SVlanPriorityFilterLb (str): optional regex of sVlanPriorityFilterLb
            SVlanTpidFilterCCM (str): optional regex of sVlanTpidFilterCCM
            SVlanTpidFilterDM (str): optional regex of sVlanTpidFilterDM
            SVlanTpidFilterLM (str): optional regex of sVlanTpidFilterLM
            SVlanTpidFilterLT (str): optional regex of sVlanTpidFilterLT
            SVlanTpidFilterLb (str): optional regex of sVlanTpidFilterLb
            SourceMpMacDM (str): optional regex of sourceMpMacDM
            SourceMpMacLM (str): optional regex of sourceMpMacLM
            SourceMpMacLT (str): optional regex of sourceMpMacLT
            SourceMpMacLb (str): optional regex of sourceMpMacLb
            TimeoutDM (str): optional regex of timeoutDM
            TimeoutLM (str): optional regex of timeoutLM
            TimeoutLT (str): optional regex of timeoutLT
            TimeoutLb (str): optional regex of timeoutLb
            TransactionId (str): optional regex of transactionId
            TransactionIdLT (str): optional regex of transactionIdLT
            TtlLT (str): optional regex of ttlLT
            TypeDM (str): optional regex of typeDM
            VlanIdFilterCCM (str): optional regex of vlanIdFilterCCM
            VlanIdFilterLT (str): optional regex of vlanIdFilterLT
            VlanIdFilterLb (str): optional regex of vlanIdFilterLb
            VlanPriorityFilterCCM (str): optional regex of vlanPriorityFilterCCM
            VlanPriorityFilterLT (str): optional regex of vlanPriorityFilterLT
            VlanPriorityFilterLb (str): optional regex of vlanPriorityFilterLb
            VlanStackingCCM (str): optional regex of vlanStackingCCM
            VlanStackingLT (str): optional regex of vlanStackingLT
            VlanStackingLb (str): optional regex of vlanStackingLb
            VlanTpidFilterCCM (str): optional regex of vlanTpidFilterCCM
            VlanTpidFilterLT (str): optional regex of vlanTpidFilterLT
            VlanTpidFilterLb (str): optional regex of vlanTpidFilterLb

        Returns:
            list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def ClearAllLearnedInfo(self, *args, **kwargs):
        """Executes the clearAllLearnedInfo operation on the server.

        Clears ALL Learned LSP Information By PCC Device.

        clearAllLearnedInfo(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

            Returns:
                list(str): ID to associate each async action invocation

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('clearAllLearnedInfo', payload=payload, response_object=None)

    def GetAllLearnedInfo(self, *args, **kwargs):
        """Executes the getAllLearnedInfo operation on the server.

        Please provide a proper help text here.

        getAllLearnedInfo(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

            Returns:
                list(str): Please provide a proper description here

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getAllLearnedInfo', payload=payload, response_object=None)

    def GetCfmAISDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmAISDbLearnedInformation operation on the server.

        Get Learned AIS Information

        getCfmAISDbLearnedInformation(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

            Returns:
                list(str): Please provide a proper description here.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmAISDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmCcmLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmCcmLearnedInformation operation on the server.

        Please provide a proper help text here.

        getCfmCcmLearnedInformation(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

            Returns:
                list(str): Please provide a proper description here.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmCcmLearnedInformation', payload=payload, response_object=None)

    def GetCfmDMDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmDMDbLearnedInformation operation on the server.

        Get Learned DM Information

        getCfmDMDbLearnedInformation(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

            Returns:
                list(str): Please provide a proper description here.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmDMDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmLCKDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmLCKDbLearnedInformation operation on the server.

        Get Learned LCK Information

        getCfmLCKDbLearnedInformation(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

            Returns:
                list(str): Please provide a proper description here.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmLCKDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmLinkTraceDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmLinkTraceDbLearnedInformation operation on the server.

        Please provide a proper help text here.

        getCfmLinkTraceDbLearnedInformation(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

            Returns:
                list(str): Please provide a proper description here.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmLinkTraceDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmLMDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmLMDbLearnedInformation operation on the server.

        Get Learned LM Information

        getCfmLMDbLearnedInformation(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

            Returns:
                list(str): Please provide a proper description here.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmLMDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmLoopbackDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmLoopbackDbLearnedInformation operation on the server.

        Please provide a proper help text here.

        getCfmLoopbackDbLearnedInformation(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

            Returns:
                list(str): Please provide a proper description here.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmLoopbackDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmTSTDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmTSTDbLearnedInformation operation on the server.

        Get Learned TST Information

        getCfmTSTDbLearnedInformation(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

            Returns:
                list(str): Please provide a proper description here.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmTSTDbLearnedInformation', payload=payload, response_object=None)
