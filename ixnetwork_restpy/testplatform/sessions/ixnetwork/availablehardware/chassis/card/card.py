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


class Card(Base):
    """This command allows the user to view version and type information for the card.
    The Card class encapsulates a list of card resources that are managed by the system.
    A list of resources can be retrieved from the server using the Card.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "card"
    _SDM_ATT_MAP = {
        "AggregationMode": "aggregationMode",
        "AggregationSupported": "aggregationSupported",
        "AvailableModes": "availableModes",
        "CardId": "cardId",
        "Description": "description",
        "PortNamingScheme": "portNamingScheme",
    }
    _SDM_ENUM_MAP = {
        "aggregationMode": [
            "notSupported",
            "mixed",
            "normal",
            "tenGigAggregation",
            "fortyGigAggregation",
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
        "portNamingScheme": ["v1", "v2"],
    }

    def __init__(self, parent, list_op=False):
        super(Card, self).__init__(parent, list_op)

    @property
    def Aggregation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.card.aggregation.aggregation.Aggregation): An instance of the Aggregation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.card.aggregation.aggregation import (
            Aggregation,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Aggregation", None) is not None:
                return self._properties.get("Aggregation")
        return Aggregation(self)

    @property
    def Port(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.card.port.port.Port): An instance of the Port class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.card.port.port import (
            Port,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Port", None) is not None:
                return self._properties.get("Port")
        return Port(self)

    @property
    def AggregationMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(notSupported | mixed | normal | tenGigAggregation | fortyGigAggregation | singleMode | dualMode | hundredGigNonFanOut | fortyGigFanOut | threeByTenGigFanOut | eightByTenGigFanOut | fourByTwentyFiveGigNonFanOut | twoByTwentyFiveGigNonFanOut | oneByFiftyGigNonFanOut | fortyGigNonFanOut | oneByTenGigFanOut | fourByTenGigFanOut | incompatibleMode | hundredGigCapturePlayback | fortyGigCapturePlayback | novusHundredGigNonFanOut | novusFourByTwentyFiveGigNonFanOut | novusTwoByFiftyGigNonFanOut | novusOneByFortyGigNonFanOut | novusFourByTenGigNonFanOut | krakenOneByFourHundredGigNonFanOut | krakenOneByTwoHundredGigNonFanOut | krakenTwoByOneHundredGigFanOut | krakenFourByFiftyGigFanOut | aresOneOneByFourHundredGigNonFanOut | aresOneOneByFourHundredGigMacSec128NonFanOut | aresOneOneByFourHundredGigMacSec256NonFanOut | aresOneTwoByTwoHundredGigFanOut | aresOneTwoByTwoHundredGigMacSecFanOut | aresOneFourByOneHundredGigFanOut | aresOneFourByOneHundredGigMacSecFanOut | aresOneEightByFiftyGigFanOut | uhdOneHundredEightByHundredGigNonFanOut | uhdOneHundredEightByFortyGigNonFanOut | uhdOneHundredSixteenByFiftyGigFanOut | uhdOneHundredThirtyTwoByTwentyFiveGigFanOut | uhdOneHundredThirtyTwoByTenGigFanOut | novus5GOneByTenGigNonFanOut | novus5GOneByTwentyFiveGigNonFanOut | novus5GOneByFiftyGigNonFanOut | novus5GOneByHundredGigNonFanOut | novus5GOneByHundredGigNonFanOutHighStream | starTwoByFourHundredGigNonFannedOutPAM4 | starTwoByFourHundredGigFannedOutPAM4RoCEv2 | starFourByTwoHundredGigFannedOutPAM4 | starFourByTwoHundredGigFannedOutPAM4RoCEv2 | starTwoByTwoHundredGigFannedOutNRZ | starEightByHundredGigFannedOutPAM4 | starEightByHundredGigFannedOutPAM4RoCEv2 | starFourByHundredGigFannedOutNRZRoCEv2 | starFourByHundredGigFannedOutNRZ | starSixteenByFiftyGigFannedOutPAM4 | starEightByFiftyGigFannedOutNRZ | starFourByFortyGigFannedOutNRZ | starSixteenByTwentyFiveGigFannedOutNRZ | starSixteenByTenGigFannedOutNRZ | starFourByHundredGigFannedOutPAM4HalfDensityHighStream | starEightByFiftyGigFannedOutPAM4HalfDensityHighStream | starEightByTwentyFiveGigFannedOutNRZHalfDensityHighStream | starEightByTenGigFannedOutNRZHalfDensityHighStream | novusHundredGigNonFanOutHighStream | novusFourByTwentyFiveGigNonFanOutHighStream | novusTwoByFiftyGigNonFanOutHighStream | novusOneByFortyGigNonFanOutHighStream | novusFourByTenGigNonFanOutHighStream | ravenEightByHundredGigFannedOutPAM4 | ravenFourByTwoHundredGigFannedOutPAM4 | ravenTwoByFourHundredGigFannedOutPAM4 | ravenOneByEightHundredGigNonFannedOutPAM4 | aresOneEightHundredQddCEightByHundredGigFannedOutPAM4 | aresOneEightHundredQddCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredQddCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredQddCOneByEightHundredGigNonFannedOutPAM4 | sertHundredGig | sertFiftyGig | sertFourtyGig | sertTwentyFiveGig | sertTenGig | aresOneEightHundredOsfpCEightByHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCOneByEightHundredGigNonFannedOutPAM4 | aresOne-M-OneByEightHundredGigPAM4-106G | aresOne-M-TwoByFourHundredGigPAM4-106G | aresOne-M-FourByTwoHundredGigPAM4-106G | aresOne-M-EightByOneHundredGigPAM4-106G | aresOne-M-OneByFourHundredGigPAM4-53G | aresOne-M-TwoByTwoHundredGigPAM4-53G | aresOne-M-FourByOneHundredGigPAM4-53G | aresOne-M-EightByFiftyGigPAM4-53G | aresOne-M-OneByTwoHundredGigNRZ-26G | aresOne-M-TwoByOneHundredGigNRZ-26G | aresOne-M-FourByFiftyGigNRZ-26G | aresOne-M-TwoByFortyGigNRZ-10G | aresOne-M-EightByTwentyFiveGigNRZ-26G | aresOne-M-EightByTenGigNRZ-10G | aresOne-M-OneByEightHundredGigPAM4-106G-RoCEv2 | aresOne-M-TwoByFourHundredGigPAM4-106G-RoCEv2 | aresOne-M-FourByTwoHundredGigPAM4-106G-RoCEv2 | aresOne-M-EightByOneHundredGigPAM4-106G-RoCEv2 | aresOne-M-OneByFourHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByTwoHundredGigPAM4-53G-RoCEv2 | aresOne-M-FourByOneHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByOneHundredGigNRZ-26G-RoCEv2): Gets or sets the aggregation mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AggregationMode"])

    @AggregationMode.setter
    def AggregationMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AggregationMode"], value)

    @property
    def AggregationSupported(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: (read only) If true, indicates that the card is operating in resource group mode and not in normal mode
        """
        return self._get_attribute(self._SDM_ATT_MAP["AggregationSupported"])

    @property
    def AvailableModes(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[notSupported | mixed | normal | tenGigAggregation | fortyGigAggregation | singleMode | dualMode | hundredGigNonFanOut | fortyGigFanOut | threeByTenGigFanOut | eightByTenGigFanOut | fourByTwentyFiveGigNonFanOut | twoByTwentyFiveGigNonFanOut | oneByFiftyGigNonFanOut | fortyGigNonFanOut | oneByTenGigFanOut | fourByTenGigFanOut | incompatibleMode | hundredGigCapturePlayback | fortyGigCapturePlayback | novusHundredGigNonFanOut | novusFourByTwentyFiveGigNonFanOut | novusTwoByFiftyGigNonFanOut | novusOneByFortyGigNonFanOut | novusFourByTenGigNonFanOut | krakenOneByFourHundredGigNonFanOut | krakenOneByTwoHundredGigNonFanOut | krakenTwoByOneHundredGigFanOut | krakenFourByFiftyGigFanOut | aresOneOneByFourHundredGigNonFanOut | aresOneOneByFourHundredGigMacSec128NonFanOut | aresOneOneByFourHundredGigMacSec256NonFanOut | aresOneTwoByTwoHundredGigFanOut | aresOneTwoByTwoHundredGigMacSecFanOut | aresOneFourByOneHundredGigFanOut | aresOneFourByOneHundredGigMacSecFanOut | aresOneEightByFiftyGigFanOut | uhdOneHundredEightByHundredGigNonFanOut | uhdOneHundredEightByFortyGigNonFanOut | uhdOneHundredSixteenByFiftyGigFanOut | uhdOneHundredThirtyTwoByTwentyFiveGigFanOut | uhdOneHundredThirtyTwoByTenGigFanOut | novus5GOneByTenGigNonFanOut | novus5GOneByTwentyFiveGigNonFanOut | novus5GOneByFiftyGigNonFanOut | novus5GOneByHundredGigNonFanOut | novus5GOneByHundredGigNonFanOutHighStream | starTwoByFourHundredGigNonFannedOutPAM4 | starTwoByFourHundredGigFannedOutPAM4RoCEv2 | starFourByTwoHundredGigFannedOutPAM4 | starFourByTwoHundredGigFannedOutPAM4RoCEv2 | starTwoByTwoHundredGigFannedOutNRZ | starEightByHundredGigFannedOutPAM4 | starEightByHundredGigFannedOutPAM4RoCEv2 | starFourByHundredGigFannedOutNRZRoCEv2 | starFourByHundredGigFannedOutNRZ | starSixteenByFiftyGigFannedOutPAM4 | starEightByFiftyGigFannedOutNRZ | starFourByFortyGigFannedOutNRZ | starSixteenByTwentyFiveGigFannedOutNRZ | starSixteenByTenGigFannedOutNRZ | starFourByHundredGigFannedOutPAM4HalfDensityHighStream | starEightByFiftyGigFannedOutPAM4HalfDensityHighStream | starEightByTwentyFiveGigFannedOutNRZHalfDensityHighStream | starEightByTenGigFannedOutNRZHalfDensityHighStream | novusHundredGigNonFanOutHighStream | novusFourByTwentyFiveGigNonFanOutHighStream | novusTwoByFiftyGigNonFanOutHighStream | novusOneByFortyGigNonFanOutHighStream | novusFourByTenGigNonFanOutHighStream | ravenEightByHundredGigFannedOutPAM4 | ravenFourByTwoHundredGigFannedOutPAM4 | ravenTwoByFourHundredGigFannedOutPAM4 | ravenOneByEightHundredGigNonFannedOutPAM4 | aresOneEightHundredQddCEightByHundredGigFannedOutPAM4 | aresOneEightHundredQddCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredQddCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredQddCOneByEightHundredGigNonFannedOutPAM4 | sertHundredGig | sertFiftyGig | sertFourtyGig | sertTwentyFiveGig | sertTenGig | aresOneEightHundredOsfpCEightByHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCOneByEightHundredGigNonFannedOutPAM4 | aresOne-M-OneByEightHundredGigPAM4-106G | aresOne-M-TwoByFourHundredGigPAM4-106G | aresOne-M-FourByTwoHundredGigPAM4-106G | aresOne-M-EightByOneHundredGigPAM4-106G | aresOne-M-OneByFourHundredGigPAM4-53G | aresOne-M-TwoByTwoHundredGigPAM4-53G | aresOne-M-FourByOneHundredGigPAM4-53G | aresOne-M-EightByFiftyGigPAM4-53G | aresOne-M-OneByTwoHundredGigNRZ-26G | aresOne-M-TwoByOneHundredGigNRZ-26G | aresOne-M-FourByFiftyGigNRZ-26G | aresOne-M-TwoByFortyGigNRZ-10G | aresOne-M-EightByTwentyFiveGigNRZ-26G | aresOne-M-EightByTenGigNRZ-10G | aresOne-M-OneByEightHundredGigPAM4-106G-RoCEv2 | aresOne-M-TwoByFourHundredGigPAM4-106G-RoCEv2 | aresOne-M-FourByTwoHundredGigPAM4-106G-RoCEv2 | aresOne-M-EightByOneHundredGigPAM4-106G-RoCEv2 | aresOne-M-OneByFourHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByTwoHundredGigPAM4-53G-RoCEv2 | aresOne-M-FourByOneHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByOneHundredGigNRZ-26G-RoCEv2]): Gets the supported port resource group modes on the card.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AvailableModes"])

    @property
    def CardId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Identifier for the card on the chassis.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CardId"])

    @property
    def Description(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Description of the card.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Description"])

    @property
    def PortNamingScheme(self):
        # type: () -> str
        """
        Returns
        -------
        - str(v1 | v2):
        """
        return self._get_attribute(self._SDM_ATT_MAP["PortNamingScheme"])

    def update(self, AggregationMode=None):
        # type: (str) -> Card
        """Updates card resource on the server.

        Args
        ----
        - AggregationMode (str(notSupported | mixed | normal | tenGigAggregation | fortyGigAggregation | singleMode | dualMode | hundredGigNonFanOut | fortyGigFanOut | threeByTenGigFanOut | eightByTenGigFanOut | fourByTwentyFiveGigNonFanOut | twoByTwentyFiveGigNonFanOut | oneByFiftyGigNonFanOut | fortyGigNonFanOut | oneByTenGigFanOut | fourByTenGigFanOut | incompatibleMode | hundredGigCapturePlayback | fortyGigCapturePlayback | novusHundredGigNonFanOut | novusFourByTwentyFiveGigNonFanOut | novusTwoByFiftyGigNonFanOut | novusOneByFortyGigNonFanOut | novusFourByTenGigNonFanOut | krakenOneByFourHundredGigNonFanOut | krakenOneByTwoHundredGigNonFanOut | krakenTwoByOneHundredGigFanOut | krakenFourByFiftyGigFanOut | aresOneOneByFourHundredGigNonFanOut | aresOneOneByFourHundredGigMacSec128NonFanOut | aresOneOneByFourHundredGigMacSec256NonFanOut | aresOneTwoByTwoHundredGigFanOut | aresOneTwoByTwoHundredGigMacSecFanOut | aresOneFourByOneHundredGigFanOut | aresOneFourByOneHundredGigMacSecFanOut | aresOneEightByFiftyGigFanOut | uhdOneHundredEightByHundredGigNonFanOut | uhdOneHundredEightByFortyGigNonFanOut | uhdOneHundredSixteenByFiftyGigFanOut | uhdOneHundredThirtyTwoByTwentyFiveGigFanOut | uhdOneHundredThirtyTwoByTenGigFanOut | novus5GOneByTenGigNonFanOut | novus5GOneByTwentyFiveGigNonFanOut | novus5GOneByFiftyGigNonFanOut | novus5GOneByHundredGigNonFanOut | novus5GOneByHundredGigNonFanOutHighStream | starTwoByFourHundredGigNonFannedOutPAM4 | starTwoByFourHundredGigFannedOutPAM4RoCEv2 | starFourByTwoHundredGigFannedOutPAM4 | starFourByTwoHundredGigFannedOutPAM4RoCEv2 | starTwoByTwoHundredGigFannedOutNRZ | starEightByHundredGigFannedOutPAM4 | starEightByHundredGigFannedOutPAM4RoCEv2 | starFourByHundredGigFannedOutNRZRoCEv2 | starFourByHundredGigFannedOutNRZ | starSixteenByFiftyGigFannedOutPAM4 | starEightByFiftyGigFannedOutNRZ | starFourByFortyGigFannedOutNRZ | starSixteenByTwentyFiveGigFannedOutNRZ | starSixteenByTenGigFannedOutNRZ | starFourByHundredGigFannedOutPAM4HalfDensityHighStream | starEightByFiftyGigFannedOutPAM4HalfDensityHighStream | starEightByTwentyFiveGigFannedOutNRZHalfDensityHighStream | starEightByTenGigFannedOutNRZHalfDensityHighStream | novusHundredGigNonFanOutHighStream | novusFourByTwentyFiveGigNonFanOutHighStream | novusTwoByFiftyGigNonFanOutHighStream | novusOneByFortyGigNonFanOutHighStream | novusFourByTenGigNonFanOutHighStream | ravenEightByHundredGigFannedOutPAM4 | ravenFourByTwoHundredGigFannedOutPAM4 | ravenTwoByFourHundredGigFannedOutPAM4 | ravenOneByEightHundredGigNonFannedOutPAM4 | aresOneEightHundredQddCEightByHundredGigFannedOutPAM4 | aresOneEightHundredQddCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredQddCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredQddCOneByEightHundredGigNonFannedOutPAM4 | sertHundredGig | sertFiftyGig | sertFourtyGig | sertTwentyFiveGig | sertTenGig | aresOneEightHundredOsfpCEightByHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCOneByEightHundredGigNonFannedOutPAM4 | aresOne-M-OneByEightHundredGigPAM4-106G | aresOne-M-TwoByFourHundredGigPAM4-106G | aresOne-M-FourByTwoHundredGigPAM4-106G | aresOne-M-EightByOneHundredGigPAM4-106G | aresOne-M-OneByFourHundredGigPAM4-53G | aresOne-M-TwoByTwoHundredGigPAM4-53G | aresOne-M-FourByOneHundredGigPAM4-53G | aresOne-M-EightByFiftyGigPAM4-53G | aresOne-M-OneByTwoHundredGigNRZ-26G | aresOne-M-TwoByOneHundredGigNRZ-26G | aresOne-M-FourByFiftyGigNRZ-26G | aresOne-M-TwoByFortyGigNRZ-10G | aresOne-M-EightByTwentyFiveGigNRZ-26G | aresOne-M-EightByTenGigNRZ-10G | aresOne-M-OneByEightHundredGigPAM4-106G-RoCEv2 | aresOne-M-TwoByFourHundredGigPAM4-106G-RoCEv2 | aresOne-M-FourByTwoHundredGigPAM4-106G-RoCEv2 | aresOne-M-EightByOneHundredGigPAM4-106G-RoCEv2 | aresOne-M-OneByFourHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByTwoHundredGigPAM4-53G-RoCEv2 | aresOne-M-FourByOneHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByOneHundredGigNRZ-26G-RoCEv2)): Gets or sets the aggregation mode.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AggregationMode=None):
        # type: (str) -> Card
        """Adds a new card resource on the json, only valid with batch add utility

        Args
        ----
        - AggregationMode (str(notSupported | mixed | normal | tenGigAggregation | fortyGigAggregation | singleMode | dualMode | hundredGigNonFanOut | fortyGigFanOut | threeByTenGigFanOut | eightByTenGigFanOut | fourByTwentyFiveGigNonFanOut | twoByTwentyFiveGigNonFanOut | oneByFiftyGigNonFanOut | fortyGigNonFanOut | oneByTenGigFanOut | fourByTenGigFanOut | incompatibleMode | hundredGigCapturePlayback | fortyGigCapturePlayback | novusHundredGigNonFanOut | novusFourByTwentyFiveGigNonFanOut | novusTwoByFiftyGigNonFanOut | novusOneByFortyGigNonFanOut | novusFourByTenGigNonFanOut | krakenOneByFourHundredGigNonFanOut | krakenOneByTwoHundredGigNonFanOut | krakenTwoByOneHundredGigFanOut | krakenFourByFiftyGigFanOut | aresOneOneByFourHundredGigNonFanOut | aresOneOneByFourHundredGigMacSec128NonFanOut | aresOneOneByFourHundredGigMacSec256NonFanOut | aresOneTwoByTwoHundredGigFanOut | aresOneTwoByTwoHundredGigMacSecFanOut | aresOneFourByOneHundredGigFanOut | aresOneFourByOneHundredGigMacSecFanOut | aresOneEightByFiftyGigFanOut | uhdOneHundredEightByHundredGigNonFanOut | uhdOneHundredEightByFortyGigNonFanOut | uhdOneHundredSixteenByFiftyGigFanOut | uhdOneHundredThirtyTwoByTwentyFiveGigFanOut | uhdOneHundredThirtyTwoByTenGigFanOut | novus5GOneByTenGigNonFanOut | novus5GOneByTwentyFiveGigNonFanOut | novus5GOneByFiftyGigNonFanOut | novus5GOneByHundredGigNonFanOut | novus5GOneByHundredGigNonFanOutHighStream | starTwoByFourHundredGigNonFannedOutPAM4 | starTwoByFourHundredGigFannedOutPAM4RoCEv2 | starFourByTwoHundredGigFannedOutPAM4 | starFourByTwoHundredGigFannedOutPAM4RoCEv2 | starTwoByTwoHundredGigFannedOutNRZ | starEightByHundredGigFannedOutPAM4 | starEightByHundredGigFannedOutPAM4RoCEv2 | starFourByHundredGigFannedOutNRZRoCEv2 | starFourByHundredGigFannedOutNRZ | starSixteenByFiftyGigFannedOutPAM4 | starEightByFiftyGigFannedOutNRZ | starFourByFortyGigFannedOutNRZ | starSixteenByTwentyFiveGigFannedOutNRZ | starSixteenByTenGigFannedOutNRZ | starFourByHundredGigFannedOutPAM4HalfDensityHighStream | starEightByFiftyGigFannedOutPAM4HalfDensityHighStream | starEightByTwentyFiveGigFannedOutNRZHalfDensityHighStream | starEightByTenGigFannedOutNRZHalfDensityHighStream | novusHundredGigNonFanOutHighStream | novusFourByTwentyFiveGigNonFanOutHighStream | novusTwoByFiftyGigNonFanOutHighStream | novusOneByFortyGigNonFanOutHighStream | novusFourByTenGigNonFanOutHighStream | ravenEightByHundredGigFannedOutPAM4 | ravenFourByTwoHundredGigFannedOutPAM4 | ravenTwoByFourHundredGigFannedOutPAM4 | ravenOneByEightHundredGigNonFannedOutPAM4 | aresOneEightHundredQddCEightByHundredGigFannedOutPAM4 | aresOneEightHundredQddCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredQddCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredQddCOneByEightHundredGigNonFannedOutPAM4 | sertHundredGig | sertFiftyGig | sertFourtyGig | sertTwentyFiveGig | sertTenGig | aresOneEightHundredOsfpCEightByHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCOneByEightHundredGigNonFannedOutPAM4 | aresOne-M-OneByEightHundredGigPAM4-106G | aresOne-M-TwoByFourHundredGigPAM4-106G | aresOne-M-FourByTwoHundredGigPAM4-106G | aresOne-M-EightByOneHundredGigPAM4-106G | aresOne-M-OneByFourHundredGigPAM4-53G | aresOne-M-TwoByTwoHundredGigPAM4-53G | aresOne-M-FourByOneHundredGigPAM4-53G | aresOne-M-EightByFiftyGigPAM4-53G | aresOne-M-OneByTwoHundredGigNRZ-26G | aresOne-M-TwoByOneHundredGigNRZ-26G | aresOne-M-FourByFiftyGigNRZ-26G | aresOne-M-TwoByFortyGigNRZ-10G | aresOne-M-EightByTwentyFiveGigNRZ-26G | aresOne-M-EightByTenGigNRZ-10G | aresOne-M-OneByEightHundredGigPAM4-106G-RoCEv2 | aresOne-M-TwoByFourHundredGigPAM4-106G-RoCEv2 | aresOne-M-FourByTwoHundredGigPAM4-106G-RoCEv2 | aresOne-M-EightByOneHundredGigPAM4-106G-RoCEv2 | aresOne-M-OneByFourHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByTwoHundredGigPAM4-53G-RoCEv2 | aresOne-M-FourByOneHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByOneHundredGigNRZ-26G-RoCEv2)): Gets or sets the aggregation mode.

        Returns
        -------
        - self: This instance with all currently retrieved card resources using find and the newly added card resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AggregationMode=None,
        AggregationSupported=None,
        AvailableModes=None,
        CardId=None,
        Description=None,
        PortNamingScheme=None,
    ):
        # type: (str, bool, List[str], int, str, str) -> Card
        """Finds and retrieves card resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve card resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all card resources from the server.

        Args
        ----
        - AggregationMode (str(notSupported | mixed | normal | tenGigAggregation | fortyGigAggregation | singleMode | dualMode | hundredGigNonFanOut | fortyGigFanOut | threeByTenGigFanOut | eightByTenGigFanOut | fourByTwentyFiveGigNonFanOut | twoByTwentyFiveGigNonFanOut | oneByFiftyGigNonFanOut | fortyGigNonFanOut | oneByTenGigFanOut | fourByTenGigFanOut | incompatibleMode | hundredGigCapturePlayback | fortyGigCapturePlayback | novusHundredGigNonFanOut | novusFourByTwentyFiveGigNonFanOut | novusTwoByFiftyGigNonFanOut | novusOneByFortyGigNonFanOut | novusFourByTenGigNonFanOut | krakenOneByFourHundredGigNonFanOut | krakenOneByTwoHundredGigNonFanOut | krakenTwoByOneHundredGigFanOut | krakenFourByFiftyGigFanOut | aresOneOneByFourHundredGigNonFanOut | aresOneOneByFourHundredGigMacSec128NonFanOut | aresOneOneByFourHundredGigMacSec256NonFanOut | aresOneTwoByTwoHundredGigFanOut | aresOneTwoByTwoHundredGigMacSecFanOut | aresOneFourByOneHundredGigFanOut | aresOneFourByOneHundredGigMacSecFanOut | aresOneEightByFiftyGigFanOut | uhdOneHundredEightByHundredGigNonFanOut | uhdOneHundredEightByFortyGigNonFanOut | uhdOneHundredSixteenByFiftyGigFanOut | uhdOneHundredThirtyTwoByTwentyFiveGigFanOut | uhdOneHundredThirtyTwoByTenGigFanOut | novus5GOneByTenGigNonFanOut | novus5GOneByTwentyFiveGigNonFanOut | novus5GOneByFiftyGigNonFanOut | novus5GOneByHundredGigNonFanOut | novus5GOneByHundredGigNonFanOutHighStream | starTwoByFourHundredGigNonFannedOutPAM4 | starTwoByFourHundredGigFannedOutPAM4RoCEv2 | starFourByTwoHundredGigFannedOutPAM4 | starFourByTwoHundredGigFannedOutPAM4RoCEv2 | starTwoByTwoHundredGigFannedOutNRZ | starEightByHundredGigFannedOutPAM4 | starEightByHundredGigFannedOutPAM4RoCEv2 | starFourByHundredGigFannedOutNRZRoCEv2 | starFourByHundredGigFannedOutNRZ | starSixteenByFiftyGigFannedOutPAM4 | starEightByFiftyGigFannedOutNRZ | starFourByFortyGigFannedOutNRZ | starSixteenByTwentyFiveGigFannedOutNRZ | starSixteenByTenGigFannedOutNRZ | starFourByHundredGigFannedOutPAM4HalfDensityHighStream | starEightByFiftyGigFannedOutPAM4HalfDensityHighStream | starEightByTwentyFiveGigFannedOutNRZHalfDensityHighStream | starEightByTenGigFannedOutNRZHalfDensityHighStream | novusHundredGigNonFanOutHighStream | novusFourByTwentyFiveGigNonFanOutHighStream | novusTwoByFiftyGigNonFanOutHighStream | novusOneByFortyGigNonFanOutHighStream | novusFourByTenGigNonFanOutHighStream | ravenEightByHundredGigFannedOutPAM4 | ravenFourByTwoHundredGigFannedOutPAM4 | ravenTwoByFourHundredGigFannedOutPAM4 | ravenOneByEightHundredGigNonFannedOutPAM4 | aresOneEightHundredQddCEightByHundredGigFannedOutPAM4 | aresOneEightHundredQddCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredQddCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredQddCOneByEightHundredGigNonFannedOutPAM4 | sertHundredGig | sertFiftyGig | sertFourtyGig | sertTwentyFiveGig | sertTenGig | aresOneEightHundredOsfpCEightByHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCOneByEightHundredGigNonFannedOutPAM4 | aresOne-M-OneByEightHundredGigPAM4-106G | aresOne-M-TwoByFourHundredGigPAM4-106G | aresOne-M-FourByTwoHundredGigPAM4-106G | aresOne-M-EightByOneHundredGigPAM4-106G | aresOne-M-OneByFourHundredGigPAM4-53G | aresOne-M-TwoByTwoHundredGigPAM4-53G | aresOne-M-FourByOneHundredGigPAM4-53G | aresOne-M-EightByFiftyGigPAM4-53G | aresOne-M-OneByTwoHundredGigNRZ-26G | aresOne-M-TwoByOneHundredGigNRZ-26G | aresOne-M-FourByFiftyGigNRZ-26G | aresOne-M-TwoByFortyGigNRZ-10G | aresOne-M-EightByTwentyFiveGigNRZ-26G | aresOne-M-EightByTenGigNRZ-10G | aresOne-M-OneByEightHundredGigPAM4-106G-RoCEv2 | aresOne-M-TwoByFourHundredGigPAM4-106G-RoCEv2 | aresOne-M-FourByTwoHundredGigPAM4-106G-RoCEv2 | aresOne-M-EightByOneHundredGigPAM4-106G-RoCEv2 | aresOne-M-OneByFourHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByTwoHundredGigPAM4-53G-RoCEv2 | aresOne-M-FourByOneHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByOneHundredGigNRZ-26G-RoCEv2)): Gets or sets the aggregation mode.
        - AggregationSupported (bool): (read only) If true, indicates that the card is operating in resource group mode and not in normal mode
        - AvailableModes (list(str[notSupported | mixed | normal | tenGigAggregation | fortyGigAggregation | singleMode | dualMode | hundredGigNonFanOut | fortyGigFanOut | threeByTenGigFanOut | eightByTenGigFanOut | fourByTwentyFiveGigNonFanOut | twoByTwentyFiveGigNonFanOut | oneByFiftyGigNonFanOut | fortyGigNonFanOut | oneByTenGigFanOut | fourByTenGigFanOut | incompatibleMode | hundredGigCapturePlayback | fortyGigCapturePlayback | novusHundredGigNonFanOut | novusFourByTwentyFiveGigNonFanOut | novusTwoByFiftyGigNonFanOut | novusOneByFortyGigNonFanOut | novusFourByTenGigNonFanOut | krakenOneByFourHundredGigNonFanOut | krakenOneByTwoHundredGigNonFanOut | krakenTwoByOneHundredGigFanOut | krakenFourByFiftyGigFanOut | aresOneOneByFourHundredGigNonFanOut | aresOneOneByFourHundredGigMacSec128NonFanOut | aresOneOneByFourHundredGigMacSec256NonFanOut | aresOneTwoByTwoHundredGigFanOut | aresOneTwoByTwoHundredGigMacSecFanOut | aresOneFourByOneHundredGigFanOut | aresOneFourByOneHundredGigMacSecFanOut | aresOneEightByFiftyGigFanOut | uhdOneHundredEightByHundredGigNonFanOut | uhdOneHundredEightByFortyGigNonFanOut | uhdOneHundredSixteenByFiftyGigFanOut | uhdOneHundredThirtyTwoByTwentyFiveGigFanOut | uhdOneHundredThirtyTwoByTenGigFanOut | novus5GOneByTenGigNonFanOut | novus5GOneByTwentyFiveGigNonFanOut | novus5GOneByFiftyGigNonFanOut | novus5GOneByHundredGigNonFanOut | novus5GOneByHundredGigNonFanOutHighStream | starTwoByFourHundredGigNonFannedOutPAM4 | starTwoByFourHundredGigFannedOutPAM4RoCEv2 | starFourByTwoHundredGigFannedOutPAM4 | starFourByTwoHundredGigFannedOutPAM4RoCEv2 | starTwoByTwoHundredGigFannedOutNRZ | starEightByHundredGigFannedOutPAM4 | starEightByHundredGigFannedOutPAM4RoCEv2 | starFourByHundredGigFannedOutNRZRoCEv2 | starFourByHundredGigFannedOutNRZ | starSixteenByFiftyGigFannedOutPAM4 | starEightByFiftyGigFannedOutNRZ | starFourByFortyGigFannedOutNRZ | starSixteenByTwentyFiveGigFannedOutNRZ | starSixteenByTenGigFannedOutNRZ | starFourByHundredGigFannedOutPAM4HalfDensityHighStream | starEightByFiftyGigFannedOutPAM4HalfDensityHighStream | starEightByTwentyFiveGigFannedOutNRZHalfDensityHighStream | starEightByTenGigFannedOutNRZHalfDensityHighStream | novusHundredGigNonFanOutHighStream | novusFourByTwentyFiveGigNonFanOutHighStream | novusTwoByFiftyGigNonFanOutHighStream | novusOneByFortyGigNonFanOutHighStream | novusFourByTenGigNonFanOutHighStream | ravenEightByHundredGigFannedOutPAM4 | ravenFourByTwoHundredGigFannedOutPAM4 | ravenTwoByFourHundredGigFannedOutPAM4 | ravenOneByEightHundredGigNonFannedOutPAM4 | aresOneEightHundredQddCEightByHundredGigFannedOutPAM4 | aresOneEightHundredQddCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredQddCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredQddCOneByEightHundredGigNonFannedOutPAM4 | sertHundredGig | sertFiftyGig | sertFourtyGig | sertTwentyFiveGig | sertTenGig | aresOneEightHundredOsfpCEightByHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCOneByEightHundredGigNonFannedOutPAM4 | aresOne-M-OneByEightHundredGigPAM4-106G | aresOne-M-TwoByFourHundredGigPAM4-106G | aresOne-M-FourByTwoHundredGigPAM4-106G | aresOne-M-EightByOneHundredGigPAM4-106G | aresOne-M-OneByFourHundredGigPAM4-53G | aresOne-M-TwoByTwoHundredGigPAM4-53G | aresOne-M-FourByOneHundredGigPAM4-53G | aresOne-M-EightByFiftyGigPAM4-53G | aresOne-M-OneByTwoHundredGigNRZ-26G | aresOne-M-TwoByOneHundredGigNRZ-26G | aresOne-M-FourByFiftyGigNRZ-26G | aresOne-M-TwoByFortyGigNRZ-10G | aresOne-M-EightByTwentyFiveGigNRZ-26G | aresOne-M-EightByTenGigNRZ-10G | aresOne-M-OneByEightHundredGigPAM4-106G-RoCEv2 | aresOne-M-TwoByFourHundredGigPAM4-106G-RoCEv2 | aresOne-M-FourByTwoHundredGigPAM4-106G-RoCEv2 | aresOne-M-EightByOneHundredGigPAM4-106G-RoCEv2 | aresOne-M-OneByFourHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByTwoHundredGigPAM4-53G-RoCEv2 | aresOne-M-FourByOneHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByOneHundredGigNRZ-26G-RoCEv2])): Gets the supported port resource group modes on the card.
        - CardId (number): Identifier for the card on the chassis.
        - Description (str): Description of the card.
        - PortNamingScheme (str(v1 | v2)):

        Returns
        -------
        - self: This instance with matching card resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of card data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the card resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def HotswapCard(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the hotswapCard operation on the server.

        API to perform chassis card hotswap

        hotswapCard(async_operation=bool)
        ---------------------------------
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
        return self._execute("hotswapCard", payload=payload, response_object=None)

    def RefreshInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the refreshInfo operation on the server.

        Refresh the hardware information.

        refreshInfo(async_operation=bool)
        ---------------------------------
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
        return self._execute("refreshInfo", payload=payload, response_object=None)
