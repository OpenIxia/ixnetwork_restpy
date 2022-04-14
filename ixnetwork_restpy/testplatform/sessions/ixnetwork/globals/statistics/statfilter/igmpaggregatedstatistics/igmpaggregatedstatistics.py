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


class IgmpAggregatedStatistics(Base):
    """Represents stats of IGMP Aggregated Statistics
    The IgmpAggregatedStatistics class encapsulates a required igmpAggregatedStatistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "igmpAggregatedStatistics"
    _SDM_ATT_MAP = {
        "GeneralQueriesRx": "generalQueriesRx",
        "GrpSpecificQueriesRx": "grpSpecificQueriesRx",
        "HostInvalidPacketsRx": "hostInvalidPacketsRx",
        "HostTotalFramesRx": "hostTotalFramesRx",
        "HostTotalFramesTx": "hostTotalFramesTx",
        "Hostv1MembershipRptsRx": "hostv1MembershipRptsRx",
        "Hostv2MembershipRptsRx": "hostv2MembershipRptsRx",
        "PortName": "portName",
        "V1MembershipRptsTx": "v1MembershipRptsTx",
        "V2LeaveTx": "v2LeaveTx",
        "V2MembershipRptsTx": "v2MembershipRptsTx",
        "V3GrpAndSrcSpecificQueriesRx": "v3GrpAndSrcSpecificQueriesRx",
        "V3MembershipRptsTx": "v3MembershipRptsTx",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(IgmpAggregatedStatistics, self).__init__(parent, list_op)

    @property
    def GeneralQueriesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: General Queries Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GeneralQueriesRx"])

    @GeneralQueriesRx.setter
    def GeneralQueriesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GeneralQueriesRx"], value)

    @property
    def GrpSpecificQueriesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Grp. Specific Queries Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GrpSpecificQueriesRx"])

    @GrpSpecificQueriesRx.setter
    def GrpSpecificQueriesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GrpSpecificQueriesRx"], value)

    @property
    def HostInvalidPacketsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Host Invalid Packets Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["HostInvalidPacketsRx"])

    @HostInvalidPacketsRx.setter
    def HostInvalidPacketsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HostInvalidPacketsRx"], value)

    @property
    def HostTotalFramesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Host Total Frames Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["HostTotalFramesRx"])

    @HostTotalFramesRx.setter
    def HostTotalFramesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HostTotalFramesRx"], value)

    @property
    def HostTotalFramesTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Host Total Frames Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["HostTotalFramesTx"])

    @HostTotalFramesTx.setter
    def HostTotalFramesTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HostTotalFramesTx"], value)

    @property
    def Hostv1MembershipRptsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Host v1 Membership Rpts. Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["Hostv1MembershipRptsRx"])

    @Hostv1MembershipRptsRx.setter
    def Hostv1MembershipRptsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Hostv1MembershipRptsRx"], value)

    @property
    def Hostv2MembershipRptsRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Host v2 Membership Rpts. Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["Hostv2MembershipRptsRx"])

    @Hostv2MembershipRptsRx.setter
    def Hostv2MembershipRptsRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Hostv2MembershipRptsRx"], value)

    @property
    def PortName(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Port Name
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortName"])

    @PortName.setter
    def PortName(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PortName"], value)

    @property
    def V1MembershipRptsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: v1 Membership Rpts. Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["V1MembershipRptsTx"])

    @V1MembershipRptsTx.setter
    def V1MembershipRptsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["V1MembershipRptsTx"], value)

    @property
    def V2LeaveTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: v2 Leave Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["V2LeaveTx"])

    @V2LeaveTx.setter
    def V2LeaveTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["V2LeaveTx"], value)

    @property
    def V2MembershipRptsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: v2 Membership Rpts. Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["V2MembershipRptsTx"])

    @V2MembershipRptsTx.setter
    def V2MembershipRptsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["V2MembershipRptsTx"], value)

    @property
    def V3GrpAndSrcSpecificQueriesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: v3 Grp. & Src. Specific Queries Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["V3GrpAndSrcSpecificQueriesRx"])

    @V3GrpAndSrcSpecificQueriesRx.setter
    def V3GrpAndSrcSpecificQueriesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["V3GrpAndSrcSpecificQueriesRx"], value)

    @property
    def V3MembershipRptsTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: v3 Membership Rpts. Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["V3MembershipRptsTx"])

    @V3MembershipRptsTx.setter
    def V3MembershipRptsTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["V3MembershipRptsTx"], value)

    def update(
        self,
        GeneralQueriesRx=None,
        GrpSpecificQueriesRx=None,
        HostInvalidPacketsRx=None,
        HostTotalFramesRx=None,
        HostTotalFramesTx=None,
        Hostv1MembershipRptsRx=None,
        Hostv2MembershipRptsRx=None,
        PortName=None,
        V1MembershipRptsTx=None,
        V2LeaveTx=None,
        V2MembershipRptsTx=None,
        V3GrpAndSrcSpecificQueriesRx=None,
        V3MembershipRptsTx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> IgmpAggregatedStatistics
        """Updates igmpAggregatedStatistics resource on the server.

        Args
        ----
        - GeneralQueriesRx (bool): General Queries Rx
        - GrpSpecificQueriesRx (bool): Grp. Specific Queries Rx
        - HostInvalidPacketsRx (bool): Host Invalid Packets Rx
        - HostTotalFramesRx (bool): Host Total Frames Rx
        - HostTotalFramesTx (bool): Host Total Frames Tx
        - Hostv1MembershipRptsRx (bool): Host v1 Membership Rpts. Rx
        - Hostv2MembershipRptsRx (bool): Host v2 Membership Rpts. Rx
        - PortName (bool): Port Name
        - V1MembershipRptsTx (bool): v1 Membership Rpts. Tx
        - V2LeaveTx (bool): v2 Leave Tx
        - V2MembershipRptsTx (bool): v2 Membership Rpts. Tx
        - V3GrpAndSrcSpecificQueriesRx (bool): v3 Grp. & Src. Specific Queries Rx
        - V3MembershipRptsTx (bool): v3 Membership Rpts. Tx

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        GeneralQueriesRx=None,
        GrpSpecificQueriesRx=None,
        HostInvalidPacketsRx=None,
        HostTotalFramesRx=None,
        HostTotalFramesTx=None,
        Hostv1MembershipRptsRx=None,
        Hostv2MembershipRptsRx=None,
        PortName=None,
        V1MembershipRptsTx=None,
        V2LeaveTx=None,
        V2MembershipRptsTx=None,
        V3GrpAndSrcSpecificQueriesRx=None,
        V3MembershipRptsTx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> IgmpAggregatedStatistics
        """Finds and retrieves igmpAggregatedStatistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve igmpAggregatedStatistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all igmpAggregatedStatistics resources from the server.

        Args
        ----
        - GeneralQueriesRx (bool): General Queries Rx
        - GrpSpecificQueriesRx (bool): Grp. Specific Queries Rx
        - HostInvalidPacketsRx (bool): Host Invalid Packets Rx
        - HostTotalFramesRx (bool): Host Total Frames Rx
        - HostTotalFramesTx (bool): Host Total Frames Tx
        - Hostv1MembershipRptsRx (bool): Host v1 Membership Rpts. Rx
        - Hostv2MembershipRptsRx (bool): Host v2 Membership Rpts. Rx
        - PortName (bool): Port Name
        - V1MembershipRptsTx (bool): v1 Membership Rpts. Tx
        - V2LeaveTx (bool): v2 Leave Tx
        - V2MembershipRptsTx (bool): v2 Membership Rpts. Tx
        - V3GrpAndSrcSpecificQueriesRx (bool): v3 Grp. & Src. Specific Queries Rx
        - V3MembershipRptsTx (bool): v3 Membership Rpts. Tx

        Returns
        -------
        - self: This instance with matching igmpAggregatedStatistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of igmpAggregatedStatistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the igmpAggregatedStatistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
