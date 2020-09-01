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


class AdvancedLearnedInfoOptions(Base):
    """CFM Learned Info Filters
    The AdvancedLearnedInfoOptions class encapsulates a required advancedLearnedInfoOptions resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'advancedLearnedInfoOptions'
    _SDM_ATT_MAP = {
        'AllCVlanCCM': 'allCVlanCCM',
        'AllDstMEPDM': 'allDstMEPDM',
        'AllDstMEPLM': 'allDstMEPLM',
        'AllDstMEPLT': 'allDstMEPLT',
        'AllDstMepLB': 'allDstMepLB',
        'AllSVlanCCM': 'allSVlanCCM',
        'AllSrcMEPDM': 'allSrcMEPDM',
        'AllSrcMEPLM': 'allSrcMEPLM',
        'AllSrcMEPLT': 'allSrcMEPLT',
        'AllSrcMepLB': 'allSrcMepLB',
        'AllVlanCCM': 'allVlanCCM',
        'CVlanIdFilterCCM': 'cVlanIdFilterCCM',
        'CVlanIdFilterDM': 'cVlanIdFilterDM',
        'CVlanIdFilterLB': 'cVlanIdFilterLB',
        'CVlanIdFilterLM': 'cVlanIdFilterLM',
        'CVlanIdFilterLT': 'cVlanIdFilterLT',
        'CVlanPriorityFilterCCM': 'cVlanPriorityFilterCCM',
        'CVlanPriorityFilterDM': 'cVlanPriorityFilterDM',
        'CVlanPriorityFilterLB': 'cVlanPriorityFilterLB',
        'CVlanPriorityFilterLM': 'cVlanPriorityFilterLM',
        'CVlanPriorityFilterLT': 'cVlanPriorityFilterLT',
        'CVlanTpidFilterCCM': 'cVlanTpidFilterCCM',
        'CVlanTpidFilterDM': 'cVlanTpidFilterDM',
        'CVlanTpidFilterLB': 'cVlanTpidFilterLB',
        'CVlanTpidFilterLM': 'cVlanTpidFilterLM',
        'CVlanTpidFilterLT': 'cVlanTpidFilterLT',
        'ConfiguredVlanDM': 'configuredVlanDM',
        'ConfiguredVlanLB': 'configuredVlanLB',
        'ConfiguredVlanLM': 'configuredVlanLM',
        'ConfiguredVlanLT': 'configuredVlanLT',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DestinationMpMacDM': 'destinationMpMacDM',
        'DestinationMpMacLB': 'destinationMpMacLB',
        'DestinationMpMacLM': 'destinationMpMacLM',
        'DestinationMpMacLT': 'destinationMpMacLT',
        'EnableVlanFilterCCM': 'enableVlanFilterCCM',
        'MdLevelLB': 'mdLevelLB',
        'MdLevelLT': 'mdLevelLT',
        'MdOrMegLevelCCM': 'mdOrMegLevelCCM',
        'MdOrMegLevelDM': 'mdOrMegLevelDM',
        'MdOrMegLevelLM': 'mdOrMegLevelLM',
        'MethodDM': 'methodDM',
        'Name': 'name',
        'SVlanIdFilterCCM': 'sVlanIdFilterCCM',
        'SVlanIdFilterDM': 'sVlanIdFilterDM',
        'SVlanIdFilterLB': 'sVlanIdFilterLB',
        'SVlanIdFilterLM': 'sVlanIdFilterLM',
        'SVlanIdFilterLT': 'sVlanIdFilterLT',
        'SVlanPriorityFilterCCM': 'sVlanPriorityFilterCCM',
        'SVlanPriorityFilterDM': 'sVlanPriorityFilterDM',
        'SVlanPriorityFilterLB': 'sVlanPriorityFilterLB',
        'SVlanPriorityFilterLM': 'sVlanPriorityFilterLM',
        'SVlanPriorityFilterLT': 'sVlanPriorityFilterLT',
        'SVlanTpidFilterCCM': 'sVlanTpidFilterCCM',
        'SVlanTpidFilterDM': 'sVlanTpidFilterDM',
        'SVlanTpidFilterLB': 'sVlanTpidFilterLB',
        'SVlanTpidFilterLM': 'sVlanTpidFilterLM',
        'SVlanTpidFilterLT': 'sVlanTpidFilterLT',
        'SourceMpMacDM': 'sourceMpMacDM',
        'SourceMpMacLB': 'sourceMpMacLB',
        'SourceMpMacLM': 'sourceMpMacLM',
        'SourceMpMacLT': 'sourceMpMacLT',
        'TimeoutDM': 'timeoutDM',
        'TimeoutLB': 'timeoutLB',
        'TimeoutLM': 'timeoutLM',
        'TimeoutLT': 'timeoutLT',
        'TransactionIdLB': 'transactionIdLB',
        'TransactionIdLT': 'transactionIdLT',
        'TtlLT': 'ttlLT',
        'TypeDM': 'typeDM',
        'VlanIdFilterCCM': 'vlanIdFilterCCM',
        'VlanIdFilterDM': 'vlanIdFilterDM',
        'VlanIdFilterLB': 'vlanIdFilterLB',
        'VlanIdFilterLM': 'vlanIdFilterLM',
        'VlanIdFilterLT': 'vlanIdFilterLT',
        'VlanPriorityFilterCCM': 'vlanPriorityFilterCCM',
        'VlanPriorityFilterDM': 'vlanPriorityFilterDM',
        'VlanPriorityFilterLB': 'vlanPriorityFilterLB',
        'VlanPriorityFilterLM': 'vlanPriorityFilterLM',
        'VlanPriorityFilterLT': 'vlanPriorityFilterLT',
        'VlanStackingCCM': 'vlanStackingCCM',
        'VlanStackingDM': 'vlanStackingDM',
        'VlanStackingLB': 'vlanStackingLB',
        'VlanStackingLM': 'vlanStackingLM',
        'VlanStackingLT': 'vlanStackingLT',
        'VlanTpidFilterCCM': 'vlanTpidFilterCCM',
        'VlanTpidFilterDM': 'vlanTpidFilterDM',
        'VlanTpidFilterLB': 'vlanTpidFilterLB',
        'VlanTpidFilterLM': 'vlanTpidFilterLM',
        'VlanTpidFilterLT': 'vlanTpidFilterLT',
    }

    def __init__(self, parent):
        super(AdvancedLearnedInfoOptions, self).__init__(parent)

    @property
    def AllCVlanCCM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include All C-VLAN
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AllCVlanCCM']))

    @property
    def AllDstMEPDM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use All Learned MEPs (in same MA) as Destination.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AllDstMEPDM']))

    @property
    def AllDstMEPLM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use All Learned MEPs (in same MA) as Destination.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AllDstMEPLM']))

    @property
    def AllDstMEPLT(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use All Learned MEPs (in same MA) as Destination.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AllDstMEPLT']))

    @property
    def AllDstMepLB(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use All Learned MEPs (in same MA) as Destination.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AllDstMepLB']))

    @property
    def AllSVlanCCM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable to display all the S-VLAN IDs without filtering using any specific S-VLAN ID.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AllSVlanCCM']))

    @property
    def AllSrcMEPDM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use All Configured MEPs as Source.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AllSrcMEPDM']))

    @property
    def AllSrcMEPLM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use All Configured MEPs as Source.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AllSrcMEPLM']))

    @property
    def AllSrcMEPLT(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use All Configured MEPs as Source.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AllSrcMEPLT']))

    @property
    def AllSrcMepLB(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use All Configured MEPs as Source.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AllSrcMepLB']))

    @property
    def AllVlanCCM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable to display all the VLAN IDs without filtering using any specific VLAN ID.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AllVlanCCM']))

    @property
    def CVlanIdFilterCCM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Filter learned information using this C-VLAN ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CVlanIdFilterCCM']))

    @property
    def CVlanIdFilterDM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this C-VLAN ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CVlanIdFilterDM']))

    @property
    def CVlanIdFilterLB(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this C-VLAN ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CVlanIdFilterLB']))

    @property
    def CVlanIdFilterLM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this C-VLAN ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CVlanIdFilterLM']))

    @property
    def CVlanIdFilterLT(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this C-VLAN ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CVlanIdFilterLT']))

    @property
    def CVlanPriorityFilterCCM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Filter learned information using this C-VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CVlanPriorityFilterCCM']))

    @property
    def CVlanPriorityFilterDM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this C-VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CVlanPriorityFilterDM']))

    @property
    def CVlanPriorityFilterLB(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this C-VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CVlanPriorityFilterLB']))

    @property
    def CVlanPriorityFilterLM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this C-VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CVlanPriorityFilterLM']))

    @property
    def CVlanPriorityFilterLT(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this C-VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CVlanPriorityFilterLT']))

    @property
    def CVlanTpidFilterCCM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Filter learned information using this C-VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CVlanTpidFilterCCM']))

    @property
    def CVlanTpidFilterDM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this C-VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CVlanTpidFilterDM']))

    @property
    def CVlanTpidFilterLB(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this C-VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CVlanTpidFilterLB']))

    @property
    def CVlanTpidFilterLM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this C-VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CVlanTpidFilterLM']))

    @property
    def CVlanTpidFilterLT(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this C-VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CVlanTpidFilterLT']))

    @property
    def ConfiguredVlanDM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Allows the configured VLAN value of the source MEP to be used in DMM PDU.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfiguredVlanDM']))

    @property
    def ConfiguredVlanLB(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Allows the configured VLAN value of the source MEP to be used in LBM PDU.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfiguredVlanLB']))

    @property
    def ConfiguredVlanLM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Allows the configured VLAN value of the source MEP to be used in LMM PDU.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfiguredVlanLM']))

    @property
    def ConfiguredVlanLT(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Allows the configured VLAN value of the source MEP to be used in LTM PDU.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfiguredVlanLT']))

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
    def DestinationMpMacDM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Destination MP MAC address.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DestinationMpMacDM']))

    @property
    def DestinationMpMacLB(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Destination MP MAC address.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DestinationMpMacLB']))

    @property
    def DestinationMpMacLM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Destination MP MAC address.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DestinationMpMacLM']))

    @property
    def DestinationMpMacLT(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Destination MP MAC address.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DestinationMpMacLT']))

    @property
    def EnableVlanFilterCCM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables filtering in learned information using VLAN
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableVlanFilterCCM']))

    @property
    def MdLevelLB(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Trigger Loopback in All or selected MD Level.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MdLevelLB']))

    @property
    def MdLevelLT(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Trigger Link Trace in All or selected MD Level.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MdLevelLT']))

    @property
    def MdOrMegLevelCCM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select any MD Level value to display only that level in learned information, if available. Select All to not use any filter.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MdOrMegLevelCCM']))

    @property
    def MdOrMegLevelDM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Trigger Delay Measurement in All or selected MD Level.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MdOrMegLevelDM']))

    @property
    def MdOrMegLevelLM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Trigger Loss Measurement in All or selected MD Level.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MdOrMegLevelLM']))

    @property
    def MethodDM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Choose a Delay Measurement Method (One or Two way).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MethodDM']))

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
    def SVlanIdFilterCCM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Filter learned information using this S-VLAN ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SVlanIdFilterCCM']))

    @property
    def SVlanIdFilterDM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this S-VLAN ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SVlanIdFilterDM']))

    @property
    def SVlanIdFilterLB(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this S-VLAN ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SVlanIdFilterLB']))

    @property
    def SVlanIdFilterLM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this S-VLAN ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SVlanIdFilterLM']))

    @property
    def SVlanIdFilterLT(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this S-VLAN ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SVlanIdFilterLT']))

    @property
    def SVlanPriorityFilterCCM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Filter learned information using this S-VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SVlanPriorityFilterCCM']))

    @property
    def SVlanPriorityFilterDM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this S-VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SVlanPriorityFilterDM']))

    @property
    def SVlanPriorityFilterLB(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this S-VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SVlanPriorityFilterLB']))

    @property
    def SVlanPriorityFilterLM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this S-VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SVlanPriorityFilterLM']))

    @property
    def SVlanPriorityFilterLT(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this S-VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SVlanPriorityFilterLT']))

    @property
    def SVlanTpidFilterCCM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Filter learned information using this S-VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SVlanTpidFilterCCM']))

    @property
    def SVlanTpidFilterDM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this S-VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SVlanTpidFilterDM']))

    @property
    def SVlanTpidFilterLB(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this S-VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SVlanTpidFilterLB']))

    @property
    def SVlanTpidFilterLM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this S-VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SVlanTpidFilterLM']))

    @property
    def SVlanTpidFilterLT(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this S-VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SVlanTpidFilterLT']))

    @property
    def SourceMpMacDM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source MEP MAC address. Unconfigured MAC address also allowed.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceMpMacDM']))

    @property
    def SourceMpMacLB(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source MEP MAC address. Unconfigured MAC address also allowed.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceMpMacLB']))

    @property
    def SourceMpMacLM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source MEP MAC address. Unconfigured MAC address also allowed.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceMpMacLM']))

    @property
    def SourceMpMacLT(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source MEP MAC address. Unconfigured MAC address also allowed.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceMpMacLT']))

    @property
    def TimeoutDM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Trigger DMM or 1DM using Timeout (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimeoutDM']))

    @property
    def TimeoutLB(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Trigger Loopback using Timeout (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimeoutLB']))

    @property
    def TimeoutLM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Trigger LMM using Timeout (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimeoutLM']))

    @property
    def TimeoutLT(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Trigger Link Trace using this Timeout
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimeoutLT']))

    @property
    def TransactionIdLB(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Transaction ID (Unconfigured MEP)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TransactionIdLB']))

    @property
    def TransactionIdLT(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Transaction ID for Unconfigured Source MEP i.e. if the Source MAC dosent match any of the learned RMEP.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TransactionIdLT']))

    @property
    def TtlLT(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Trigger Link Trace using this TTL
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TtlLT']))

    @property
    def TypeDM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Delay measurement type (DM or DVM).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TypeDM']))

    @property
    def VlanIdFilterCCM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Filter learned information using this VLAN ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanIdFilterCCM']))

    @property
    def VlanIdFilterDM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this VLAN ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanIdFilterDM']))

    @property
    def VlanIdFilterLB(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this VLAN ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanIdFilterLB']))

    @property
    def VlanIdFilterLM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this VLAN ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanIdFilterLM']))

    @property
    def VlanIdFilterLT(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this VLAN ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanIdFilterLT']))

    @property
    def VlanPriorityFilterCCM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Filter learned information using this VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanPriorityFilterCCM']))

    @property
    def VlanPriorityFilterDM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanPriorityFilterDM']))

    @property
    def VlanPriorityFilterLB(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanPriorityFilterLB']))

    @property
    def VlanPriorityFilterLM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanPriorityFilterLM']))

    @property
    def VlanPriorityFilterLT(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanPriorityFilterLT']))

    @property
    def VlanStackingCCM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): No VLAN displays all learned information that dosenot belongs to any VLAN. Single or Stacked VLAN displays learned information with one or two VLAN respectively.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanStackingCCM']))

    @property
    def VlanStackingDM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): No VLAN dosent include any VLAN info in the PDU. Single or Stacked VLAN includes the following configuration options.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanStackingDM']))

    @property
    def VlanStackingLB(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): No VLAN dosent include any VLAN info in the PDU. Single or Stacked VLAN includes the following configuration options.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanStackingLB']))

    @property
    def VlanStackingLM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): No VLAN dosent include any VLAN info in the PDU. Single or Stacked VLAN includes the following configuration options.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanStackingLM']))

    @property
    def VlanStackingLT(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): No VLAN dosent include any VLAN info in the PDU. Single or Stacked VLAN includes the following configuration options.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanStackingLT']))

    @property
    def VlanTpidFilterCCM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Filter learned information using this VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanTpidFilterCCM']))

    @property
    def VlanTpidFilterDM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanTpidFilterDM']))

    @property
    def VlanTpidFilterLB(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanTpidFilterLB']))

    @property
    def VlanTpidFilterLM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanTpidFilterLM']))

    @property
    def VlanTpidFilterLT(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Triggered PDU includes this VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VlanTpidFilterLT']))

    def update(self, Name=None):
        """Updates advancedLearnedInfoOptions resource on the server.

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

    def get_device_ids(self, PortNames=None, AllCVlanCCM=None, AllDstMEPDM=None, AllDstMEPLM=None, AllDstMEPLT=None, AllDstMepLB=None, AllSVlanCCM=None, AllSrcMEPDM=None, AllSrcMEPLM=None, AllSrcMEPLT=None, AllSrcMepLB=None, AllVlanCCM=None, CVlanIdFilterCCM=None, CVlanIdFilterDM=None, CVlanIdFilterLB=None, CVlanIdFilterLM=None, CVlanIdFilterLT=None, CVlanPriorityFilterCCM=None, CVlanPriorityFilterDM=None, CVlanPriorityFilterLB=None, CVlanPriorityFilterLM=None, CVlanPriorityFilterLT=None, CVlanTpidFilterCCM=None, CVlanTpidFilterDM=None, CVlanTpidFilterLB=None, CVlanTpidFilterLM=None, CVlanTpidFilterLT=None, ConfiguredVlanDM=None, ConfiguredVlanLB=None, ConfiguredVlanLM=None, ConfiguredVlanLT=None, DestinationMpMacDM=None, DestinationMpMacLB=None, DestinationMpMacLM=None, DestinationMpMacLT=None, EnableVlanFilterCCM=None, MdLevelLB=None, MdLevelLT=None, MdOrMegLevelCCM=None, MdOrMegLevelDM=None, MdOrMegLevelLM=None, MethodDM=None, SVlanIdFilterCCM=None, SVlanIdFilterDM=None, SVlanIdFilterLB=None, SVlanIdFilterLM=None, SVlanIdFilterLT=None, SVlanPriorityFilterCCM=None, SVlanPriorityFilterDM=None, SVlanPriorityFilterLB=None, SVlanPriorityFilterLM=None, SVlanPriorityFilterLT=None, SVlanTpidFilterCCM=None, SVlanTpidFilterDM=None, SVlanTpidFilterLB=None, SVlanTpidFilterLM=None, SVlanTpidFilterLT=None, SourceMpMacDM=None, SourceMpMacLB=None, SourceMpMacLM=None, SourceMpMacLT=None, TimeoutDM=None, TimeoutLB=None, TimeoutLM=None, TimeoutLT=None, TransactionIdLB=None, TransactionIdLT=None, TtlLT=None, TypeDM=None, VlanIdFilterCCM=None, VlanIdFilterDM=None, VlanIdFilterLB=None, VlanIdFilterLM=None, VlanIdFilterLT=None, VlanPriorityFilterCCM=None, VlanPriorityFilterDM=None, VlanPriorityFilterLB=None, VlanPriorityFilterLM=None, VlanPriorityFilterLT=None, VlanStackingCCM=None, VlanStackingDM=None, VlanStackingLB=None, VlanStackingLM=None, VlanStackingLT=None, VlanTpidFilterCCM=None, VlanTpidFilterDM=None, VlanTpidFilterLB=None, VlanTpidFilterLM=None, VlanTpidFilterLT=None):
        """Base class infrastructure that gets a list of advancedLearnedInfoOptions device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AllCVlanCCM (str): optional regex of allCVlanCCM
        - AllDstMEPDM (str): optional regex of allDstMEPDM
        - AllDstMEPLM (str): optional regex of allDstMEPLM
        - AllDstMEPLT (str): optional regex of allDstMEPLT
        - AllDstMepLB (str): optional regex of allDstMepLB
        - AllSVlanCCM (str): optional regex of allSVlanCCM
        - AllSrcMEPDM (str): optional regex of allSrcMEPDM
        - AllSrcMEPLM (str): optional regex of allSrcMEPLM
        - AllSrcMEPLT (str): optional regex of allSrcMEPLT
        - AllSrcMepLB (str): optional regex of allSrcMepLB
        - AllVlanCCM (str): optional regex of allVlanCCM
        - CVlanIdFilterCCM (str): optional regex of cVlanIdFilterCCM
        - CVlanIdFilterDM (str): optional regex of cVlanIdFilterDM
        - CVlanIdFilterLB (str): optional regex of cVlanIdFilterLB
        - CVlanIdFilterLM (str): optional regex of cVlanIdFilterLM
        - CVlanIdFilterLT (str): optional regex of cVlanIdFilterLT
        - CVlanPriorityFilterCCM (str): optional regex of cVlanPriorityFilterCCM
        - CVlanPriorityFilterDM (str): optional regex of cVlanPriorityFilterDM
        - CVlanPriorityFilterLB (str): optional regex of cVlanPriorityFilterLB
        - CVlanPriorityFilterLM (str): optional regex of cVlanPriorityFilterLM
        - CVlanPriorityFilterLT (str): optional regex of cVlanPriorityFilterLT
        - CVlanTpidFilterCCM (str): optional regex of cVlanTpidFilterCCM
        - CVlanTpidFilterDM (str): optional regex of cVlanTpidFilterDM
        - CVlanTpidFilterLB (str): optional regex of cVlanTpidFilterLB
        - CVlanTpidFilterLM (str): optional regex of cVlanTpidFilterLM
        - CVlanTpidFilterLT (str): optional regex of cVlanTpidFilterLT
        - ConfiguredVlanDM (str): optional regex of configuredVlanDM
        - ConfiguredVlanLB (str): optional regex of configuredVlanLB
        - ConfiguredVlanLM (str): optional regex of configuredVlanLM
        - ConfiguredVlanLT (str): optional regex of configuredVlanLT
        - DestinationMpMacDM (str): optional regex of destinationMpMacDM
        - DestinationMpMacLB (str): optional regex of destinationMpMacLB
        - DestinationMpMacLM (str): optional regex of destinationMpMacLM
        - DestinationMpMacLT (str): optional regex of destinationMpMacLT
        - EnableVlanFilterCCM (str): optional regex of enableVlanFilterCCM
        - MdLevelLB (str): optional regex of mdLevelLB
        - MdLevelLT (str): optional regex of mdLevelLT
        - MdOrMegLevelCCM (str): optional regex of mdOrMegLevelCCM
        - MdOrMegLevelDM (str): optional regex of mdOrMegLevelDM
        - MdOrMegLevelLM (str): optional regex of mdOrMegLevelLM
        - MethodDM (str): optional regex of methodDM
        - SVlanIdFilterCCM (str): optional regex of sVlanIdFilterCCM
        - SVlanIdFilterDM (str): optional regex of sVlanIdFilterDM
        - SVlanIdFilterLB (str): optional regex of sVlanIdFilterLB
        - SVlanIdFilterLM (str): optional regex of sVlanIdFilterLM
        - SVlanIdFilterLT (str): optional regex of sVlanIdFilterLT
        - SVlanPriorityFilterCCM (str): optional regex of sVlanPriorityFilterCCM
        - SVlanPriorityFilterDM (str): optional regex of sVlanPriorityFilterDM
        - SVlanPriorityFilterLB (str): optional regex of sVlanPriorityFilterLB
        - SVlanPriorityFilterLM (str): optional regex of sVlanPriorityFilterLM
        - SVlanPriorityFilterLT (str): optional regex of sVlanPriorityFilterLT
        - SVlanTpidFilterCCM (str): optional regex of sVlanTpidFilterCCM
        - SVlanTpidFilterDM (str): optional regex of sVlanTpidFilterDM
        - SVlanTpidFilterLB (str): optional regex of sVlanTpidFilterLB
        - SVlanTpidFilterLM (str): optional regex of sVlanTpidFilterLM
        - SVlanTpidFilterLT (str): optional regex of sVlanTpidFilterLT
        - SourceMpMacDM (str): optional regex of sourceMpMacDM
        - SourceMpMacLB (str): optional regex of sourceMpMacLB
        - SourceMpMacLM (str): optional regex of sourceMpMacLM
        - SourceMpMacLT (str): optional regex of sourceMpMacLT
        - TimeoutDM (str): optional regex of timeoutDM
        - TimeoutLB (str): optional regex of timeoutLB
        - TimeoutLM (str): optional regex of timeoutLM
        - TimeoutLT (str): optional regex of timeoutLT
        - TransactionIdLB (str): optional regex of transactionIdLB
        - TransactionIdLT (str): optional regex of transactionIdLT
        - TtlLT (str): optional regex of ttlLT
        - TypeDM (str): optional regex of typeDM
        - VlanIdFilterCCM (str): optional regex of vlanIdFilterCCM
        - VlanIdFilterDM (str): optional regex of vlanIdFilterDM
        - VlanIdFilterLB (str): optional regex of vlanIdFilterLB
        - VlanIdFilterLM (str): optional regex of vlanIdFilterLM
        - VlanIdFilterLT (str): optional regex of vlanIdFilterLT
        - VlanPriorityFilterCCM (str): optional regex of vlanPriorityFilterCCM
        - VlanPriorityFilterDM (str): optional regex of vlanPriorityFilterDM
        - VlanPriorityFilterLB (str): optional regex of vlanPriorityFilterLB
        - VlanPriorityFilterLM (str): optional regex of vlanPriorityFilterLM
        - VlanPriorityFilterLT (str): optional regex of vlanPriorityFilterLT
        - VlanStackingCCM (str): optional regex of vlanStackingCCM
        - VlanStackingDM (str): optional regex of vlanStackingDM
        - VlanStackingLB (str): optional regex of vlanStackingLB
        - VlanStackingLM (str): optional regex of vlanStackingLM
        - VlanStackingLT (str): optional regex of vlanStackingLT
        - VlanTpidFilterCCM (str): optional regex of vlanTpidFilterCCM
        - VlanTpidFilterDM (str): optional regex of vlanTpidFilterDM
        - VlanTpidFilterLB (str): optional regex of vlanTpidFilterLB
        - VlanTpidFilterLM (str): optional regex of vlanTpidFilterLM
        - VlanTpidFilterLT (str): optional regex of vlanTpidFilterLT

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def ClearAllLearnedInfo(self, *args, **kwargs):
        """Executes the clearAllLearnedInfo operation on the server.

        Clears All Learned Info for the selected Root MP.

        clearAllLearnedInfo(Arg2=list)list
        ----------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('clearAllLearnedInfo', payload=payload, response_object=None)

    def GetCfmAISDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmAISDbLearnedInformation operation on the server.

        Get Learned AIS Information

        getCfmAISDbLearnedInformation(Arg2=list)list
        --------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
        - Returns list(str): Please provide a proper description here.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmAISDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmCcmLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmCcmLearnedInformation operation on the server.

        Please provide a proper help text here.

        getCfmCcmLearnedInformation(Arg2=list)list
        ------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
        - Returns list(str): Please provide a proper description here.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmCcmLearnedInformation', payload=payload, response_object=None)

    def GetCfmDMDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmDMDbLearnedInformation operation on the server.

        Get Learned DM Information

        getCfmDMDbLearnedInformation(Arg2=list)list
        -------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
        - Returns list(str): Please provide a proper description here.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmDMDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmLCKDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmLCKDbLearnedInformation operation on the server.

        Get Learned LCK Information

        getCfmLCKDbLearnedInformation(Arg2=list)list
        --------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
        - Returns list(str): Please provide a proper description here.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmLCKDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmLinkTraceDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmLinkTraceDbLearnedInformation operation on the server.

        Please provide a proper help text here.

        getCfmLinkTraceDbLearnedInformation(Arg2=list)list
        --------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
        - Returns list(str): Please provide a proper description here.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmLinkTraceDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmLMDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmLMDbLearnedInformation operation on the server.

        Get Learned LM Information

        getCfmLMDbLearnedInformation(Arg2=list)list
        -------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
        - Returns list(str): Please provide a proper description here.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmLMDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmLoopbackDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmLoopbackDbLearnedInformation operation on the server.

        Please provide a proper help text here.

        getCfmLoopbackDbLearnedInformation(Arg2=list)list
        -------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
        - Returns list(str): Please provide a proper description here.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmLoopbackDbLearnedInformation', payload=payload, response_object=None)

    def GetCfmTSTDbLearnedInformation(self, *args, **kwargs):
        """Executes the getCfmTSTDbLearnedInformation operation on the server.

        Get Learned TST Information

        getCfmTSTDbLearnedInformation(Arg2=list)list
        --------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
        - Returns list(str): Please provide a proper description here.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getCfmTSTDbLearnedInformation', payload=payload, response_object=None)

    def GetPeriodicDMLearnedInformation(self, *args, **kwargs):
        """Executes the getPeriodicDMLearnedInformation operation on the server.

        Please provide a proper help text here.

        getPeriodicDMLearnedInformation(Arg2=list)list
        ----------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
        - Returns list(str): Please provide a proper description here.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPeriodicDMLearnedInformation', payload=payload, response_object=None)

    def GetPeriodicLBLearnedInformation(self, *args, **kwargs):
        """Executes the getPeriodicLBLearnedInformation operation on the server.

        Please provide a proper help text here.

        getPeriodicLBLearnedInformation(Arg2=list)list
        ----------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
        - Returns list(str): Please provide a proper description here.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPeriodicLBLearnedInformation', payload=payload, response_object=None)

    def GetPeriodicLMLearnedInformation(self, *args, **kwargs):
        """Executes the getPeriodicLMLearnedInformation operation on the server.

        Please provide a proper help text here.

        getPeriodicLMLearnedInformation(Arg2=list)list
        ----------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
        - Returns list(str): Please provide a proper description here.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPeriodicLMLearnedInformation', payload=payload, response_object=None)

    def GetPeriodicLTLearnedInformation(self, *args, **kwargs):
        """Executes the getPeriodicLTLearnedInformation operation on the server.

        Please provide a proper help text here.

        getPeriodicLTLearnedInformation(Arg2=list)list
        ----------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.
        - Returns list(str): Please provide a proper description here.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPeriodicLTLearnedInformation', payload=payload, response_object=None)
