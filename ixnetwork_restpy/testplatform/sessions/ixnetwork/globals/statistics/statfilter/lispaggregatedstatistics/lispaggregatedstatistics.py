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


class LispAggregatedStatistics(Base):
    """Represents stats of LISP Aggregated Statistics
    The LispAggregatedStatistics class encapsulates a required lispAggregatedStatistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "lispAggregatedStatistics"
    _SDM_ATT_MAP = {
        "EidRefreshMapRequestRx": "eidRefreshMapRequestRx",
        "EidRefreshMapRequestTx": "eidRefreshMapRequestTx",
        "EidsRequestedCount": "eidsRequestedCount",
        "EidsResolvedCount": "eidsResolvedCount",
        "EncapMapRequestRx": "encapMapRequestRx",
        "EncapMapRequestTx": "encapMapRequestTx",
        "EtrConfigured": "etrConfigured",
        "EtrRunning": "etrRunning",
        "ItrConfigured": "itrConfigured",
        "ItrRunning": "itrRunning",
        "MapNotifyFormatErrorCount": "mapNotifyFormatErrorCount",
        "MapNotifyRx": "mapNotifyRx",
        "MapNotifyTx": "mapNotifyTx",
        "MapRegisterFormatErrorCount": "mapRegisterFormatErrorCount",
        "MapRegisterRx": "mapRegisterRx",
        "MapRegisterTx": "mapRegisterTx",
        "MapReplyFormatErrorCount": "mapReplyFormatErrorCount",
        "MapReplyRx": "mapReplyRx",
        "MapReplyTx": "mapReplyTx",
        "MapRequestFormatErrorCount": "mapRequestFormatErrorCount",
        "MsMRConfigured": "msMRConfigured",
        "MsMRRunning": "msMRRunning",
        "NegativeMapReplyRx": "negativeMapReplyRx",
        "NegativeMapReplyTx": "negativeMapReplyTx",
        "PortName": "portName",
        "RlocProbeMapReplyRx": "rlocProbeMapReplyRx",
        "RlocProbeMapReplyTx": "rlocProbeMapReplyTx",
        "RlocProbeMapRequestRx": "rlocProbeMapRequestRx",
        "RlocProbeMapRequestTx": "rlocProbeMapRequestTx",
        "XtrConfigured": "xtrConfigured",
        "XtrRunning": "xtrRunning",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(LispAggregatedStatistics, self).__init__(parent, list_op)

    @property
    def EidRefreshMapRequestRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: EID Refresh Map Request Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["EidRefreshMapRequestRx"])

    @EidRefreshMapRequestRx.setter
    def EidRefreshMapRequestRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EidRefreshMapRequestRx"], value)

    @property
    def EidRefreshMapRequestTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: EID Refresh Map Request Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["EidRefreshMapRequestTx"])

    @EidRefreshMapRequestTx.setter
    def EidRefreshMapRequestTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EidRefreshMapRequestTx"], value)

    @property
    def EidsRequestedCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: EIDs Requested Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["EidsRequestedCount"])

    @EidsRequestedCount.setter
    def EidsRequestedCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EidsRequestedCount"], value)

    @property
    def EidsResolvedCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: EIDs Resolved Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["EidsResolvedCount"])

    @EidsResolvedCount.setter
    def EidsResolvedCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EidsResolvedCount"], value)

    @property
    def EncapMapRequestRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Encap Map Request Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["EncapMapRequestRx"])

    @EncapMapRequestRx.setter
    def EncapMapRequestRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EncapMapRequestRx"], value)

    @property
    def EncapMapRequestTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Encap Map Request Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["EncapMapRequestTx"])

    @EncapMapRequestTx.setter
    def EncapMapRequestTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EncapMapRequestTx"], value)

    @property
    def EtrConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ETR Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["EtrConfigured"])

    @EtrConfigured.setter
    def EtrConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EtrConfigured"], value)

    @property
    def EtrRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ETR Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["EtrRunning"])

    @EtrRunning.setter
    def EtrRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EtrRunning"], value)

    @property
    def ItrConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ITR Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["ItrConfigured"])

    @ItrConfigured.setter
    def ItrConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ItrConfigured"], value)

    @property
    def ItrRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: ITR Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["ItrRunning"])

    @ItrRunning.setter
    def ItrRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ItrRunning"], value)

    @property
    def MapNotifyFormatErrorCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Map Notify Format Error Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["MapNotifyFormatErrorCount"])

    @MapNotifyFormatErrorCount.setter
    def MapNotifyFormatErrorCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MapNotifyFormatErrorCount"], value)

    @property
    def MapNotifyRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Map Notify Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MapNotifyRx"])

    @MapNotifyRx.setter
    def MapNotifyRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MapNotifyRx"], value)

    @property
    def MapNotifyTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Map Notify Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MapNotifyTx"])

    @MapNotifyTx.setter
    def MapNotifyTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MapNotifyTx"], value)

    @property
    def MapRegisterFormatErrorCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Map Register Format Error Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["MapRegisterFormatErrorCount"])

    @MapRegisterFormatErrorCount.setter
    def MapRegisterFormatErrorCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MapRegisterFormatErrorCount"], value)

    @property
    def MapRegisterRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Map Register Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MapRegisterRx"])

    @MapRegisterRx.setter
    def MapRegisterRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MapRegisterRx"], value)

    @property
    def MapRegisterTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Map Register Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MapRegisterTx"])

    @MapRegisterTx.setter
    def MapRegisterTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MapRegisterTx"], value)

    @property
    def MapReplyFormatErrorCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Map Reply Format Error Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["MapReplyFormatErrorCount"])

    @MapReplyFormatErrorCount.setter
    def MapReplyFormatErrorCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MapReplyFormatErrorCount"], value)

    @property
    def MapReplyRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Map Reply Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MapReplyRx"])

    @MapReplyRx.setter
    def MapReplyRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MapReplyRx"], value)

    @property
    def MapReplyTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Map Reply Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["MapReplyTx"])

    @MapReplyTx.setter
    def MapReplyTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MapReplyTx"], value)

    @property
    def MapRequestFormatErrorCount(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Map Request Format Error Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["MapRequestFormatErrorCount"])

    @MapRequestFormatErrorCount.setter
    def MapRequestFormatErrorCount(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MapRequestFormatErrorCount"], value)

    @property
    def MsMRConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MS/MR Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["MsMRConfigured"])

    @MsMRConfigured.setter
    def MsMRConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MsMRConfigured"], value)

    @property
    def MsMRRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: MS/MR Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["MsMRRunning"])

    @MsMRRunning.setter
    def MsMRRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["MsMRRunning"], value)

    @property
    def NegativeMapReplyRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Negative Map Reply Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["NegativeMapReplyRx"])

    @NegativeMapReplyRx.setter
    def NegativeMapReplyRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NegativeMapReplyRx"], value)

    @property
    def NegativeMapReplyTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Negative Map Reply Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["NegativeMapReplyTx"])

    @NegativeMapReplyTx.setter
    def NegativeMapReplyTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NegativeMapReplyTx"], value)

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
    def RlocProbeMapReplyRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RLOC Probe Map Reply Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RlocProbeMapReplyRx"])

    @RlocProbeMapReplyRx.setter
    def RlocProbeMapReplyRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RlocProbeMapReplyRx"], value)

    @property
    def RlocProbeMapReplyTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RLOC Probe Map Reply Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RlocProbeMapReplyTx"])

    @RlocProbeMapReplyTx.setter
    def RlocProbeMapReplyTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RlocProbeMapReplyTx"], value)

    @property
    def RlocProbeMapRequestRx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RLOC Probe Map Request Rx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RlocProbeMapRequestRx"])

    @RlocProbeMapRequestRx.setter
    def RlocProbeMapRequestRx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RlocProbeMapRequestRx"], value)

    @property
    def RlocProbeMapRequestTx(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: RLOC Probe Map Request Tx
        """
        return self._get_attribute(self._SDM_ATT_MAP["RlocProbeMapRequestTx"])

    @RlocProbeMapRequestTx.setter
    def RlocProbeMapRequestTx(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RlocProbeMapRequestTx"], value)

    @property
    def XtrConfigured(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: xTR Configured
        """
        return self._get_attribute(self._SDM_ATT_MAP["XtrConfigured"])

    @XtrConfigured.setter
    def XtrConfigured(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["XtrConfigured"], value)

    @property
    def XtrRunning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: xTR Running
        """
        return self._get_attribute(self._SDM_ATT_MAP["XtrRunning"])

    @XtrRunning.setter
    def XtrRunning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["XtrRunning"], value)

    def update(
        self,
        EidRefreshMapRequestRx=None,
        EidRefreshMapRequestTx=None,
        EidsRequestedCount=None,
        EidsResolvedCount=None,
        EncapMapRequestRx=None,
        EncapMapRequestTx=None,
        EtrConfigured=None,
        EtrRunning=None,
        ItrConfigured=None,
        ItrRunning=None,
        MapNotifyFormatErrorCount=None,
        MapNotifyRx=None,
        MapNotifyTx=None,
        MapRegisterFormatErrorCount=None,
        MapRegisterRx=None,
        MapRegisterTx=None,
        MapReplyFormatErrorCount=None,
        MapReplyRx=None,
        MapReplyTx=None,
        MapRequestFormatErrorCount=None,
        MsMRConfigured=None,
        MsMRRunning=None,
        NegativeMapReplyRx=None,
        NegativeMapReplyTx=None,
        PortName=None,
        RlocProbeMapReplyRx=None,
        RlocProbeMapReplyTx=None,
        RlocProbeMapRequestRx=None,
        RlocProbeMapRequestTx=None,
        XtrConfigured=None,
        XtrRunning=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> LispAggregatedStatistics
        """Updates lispAggregatedStatistics resource on the server.

        Args
        ----
        - EidRefreshMapRequestRx (bool): EID Refresh Map Request Rx
        - EidRefreshMapRequestTx (bool): EID Refresh Map Request Tx
        - EidsRequestedCount (bool): EIDs Requested Count
        - EidsResolvedCount (bool): EIDs Resolved Count
        - EncapMapRequestRx (bool): Encap Map Request Rx
        - EncapMapRequestTx (bool): Encap Map Request Tx
        - EtrConfigured (bool): ETR Configured
        - EtrRunning (bool): ETR Running
        - ItrConfigured (bool): ITR Configured
        - ItrRunning (bool): ITR Running
        - MapNotifyFormatErrorCount (bool): Map Notify Format Error Count
        - MapNotifyRx (bool): Map Notify Rx
        - MapNotifyTx (bool): Map Notify Tx
        - MapRegisterFormatErrorCount (bool): Map Register Format Error Count
        - MapRegisterRx (bool): Map Register Rx
        - MapRegisterTx (bool): Map Register Tx
        - MapReplyFormatErrorCount (bool): Map Reply Format Error Count
        - MapReplyRx (bool): Map Reply Rx
        - MapReplyTx (bool): Map Reply Tx
        - MapRequestFormatErrorCount (bool): Map Request Format Error Count
        - MsMRConfigured (bool): MS/MR Configured
        - MsMRRunning (bool): MS/MR Running
        - NegativeMapReplyRx (bool): Negative Map Reply Rx
        - NegativeMapReplyTx (bool): Negative Map Reply Tx
        - PortName (bool): Port Name
        - RlocProbeMapReplyRx (bool): RLOC Probe Map Reply Rx
        - RlocProbeMapReplyTx (bool): RLOC Probe Map Reply Tx
        - RlocProbeMapRequestRx (bool): RLOC Probe Map Request Rx
        - RlocProbeMapRequestTx (bool): RLOC Probe Map Request Tx
        - XtrConfigured (bool): xTR Configured
        - XtrRunning (bool): xTR Running

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        EidRefreshMapRequestRx=None,
        EidRefreshMapRequestTx=None,
        EidsRequestedCount=None,
        EidsResolvedCount=None,
        EncapMapRequestRx=None,
        EncapMapRequestTx=None,
        EtrConfigured=None,
        EtrRunning=None,
        ItrConfigured=None,
        ItrRunning=None,
        MapNotifyFormatErrorCount=None,
        MapNotifyRx=None,
        MapNotifyTx=None,
        MapRegisterFormatErrorCount=None,
        MapRegisterRx=None,
        MapRegisterTx=None,
        MapReplyFormatErrorCount=None,
        MapReplyRx=None,
        MapReplyTx=None,
        MapRequestFormatErrorCount=None,
        MsMRConfigured=None,
        MsMRRunning=None,
        NegativeMapReplyRx=None,
        NegativeMapReplyTx=None,
        PortName=None,
        RlocProbeMapReplyRx=None,
        RlocProbeMapReplyTx=None,
        RlocProbeMapRequestRx=None,
        RlocProbeMapRequestTx=None,
        XtrConfigured=None,
        XtrRunning=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> LispAggregatedStatistics
        """Finds and retrieves lispAggregatedStatistics resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve lispAggregatedStatistics resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all lispAggregatedStatistics resources from the server.

        Args
        ----
        - EidRefreshMapRequestRx (bool): EID Refresh Map Request Rx
        - EidRefreshMapRequestTx (bool): EID Refresh Map Request Tx
        - EidsRequestedCount (bool): EIDs Requested Count
        - EidsResolvedCount (bool): EIDs Resolved Count
        - EncapMapRequestRx (bool): Encap Map Request Rx
        - EncapMapRequestTx (bool): Encap Map Request Tx
        - EtrConfigured (bool): ETR Configured
        - EtrRunning (bool): ETR Running
        - ItrConfigured (bool): ITR Configured
        - ItrRunning (bool): ITR Running
        - MapNotifyFormatErrorCount (bool): Map Notify Format Error Count
        - MapNotifyRx (bool): Map Notify Rx
        - MapNotifyTx (bool): Map Notify Tx
        - MapRegisterFormatErrorCount (bool): Map Register Format Error Count
        - MapRegisterRx (bool): Map Register Rx
        - MapRegisterTx (bool): Map Register Tx
        - MapReplyFormatErrorCount (bool): Map Reply Format Error Count
        - MapReplyRx (bool): Map Reply Rx
        - MapReplyTx (bool): Map Reply Tx
        - MapRequestFormatErrorCount (bool): Map Request Format Error Count
        - MsMRConfigured (bool): MS/MR Configured
        - MsMRRunning (bool): MS/MR Running
        - NegativeMapReplyRx (bool): Negative Map Reply Rx
        - NegativeMapReplyTx (bool): Negative Map Reply Tx
        - PortName (bool): Port Name
        - RlocProbeMapReplyRx (bool): RLOC Probe Map Reply Rx
        - RlocProbeMapReplyTx (bool): RLOC Probe Map Reply Tx
        - RlocProbeMapRequestRx (bool): RLOC Probe Map Request Rx
        - RlocProbeMapRequestTx (bool): RLOC Probe Map Request Tx
        - XtrConfigured (bool): xTR Configured
        - XtrRunning (bool): xTR Running

        Returns
        -------
        - self: This instance with matching lispAggregatedStatistics resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of lispAggregatedStatistics data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the lispAggregatedStatistics resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
