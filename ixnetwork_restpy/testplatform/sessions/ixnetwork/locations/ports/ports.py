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


class Ports(Base):
    """
    The Ports class encapsulates a list of ports resources that are managed by the system.
    A list of resources can be retrieved from the server using the Ports.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "ports"
    _SDM_ATT_MAP = {
        "Description": "description",
        "IsAvailable": "isAvailable",
        "IsBusy": "isBusy",
        "IsLinkUp": "isLinkUp",
        "Location": "location",
        "Owner": "owner",
        "PeerPortDescription": "peerPortDescription",
        "PeerPortId": "peerPortId",
        "PeerSystemIp": "peerSystemIp",
        "PeerSystemMac": "peerSystemMac",
        "PeerSystemName": "peerSystemName",
        "ResourceMode": "resourceMode",
    }
    _SDM_ENUM_MAP = {
        "resourceMode": [
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
            "notApplicable",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(Ports, self).__init__(parent, list_op)

    @property
    def Description(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Port description.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Description"])

    @property
    def IsAvailable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Is port ownership with current user.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsAvailable"])

    @property
    def IsBusy(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Is port in transition, being connected or released.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsBusy"])

    @property
    def IsLinkUp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Is port in link up state.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsLinkUp"])

    @property
    def Location(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Connecton information of this port. When location is assigned IxNetwork will try to connect to the device if the device is not connected.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Location"])

    @property
    def Owner(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Port owner.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Owner"])

    @property
    def PeerPortDescription(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Discovered peer port description.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeerPortDescription"])

    @property
    def PeerPortId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The port ID of the discovered peer port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeerPortId"])

    @property
    def PeerSystemIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The IP address of the discovered peer system.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeerSystemIp"])

    @property
    def PeerSystemMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The MAC address of the discovered peer system.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeerSystemMac"])

    @property
    def PeerSystemName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The system name of the discovered peer.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PeerSystemName"])

    @property
    def ResourceMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(normal | tenGig | fortyGig | singleMode | dualMode | hundredGigNonFanOut | fortyGigFanOut | threeByTenGigFanOut | eightByTenGigFanOut | fourByTwentyFiveGigNonFanOut | twoByTwentyFiveGigNonFanOut | oneByFiftyGigNonFanOut | fortyGigNonFanOut | oneByTenGigFanOut | fourByTenGigFanOut | incompatibleMode | hundredGigCapturePlayback | fortyGigCapturePlayback | novusHundredGigNonFanOut | novusFourByTwentyFiveGigNonFanOut | novusTwoByFiftyGigNonFanOut | novusOneByFortyGigNonFanOut | novusFourByTenGigNonFanOut | krakenOneByFourHundredGigNonFanOut | krakenOneByTwoHundredGigNonFanOut | krakenTwoByOneHundredGigFanOut | krakenFourByFiftyGigFanOut | aresOneOneByFourHundredGigNonFanOut | aresOneOneByFourHundredGigMacSec128NonFanOut | aresOneOneByFourHundredGigMacSec256NonFanOut | aresOneTwoByTwoHundredGigFanOut | aresOneTwoByTwoHundredGigMacSecFanOut | aresOneFourByOneHundredGigFanOut | aresOneFourByOneHundredGigMacSecFanOut | aresOneEightByFiftyGigFanOut | uhdOneHundredEightByHundredGigNonFanOut | uhdOneHundredEightByFortyGigNonFanOut | uhdOneHundredSixteenByFiftyGigFanOut | uhdOneHundredThirtyTwoByTwentyFiveGigFanOut | uhdOneHundredThirtyTwoByTenGigFanOut | novus5GOneByTenGigNonFanOut | novus5GOneByTwentyFiveGigNonFanOut | novus5GOneByFiftyGigNonFanOut | novus5GOneByHundredGigNonFanOut | novus5GOneByHundredGigNonFanOutHighStream | starTwoByFourHundredGigNonFannedOutPAM4 | starTwoByFourHundredGigFannedOutPAM4RoCEv2 | starFourByTwoHundredGigFannedOutPAM4 | starFourByTwoHundredGigFannedOutPAM4RoCEv2 | starTwoByTwoHundredGigFannedOutNRZ | starEightByHundredGigFannedOutPAM4 | starEightByHundredGigFannedOutPAM4RoCEv2 | starFourByHundredGigFannedOutNRZRoCEv2 | starFourByHundredGigFannedOutNRZ | starSixteenByFiftyGigFannedOutPAM4 | starEightByFiftyGigFannedOutNRZ | starFourByFortyGigFannedOutNRZ | starSixteenByTwentyFiveGigFannedOutNRZ | starSixteenByTenGigFannedOutNRZ | starFourByHundredGigFannedOutPAM4HalfDensityHighStream | starEightByFiftyGigFannedOutPAM4HalfDensityHighStream | starEightByTwentyFiveGigFannedOutNRZHalfDensityHighStream | starEightByTenGigFannedOutNRZHalfDensityHighStream | novusHundredGigNonFanOutHighStream | novusFourByTwentyFiveGigNonFanOutHighStream | novusTwoByFiftyGigNonFanOutHighStream | novusOneByFortyGigNonFanOutHighStream | novusFourByTenGigNonFanOutHighStream | ravenEightByHundredGigFannedOutPAM4 | ravenFourByTwoHundredGigFannedOutPAM4 | ravenTwoByFourHundredGigFannedOutPAM4 | ravenOneByEightHundredGigNonFannedOutPAM4 | aresOneEightHundredQddCEightByHundredGigFannedOutPAM4 | aresOneEightHundredQddCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredQddCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredQddCOneByEightHundredGigNonFannedOutPAM4 | sertHundredGig | sertFiftyGig | sertFourtyGig | sertTwentyFiveGig | sertTenGig | aresOneEightHundredOsfpCEightByHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCOneByEightHundredGigNonFannedOutPAM4 | aresOne-M-OneByEightHundredGigPAM4-106G | aresOne-M-TwoByFourHundredGigPAM4-106G | aresOne-M-FourByTwoHundredGigPAM4-106G | aresOne-M-EightByOneHundredGigPAM4-106G | aresOne-M-OneByFourHundredGigPAM4-53G | aresOne-M-TwoByTwoHundredGigPAM4-53G | aresOne-M-FourByOneHundredGigPAM4-53G | aresOne-M-EightByFiftyGigPAM4-53G | aresOne-M-OneByTwoHundredGigNRZ-26G | aresOne-M-TwoByOneHundredGigNRZ-26G | aresOne-M-FourByFiftyGigNRZ-26G | aresOne-M-TwoByFortyGigNRZ-10G | aresOne-M-EightByTwentyFiveGigNRZ-26G | aresOne-M-EightByTenGigNRZ-10G | aresOne-M-OneByEightHundredGigPAM4-106G-RoCEv2 | aresOne-M-TwoByFourHundredGigPAM4-106G-RoCEv2 | aresOne-M-FourByTwoHundredGigPAM4-106G-RoCEv2 | aresOne-M-EightByOneHundredGigPAM4-106G-RoCEv2 | aresOne-M-OneByFourHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByTwoHundredGigPAM4-53G-RoCEv2 | aresOne-M-FourByOneHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByOneHundredGigNRZ-26G-RoCEv2 | notApplicable): Gets the current port resource group mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ResourceMode"])

    def add(self):
        """Adds a new ports resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved ports resources using find and the newly added ports resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Description=None,
        IsAvailable=None,
        IsBusy=None,
        IsLinkUp=None,
        Location=None,
        Owner=None,
        PeerPortDescription=None,
        PeerPortId=None,
        PeerSystemIp=None,
        PeerSystemMac=None,
        PeerSystemName=None,
        ResourceMode=None,
    ):
        # type: (str, bool, bool, bool, str, str, str, str, str, str, str, str) -> Ports
        """Finds and retrieves ports resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ports resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ports resources from the server.

        Args
        ----
        - Description (str): Port description.
        - IsAvailable (bool): Is port ownership with current user.
        - IsBusy (bool): Is port in transition, being connected or released.
        - IsLinkUp (bool): Is port in link up state.
        - Location (str): Connecton information of this port. When location is assigned IxNetwork will try to connect to the device if the device is not connected.
        - Owner (str): Port owner.
        - PeerPortDescription (str): Discovered peer port description.
        - PeerPortId (str): The port ID of the discovered peer port.
        - PeerSystemIp (str): The IP address of the discovered peer system.
        - PeerSystemMac (str): The MAC address of the discovered peer system.
        - PeerSystemName (str): The system name of the discovered peer.
        - ResourceMode (str(normal | tenGig | fortyGig | singleMode | dualMode | hundredGigNonFanOut | fortyGigFanOut | threeByTenGigFanOut | eightByTenGigFanOut | fourByTwentyFiveGigNonFanOut | twoByTwentyFiveGigNonFanOut | oneByFiftyGigNonFanOut | fortyGigNonFanOut | oneByTenGigFanOut | fourByTenGigFanOut | incompatibleMode | hundredGigCapturePlayback | fortyGigCapturePlayback | novusHundredGigNonFanOut | novusFourByTwentyFiveGigNonFanOut | novusTwoByFiftyGigNonFanOut | novusOneByFortyGigNonFanOut | novusFourByTenGigNonFanOut | krakenOneByFourHundredGigNonFanOut | krakenOneByTwoHundredGigNonFanOut | krakenTwoByOneHundredGigFanOut | krakenFourByFiftyGigFanOut | aresOneOneByFourHundredGigNonFanOut | aresOneOneByFourHundredGigMacSec128NonFanOut | aresOneOneByFourHundredGigMacSec256NonFanOut | aresOneTwoByTwoHundredGigFanOut | aresOneTwoByTwoHundredGigMacSecFanOut | aresOneFourByOneHundredGigFanOut | aresOneFourByOneHundredGigMacSecFanOut | aresOneEightByFiftyGigFanOut | uhdOneHundredEightByHundredGigNonFanOut | uhdOneHundredEightByFortyGigNonFanOut | uhdOneHundredSixteenByFiftyGigFanOut | uhdOneHundredThirtyTwoByTwentyFiveGigFanOut | uhdOneHundredThirtyTwoByTenGigFanOut | novus5GOneByTenGigNonFanOut | novus5GOneByTwentyFiveGigNonFanOut | novus5GOneByFiftyGigNonFanOut | novus5GOneByHundredGigNonFanOut | novus5GOneByHundredGigNonFanOutHighStream | starTwoByFourHundredGigNonFannedOutPAM4 | starTwoByFourHundredGigFannedOutPAM4RoCEv2 | starFourByTwoHundredGigFannedOutPAM4 | starFourByTwoHundredGigFannedOutPAM4RoCEv2 | starTwoByTwoHundredGigFannedOutNRZ | starEightByHundredGigFannedOutPAM4 | starEightByHundredGigFannedOutPAM4RoCEv2 | starFourByHundredGigFannedOutNRZRoCEv2 | starFourByHundredGigFannedOutNRZ | starSixteenByFiftyGigFannedOutPAM4 | starEightByFiftyGigFannedOutNRZ | starFourByFortyGigFannedOutNRZ | starSixteenByTwentyFiveGigFannedOutNRZ | starSixteenByTenGigFannedOutNRZ | starFourByHundredGigFannedOutPAM4HalfDensityHighStream | starEightByFiftyGigFannedOutPAM4HalfDensityHighStream | starEightByTwentyFiveGigFannedOutNRZHalfDensityHighStream | starEightByTenGigFannedOutNRZHalfDensityHighStream | novusHundredGigNonFanOutHighStream | novusFourByTwentyFiveGigNonFanOutHighStream | novusTwoByFiftyGigNonFanOutHighStream | novusOneByFortyGigNonFanOutHighStream | novusFourByTenGigNonFanOutHighStream | ravenEightByHundredGigFannedOutPAM4 | ravenFourByTwoHundredGigFannedOutPAM4 | ravenTwoByFourHundredGigFannedOutPAM4 | ravenOneByEightHundredGigNonFannedOutPAM4 | aresOneEightHundredQddCEightByHundredGigFannedOutPAM4 | aresOneEightHundredQddCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredQddCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredQddCOneByEightHundredGigNonFannedOutPAM4 | sertHundredGig | sertFiftyGig | sertFourtyGig | sertTwentyFiveGig | sertTenGig | aresOneEightHundredOsfpCEightByHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCFourByTwoHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCTwoByFourHundredGigFannedOutPAM4 | aresOneEightHundredOsfpCOneByEightHundredGigNonFannedOutPAM4 | aresOne-M-OneByEightHundredGigPAM4-106G | aresOne-M-TwoByFourHundredGigPAM4-106G | aresOne-M-FourByTwoHundredGigPAM4-106G | aresOne-M-EightByOneHundredGigPAM4-106G | aresOne-M-OneByFourHundredGigPAM4-53G | aresOne-M-TwoByTwoHundredGigPAM4-53G | aresOne-M-FourByOneHundredGigPAM4-53G | aresOne-M-EightByFiftyGigPAM4-53G | aresOne-M-OneByTwoHundredGigNRZ-26G | aresOne-M-TwoByOneHundredGigNRZ-26G | aresOne-M-FourByFiftyGigNRZ-26G | aresOne-M-TwoByFortyGigNRZ-10G | aresOne-M-EightByTwentyFiveGigNRZ-26G | aresOne-M-EightByTenGigNRZ-10G | aresOne-M-OneByEightHundredGigPAM4-106G-RoCEv2 | aresOne-M-TwoByFourHundredGigPAM4-106G-RoCEv2 | aresOne-M-FourByTwoHundredGigPAM4-106G-RoCEv2 | aresOne-M-EightByOneHundredGigPAM4-106G-RoCEv2 | aresOne-M-OneByFourHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByTwoHundredGigPAM4-53G-RoCEv2 | aresOne-M-FourByOneHundredGigPAM4-53G-RoCEv2 | aresOne-M-TwoByOneHundredGigNRZ-26G-RoCEv2 | notApplicable)): Gets the current port resource group mode.

        Returns
        -------
        - self: This instance with matching ports resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ports data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ports resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def ClearOwnership(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the clearOwnership operation on the server.

        Clears ownership on a list of location ports.

        clearOwnership(async_operation=bool)
        ------------------------------------
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
        return self._execute("clearOwnership", payload=payload, response_object=None)
