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


class IsisPseudoTraffEngProfile(Base):
    """ISIS Pseudo Node Traffic Engineering Profiles
    The IsisPseudoTraffEngProfile class encapsulates a required isisPseudoTraffEngProfile resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'isisPseudoTraffEngProfile'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'ActiveTo': 'activeTo',
        'AdministratorGroup': 'administratorGroup',
        'AdministratorGroupTo': 'administratorGroupTo',
        'AdvAppSpecificTraffic': 'advAppSpecificTraffic',
        'AdvMinMaxUniDiLinkDelay': 'advMinMaxUniDiLinkDelay',
        'AdvMinMaxUniDiLinkDelayTo': 'advMinMaxUniDiLinkDelayTo',
        'AdvUniDirAvailableBw': 'advUniDirAvailableBw',
        'AdvUniDirAvailableBwTo': 'advUniDirAvailableBwTo',
        'AdvUniDirDelayVariation': 'advUniDirDelayVariation',
        'AdvUniDirDelayVariationTo': 'advUniDirDelayVariationTo',
        'AdvUniDirLinkLoss': 'advUniDirLinkLoss',
        'AdvUniDirLinkLossTo': 'advUniDirLinkLossTo',
        'AdvUniDirResidualBw': 'advUniDirResidualBw',
        'AdvUniDirResidualBwTo': 'advUniDirResidualBwTo',
        'AdvUniDirUtilizedBw': 'advUniDirUtilizedBw',
        'AdvUniDirUtilizedBwTo': 'advUniDirUtilizedBwTo',
        'AdvertiseExtAdminGroup': 'advertiseExtAdminGroup',
        'AdvertiseExtAdminGroupTo': 'advertiseExtAdminGroupTo',
        'AdvertiseUniDiLinkDelay': 'advertiseUniDiLinkDelay',
        'AdvertiseUniDiLinkDelayTo': 'advertiseUniDiLinkDelayTo',
        'BandwidthPriority0_Bps': 'bandwidthPriority0_Bps',
        'BandwidthPriority0_BpsTo': 'bandwidthPriority0_BpsTo',
        'BandwidthPriority1_Bps': 'bandwidthPriority1_Bps',
        'BandwidthPriority1_BpsTo': 'bandwidthPriority1_BpsTo',
        'BandwidthPriority2_Bps': 'bandwidthPriority2_Bps',
        'BandwidthPriority2_BpsTo': 'bandwidthPriority2_BpsTo',
        'BandwidthPriority3_Bps': 'bandwidthPriority3_Bps',
        'BandwidthPriority3_BpsTo': 'bandwidthPriority3_BpsTo',
        'BandwidthPriority4_Bps': 'bandwidthPriority4_Bps',
        'BandwidthPriority4_BpsTo': 'bandwidthPriority4_BpsTo',
        'BandwidthPriority5_Bps': 'bandwidthPriority5_Bps',
        'BandwidthPriority5_BpsTo': 'bandwidthPriority5_BpsTo',
        'BandwidthPriority6_Bps': 'bandwidthPriority6_Bps',
        'BandwidthPriority6_BpsTo': 'bandwidthPriority6_BpsTo',
        'BandwidthPriority7_Bps': 'bandwidthPriority7_Bps',
        'BandwidthPriority7_BpsTo': 'bandwidthPriority7_BpsTo',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'ExtAdminGroup': 'extAdminGroup',
        'ExtAdminGroupLength': 'extAdminGroupLength',
        'ExtAdminGroupLengthTo': 'extAdminGroupLengthTo',
        'ExtAdminGroupTo': 'extAdminGroupTo',
        'LFlag': 'lFlag',
        'MaxBandwidth_Bps': 'maxBandwidth_Bps',
        'MaxBandwidth_BpsTo': 'maxBandwidth_BpsTo',
        'MaxReservableBandwidth_Bps': 'maxReservableBandwidth_Bps',
        'MaxReservableBandwidth_BpsTo': 'maxReservableBandwidth_BpsTo',
        'MetricLevel': 'metricLevel',
        'MetricLevelTo': 'metricLevelTo',
        'MinMaxUniDirLinkDelayABit': 'minMaxUniDirLinkDelayABit',
        'MinMaxUniDirLinkDelayABitTo': 'minMaxUniDirLinkDelayABitTo',
        'MtApplicabilityForIPv6': 'mtApplicabilityForIPv6',
        'MtIdTo': 'mtIdTo',
        'Name': 'name',
        'StdAppType': 'stdAppType',
        'UniDirAvailableBw': 'uniDirAvailableBw',
        'UniDirAvailableBwTo': 'uniDirAvailableBwTo',
        'UniDirLinkDelay': 'uniDirLinkDelay',
        'UniDirLinkDelayABit': 'uniDirLinkDelayABit',
        'UniDirLinkDelayABitTo': 'uniDirLinkDelayABitTo',
        'UniDirLinkDelayTo': 'uniDirLinkDelayTo',
        'UniDirLinkDelayVariation': 'uniDirLinkDelayVariation',
        'UniDirLinkDelayVariationTo': 'uniDirLinkDelayVariationTo',
        'UniDirLinkLoss': 'uniDirLinkLoss',
        'UniDirLinkLossABit': 'uniDirLinkLossABit',
        'UniDirLinkLossABitTo': 'uniDirLinkLossABitTo',
        'UniDirLinkLossTo': 'uniDirLinkLossTo',
        'UniDirLinkMaxDelay': 'uniDirLinkMaxDelay',
        'UniDirLinkMaxDelayTo': 'uniDirLinkMaxDelayTo',
        'UniDirLinkMinDelay': 'uniDirLinkMinDelay',
        'UniDirLinkMinDelayTo': 'uniDirLinkMinDelayTo',
        'UniDirResidualBw': 'uniDirResidualBw',
        'UniDirResidualBwTo': 'uniDirResidualBwTo',
        'UniDirUtilizedBw': 'uniDirUtilizedBw',
        'UniDirUtilizedBwTo': 'uniDirUtilizedBwTo',
        'UserDefAppBm': 'userDefAppBm',
        'UserDefAppBmLen': 'userDefAppBmLen',
    }

    def __init__(self, parent):
        super(IsisPseudoTraffEngProfile, self).__init__(parent)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def ActiveTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ActiveTo']))

    @property
    def AdministratorGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Administrator Group
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdministratorGroup']))

    @property
    def AdministratorGroupTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Administrator Group
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdministratorGroupTo']))

    @property
    def AdvAppSpecificTraffic(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If this is set to True, link attributes will be advertised as sub-TLV of TLVs 22,23,141,222 and 223 If set to False, the link atrributes will be advertised as wither sub-sub-tlv of Application Specific Link Attributes sub-TLV (Type 26) or sub-tlv of TLVs 22,23,141,222 and 223 depending upon the configuration of L flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvAppSpecificTraffic']))

    @property
    def AdvMinMaxUniDiLinkDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Min/Max Uni-Directional Link Delay
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvMinMaxUniDiLinkDelay']))

    @property
    def AdvMinMaxUniDiLinkDelayTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Min/Max Uni-Directional Link Delay
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvMinMaxUniDiLinkDelayTo']))

    @property
    def AdvUniDirAvailableBw(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Available BW
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvUniDirAvailableBw']))

    @property
    def AdvUniDirAvailableBwTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Available BW
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvUniDirAvailableBwTo']))

    @property
    def AdvUniDirDelayVariation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Delay Variation
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvUniDirDelayVariation']))

    @property
    def AdvUniDirDelayVariationTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Delay Variation
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvUniDirDelayVariationTo']))

    @property
    def AdvUniDirLinkLoss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Link Loss
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvUniDirLinkLoss']))

    @property
    def AdvUniDirLinkLossTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Link Loss
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvUniDirLinkLossTo']))

    @property
    def AdvUniDirResidualBw(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Residual BW
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvUniDirResidualBw']))

    @property
    def AdvUniDirResidualBwTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Residual BW
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvUniDirResidualBwTo']))

    @property
    def AdvUniDirUtilizedBw(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Utilized BW
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvUniDirUtilizedBw']))

    @property
    def AdvUniDirUtilizedBwTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Utilized BW
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvUniDirUtilizedBwTo']))

    @property
    def AdvertiseExtAdminGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Ext Admin Group
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseExtAdminGroup']))

    @property
    def AdvertiseExtAdminGroupTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Ext Admin Group
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseExtAdminGroupTo']))

    @property
    def AdvertiseUniDiLinkDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Link Delay
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseUniDiLinkDelay']))

    @property
    def AdvertiseUniDiLinkDelayTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Link Delay
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseUniDiLinkDelayTo']))

    @property
    def BandwidthPriority0_Bps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 0 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority0_Bps']))

    @property
    def BandwidthPriority0_BpsTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 0 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority0_BpsTo']))

    @property
    def BandwidthPriority1_Bps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 1 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority1_Bps']))

    @property
    def BandwidthPriority1_BpsTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 1 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority1_BpsTo']))

    @property
    def BandwidthPriority2_Bps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 2 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority2_Bps']))

    @property
    def BandwidthPriority2_BpsTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 2 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority2_BpsTo']))

    @property
    def BandwidthPriority3_Bps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 3 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority3_Bps']))

    @property
    def BandwidthPriority3_BpsTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 3 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority3_BpsTo']))

    @property
    def BandwidthPriority4_Bps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 4 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority4_Bps']))

    @property
    def BandwidthPriority4_BpsTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 4 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority4_BpsTo']))

    @property
    def BandwidthPriority5_Bps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 5 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority5_Bps']))

    @property
    def BandwidthPriority5_BpsTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 5 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority5_BpsTo']))

    @property
    def BandwidthPriority6_Bps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 6 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority6_Bps']))

    @property
    def BandwidthPriority6_BpsTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 6 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority6_BpsTo']))

    @property
    def BandwidthPriority7_Bps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 7 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority7_Bps']))

    @property
    def BandwidthPriority7_BpsTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 7 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BandwidthPriority7_BpsTo']))

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
    def ExtAdminGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext Admin Group
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExtAdminGroup']))

    @property
    def ExtAdminGroupLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext Admin Group Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExtAdminGroupLength']))

    @property
    def ExtAdminGroupLengthTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext Admin Group Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExtAdminGroupLengthTo']))

    @property
    def ExtAdminGroupTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext Admin Group
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExtAdminGroupTo']))

    @property
    def LFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set to False, all link attributes will be advertised as sub-sub-tlv of sub tlv Application Specific Link Attributes sub-TLV (Type 16) of TLV 22,23,141,222 and 223 If true, then all link attributes will be advertised as sub-TLV of TLV 22,23,141,222 and 223.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LFlag']))

    @property
    def MaxBandwidth_Bps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Bandwidth (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxBandwidth_Bps']))

    @property
    def MaxBandwidth_BpsTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Bandwidth (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxBandwidth_BpsTo']))

    @property
    def MaxReservableBandwidth_Bps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Reservable Bandwidth (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxReservableBandwidth_Bps']))

    @property
    def MaxReservableBandwidth_BpsTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Reservable Bandwidth (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxReservableBandwidth_BpsTo']))

    @property
    def MetricLevel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Metric Level
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MetricLevel']))

    @property
    def MetricLevelTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Metric Level
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MetricLevelTo']))

    @property
    def MinMaxUniDirLinkDelayABit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MinMaxUniDirLinkDelayABit']))

    @property
    def MinMaxUniDirLinkDelayABitTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MinMaxUniDirLinkDelayABitTo']))

    @property
    def MtApplicabilityForIPv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multi-Topology Applicability for IPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MtApplicabilityForIPv6']))

    @property
    def MtIdTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MTID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MtIdTo']))

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
    def StdAppType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Standard Appplication Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StdAppType']))

    @property
    def UniDirAvailableBw(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Available BW (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UniDirAvailableBw']))

    @property
    def UniDirAvailableBwTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Available BW (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UniDirAvailableBwTo']))

    @property
    def UniDirLinkDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Delay (us)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UniDirLinkDelay']))

    @property
    def UniDirLinkDelayABit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UniDirLinkDelayABit']))

    @property
    def UniDirLinkDelayABitTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UniDirLinkDelayABitTo']))

    @property
    def UniDirLinkDelayTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Delay (us)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UniDirLinkDelayTo']))

    @property
    def UniDirLinkDelayVariation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Delay Variation(us)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UniDirLinkDelayVariation']))

    @property
    def UniDirLinkDelayVariationTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Delay Variation(us)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UniDirLinkDelayVariationTo']))

    @property
    def UniDirLinkLoss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Link Loss(%)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UniDirLinkLoss']))

    @property
    def UniDirLinkLossABit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UniDirLinkLossABit']))

    @property
    def UniDirLinkLossABitTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UniDirLinkLossABitTo']))

    @property
    def UniDirLinkLossTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Link Loss(%)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UniDirLinkLossTo']))

    @property
    def UniDirLinkMaxDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Delay(us)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UniDirLinkMaxDelay']))

    @property
    def UniDirLinkMaxDelayTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Delay(us)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UniDirLinkMaxDelayTo']))

    @property
    def UniDirLinkMinDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Minimum Delay (us)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UniDirLinkMinDelay']))

    @property
    def UniDirLinkMinDelayTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Minimum Delay (us)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UniDirLinkMinDelayTo']))

    @property
    def UniDirResidualBw(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Residual BW (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UniDirResidualBw']))

    @property
    def UniDirResidualBwTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Residual BW (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UniDirResidualBwTo']))

    @property
    def UniDirUtilizedBw(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Utilized BW (Bytes/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UniDirUtilizedBw']))

    @property
    def UniDirUtilizedBwTo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Utilized BW (Bytes/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UniDirUtilizedBwTo']))

    @property
    def UserDefAppBm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User Defined Application BM
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UserDefAppBm']))

    @property
    def UserDefAppBmLen(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User Defined Application BM Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UserDefAppBmLen']))

    def update(self, Name=None):
        """Updates isisPseudoTraffEngProfile resource on the server.

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

    def get_device_ids(self, PortNames=None, Active=None, ActiveTo=None, AdministratorGroup=None, AdministratorGroupTo=None, AdvAppSpecificTraffic=None, AdvMinMaxUniDiLinkDelay=None, AdvMinMaxUniDiLinkDelayTo=None, AdvUniDirAvailableBw=None, AdvUniDirAvailableBwTo=None, AdvUniDirDelayVariation=None, AdvUniDirDelayVariationTo=None, AdvUniDirLinkLoss=None, AdvUniDirLinkLossTo=None, AdvUniDirResidualBw=None, AdvUniDirResidualBwTo=None, AdvUniDirUtilizedBw=None, AdvUniDirUtilizedBwTo=None, AdvertiseExtAdminGroup=None, AdvertiseExtAdminGroupTo=None, AdvertiseUniDiLinkDelay=None, AdvertiseUniDiLinkDelayTo=None, BandwidthPriority0_Bps=None, BandwidthPriority0_BpsTo=None, BandwidthPriority1_Bps=None, BandwidthPriority1_BpsTo=None, BandwidthPriority2_Bps=None, BandwidthPriority2_BpsTo=None, BandwidthPriority3_Bps=None, BandwidthPriority3_BpsTo=None, BandwidthPriority4_Bps=None, BandwidthPriority4_BpsTo=None, BandwidthPriority5_Bps=None, BandwidthPriority5_BpsTo=None, BandwidthPriority6_Bps=None, BandwidthPriority6_BpsTo=None, BandwidthPriority7_Bps=None, BandwidthPriority7_BpsTo=None, ExtAdminGroup=None, ExtAdminGroupLength=None, ExtAdminGroupLengthTo=None, ExtAdminGroupTo=None, LFlag=None, MaxBandwidth_Bps=None, MaxBandwidth_BpsTo=None, MaxReservableBandwidth_Bps=None, MaxReservableBandwidth_BpsTo=None, MetricLevel=None, MetricLevelTo=None, MinMaxUniDirLinkDelayABit=None, MinMaxUniDirLinkDelayABitTo=None, MtApplicabilityForIPv6=None, MtIdTo=None, StdAppType=None, UniDirAvailableBw=None, UniDirAvailableBwTo=None, UniDirLinkDelay=None, UniDirLinkDelayABit=None, UniDirLinkDelayABitTo=None, UniDirLinkDelayTo=None, UniDirLinkDelayVariation=None, UniDirLinkDelayVariationTo=None, UniDirLinkLoss=None, UniDirLinkLossABit=None, UniDirLinkLossABitTo=None, UniDirLinkLossTo=None, UniDirLinkMaxDelay=None, UniDirLinkMaxDelayTo=None, UniDirLinkMinDelay=None, UniDirLinkMinDelayTo=None, UniDirResidualBw=None, UniDirResidualBwTo=None, UniDirUtilizedBw=None, UniDirUtilizedBwTo=None, UserDefAppBm=None, UserDefAppBmLen=None):
        """Base class infrastructure that gets a list of isisPseudoTraffEngProfile device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - ActiveTo (str): optional regex of activeTo
        - AdministratorGroup (str): optional regex of administratorGroup
        - AdministratorGroupTo (str): optional regex of administratorGroupTo
        - AdvAppSpecificTraffic (str): optional regex of advAppSpecificTraffic
        - AdvMinMaxUniDiLinkDelay (str): optional regex of advMinMaxUniDiLinkDelay
        - AdvMinMaxUniDiLinkDelayTo (str): optional regex of advMinMaxUniDiLinkDelayTo
        - AdvUniDirAvailableBw (str): optional regex of advUniDirAvailableBw
        - AdvUniDirAvailableBwTo (str): optional regex of advUniDirAvailableBwTo
        - AdvUniDirDelayVariation (str): optional regex of advUniDirDelayVariation
        - AdvUniDirDelayVariationTo (str): optional regex of advUniDirDelayVariationTo
        - AdvUniDirLinkLoss (str): optional regex of advUniDirLinkLoss
        - AdvUniDirLinkLossTo (str): optional regex of advUniDirLinkLossTo
        - AdvUniDirResidualBw (str): optional regex of advUniDirResidualBw
        - AdvUniDirResidualBwTo (str): optional regex of advUniDirResidualBwTo
        - AdvUniDirUtilizedBw (str): optional regex of advUniDirUtilizedBw
        - AdvUniDirUtilizedBwTo (str): optional regex of advUniDirUtilizedBwTo
        - AdvertiseExtAdminGroup (str): optional regex of advertiseExtAdminGroup
        - AdvertiseExtAdminGroupTo (str): optional regex of advertiseExtAdminGroupTo
        - AdvertiseUniDiLinkDelay (str): optional regex of advertiseUniDiLinkDelay
        - AdvertiseUniDiLinkDelayTo (str): optional regex of advertiseUniDiLinkDelayTo
        - BandwidthPriority0_Bps (str): optional regex of bandwidthPriority0_Bps
        - BandwidthPriority0_BpsTo (str): optional regex of bandwidthPriority0_BpsTo
        - BandwidthPriority1_Bps (str): optional regex of bandwidthPriority1_Bps
        - BandwidthPriority1_BpsTo (str): optional regex of bandwidthPriority1_BpsTo
        - BandwidthPriority2_Bps (str): optional regex of bandwidthPriority2_Bps
        - BandwidthPriority2_BpsTo (str): optional regex of bandwidthPriority2_BpsTo
        - BandwidthPriority3_Bps (str): optional regex of bandwidthPriority3_Bps
        - BandwidthPriority3_BpsTo (str): optional regex of bandwidthPriority3_BpsTo
        - BandwidthPriority4_Bps (str): optional regex of bandwidthPriority4_Bps
        - BandwidthPriority4_BpsTo (str): optional regex of bandwidthPriority4_BpsTo
        - BandwidthPriority5_Bps (str): optional regex of bandwidthPriority5_Bps
        - BandwidthPriority5_BpsTo (str): optional regex of bandwidthPriority5_BpsTo
        - BandwidthPriority6_Bps (str): optional regex of bandwidthPriority6_Bps
        - BandwidthPriority6_BpsTo (str): optional regex of bandwidthPriority6_BpsTo
        - BandwidthPriority7_Bps (str): optional regex of bandwidthPriority7_Bps
        - BandwidthPriority7_BpsTo (str): optional regex of bandwidthPriority7_BpsTo
        - ExtAdminGroup (str): optional regex of extAdminGroup
        - ExtAdminGroupLength (str): optional regex of extAdminGroupLength
        - ExtAdminGroupLengthTo (str): optional regex of extAdminGroupLengthTo
        - ExtAdminGroupTo (str): optional regex of extAdminGroupTo
        - LFlag (str): optional regex of lFlag
        - MaxBandwidth_Bps (str): optional regex of maxBandwidth_Bps
        - MaxBandwidth_BpsTo (str): optional regex of maxBandwidth_BpsTo
        - MaxReservableBandwidth_Bps (str): optional regex of maxReservableBandwidth_Bps
        - MaxReservableBandwidth_BpsTo (str): optional regex of maxReservableBandwidth_BpsTo
        - MetricLevel (str): optional regex of metricLevel
        - MetricLevelTo (str): optional regex of metricLevelTo
        - MinMaxUniDirLinkDelayABit (str): optional regex of minMaxUniDirLinkDelayABit
        - MinMaxUniDirLinkDelayABitTo (str): optional regex of minMaxUniDirLinkDelayABitTo
        - MtApplicabilityForIPv6 (str): optional regex of mtApplicabilityForIPv6
        - MtIdTo (str): optional regex of mtIdTo
        - StdAppType (str): optional regex of stdAppType
        - UniDirAvailableBw (str): optional regex of uniDirAvailableBw
        - UniDirAvailableBwTo (str): optional regex of uniDirAvailableBwTo
        - UniDirLinkDelay (str): optional regex of uniDirLinkDelay
        - UniDirLinkDelayABit (str): optional regex of uniDirLinkDelayABit
        - UniDirLinkDelayABitTo (str): optional regex of uniDirLinkDelayABitTo
        - UniDirLinkDelayTo (str): optional regex of uniDirLinkDelayTo
        - UniDirLinkDelayVariation (str): optional regex of uniDirLinkDelayVariation
        - UniDirLinkDelayVariationTo (str): optional regex of uniDirLinkDelayVariationTo
        - UniDirLinkLoss (str): optional regex of uniDirLinkLoss
        - UniDirLinkLossABit (str): optional regex of uniDirLinkLossABit
        - UniDirLinkLossABitTo (str): optional regex of uniDirLinkLossABitTo
        - UniDirLinkLossTo (str): optional regex of uniDirLinkLossTo
        - UniDirLinkMaxDelay (str): optional regex of uniDirLinkMaxDelay
        - UniDirLinkMaxDelayTo (str): optional regex of uniDirLinkMaxDelayTo
        - UniDirLinkMinDelay (str): optional regex of uniDirLinkMinDelay
        - UniDirLinkMinDelayTo (str): optional regex of uniDirLinkMinDelayTo
        - UniDirResidualBw (str): optional regex of uniDirResidualBw
        - UniDirResidualBwTo (str): optional regex of uniDirResidualBwTo
        - UniDirUtilizedBw (str): optional regex of uniDirUtilizedBw
        - UniDirUtilizedBwTo (str): optional regex of uniDirUtilizedBwTo
        - UserDefAppBm (str): optional regex of userDefAppBm
        - UserDefAppBmLen (str): optional regex of userDefAppBmLen

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Abort(self):
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('abort', payload=payload, response_object=None)

    def Start(self):
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('stop', payload=payload, response_object=None)
