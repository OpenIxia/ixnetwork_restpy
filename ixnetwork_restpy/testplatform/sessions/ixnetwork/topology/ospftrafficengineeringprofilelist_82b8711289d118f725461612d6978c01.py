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


class OspfTrafficEngineeringProfileList(Base):
    """OSPF Traffic Engineering Profiles
    The OspfTrafficEngineeringProfileList class encapsulates a required ospfTrafficEngineeringProfileList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "ospfTrafficEngineeringProfileList"
    _SDM_ATT_MAP = {
        "Active": "active",
        "AdministratorGroup": "administratorGroup",
        "AdvMinMaxUniDiLinkDelay": "advMinMaxUniDiLinkDelay",
        "AdvUniDirAvailableBw": "advUniDirAvailableBw",
        "AdvUniDirDelayVariation": "advUniDirDelayVariation",
        "AdvUniDirLinkLoss": "advUniDirLinkLoss",
        "AdvUniDirResidualBw": "advUniDirResidualBw",
        "AdvUniDirUtilizedBw": "advUniDirUtilizedBw",
        "AdvertiseExtAdminGroup": "advertiseExtAdminGroup",
        "AdvertiseUniDiLinkDelay": "advertiseUniDiLinkDelay",
        "BandwidthPriority0": "bandwidthPriority0",
        "BandwidthPriority1": "bandwidthPriority1",
        "BandwidthPriority2": "bandwidthPriority2",
        "BandwidthPriority3": "bandwidthPriority3",
        "BandwidthPriority4": "bandwidthPriority4",
        "BandwidthPriority5": "bandwidthPriority5",
        "BandwidthPriority6": "bandwidthPriority6",
        "BandwidthPriority7": "bandwidthPriority7",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "ExtAdminGroup": "extAdminGroup",
        "ExtAdminGroupLength": "extAdminGroupLength",
        "MaxBandwidth": "maxBandwidth",
        "MaxReservableBandwidth": "maxReservableBandwidth",
        "MetricLevel": "metricLevel",
        "MinMaxUniDirLinkDelayABit": "minMaxUniDirLinkDelayABit",
        "Name": "name",
        "UniDirAvailableBw": "uniDirAvailableBw",
        "UniDirLinkDelay": "uniDirLinkDelay",
        "UniDirLinkDelayABit": "uniDirLinkDelayABit",
        "UniDirLinkDelayVariation": "uniDirLinkDelayVariation",
        "UniDirLinkLoss": "uniDirLinkLoss",
        "UniDirLinkLossABit": "uniDirLinkLossABit",
        "UniDirLinkMaxDelay": "uniDirLinkMaxDelay",
        "UniDirLinkMinDelay": "uniDirLinkMinDelay",
        "UniDirResidualBw": "uniDirResidualBw",
        "UniDirUtilizedBw": "uniDirUtilizedBw",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(OspfTrafficEngineeringProfileList, self).__init__(parent, list_op)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Active"]))

    @property
    def AdministratorGroup(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Administrator Group
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdministratorGroup"])
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
    def AdvertiseExtAdminGroup(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Ext Admin Group
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
    def BandwidthPriority0(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 0 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority0"])
        )

    @property
    def BandwidthPriority1(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 1 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority1"])
        )

    @property
    def BandwidthPriority2(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 2 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority2"])
        )

    @property
    def BandwidthPriority3(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 3 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority3"])
        )

    @property
    def BandwidthPriority4(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 4 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority4"])
        )

    @property
    def BandwidthPriority5(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 5 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority5"])
        )

    @property
    def BandwidthPriority6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 6 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority6"])
        )

    @property
    def BandwidthPriority7(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 7 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority7"])
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
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext Admin Group
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ExtAdminGroup"]))

    @property
    def ExtAdminGroupLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ext Admin Group Length
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
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Bandwidth (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxBandwidth"]))

    @property
    def MaxReservableBandwidth(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Reservable Bandwidth (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxReservableBandwidth"])
        )

    @property
    def MetricLevel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TE Metric Level
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MetricLevel"]))

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

    def update(self, Name=None):
        # type: (str) -> OspfTrafficEngineeringProfileList
        """Updates ospfTrafficEngineeringProfileList resource on the server.

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
        # type: (int, str, str) -> OspfTrafficEngineeringProfileList
        """Finds and retrieves ospfTrafficEngineeringProfileList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ospfTrafficEngineeringProfileList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ospfTrafficEngineeringProfileList resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching ospfTrafficEngineeringProfileList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ospfTrafficEngineeringProfileList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ospfTrafficEngineeringProfileList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

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

    def get_device_ids(
        self,
        PortNames=None,
        Active=None,
        AdministratorGroup=None,
        AdvMinMaxUniDiLinkDelay=None,
        AdvUniDirAvailableBw=None,
        AdvUniDirDelayVariation=None,
        AdvUniDirLinkLoss=None,
        AdvUniDirResidualBw=None,
        AdvUniDirUtilizedBw=None,
        AdvertiseExtAdminGroup=None,
        AdvertiseUniDiLinkDelay=None,
        BandwidthPriority0=None,
        BandwidthPriority1=None,
        BandwidthPriority2=None,
        BandwidthPriority3=None,
        BandwidthPriority4=None,
        BandwidthPriority5=None,
        BandwidthPriority6=None,
        BandwidthPriority7=None,
        ExtAdminGroup=None,
        ExtAdminGroupLength=None,
        MaxBandwidth=None,
        MaxReservableBandwidth=None,
        MetricLevel=None,
        MinMaxUniDirLinkDelayABit=None,
        UniDirAvailableBw=None,
        UniDirLinkDelay=None,
        UniDirLinkDelayABit=None,
        UniDirLinkDelayVariation=None,
        UniDirLinkLoss=None,
        UniDirLinkLossABit=None,
        UniDirLinkMaxDelay=None,
        UniDirLinkMinDelay=None,
        UniDirResidualBw=None,
        UniDirUtilizedBw=None,
    ):
        """Base class infrastructure that gets a list of ospfTrafficEngineeringProfileList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AdministratorGroup (str): optional regex of administratorGroup
        - AdvMinMaxUniDiLinkDelay (str): optional regex of advMinMaxUniDiLinkDelay
        - AdvUniDirAvailableBw (str): optional regex of advUniDirAvailableBw
        - AdvUniDirDelayVariation (str): optional regex of advUniDirDelayVariation
        - AdvUniDirLinkLoss (str): optional regex of advUniDirLinkLoss
        - AdvUniDirResidualBw (str): optional regex of advUniDirResidualBw
        - AdvUniDirUtilizedBw (str): optional regex of advUniDirUtilizedBw
        - AdvertiseExtAdminGroup (str): optional regex of advertiseExtAdminGroup
        - AdvertiseUniDiLinkDelay (str): optional regex of advertiseUniDiLinkDelay
        - BandwidthPriority0 (str): optional regex of bandwidthPriority0
        - BandwidthPriority1 (str): optional regex of bandwidthPriority1
        - BandwidthPriority2 (str): optional regex of bandwidthPriority2
        - BandwidthPriority3 (str): optional regex of bandwidthPriority3
        - BandwidthPriority4 (str): optional regex of bandwidthPriority4
        - BandwidthPriority5 (str): optional regex of bandwidthPriority5
        - BandwidthPriority6 (str): optional regex of bandwidthPriority6
        - BandwidthPriority7 (str): optional regex of bandwidthPriority7
        - ExtAdminGroup (str): optional regex of extAdminGroup
        - ExtAdminGroupLength (str): optional regex of extAdminGroupLength
        - MaxBandwidth (str): optional regex of maxBandwidth
        - MaxReservableBandwidth (str): optional regex of maxReservableBandwidth
        - MetricLevel (str): optional regex of metricLevel
        - MinMaxUniDirLinkDelayABit (str): optional regex of minMaxUniDirLinkDelayABit
        - UniDirAvailableBw (str): optional regex of uniDirAvailableBw
        - UniDirLinkDelay (str): optional regex of uniDirLinkDelay
        - UniDirLinkDelayABit (str): optional regex of uniDirLinkDelayABit
        - UniDirLinkDelayVariation (str): optional regex of uniDirLinkDelayVariation
        - UniDirLinkLoss (str): optional regex of uniDirLinkLoss
        - UniDirLinkLossABit (str): optional regex of uniDirLinkLossABit
        - UniDirLinkMaxDelay (str): optional regex of uniDirLinkMaxDelay
        - UniDirLinkMinDelay (str): optional regex of uniDirLinkMinDelay
        - UniDirResidualBw (str): optional regex of uniDirResidualBw
        - UniDirUtilizedBw (str): optional regex of uniDirUtilizedBw

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
