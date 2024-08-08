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
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class OspfPseudoTrafficEngineeringProfileList(Base):
    """OSPF Traffic Engineering Profiles
    The OspfPseudoTrafficEngineeringProfileList class encapsulates a required ospfPseudoTrafficEngineeringProfileList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "ospfPseudoTrafficEngineeringProfileList"
    _SDM_ATT_MAP = {
        "Active": "active",
        "ActiveTo": "activeTo",
        "AdministratorGroup": "administratorGroup",
        "AdministratorGroupTo": "administratorGroupTo",
        "AdvMinMaxUniDiLinkDelay": "advMinMaxUniDiLinkDelay",
        "AdvMinMaxUniDiLinkDelayTo": "advMinMaxUniDiLinkDelayTo",
        "AdvUniDirAvailableBw": "advUniDirAvailableBw",
        "AdvUniDirAvailableBwTo": "advUniDirAvailableBwTo",
        "AdvUniDirDelayVariation": "advUniDirDelayVariation",
        "AdvUniDirDelayVariationTo": "advUniDirDelayVariationTo",
        "AdvUniDirLinkLoss": "advUniDirLinkLoss",
        "AdvUniDirLinkLossTo": "advUniDirLinkLossTo",
        "AdvUniDirResidualBw": "advUniDirResidualBw",
        "AdvUniDirResidualBwTo": "advUniDirResidualBwTo",
        "AdvUniDirUtilizedBw": "advUniDirUtilizedBw",
        "AdvUniDirUtilizedBwTo": "advUniDirUtilizedBwTo",
        "AdvertiseExtAdminGroup": "advertiseExtAdminGroup",
        "AdvertiseUniDiLinkDelay": "advertiseUniDiLinkDelay",
        "AdvertiseUniDiLinkDelayTo": "advertiseUniDiLinkDelayTo",
        "BandwidthPriority0": "bandwidthPriority0",
        "BandwidthPriority0To": "bandwidthPriority0To",
        "BandwidthPriority1": "bandwidthPriority1",
        "BandwidthPriority1To": "bandwidthPriority1To",
        "BandwidthPriority2": "bandwidthPriority2",
        "BandwidthPriority2To": "bandwidthPriority2To",
        "BandwidthPriority3": "bandwidthPriority3",
        "BandwidthPriority3To": "bandwidthPriority3To",
        "BandwidthPriority4": "bandwidthPriority4",
        "BandwidthPriority4To": "bandwidthPriority4To",
        "BandwidthPriority5": "bandwidthPriority5",
        "BandwidthPriority5To": "bandwidthPriority5To",
        "BandwidthPriority6": "bandwidthPriority6",
        "BandwidthPriority6To": "bandwidthPriority6To",
        "BandwidthPriority7": "bandwidthPriority7",
        "BandwidthPriority7To": "bandwidthPriority7To",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "ExtAdminGroup": "extAdminGroup",
        "ExtAdminGroupLength": "extAdminGroupLength",
        "MaxBandwidth": "maxBandwidth",
        "MaxBandwidthTo": "maxBandwidthTo",
        "MaxReservableBandwidth": "maxReservableBandwidth",
        "MaxReservableBandwidthTo": "maxReservableBandwidthTo",
        "MetricLevel": "metricLevel",
        "MetricLevelTo": "metricLevelTo",
        "MinMaxUniDirLinkDelayABit": "minMaxUniDirLinkDelayABit",
        "MinMaxUniDirLinkDelayABitTo": "minMaxUniDirLinkDelayABitTo",
        "Name": "name",
        "UniDirAvailableBw": "uniDirAvailableBw",
        "UniDirAvailableBwTo": "uniDirAvailableBwTo",
        "UniDirLinkDelay": "uniDirLinkDelay",
        "UniDirLinkDelayABit": "uniDirLinkDelayABit",
        "UniDirLinkDelayABitTo": "uniDirLinkDelayABitTo",
        "UniDirLinkDelayTo": "uniDirLinkDelayTo",
        "UniDirLinkDelayVariation": "uniDirLinkDelayVariation",
        "UniDirLinkDelayVariationTo": "uniDirLinkDelayVariationTo",
        "UniDirLinkLoss": "uniDirLinkLoss",
        "UniDirLinkLossABit": "uniDirLinkLossABit",
        "UniDirLinkLossABitTo": "uniDirLinkLossABitTo",
        "UniDirLinkLossTo": "uniDirLinkLossTo",
        "UniDirLinkMaxDelay": "uniDirLinkMaxDelay",
        "UniDirLinkMaxDelayTo": "uniDirLinkMaxDelayTo",
        "UniDirLinkMinDelay": "uniDirLinkMinDelay",
        "UniDirLinkMinDelayTo": "uniDirLinkMinDelayTo",
        "UniDirResidualBw": "uniDirResidualBw",
        "UniDirResidualBwTo": "uniDirResidualBwTo",
        "UniDirUtilizedBw": "uniDirUtilizedBw",
        "UniDirUtilizedBwTo": "uniDirUtilizedBwTo",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(OspfPseudoTrafficEngineeringProfileList, self).__init__(parent, list_op)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Active"]))

    @property
    def ActiveTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TE To-Node Enable/Disable.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ActiveTo"]))

    @property
    def AdministratorGroup(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Administrator Group.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdministratorGroup"])
        )

    @property
    def AdministratorGroupTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Administrator Group.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdministratorGroupTo"])
        )

    @property
    def AdvMinMaxUniDiLinkDelay(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Min/Max Uni-Directional Link Delay Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvMinMaxUniDiLinkDelay"])
        )

    @property
    def AdvMinMaxUniDiLinkDelayTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Min/Max Uni-Directional Link Delay Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvMinMaxUniDiLinkDelayTo"])
        )

    @property
    def AdvUniDirAvailableBw(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Available Bandwidth Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvUniDirAvailableBw"])
        )

    @property
    def AdvUniDirAvailableBwTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Available Bandwidth Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvUniDirAvailableBwTo"])
        )

    @property
    def AdvUniDirDelayVariation(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Delay Variation Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvUniDirDelayVariation"])
        )

    @property
    def AdvUniDirDelayVariationTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Delay Variation Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvUniDirDelayVariationTo"])
        )

    @property
    def AdvUniDirLinkLoss(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Link Loss Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvUniDirLinkLoss"])
        )

    @property
    def AdvUniDirLinkLossTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Link Loss Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvUniDirLinkLossTo"])
        )

    @property
    def AdvUniDirResidualBw(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Residual Bandwidth Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvUniDirResidualBw"])
        )

    @property
    def AdvUniDirResidualBwTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Residual Bandwidth Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvUniDirResidualBwTo"])
        )

    @property
    def AdvUniDirUtilizedBw(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Utilized Bandwidth Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvUniDirUtilizedBw"])
        )

    @property
    def AdvUniDirUtilizedBwTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Utilized Bandwidth Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvUniDirUtilizedBwTo"])
        )

    @property
    def AdvertiseExtAdminGroup(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Advertise Ext Admin Group.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvertiseExtAdminGroup"])
        )

    @property
    def AdvertiseUniDiLinkDelay(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Link Delay Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvertiseUniDiLinkDelay"])
        )

    @property
    def AdvertiseUniDiLinkDelayTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Uni-Directional Link Delay Sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvertiseUniDiLinkDelayTo"])
        )

    @property
    def BandwidthPriority0(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Bandwidth for Priority 0 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority0"])
        )

    @property
    def BandwidthPriority0To(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 0 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority0To"])
        )

    @property
    def BandwidthPriority1(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Bandwidth for Priority 1 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority1"])
        )

    @property
    def BandwidthPriority1To(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 1 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority1To"])
        )

    @property
    def BandwidthPriority2(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Bandwidth for Priority 2 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority2"])
        )

    @property
    def BandwidthPriority2To(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 2 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority2To"])
        )

    @property
    def BandwidthPriority3(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Bandwidth for Priority 3 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority3"])
        )

    @property
    def BandwidthPriority3To(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 3 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority3To"])
        )

    @property
    def BandwidthPriority4(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Bandwidth for Priority 4 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority4"])
        )

    @property
    def BandwidthPriority4To(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 4 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority4To"])
        )

    @property
    def BandwidthPriority5(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Bandwidth for Priority 5 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority5"])
        )

    @property
    def BandwidthPriority5To(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 5 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority5To"])
        )

    @property
    def BandwidthPriority6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Bandwidth for Priority 6 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority6"])
        )

    @property
    def BandwidthPriority6To(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 6 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority6To"])
        )

    @property
    def BandwidthPriority7(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Bandwidth for Priority 7 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority7"])
        )

    @property
    def BandwidthPriority7To(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 7 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority7To"])
        )

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def ExtAdminGroup(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Ext Admin Group.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ExtAdminGroup"]))

    @property
    def ExtAdminGroupLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Ext Admin Group Length.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtAdminGroupLength"])
        )

    @property
    def MaxBandwidth(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Maximum Bandwidth (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxBandwidth"]))

    @property
    def MaxBandwidthTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Maximum Bandwidth (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxBandwidthTo"])
        )

    @property
    def MaxReservableBandwidth(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Maximum Reservable Bandwidth (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxReservableBandwidth"])
        )

    @property
    def MaxReservableBandwidthTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Maximum Reservable Bandwidth (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxReservableBandwidthTo"])
        )

    @property
    def MetricLevel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, TE Metric Level.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MetricLevel"]))

    @property
    def MetricLevelTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, TE Metric Level.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MetricLevelTo"]))

    @property
    def MinMaxUniDirLinkDelayABit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Anomalous Bit. Set whenthe measured value exceeds configured maximum threshold.Cleared otherwise.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MinMaxUniDirLinkDelayABit"])
        )

    @property
    def MinMaxUniDirLinkDelayABitTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Anomalous Bit. Set whenthe measured value exceeds configured maximum threshold.Cleared otherwise.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MinMaxUniDirLinkDelayABitTo"])
        )

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def UniDirAvailableBw(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Available Bandwidth on a link, forwardingadjacency, or bundled link with unitsof Bytes Per Second encoded in IEEE floating point format.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniDirAvailableBw"])
        )

    @property
    def UniDirAvailableBwTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Available Bandwidth on a link, forwardingadjacency, or bundled link with unitsof Bytes Per Second encoded in IEEE floating point format.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniDirAvailableBwTo"])
        )

    @property
    def UniDirLinkDelay(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Average Link Delay in microseconds (us)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniDirLinkDelay"])
        )

    @property
    def UniDirLinkDelayABit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Anomalous Bit. Set whenthe measured value exceeds configured maximum threshold.Cleared otherwise.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniDirLinkDelayABit"])
        )

    @property
    def UniDirLinkDelayABitTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Anomalous Bit. Set whenthe measured value exceeds configured maximum threshold.Cleared otherwise.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniDirLinkDelayABitTo"])
        )

    @property
    def UniDirLinkDelayTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Average Link Delay in microseconds (us)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniDirLinkDelayTo"])
        )

    @property
    def UniDirLinkDelayVariation(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Average Link Delay variation over aconfigurable interval in microseconds.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniDirLinkDelayVariation"])
        )

    @property
    def UniDirLinkDelayVariationTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Average Link Delay variation over aconfigurable interval in microseconds.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniDirLinkDelayVariationTo"])
        )

    @property
    def UniDirLinkLoss(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Link Packet loss as a percentage of thetotal traffic sent over a configurable interval.The basic unit is 0.000003%, where (2^24 - 2) is 50.331642%.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniDirLinkLoss"])
        )

    @property
    def UniDirLinkLossABit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Anomalous Bit. Set whenthe measured value exceeds configured maximum threshold.Cleared otherwise.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniDirLinkLossABit"])
        )

    @property
    def UniDirLinkLossABitTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Anomalous Bit. Set whenthe measured value exceeds configured maximum threshold.Cleared otherwise.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniDirLinkLossABitTo"])
        )

    @property
    def UniDirLinkLossTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Link Packet loss as a percentage of thetotal traffic sent over a configurable interval.The basic unit is 0.000003%, where (2^24 - 2) is 50.331642%.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniDirLinkLossTo"])
        )

    @property
    def UniDirLinkMaxDelay(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Measured Link Delay value inmicroseconds over a configurable interval.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniDirLinkMaxDelay"])
        )

    @property
    def UniDirLinkMaxDelayTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Measured Link Delay value inmicroseconds over a configurable interval.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniDirLinkMaxDelayTo"])
        )

    @property
    def UniDirLinkMinDelay(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Minimum measured link delay value inmicroseconds over a configurable interval.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniDirLinkMinDelay"])
        )

    @property
    def UniDirLinkMinDelayTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Minimum measured link delay value inmicroseconds over a configurable interval.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniDirLinkMinDelayTo"])
        )

    @property
    def UniDirResidualBw(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Residual Bandwidth on a link, forwardingadjacency, or bundled link with units of Bytes Per Secondencoded in IEEE floating point format.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniDirResidualBw"])
        )

    @property
    def UniDirResidualBwTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Residual Bandwidth on a link, forwardingadjacency, or bundled link with units of Bytes Per Secondencoded in IEEE floating point format.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniDirResidualBwTo"])
        )

    @property
    def UniDirUtilizedBw(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Bandwidth Utilization on a link, forwardingadjacency, or bundled link with unitsof Bytes Per Second encoded in IEEE floating-point format.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniDirUtilizedBw"])
        )

    @property
    def UniDirUtilizedBwTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Bandwidth Utilization on a link, forwardingadjacency, or bundled link with unitsof Bytes Per Second encoded in IEEE floating-point format.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniDirUtilizedBwTo"])
        )

    def update(self, Name=None):
        # type: (str) -> OspfPseudoTrafficEngineeringProfileList
        """Updates ospfPseudoTrafficEngineeringProfileList resource on the server.

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

    def find(self, Count=None, DescriptiveName=None, Name=None):
        # type: (int, str, str) -> OspfPseudoTrafficEngineeringProfileList
        """Finds and retrieves ospfPseudoTrafficEngineeringProfileList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ospfPseudoTrafficEngineeringProfileList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ospfPseudoTrafficEngineeringProfileList resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching ospfPseudoTrafficEngineeringProfileList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ospfPseudoTrafficEngineeringProfileList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ospfPseudoTrafficEngineeringProfileList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Abort(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        abort(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("abort", payload=payload, response_object=None)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, async_operation=bool)
        ----------------------------------------------
        - Arg2 (bool):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("addDeleteTags", payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("start", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stop", payload=payload, response_object=None)

    def get_device_ids(
        self,
        PortNames=None,
        Active=None,
        ActiveTo=None,
        AdministratorGroup=None,
        AdministratorGroupTo=None,
        AdvMinMaxUniDiLinkDelay=None,
        AdvMinMaxUniDiLinkDelayTo=None,
        AdvUniDirAvailableBw=None,
        AdvUniDirAvailableBwTo=None,
        AdvUniDirDelayVariation=None,
        AdvUniDirDelayVariationTo=None,
        AdvUniDirLinkLoss=None,
        AdvUniDirLinkLossTo=None,
        AdvUniDirResidualBw=None,
        AdvUniDirResidualBwTo=None,
        AdvUniDirUtilizedBw=None,
        AdvUniDirUtilizedBwTo=None,
        AdvertiseExtAdminGroup=None,
        AdvertiseUniDiLinkDelay=None,
        AdvertiseUniDiLinkDelayTo=None,
        BandwidthPriority0=None,
        BandwidthPriority0To=None,
        BandwidthPriority1=None,
        BandwidthPriority1To=None,
        BandwidthPriority2=None,
        BandwidthPriority2To=None,
        BandwidthPriority3=None,
        BandwidthPriority3To=None,
        BandwidthPriority4=None,
        BandwidthPriority4To=None,
        BandwidthPriority5=None,
        BandwidthPriority5To=None,
        BandwidthPriority6=None,
        BandwidthPriority6To=None,
        BandwidthPriority7=None,
        BandwidthPriority7To=None,
        ExtAdminGroup=None,
        ExtAdminGroupLength=None,
        MaxBandwidth=None,
        MaxBandwidthTo=None,
        MaxReservableBandwidth=None,
        MaxReservableBandwidthTo=None,
        MetricLevel=None,
        MetricLevelTo=None,
        MinMaxUniDirLinkDelayABit=None,
        MinMaxUniDirLinkDelayABitTo=None,
        UniDirAvailableBw=None,
        UniDirAvailableBwTo=None,
        UniDirLinkDelay=None,
        UniDirLinkDelayABit=None,
        UniDirLinkDelayABitTo=None,
        UniDirLinkDelayTo=None,
        UniDirLinkDelayVariation=None,
        UniDirLinkDelayVariationTo=None,
        UniDirLinkLoss=None,
        UniDirLinkLossABit=None,
        UniDirLinkLossABitTo=None,
        UniDirLinkLossTo=None,
        UniDirLinkMaxDelay=None,
        UniDirLinkMaxDelayTo=None,
        UniDirLinkMinDelay=None,
        UniDirLinkMinDelayTo=None,
        UniDirResidualBw=None,
        UniDirResidualBwTo=None,
        UniDirUtilizedBw=None,
        UniDirUtilizedBwTo=None,
    ):
        """Base class infrastructure that gets a list of ospfPseudoTrafficEngineeringProfileList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - ActiveTo (str): optional regex of activeTo
        - AdministratorGroup (str): optional regex of administratorGroup
        - AdministratorGroupTo (str): optional regex of administratorGroupTo
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
        - AdvertiseUniDiLinkDelay (str): optional regex of advertiseUniDiLinkDelay
        - AdvertiseUniDiLinkDelayTo (str): optional regex of advertiseUniDiLinkDelayTo
        - BandwidthPriority0 (str): optional regex of bandwidthPriority0
        - BandwidthPriority0To (str): optional regex of bandwidthPriority0To
        - BandwidthPriority1 (str): optional regex of bandwidthPriority1
        - BandwidthPriority1To (str): optional regex of bandwidthPriority1To
        - BandwidthPriority2 (str): optional regex of bandwidthPriority2
        - BandwidthPriority2To (str): optional regex of bandwidthPriority2To
        - BandwidthPriority3 (str): optional regex of bandwidthPriority3
        - BandwidthPriority3To (str): optional regex of bandwidthPriority3To
        - BandwidthPriority4 (str): optional regex of bandwidthPriority4
        - BandwidthPriority4To (str): optional regex of bandwidthPriority4To
        - BandwidthPriority5 (str): optional regex of bandwidthPriority5
        - BandwidthPriority5To (str): optional regex of bandwidthPriority5To
        - BandwidthPriority6 (str): optional regex of bandwidthPriority6
        - BandwidthPriority6To (str): optional regex of bandwidthPriority6To
        - BandwidthPriority7 (str): optional regex of bandwidthPriority7
        - BandwidthPriority7To (str): optional regex of bandwidthPriority7To
        - ExtAdminGroup (str): optional regex of extAdminGroup
        - ExtAdminGroupLength (str): optional regex of extAdminGroupLength
        - MaxBandwidth (str): optional regex of maxBandwidth
        - MaxBandwidthTo (str): optional regex of maxBandwidthTo
        - MaxReservableBandwidth (str): optional regex of maxReservableBandwidth
        - MaxReservableBandwidthTo (str): optional regex of maxReservableBandwidthTo
        - MetricLevel (str): optional regex of metricLevel
        - MetricLevelTo (str): optional regex of metricLevelTo
        - MinMaxUniDirLinkDelayABit (str): optional regex of minMaxUniDirLinkDelayABit
        - MinMaxUniDirLinkDelayABitTo (str): optional regex of minMaxUniDirLinkDelayABitTo
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

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
