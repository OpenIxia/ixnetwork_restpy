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


class RoceV2DcqcnParams(Base):
    """This object provides different options for the DCQCN settings for Tx Port.
    The RoceV2DcqcnParams class encapsulates a required roceV2DcqcnParams resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "roceV2DcqcnParams"
    _SDM_ATT_MAP = {
        "AdditiveIncrRate": "additiveIncrRate",
        "AlphaG": "alphaG",
        "AlphaUpdatePeriod": "alphaUpdatePeriod",
        "ByteResetCount": "byteResetCount",
        "Enabled": "enabled",
        "HyperIncrRate": "hyperIncrRate",
        "InitAlpha": "initAlpha",
        "InitRateOnFirstCnpReceived": "initRateOnFirstCnpReceived",
        "MaxFlowRateDecrPerStep": "maxFlowRateDecrPerStep",
        "MinRateLimit": "minRateLimit",
        "RateIncrTimerResetPeriod": "rateIncrTimerResetPeriod",
        "RateReduceMonitorPeriod": "rateReduceMonitorPeriod",
        "StageThreshold": "stageThreshold",
        "TargetRateClamp": "targetRateClamp",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(RoceV2DcqcnParams, self).__init__(parent, list_op)

    @property
    def AdditiveIncrRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: additiveIncrRate
        """
        return self._get_attribute(self._SDM_ATT_MAP["AdditiveIncrRate"])

    @AdditiveIncrRate.setter
    def AdditiveIncrRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AdditiveIncrRate"], value)

    @property
    def AlphaG(self):
        # type: () -> int
        """
        Returns
        -------
        - number: alphaG
        """
        return self._get_attribute(self._SDM_ATT_MAP["AlphaG"])

    @AlphaG.setter
    def AlphaG(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AlphaG"], value)

    @property
    def AlphaUpdatePeriod(self):
        # type: () -> int
        """
        Returns
        -------
        - number: alphaUpdatePeriod
        """
        return self._get_attribute(self._SDM_ATT_MAP["AlphaUpdatePeriod"])

    @AlphaUpdatePeriod.setter
    def AlphaUpdatePeriod(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AlphaUpdatePeriod"], value)

    @property
    def ByteResetCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: byteResetCount
        """
        return self._get_attribute(self._SDM_ATT_MAP["ByteResetCount"])

    @ByteResetCount.setter
    def ByteResetCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ByteResetCount"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def HyperIncrRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: hyperIncrRate
        """
        return self._get_attribute(self._SDM_ATT_MAP["HyperIncrRate"])

    @HyperIncrRate.setter
    def HyperIncrRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["HyperIncrRate"], value)

    @property
    def InitAlpha(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Initial Alpha
        """
        return self._get_attribute(self._SDM_ATT_MAP["InitAlpha"])

    @InitAlpha.setter
    def InitAlpha(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InitAlpha"], value)

    @property
    def InitRateOnFirstCnpReceived(self):
        # type: () -> int
        """
        Returns
        -------
        - number: initRateOnFirstCnpReceived
        """
        return self._get_attribute(self._SDM_ATT_MAP["InitRateOnFirstCnpReceived"])

    @InitRateOnFirstCnpReceived.setter
    def InitRateOnFirstCnpReceived(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InitRateOnFirstCnpReceived"], value)

    @property
    def MaxFlowRateDecrPerStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: maxFlowRateDecrPerStep
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxFlowRateDecrPerStep"])

    @MaxFlowRateDecrPerStep.setter
    def MaxFlowRateDecrPerStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxFlowRateDecrPerStep"], value)

    @property
    def MinRateLimit(self):
        # type: () -> int
        """
        Returns
        -------
        - number: minRateLimit
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinRateLimit"])

    @MinRateLimit.setter
    def MinRateLimit(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinRateLimit"], value)

    @property
    def RateIncrTimerResetPeriod(self):
        # type: () -> int
        """
        Returns
        -------
        - number: rateIncrTimerResetPeriod
        """
        return self._get_attribute(self._SDM_ATT_MAP["RateIncrTimerResetPeriod"])

    @RateIncrTimerResetPeriod.setter
    def RateIncrTimerResetPeriod(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RateIncrTimerResetPeriod"], value)

    @property
    def RateReduceMonitorPeriod(self):
        # type: () -> int
        """
        Returns
        -------
        - number: rateReduceMonitorPeriod
        """
        return self._get_attribute(self._SDM_ATT_MAP["RateReduceMonitorPeriod"])

    @RateReduceMonitorPeriod.setter
    def RateReduceMonitorPeriod(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RateReduceMonitorPeriod"], value)

    @property
    def StageThreshold(self):
        # type: () -> int
        """
        Returns
        -------
        - number: stageThreshold
        """
        return self._get_attribute(self._SDM_ATT_MAP["StageThreshold"])

    @StageThreshold.setter
    def StageThreshold(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StageThreshold"], value)

    @property
    def TargetRateClamp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TargetRateClamp"])

    @TargetRateClamp.setter
    def TargetRateClamp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TargetRateClamp"], value)

    def update(
        self,
        AdditiveIncrRate=None,
        AlphaG=None,
        AlphaUpdatePeriod=None,
        ByteResetCount=None,
        Enabled=None,
        HyperIncrRate=None,
        InitAlpha=None,
        InitRateOnFirstCnpReceived=None,
        MaxFlowRateDecrPerStep=None,
        MinRateLimit=None,
        RateIncrTimerResetPeriod=None,
        RateReduceMonitorPeriod=None,
        StageThreshold=None,
        TargetRateClamp=None,
    ):
        # type: (int, int, int, int, bool, int, int, int, int, int, int, int, int, bool) -> RoceV2DcqcnParams
        """Updates roceV2DcqcnParams resource on the server.

        Args
        ----
        - AdditiveIncrRate (number): additiveIncrRate
        - AlphaG (number): alphaG
        - AlphaUpdatePeriod (number): alphaUpdatePeriod
        - ByteResetCount (number): byteResetCount
        - Enabled (bool):
        - HyperIncrRate (number): hyperIncrRate
        - InitAlpha (number): Initial Alpha
        - InitRateOnFirstCnpReceived (number): initRateOnFirstCnpReceived
        - MaxFlowRateDecrPerStep (number): maxFlowRateDecrPerStep
        - MinRateLimit (number): minRateLimit
        - RateIncrTimerResetPeriod (number): rateIncrTimerResetPeriod
        - RateReduceMonitorPeriod (number): rateReduceMonitorPeriod
        - StageThreshold (number): stageThreshold
        - TargetRateClamp (bool):

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AdditiveIncrRate=None,
        AlphaG=None,
        AlphaUpdatePeriod=None,
        ByteResetCount=None,
        Enabled=None,
        HyperIncrRate=None,
        InitAlpha=None,
        InitRateOnFirstCnpReceived=None,
        MaxFlowRateDecrPerStep=None,
        MinRateLimit=None,
        RateIncrTimerResetPeriod=None,
        RateReduceMonitorPeriod=None,
        StageThreshold=None,
        TargetRateClamp=None,
    ):
        # type: (int, int, int, int, bool, int, int, int, int, int, int, int, int, bool) -> RoceV2DcqcnParams
        """Finds and retrieves roceV2DcqcnParams resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve roceV2DcqcnParams resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all roceV2DcqcnParams resources from the server.

        Args
        ----
        - AdditiveIncrRate (number): additiveIncrRate
        - AlphaG (number): alphaG
        - AlphaUpdatePeriod (number): alphaUpdatePeriod
        - ByteResetCount (number): byteResetCount
        - Enabled (bool):
        - HyperIncrRate (number): hyperIncrRate
        - InitAlpha (number): Initial Alpha
        - InitRateOnFirstCnpReceived (number): initRateOnFirstCnpReceived
        - MaxFlowRateDecrPerStep (number): maxFlowRateDecrPerStep
        - MinRateLimit (number): minRateLimit
        - RateIncrTimerResetPeriod (number): rateIncrTimerResetPeriod
        - RateReduceMonitorPeriod (number): rateReduceMonitorPeriod
        - StageThreshold (number): stageThreshold
        - TargetRateClamp (bool):

        Returns
        -------
        - self: This instance with matching roceV2DcqcnParams resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of roceV2DcqcnParams data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the roceV2DcqcnParams resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
