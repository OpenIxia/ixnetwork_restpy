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


class MldAggregatedStatistics(Base):
    """Represents stats of MLD Aggregated Statistics
    The MldAggregatedStatistics class encapsulates a required mldAggregatedStatistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "mldAggregatedStatistics"
    _SDM_ATT_MAP = {
        "DoneTx": "doneTx",
        "GrpAndSrcSpecificQueriesRx": "grpAndSrcSpecificQueriesRx",
        "HostInvalidPacketsRx": "hostInvalidPacketsRx",
        "HostTotalFramesRx": "hostTotalFramesRx",
        "HostTotalFramesTx": "hostTotalFramesTx",
        "Hostv1MembershipRptsRx": "hostv1MembershipRptsRx",
        "PortName": "portName",
        "V1GeneralQueriesRx": "v1GeneralQueriesRx",
        "V1GrpSpecificQueriesRx": "v1GrpSpecificQueriesRx",
        "V1MembershipRptsTx": "v1MembershipRptsTx",
        "V2GeneralQueriesRx": "v2GeneralQueriesRx",
        "V2GrpSpecificQueriesRx": "v2GrpSpecificQueriesRx",
        "V2MembershipRptsTx": "v2MembershipRptsTx",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(MldAggregatedStatistics, self).__init__(parent, list_op)

    @property
    def DoneTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Done Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["DoneTx"])

    @DoneTx.setter
    def DoneTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DoneTx"], value)

    @property
    def GrpAndSrcSpecificQueriesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Grp. & Src. Specific Queries Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["GrpAndSrcSpecificQueriesRx"])

    @GrpAndSrcSpecificQueriesRx.setter
    def GrpAndSrcSpecificQueriesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GrpAndSrcSpecificQueriesRx"], value)

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
    def V1GeneralQueriesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: v1 General Queries Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["V1GeneralQueriesRx"])

    @V1GeneralQueriesRx.setter
    def V1GeneralQueriesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["V1GeneralQueriesRx"], value)

    @property
    def V1GrpSpecificQueriesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: v1 Grp. Specific Queries Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["V1GrpSpecificQueriesRx"])

    @V1GrpSpecificQueriesRx.setter
    def V1GrpSpecificQueriesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["V1GrpSpecificQueriesRx"], value)

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
    def V2GeneralQueriesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: v2 General Queries Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["V2GeneralQueriesRx"])

    @V2GeneralQueriesRx.setter
    def V2GeneralQueriesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["V2GeneralQueriesRx"], value)

    @property
    def V2GrpSpecificQueriesRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: v2 Grp. Specific Queries Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["V2GrpSpecificQueriesRx"])

    @V2GrpSpecificQueriesRx.setter
    def V2GrpSpecificQueriesRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["V2GrpSpecificQueriesRx"], value)

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

    def update(
        self,
        DoneTx=None,
        GrpAndSrcSpecificQueriesRx=None,
        HostInvalidPacketsRx=None,
        HostTotalFramesRx=None,
        HostTotalFramesTx=None,
        Hostv1MembershipRptsRx=None,
        PortName=None,
        V1GeneralQueriesRx=None,
        V1GrpSpecificQueriesRx=None,
        V1MembershipRptsTx=None,
        V2GeneralQueriesRx=None,
        V2GrpSpecificQueriesRx=None,
        V2MembershipRptsTx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> MldAggregatedStatistics
        """Updates mldAggregatedStatistics resource on the server.

        Args
        ----
        - DoneTx (bool): Done Tx
        - GrpAndSrcSpecificQueriesRx (bool): Grp. & Src. Specific Queries Rx
        - HostInvalidPacketsRx (bool): Host Invalid Packets Rx
        - HostTotalFramesRx (bool): Host Total Frames Rx
        - HostTotalFramesTx (bool): Host Total Frames Tx
        - Hostv1MembershipRptsRx (bool): Host v1 Membership Rpts. Rx
        - PortName (bool): Port Name
        - V1GeneralQueriesRx (bool): v1 General Queries Rx
        - V1GrpSpecificQueriesRx (bool): v1 Grp. Specific Queries Rx
        - V1MembershipRptsTx (bool): v1 Membership Rpts. Tx
        - V2GeneralQueriesRx (bool): v2 General Queries Rx
        - V2GrpSpecificQueriesRx (bool): v2 Grp. Specific Queries Rx
        - V2MembershipRptsTx (bool): v2 Membership Rpts. Tx

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        DoneTx=None,
        GrpAndSrcSpecificQueriesRx=None,
        HostInvalidPacketsRx=None,
        HostTotalFramesRx=None,
        HostTotalFramesTx=None,
        Hostv1MembershipRptsRx=None,
        PortName=None,
        V1GeneralQueriesRx=None,
        V1GrpSpecificQueriesRx=None,
        V1MembershipRptsTx=None,
        V2GeneralQueriesRx=None,
        V2GrpSpecificQueriesRx=None,
        V2MembershipRptsTx=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> MldAggregatedStatistics
        """Finds and retrieves mldAggregatedStatistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve mldAggregatedStatistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all mldAggregatedStatistics resources from the server.

        Args
        ----
        - DoneTx (bool): Done Tx
        - GrpAndSrcSpecificQueriesRx (bool): Grp. & Src. Specific Queries Rx
        - HostInvalidPacketsRx (bool): Host Invalid Packets Rx
        - HostTotalFramesRx (bool): Host Total Frames Rx
        - HostTotalFramesTx (bool): Host Total Frames Tx
        - Hostv1MembershipRptsRx (bool): Host v1 Membership Rpts. Rx
        - PortName (bool): Port Name
        - V1GeneralQueriesRx (bool): v1 General Queries Rx
        - V1GrpSpecificQueriesRx (bool): v1 Grp. Specific Queries Rx
        - V1MembershipRptsTx (bool): v1 Membership Rpts. Tx
        - V2GeneralQueriesRx (bool): v2 General Queries Rx
        - V2GrpSpecificQueriesRx (bool): v2 Grp. Specific Queries Rx
        - V2MembershipRptsTx (bool): v2 Membership Rpts. Tx

        Returns
        -------
        - self: This instance with matching mldAggregatedStatistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of mldAggregatedStatistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the mldAggregatedStatistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
