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


class Aggregation(Base):
    """The Card resource group.
    The Aggregation class encapsulates a list of aggregation resources that are managed by the system.
    A list of resources can be retrieved from the server using the Aggregation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "aggregation"
    _SDM_ATT_MAP = {
        "ActivePort": "activePort",
        "ActivePorts": "activePorts",
        "AvailableModes": "availableModes",
        "Mode": "mode",
        "ResourcePorts": "resourcePorts",
    }
    _SDM_ENUM_MAP = {
        "mode": [
            "normal",
            "tenGig",
            "fortyGig",
            "singleMode",
            "dualMode",
            "hundredGigNonFanOut",
            "fortyGigFanOut",
            "threeByTenGigFanOut",
            "eightByTenGigFanOut",
            "fourByTwentyFiveGigNonFanOut",
            "twoByTwentyFiveGigNonFanOut",
            "oneByFiftyGigNonFanOut",
            "fortyGigNonFanOut",
            "oneByTenGigFanOut",
            "fourByTenGigFanOut",
            "incompatibleMode",
            "hundredGigCapturePlayback",
            "fortyGigCapturePlayback",
            "novusHundredGigNonFanOut",
            "novusFourByTwentyFiveGigNonFanOut",
            "novusTwoByFiftyGigNonFanOut",
            "novusOneByFortyGigNonFanOut",
            "novusFourByTenGigNonFanOut",
            "krakenOneByFourHundredGigNonFanOut",
            "krakenOneByTwoHundredGigNonFanOut",
            "krakenTwoByOneHundredGigFanOut",
            "krakenFourByFiftyGigFanOut",
            "aresOneOneByFourHundredGigNonFanOut",
            "aresOneOneByFourHundredGigMacSec128NonFanOut",
            "aresOneOneByFourHundredGigMacSec256NonFanOut",
            "aresOneTwoByTwoHundredGigFanOut",
            "aresOneTwoByTwoHundredGigMacSecFanOut",
            "aresOneFourByOneHundredGigFanOut",
            "aresOneFourByOneHundredGigMacSecFanOut",
            "aresOneEightByFiftyGigFanOut",
            "uhdOneHundredEightByHundredGigNonFanOut",
            "uhdOneHundredEightByFortyGigNonFanOut",
            "uhdOneHundredSixteenByFiftyGigFanOut",
            "uhdOneHundredThirtyTwoByTwentyFiveGigFanOut",
            "uhdOneHundredThirtyTwoByTenGigFanOut",
            "novus5GOneByTenGigNonFanOut",
            "novus5GOneByTwentyFiveGigNonFanOut",
            "novus5GOneByFiftyGigNonFanOut",
            "novus5GOneByHundredGigNonFanOut",
            "novus5GOneByHundredGigNonFanOutHighStream",
            "starTwoByFourHundredGigNonFannedOutPAM4",
            "starTwoByFourHundredGigFannedOutPAM4RoCEv2",
            "starFourByTwoHundredGigFannedOutPAM4",
            "starFourByTwoHundredGigFannedOutPAM4RoCEv2",
            "starTwoByTwoHundredGigFannedOutNRZ",
            "starEightByHundredGigFannedOutPAM4",
            "starEightByHundredGigFannedOutPAM4RoCEv2",
            "starFourByHundredGigFannedOutNRZRoCEv2",
            "starFourByHundredGigFannedOutNRZ",
            "starSixteenByFiftyGigFannedOutPAM4",
            "starEightByFiftyGigFannedOutNRZ",
            "starFourByFortyGigFannedOutNRZ",
            "starSixteenByTwentyFiveGigFannedOutNRZ",
            "starSixteenByTenGigFannedOutNRZ",
            "starFourByHundredGigFannedOutPAM4HalfDensityHighStream",
            "starEightByFiftyGigFannedOutPAM4HalfDensityHighStream",
            "starEightByTwentyFiveGigFannedOutNRZHalfDensityHighStream",
            "starEightByTenGigFannedOutNRZHalfDensityHighStream",
            "novusHundredGigNonFanOutHighStream",
            "novusFourByTwentyFiveGigNonFanOutHighStream",
            "novusTwoByFiftyGigNonFanOutHighStream",
            "novusOneByFortyGigNonFanOutHighStream",
            "novusFourByTenGigNonFanOutHighStream",
            "ravenEightByHundredGigFannedOutPAM4",
            "ravenFourByTwoHundredGigFannedOutPAM4",
            "ravenTwoByFourHundredGigFannedOutPAM4",
            "ravenOneByEightHundredGigNonFannedOutPAM4",
            "aresOneEightHundredQddCEightByHundredGigFannedOutPAM4",
            "aresOneEightHundredQddCFourByTwoHundredGigFannedOutPAM4",
            "aresOneEightHundredQddCTwoByFourHundredGigFannedOutPAM4",
            "aresOneEightHundredQddCOneByEightHundredGigNonFannedOutPAM4",
            "sertHundredGig",
            "sertFiftyGig",
            "sertFourtyGig",
            "sertTwentyFiveGig",
            "sertTenGig",
            "aresOneEightHundredOsfpCEightByHundredGigFannedOutPAM4",
            "aresOneEightHundredOsfpCFourByTwoHundredGigFannedOutPAM4",
            "aresOneEightHundredOsfpCTwoByFourHundredGigFannedOutPAM4",
            "aresOneEightHundredOsfpCOneByEightHundredGigNonFannedOutPAM4",
            "aresOne-M-OneByEightHundredGigPAM4-106G",
            "aresOne-M-TwoByFourHundredGigPAM4-106G",
            "aresOne-M-FourByTwoHundredGigPAM4-106G",
            "aresOne-M-EightByOneHundredGigPAM4-106G",
            "aresOne-M-OneByFourHundredGigPAM4-53G",
            "aresOne-M-TwoByTwoHundredGigPAM4-53G",
            "aresOne-M-FourByOneHundredGigPAM4-53G",
            "aresOne-M-EightByFiftyGigPAM4-53G",
            "aresOne-M-OneByTwoHundredGigNRZ-26G",
            "aresOne-M-TwoByOneHundredGigNRZ-26G",
            "aresOne-M-FourByFiftyGigNRZ-26G",
            "aresOne-M-TwoByFortyGigNRZ-10G",
            "aresOne-M-EightByTwentyFiveGigNRZ-26G",
            "aresOne-M-EightByTenGigNRZ-10G",
            "aresOne-M-OneByEightHundredGigPAM4-106G-RoCEv2",
            "aresOne-M-TwoByFourHundredGigPAM4-106G-RoCEv2",
            "aresOne-M-FourByTwoHundredGigPAM4-106G-RoCEv2",
            "aresOne-M-EightByOneHundredGigPAM4-106G-RoCEv2",
            "aresOne-M-OneByFourHundredGigPAM4-53G-RoCEv2",
            "aresOne-M-TwoByTwoHundredGigPAM4-53G-RoCEv2",
            "aresOne-M-FourByOneHundredGigPAM4-53G-RoCEv2",
            "aresOne-M-TwoByOneHundredGigNRZ-26G-RoCEv2",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(Aggregation, self).__init__(parent, list_op)

    @property
    def ActivePort(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/availableHardware/chassis/card/port): Deprecated. Use activePorts instead.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ActivePort"])

    @property
    def ActivePorts(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/availableHardware/chassis/card/port]): All active ports from Resource Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ActivePorts"])

    @property
    def AvailableModes(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[normal | tenGig | fortyGig | singleMode | dualMode | hundredGigNonFanOut | fortyGigFanOut | threeByTenGigFanOut | eightByTenGigFanOut | fourByTwentyFiveGigNonFanOut | twoByTwentyFiveGigNonFanOut | oneByFiftyGigNonFanOut | fortyGigNonFanOut | oneByTenGigFanOut | fourByTenGigFanOut | incompatibleMode | hundredGigCapturePlayback | fortyGigCapturePlayback | novusHundredGigNonFanOut | novusFourByTwentyFiveGigNonFanOut | novusTwoByFiftyGigNonFanOut | novusOneByFortyGigNonFanOut | novusFourByTenGigNonFanOut | krakenOneByFourHundredGigNonFanOut | krakenOneByTwoHundredGigNonFanOut | krakenTwoByOneHundredGigFanOut | krakenFourByFiftyGigFanOut | aresOneOneByFourHundredGigNonFanOut | aresOneOneByFourHundredGigMacSec128NonFanOut | aresOneOneByFourHundredGigMacSec256NonFanOut | aresOneTwoByTwoHundredGigFanOut | aresOneTwoByTwoHundredGigMacSecFanOut | aresOneFourByOneHundredGigFanOut | aresOneFourByOneHundredGigMacSecFanOut | aresOneEightByFiftyGigFanOut | uhdOneHundredEightByHundredGigNonFanOut | uhdOneHundredEightByFortyGigNonFanOut | uhdOneHundredSixteenByFiftyGigFanOut | uhdOneHundredThirtyTwoByTwentyFiveGigFanOut | uhdOneHundredThirtyTwoByTenGigFanOut | novus5GOneByTenGigNonFanOut | novus5GOneByTwentyFiveGigNonFanOut | novus5GOneByFiftyGigNonFanOut | novus5GOneByHundredGigNonFanOut | novus5GOneByHundredGigNonFanOutHighStream | starTwoByFourHundredGigNonFannedOutPAM4 | starTwoByFourHundredGigFannedOutPAM4RoCEv2 | starFourByTwoHundredGigFannedOutPAM4 | starFourByTwoHundredGigFannedOutPAM4RoCEv2 | starTwoByTwoHundredGigFannedOutNRZ | starEightByHundredGigFannedOutPAM4 | starEightByHundredGigFannedOutPAM4RoCEv2 | starFourByHundredGigFannedOutNRZRoCEv2 | starFourByHundredGigFannedOutNRZ | starSixteenByFiftyGigFannedOutPAM4 | starEightByFiftyGigFannedOutNRZ | starFourByFortyGigFannedOutNRZ | starSixteenByTwentyFiveGigFannedOutNRZ | starSixteenByTenGigFannedOutNRZ | starFourByHundredGigFannedOutPAM4HalfDensityHighStream | starEightByFiftyGigFannedOutPAM4HalfDensityHighStream | starEightByTwentyFiveGigFannedOutNRZHalfDensityHighStream | starEightByTenGigFannedOutNRZHalfDensityHighStream | novusHundredGigNonFanOutHighStream | novusFourByTwentyFiveGigNonFanOutHighStream | novusTwoByFiftyGigNonFanOutHighStream | novusOneByFortyGigNonFanOutHighStream | novusFourByTenGigNonFanOutHighStream | ravenEightByHundredGigFannedOutPAM4 | ravenFourByTwoHundredGigFannedOutPAM4 | ravenTwoByFourHundredGigFannedOutPAM4 | ravenOneByEightHundredGigNonFannedOutPAM4 | aresOneEightHundredQddCEightByHundredGigFannedOutPAM4 | aresOneEightHundredQddCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredQddCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredQddCOneByEightHundredGigNonFannedOutPAM4 | sertHundredGig | sertFiftyGig | sertFourtyGig | sertTwentyFiveGig | sertTenGig | aresOneEightHundredOsfpCEightByHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCOneByEightHundredGigNonFannedOutPAM4 | aresOne-M-OneByEightHundredGigPAM4-106G | aresOne-M-TwoByFourHundredGigPAM4-106G | aresOne-M-FourByTwoHundredGigPAM4-106G | aresOne-M-EightByOneHundredGigPAM4-106G | aresOne-M-OneByFourHundredGigPAM4-53G | aresOne-M-TwoByTwoHundredGigPAM4-53G | aresOne-M-FourByOneHundredGigPAM4-53G | aresOne-M-EightByFiftyGigPAM4-53G | aresOne-M-OneByTwoHundredGigNRZ-26G | aresOne-M-TwoByOneHundredGigNRZ-26G | aresOne-M-FourByFiftyGigNRZ-26G | aresOne-M-TwoByFortyGigNRZ-10G | aresOne-M-EightByTwentyFiveGigNRZ-26G | aresOne-M-EightByTenGigNRZ-10G | aresOne-M-OneByEightHundredGigPAM4-106G-RoCEv2 | aresOne-M-TwoByFourHundredGigPAM4-106G-RoCEv2 | aresOne-M-FourByTwoHundredGigPAM4-106G-RoCEv2 | aresOne-M-EightByOneHundredGigPAM4-106G-RoCEv2 | aresOne-M-OneByFourHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByTwoHundredGigPAM4-53G-RoCEv2 | aresOne-M-FourByOneHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByOneHundredGigNRZ-26G-RoCEv2]): Gets the supported resource group modes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AvailableModes"])

    @property
    def Mode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(normal | tenGig | fortyGig | singleMode | dualMode | hundredGigNonFanOut | fortyGigFanOut | threeByTenGigFanOut | eightByTenGigFanOut | fourByTwentyFiveGigNonFanOut | twoByTwentyFiveGigNonFanOut | oneByFiftyGigNonFanOut | fortyGigNonFanOut | oneByTenGigFanOut | fourByTenGigFanOut | incompatibleMode | hundredGigCapturePlayback | fortyGigCapturePlayback | novusHundredGigNonFanOut | novusFourByTwentyFiveGigNonFanOut | novusTwoByFiftyGigNonFanOut | novusOneByFortyGigNonFanOut | novusFourByTenGigNonFanOut | krakenOneByFourHundredGigNonFanOut | krakenOneByTwoHundredGigNonFanOut | krakenTwoByOneHundredGigFanOut | krakenFourByFiftyGigFanOut | aresOneOneByFourHundredGigNonFanOut | aresOneOneByFourHundredGigMacSec128NonFanOut | aresOneOneByFourHundredGigMacSec256NonFanOut | aresOneTwoByTwoHundredGigFanOut | aresOneTwoByTwoHundredGigMacSecFanOut | aresOneFourByOneHundredGigFanOut | aresOneFourByOneHundredGigMacSecFanOut | aresOneEightByFiftyGigFanOut | uhdOneHundredEightByHundredGigNonFanOut | uhdOneHundredEightByFortyGigNonFanOut | uhdOneHundredSixteenByFiftyGigFanOut | uhdOneHundredThirtyTwoByTwentyFiveGigFanOut | uhdOneHundredThirtyTwoByTenGigFanOut | novus5GOneByTenGigNonFanOut | novus5GOneByTwentyFiveGigNonFanOut | novus5GOneByFiftyGigNonFanOut | novus5GOneByHundredGigNonFanOut | novus5GOneByHundredGigNonFanOutHighStream | starTwoByFourHundredGigNonFannedOutPAM4 | starTwoByFourHundredGigFannedOutPAM4RoCEv2 | starFourByTwoHundredGigFannedOutPAM4 | starFourByTwoHundredGigFannedOutPAM4RoCEv2 | starTwoByTwoHundredGigFannedOutNRZ | starEightByHundredGigFannedOutPAM4 | starEightByHundredGigFannedOutPAM4RoCEv2 | starFourByHundredGigFannedOutNRZRoCEv2 | starFourByHundredGigFannedOutNRZ | starSixteenByFiftyGigFannedOutPAM4 | starEightByFiftyGigFannedOutNRZ | starFourByFortyGigFannedOutNRZ | starSixteenByTwentyFiveGigFannedOutNRZ | starSixteenByTenGigFannedOutNRZ | starFourByHundredGigFannedOutPAM4HalfDensityHighStream | starEightByFiftyGigFannedOutPAM4HalfDensityHighStream | starEightByTwentyFiveGigFannedOutNRZHalfDensityHighStream | starEightByTenGigFannedOutNRZHalfDensityHighStream | novusHundredGigNonFanOutHighStream | novusFourByTwentyFiveGigNonFanOutHighStream | novusTwoByFiftyGigNonFanOutHighStream | novusOneByFortyGigNonFanOutHighStream | novusFourByTenGigNonFanOutHighStream | ravenEightByHundredGigFannedOutPAM4 | ravenFourByTwoHundredGigFannedOutPAM4 | ravenTwoByFourHundredGigFannedOutPAM4 | ravenOneByEightHundredGigNonFannedOutPAM4 | aresOneEightHundredQddCEightByHundredGigFannedOutPAM4 | aresOneEightHundredQddCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredQddCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredQddCOneByEightHundredGigNonFannedOutPAM4 | sertHundredGig | sertFiftyGig | sertFourtyGig | sertTwentyFiveGig | sertTenGig | aresOneEightHundredOsfpCEightByHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCOneByEightHundredGigNonFannedOutPAM4 | aresOne-M-OneByEightHundredGigPAM4-106G | aresOne-M-TwoByFourHundredGigPAM4-106G | aresOne-M-FourByTwoHundredGigPAM4-106G | aresOne-M-EightByOneHundredGigPAM4-106G | aresOne-M-OneByFourHundredGigPAM4-53G | aresOne-M-TwoByTwoHundredGigPAM4-53G | aresOne-M-FourByOneHundredGigPAM4-53G | aresOne-M-EightByFiftyGigPAM4-53G | aresOne-M-OneByTwoHundredGigNRZ-26G | aresOne-M-TwoByOneHundredGigNRZ-26G | aresOne-M-FourByFiftyGigNRZ-26G | aresOne-M-TwoByFortyGigNRZ-10G | aresOne-M-EightByTwentyFiveGigNRZ-26G | aresOne-M-EightByTenGigNRZ-10G | aresOne-M-OneByEightHundredGigPAM4-106G-RoCEv2 | aresOne-M-TwoByFourHundredGigPAM4-106G-RoCEv2 | aresOne-M-FourByTwoHundredGigPAM4-106G-RoCEv2 | aresOne-M-EightByOneHundredGigPAM4-106G-RoCEv2 | aresOne-M-OneByFourHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByTwoHundredGigPAM4-53G-RoCEv2 | aresOne-M-FourByOneHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByOneHundredGigNRZ-26G-RoCEv2): Resource Group mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mode"])

    @Mode.setter
    def Mode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mode"], value)

    @property
    def ResourcePorts(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/availableHardware/chassis/card/port]): All ports from Resource Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ResourcePorts"])

    def update(self, Mode=None):
        # type: (str) -> Aggregation
        """Updates aggregation resource on the server.

        Args
        ----
        - Mode (str(normal | tenGig | fortyGig | singleMode | dualMode | hundredGigNonFanOut | fortyGigFanOut | threeByTenGigFanOut | eightByTenGigFanOut | fourByTwentyFiveGigNonFanOut | twoByTwentyFiveGigNonFanOut | oneByFiftyGigNonFanOut | fortyGigNonFanOut | oneByTenGigFanOut | fourByTenGigFanOut | incompatibleMode | hundredGigCapturePlayback | fortyGigCapturePlayback | novusHundredGigNonFanOut | novusFourByTwentyFiveGigNonFanOut | novusTwoByFiftyGigNonFanOut | novusOneByFortyGigNonFanOut | novusFourByTenGigNonFanOut | krakenOneByFourHundredGigNonFanOut | krakenOneByTwoHundredGigNonFanOut | krakenTwoByOneHundredGigFanOut | krakenFourByFiftyGigFanOut | aresOneOneByFourHundredGigNonFanOut | aresOneOneByFourHundredGigMacSec128NonFanOut | aresOneOneByFourHundredGigMacSec256NonFanOut | aresOneTwoByTwoHundredGigFanOut | aresOneTwoByTwoHundredGigMacSecFanOut | aresOneFourByOneHundredGigFanOut | aresOneFourByOneHundredGigMacSecFanOut | aresOneEightByFiftyGigFanOut | uhdOneHundredEightByHundredGigNonFanOut | uhdOneHundredEightByFortyGigNonFanOut | uhdOneHundredSixteenByFiftyGigFanOut | uhdOneHundredThirtyTwoByTwentyFiveGigFanOut | uhdOneHundredThirtyTwoByTenGigFanOut | novus5GOneByTenGigNonFanOut | novus5GOneByTwentyFiveGigNonFanOut | novus5GOneByFiftyGigNonFanOut | novus5GOneByHundredGigNonFanOut | novus5GOneByHundredGigNonFanOutHighStream | starTwoByFourHundredGigNonFannedOutPAM4 | starTwoByFourHundredGigFannedOutPAM4RoCEv2 | starFourByTwoHundredGigFannedOutPAM4 | starFourByTwoHundredGigFannedOutPAM4RoCEv2 | starTwoByTwoHundredGigFannedOutNRZ | starEightByHundredGigFannedOutPAM4 | starEightByHundredGigFannedOutPAM4RoCEv2 | starFourByHundredGigFannedOutNRZRoCEv2 | starFourByHundredGigFannedOutNRZ | starSixteenByFiftyGigFannedOutPAM4 | starEightByFiftyGigFannedOutNRZ | starFourByFortyGigFannedOutNRZ | starSixteenByTwentyFiveGigFannedOutNRZ | starSixteenByTenGigFannedOutNRZ | starFourByHundredGigFannedOutPAM4HalfDensityHighStream | starEightByFiftyGigFannedOutPAM4HalfDensityHighStream | starEightByTwentyFiveGigFannedOutNRZHalfDensityHighStream | starEightByTenGigFannedOutNRZHalfDensityHighStream | novusHundredGigNonFanOutHighStream | novusFourByTwentyFiveGigNonFanOutHighStream | novusTwoByFiftyGigNonFanOutHighStream | novusOneByFortyGigNonFanOutHighStream | novusFourByTenGigNonFanOutHighStream | ravenEightByHundredGigFannedOutPAM4 | ravenFourByTwoHundredGigFannedOutPAM4 | ravenTwoByFourHundredGigFannedOutPAM4 | ravenOneByEightHundredGigNonFannedOutPAM4 | aresOneEightHundredQddCEightByHundredGigFannedOutPAM4 | aresOneEightHundredQddCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredQddCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredQddCOneByEightHundredGigNonFannedOutPAM4 | sertHundredGig | sertFiftyGig | sertFourtyGig | sertTwentyFiveGig | sertTenGig | aresOneEightHundredOsfpCEightByHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCOneByEightHundredGigNonFannedOutPAM4 | aresOne-M-OneByEightHundredGigPAM4-106G | aresOne-M-TwoByFourHundredGigPAM4-106G | aresOne-M-FourByTwoHundredGigPAM4-106G | aresOne-M-EightByOneHundredGigPAM4-106G | aresOne-M-OneByFourHundredGigPAM4-53G | aresOne-M-TwoByTwoHundredGigPAM4-53G | aresOne-M-FourByOneHundredGigPAM4-53G | aresOne-M-EightByFiftyGigPAM4-53G | aresOne-M-OneByTwoHundredGigNRZ-26G | aresOne-M-TwoByOneHundredGigNRZ-26G | aresOne-M-FourByFiftyGigNRZ-26G | aresOne-M-TwoByFortyGigNRZ-10G | aresOne-M-EightByTwentyFiveGigNRZ-26G | aresOne-M-EightByTenGigNRZ-10G | aresOne-M-OneByEightHundredGigPAM4-106G-RoCEv2 | aresOne-M-TwoByFourHundredGigPAM4-106G-RoCEv2 | aresOne-M-FourByTwoHundredGigPAM4-106G-RoCEv2 | aresOne-M-EightByOneHundredGigPAM4-106G-RoCEv2 | aresOne-M-OneByFourHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByTwoHundredGigPAM4-53G-RoCEv2 | aresOne-M-FourByOneHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByOneHundredGigNRZ-26G-RoCEv2)): Resource Group mode.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Mode=None):
        # type: (str) -> Aggregation
        """Adds a new aggregation resource on the json, only valid with batch add utility

        Args
        ----
        - Mode (str(normal | tenGig | fortyGig | singleMode | dualMode | hundredGigNonFanOut | fortyGigFanOut | threeByTenGigFanOut | eightByTenGigFanOut | fourByTwentyFiveGigNonFanOut | twoByTwentyFiveGigNonFanOut | oneByFiftyGigNonFanOut | fortyGigNonFanOut | oneByTenGigFanOut | fourByTenGigFanOut | incompatibleMode | hundredGigCapturePlayback | fortyGigCapturePlayback | novusHundredGigNonFanOut | novusFourByTwentyFiveGigNonFanOut | novusTwoByFiftyGigNonFanOut | novusOneByFortyGigNonFanOut | novusFourByTenGigNonFanOut | krakenOneByFourHundredGigNonFanOut | krakenOneByTwoHundredGigNonFanOut | krakenTwoByOneHundredGigFanOut | krakenFourByFiftyGigFanOut | aresOneOneByFourHundredGigNonFanOut | aresOneOneByFourHundredGigMacSec128NonFanOut | aresOneOneByFourHundredGigMacSec256NonFanOut | aresOneTwoByTwoHundredGigFanOut | aresOneTwoByTwoHundredGigMacSecFanOut | aresOneFourByOneHundredGigFanOut | aresOneFourByOneHundredGigMacSecFanOut | aresOneEightByFiftyGigFanOut | uhdOneHundredEightByHundredGigNonFanOut | uhdOneHundredEightByFortyGigNonFanOut | uhdOneHundredSixteenByFiftyGigFanOut | uhdOneHundredThirtyTwoByTwentyFiveGigFanOut | uhdOneHundredThirtyTwoByTenGigFanOut | novus5GOneByTenGigNonFanOut | novus5GOneByTwentyFiveGigNonFanOut | novus5GOneByFiftyGigNonFanOut | novus5GOneByHundredGigNonFanOut | novus5GOneByHundredGigNonFanOutHighStream | starTwoByFourHundredGigNonFannedOutPAM4 | starTwoByFourHundredGigFannedOutPAM4RoCEv2 | starFourByTwoHundredGigFannedOutPAM4 | starFourByTwoHundredGigFannedOutPAM4RoCEv2 | starTwoByTwoHundredGigFannedOutNRZ | starEightByHundredGigFannedOutPAM4 | starEightByHundredGigFannedOutPAM4RoCEv2 | starFourByHundredGigFannedOutNRZRoCEv2 | starFourByHundredGigFannedOutNRZ | starSixteenByFiftyGigFannedOutPAM4 | starEightByFiftyGigFannedOutNRZ | starFourByFortyGigFannedOutNRZ | starSixteenByTwentyFiveGigFannedOutNRZ | starSixteenByTenGigFannedOutNRZ | starFourByHundredGigFannedOutPAM4HalfDensityHighStream | starEightByFiftyGigFannedOutPAM4HalfDensityHighStream | starEightByTwentyFiveGigFannedOutNRZHalfDensityHighStream | starEightByTenGigFannedOutNRZHalfDensityHighStream | novusHundredGigNonFanOutHighStream | novusFourByTwentyFiveGigNonFanOutHighStream | novusTwoByFiftyGigNonFanOutHighStream | novusOneByFortyGigNonFanOutHighStream | novusFourByTenGigNonFanOutHighStream | ravenEightByHundredGigFannedOutPAM4 | ravenFourByTwoHundredGigFannedOutPAM4 | ravenTwoByFourHundredGigFannedOutPAM4 | ravenOneByEightHundredGigNonFannedOutPAM4 | aresOneEightHundredQddCEightByHundredGigFannedOutPAM4 | aresOneEightHundredQddCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredQddCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredQddCOneByEightHundredGigNonFannedOutPAM4 | sertHundredGig | sertFiftyGig | sertFourtyGig | sertTwentyFiveGig | sertTenGig | aresOneEightHundredOsfpCEightByHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCOneByEightHundredGigNonFannedOutPAM4 | aresOne-M-OneByEightHundredGigPAM4-106G | aresOne-M-TwoByFourHundredGigPAM4-106G | aresOne-M-FourByTwoHundredGigPAM4-106G | aresOne-M-EightByOneHundredGigPAM4-106G | aresOne-M-OneByFourHundredGigPAM4-53G | aresOne-M-TwoByTwoHundredGigPAM4-53G | aresOne-M-FourByOneHundredGigPAM4-53G | aresOne-M-EightByFiftyGigPAM4-53G | aresOne-M-OneByTwoHundredGigNRZ-26G | aresOne-M-TwoByOneHundredGigNRZ-26G | aresOne-M-FourByFiftyGigNRZ-26G | aresOne-M-TwoByFortyGigNRZ-10G | aresOne-M-EightByTwentyFiveGigNRZ-26G | aresOne-M-EightByTenGigNRZ-10G | aresOne-M-OneByEightHundredGigPAM4-106G-RoCEv2 | aresOne-M-TwoByFourHundredGigPAM4-106G-RoCEv2 | aresOne-M-FourByTwoHundredGigPAM4-106G-RoCEv2 | aresOne-M-EightByOneHundredGigPAM4-106G-RoCEv2 | aresOne-M-OneByFourHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByTwoHundredGigPAM4-53G-RoCEv2 | aresOne-M-FourByOneHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByOneHundredGigNRZ-26G-RoCEv2)): Resource Group mode.

        Returns
        -------
        - self: This instance with all currently retrieved aggregation resources using find and the newly added aggregation resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ActivePort=None,
        ActivePorts=None,
        AvailableModes=None,
        Mode=None,
        ResourcePorts=None,
    ):
        # type: (str, List[str], List[str], str, List[str]) -> Aggregation
        """Finds and retrieves aggregation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve aggregation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all aggregation resources from the server.

        Args
        ----
        - ActivePort (str(None | /api/v1/sessions/1/ixnetwork/availableHardware/chassis/card/port)): Deprecated. Use activePorts instead.
        - ActivePorts (list(str[None | /api/v1/sessions/1/ixnetwork/availableHardware/chassis/card/port])): All active ports from Resource Group.
        - AvailableModes (list(str[normal | tenGig | fortyGig | singleMode | dualMode | hundredGigNonFanOut | fortyGigFanOut | threeByTenGigFanOut | eightByTenGigFanOut | fourByTwentyFiveGigNonFanOut | twoByTwentyFiveGigNonFanOut | oneByFiftyGigNonFanOut | fortyGigNonFanOut | oneByTenGigFanOut | fourByTenGigFanOut | incompatibleMode | hundredGigCapturePlayback | fortyGigCapturePlayback | novusHundredGigNonFanOut | novusFourByTwentyFiveGigNonFanOut | novusTwoByFiftyGigNonFanOut | novusOneByFortyGigNonFanOut | novusFourByTenGigNonFanOut | krakenOneByFourHundredGigNonFanOut | krakenOneByTwoHundredGigNonFanOut | krakenTwoByOneHundredGigFanOut | krakenFourByFiftyGigFanOut | aresOneOneByFourHundredGigNonFanOut | aresOneOneByFourHundredGigMacSec128NonFanOut | aresOneOneByFourHundredGigMacSec256NonFanOut | aresOneTwoByTwoHundredGigFanOut | aresOneTwoByTwoHundredGigMacSecFanOut | aresOneFourByOneHundredGigFanOut | aresOneFourByOneHundredGigMacSecFanOut | aresOneEightByFiftyGigFanOut | uhdOneHundredEightByHundredGigNonFanOut | uhdOneHundredEightByFortyGigNonFanOut | uhdOneHundredSixteenByFiftyGigFanOut | uhdOneHundredThirtyTwoByTwentyFiveGigFanOut | uhdOneHundredThirtyTwoByTenGigFanOut | novus5GOneByTenGigNonFanOut | novus5GOneByTwentyFiveGigNonFanOut | novus5GOneByFiftyGigNonFanOut | novus5GOneByHundredGigNonFanOut | novus5GOneByHundredGigNonFanOutHighStream | starTwoByFourHundredGigNonFannedOutPAM4 | starTwoByFourHundredGigFannedOutPAM4RoCEv2 | starFourByTwoHundredGigFannedOutPAM4 | starFourByTwoHundredGigFannedOutPAM4RoCEv2 | starTwoByTwoHundredGigFannedOutNRZ | starEightByHundredGigFannedOutPAM4 | starEightByHundredGigFannedOutPAM4RoCEv2 | starFourByHundredGigFannedOutNRZRoCEv2 | starFourByHundredGigFannedOutNRZ | starSixteenByFiftyGigFannedOutPAM4 | starEightByFiftyGigFannedOutNRZ | starFourByFortyGigFannedOutNRZ | starSixteenByTwentyFiveGigFannedOutNRZ | starSixteenByTenGigFannedOutNRZ | starFourByHundredGigFannedOutPAM4HalfDensityHighStream | starEightByFiftyGigFannedOutPAM4HalfDensityHighStream | starEightByTwentyFiveGigFannedOutNRZHalfDensityHighStream | starEightByTenGigFannedOutNRZHalfDensityHighStream | novusHundredGigNonFanOutHighStream | novusFourByTwentyFiveGigNonFanOutHighStream | novusTwoByFiftyGigNonFanOutHighStream | novusOneByFortyGigNonFanOutHighStream | novusFourByTenGigNonFanOutHighStream | ravenEightByHundredGigFannedOutPAM4 | ravenFourByTwoHundredGigFannedOutPAM4 | ravenTwoByFourHundredGigFannedOutPAM4 | ravenOneByEightHundredGigNonFannedOutPAM4 | aresOneEightHundredQddCEightByHundredGigFannedOutPAM4 | aresOneEightHundredQddCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredQddCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredQddCOneByEightHundredGigNonFannedOutPAM4 | sertHundredGig | sertFiftyGig | sertFourtyGig | sertTwentyFiveGig | sertTenGig | aresOneEightHundredOsfpCEightByHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCOneByEightHundredGigNonFannedOutPAM4 | aresOne-M-OneByEightHundredGigPAM4-106G | aresOne-M-TwoByFourHundredGigPAM4-106G | aresOne-M-FourByTwoHundredGigPAM4-106G | aresOne-M-EightByOneHundredGigPAM4-106G | aresOne-M-OneByFourHundredGigPAM4-53G | aresOne-M-TwoByTwoHundredGigPAM4-53G | aresOne-M-FourByOneHundredGigPAM4-53G | aresOne-M-EightByFiftyGigPAM4-53G | aresOne-M-OneByTwoHundredGigNRZ-26G | aresOne-M-TwoByOneHundredGigNRZ-26G | aresOne-M-FourByFiftyGigNRZ-26G | aresOne-M-TwoByFortyGigNRZ-10G | aresOne-M-EightByTwentyFiveGigNRZ-26G | aresOne-M-EightByTenGigNRZ-10G | aresOne-M-OneByEightHundredGigPAM4-106G-RoCEv2 | aresOne-M-TwoByFourHundredGigPAM4-106G-RoCEv2 | aresOne-M-FourByTwoHundredGigPAM4-106G-RoCEv2 | aresOne-M-EightByOneHundredGigPAM4-106G-RoCEv2 | aresOne-M-OneByFourHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByTwoHundredGigPAM4-53G-RoCEv2 | aresOne-M-FourByOneHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByOneHundredGigNRZ-26G-RoCEv2])): Gets the supported resource group modes.
        - Mode (str(normal | tenGig | fortyGig | singleMode | dualMode | hundredGigNonFanOut | fortyGigFanOut | threeByTenGigFanOut | eightByTenGigFanOut | fourByTwentyFiveGigNonFanOut | twoByTwentyFiveGigNonFanOut | oneByFiftyGigNonFanOut | fortyGigNonFanOut | oneByTenGigFanOut | fourByTenGigFanOut | incompatibleMode | hundredGigCapturePlayback | fortyGigCapturePlayback | novusHundredGigNonFanOut | novusFourByTwentyFiveGigNonFanOut | novusTwoByFiftyGigNonFanOut | novusOneByFortyGigNonFanOut | novusFourByTenGigNonFanOut | krakenOneByFourHundredGigNonFanOut | krakenOneByTwoHundredGigNonFanOut | krakenTwoByOneHundredGigFanOut | krakenFourByFiftyGigFanOut | aresOneOneByFourHundredGigNonFanOut | aresOneOneByFourHundredGigMacSec128NonFanOut | aresOneOneByFourHundredGigMacSec256NonFanOut | aresOneTwoByTwoHundredGigFanOut | aresOneTwoByTwoHundredGigMacSecFanOut | aresOneFourByOneHundredGigFanOut | aresOneFourByOneHundredGigMacSecFanOut | aresOneEightByFiftyGigFanOut | uhdOneHundredEightByHundredGigNonFanOut | uhdOneHundredEightByFortyGigNonFanOut | uhdOneHundredSixteenByFiftyGigFanOut | uhdOneHundredThirtyTwoByTwentyFiveGigFanOut | uhdOneHundredThirtyTwoByTenGigFanOut | novus5GOneByTenGigNonFanOut | novus5GOneByTwentyFiveGigNonFanOut | novus5GOneByFiftyGigNonFanOut | novus5GOneByHundredGigNonFanOut | novus5GOneByHundredGigNonFanOutHighStream | starTwoByFourHundredGigNonFannedOutPAM4 | starTwoByFourHundredGigFannedOutPAM4RoCEv2 | starFourByTwoHundredGigFannedOutPAM4 | starFourByTwoHundredGigFannedOutPAM4RoCEv2 | starTwoByTwoHundredGigFannedOutNRZ | starEightByHundredGigFannedOutPAM4 | starEightByHundredGigFannedOutPAM4RoCEv2 | starFourByHundredGigFannedOutNRZRoCEv2 | starFourByHundredGigFannedOutNRZ | starSixteenByFiftyGigFannedOutPAM4 | starEightByFiftyGigFannedOutNRZ | starFourByFortyGigFannedOutNRZ | starSixteenByTwentyFiveGigFannedOutNRZ | starSixteenByTenGigFannedOutNRZ | starFourByHundredGigFannedOutPAM4HalfDensityHighStream | starEightByFiftyGigFannedOutPAM4HalfDensityHighStream | starEightByTwentyFiveGigFannedOutNRZHalfDensityHighStream | starEightByTenGigFannedOutNRZHalfDensityHighStream | novusHundredGigNonFanOutHighStream | novusFourByTwentyFiveGigNonFanOutHighStream | novusTwoByFiftyGigNonFanOutHighStream | novusOneByFortyGigNonFanOutHighStream | novusFourByTenGigNonFanOutHighStream | ravenEightByHundredGigFannedOutPAM4 | ravenFourByTwoHundredGigFannedOutPAM4 | ravenTwoByFourHundredGigFannedOutPAM4 | ravenOneByEightHundredGigNonFannedOutPAM4 | aresOneEightHundredQddCEightByHundredGigFannedOutPAM4 | aresOneEightHundredQddCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredQddCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredQddCOneByEightHundredGigNonFannedOutPAM4 | sertHundredGig | sertFiftyGig | sertFourtyGig | sertTwentyFiveGig | sertTenGig | aresOneEightHundredOsfpCEightByHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCOneByEightHundredGigNonFannedOutPAM4 | aresOne-M-OneByEightHundredGigPAM4-106G | aresOne-M-TwoByFourHundredGigPAM4-106G | aresOne-M-FourByTwoHundredGigPAM4-106G | aresOne-M-EightByOneHundredGigPAM4-106G | aresOne-M-OneByFourHundredGigPAM4-53G | aresOne-M-TwoByTwoHundredGigPAM4-53G | aresOne-M-FourByOneHundredGigPAM4-53G | aresOne-M-EightByFiftyGigPAM4-53G | aresOne-M-OneByTwoHundredGigNRZ-26G | aresOne-M-TwoByOneHundredGigNRZ-26G | aresOne-M-FourByFiftyGigNRZ-26G | aresOne-M-TwoByFortyGigNRZ-10G | aresOne-M-EightByTwentyFiveGigNRZ-26G | aresOne-M-EightByTenGigNRZ-10G | aresOne-M-OneByEightHundredGigPAM4-106G-RoCEv2 | aresOne-M-TwoByFourHundredGigPAM4-106G-RoCEv2 | aresOne-M-FourByTwoHundredGigPAM4-106G-RoCEv2 | aresOne-M-EightByOneHundredGigPAM4-106G-RoCEv2 | aresOne-M-OneByFourHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByTwoHundredGigPAM4-53G-RoCEv2 | aresOne-M-FourByOneHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByOneHundredGigNRZ-26G-RoCEv2)): Resource Group mode.
        - ResourcePorts (list(str[None | /api/v1/sessions/1/ixnetwork/availableHardware/chassis/card/port])): All ports from Resource Group.

        Returns
        -------
        - self: This instance with matching aggregation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of aggregation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the aggregation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
