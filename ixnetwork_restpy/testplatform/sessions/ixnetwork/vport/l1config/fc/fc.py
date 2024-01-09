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


class Fc(Base):
    """Fibre Channel configuration settings.
    The Fc class encapsulates a required fc resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "fc"
    _SDM_ATT_MAP = {
        "AvailableSpeeds": "availableSpeeds",
        "CanModifySpeed": "canModifySpeed",
        "CanSetMultipleSpeeds": "canSetMultipleSpeeds",
        "CreditStarvationValue": "creditStarvationValue",
        "EnableEmissionLoweringProtocol": "enableEmissionLoweringProtocol",
        "EnablePPM": "enablePPM",
        "FixedDelayValue": "fixedDelayValue",
        "ForceErrors": "forceErrors",
        "Loopback": "loopback",
        "MaxDelayForRandomValue": "maxDelayForRandomValue",
        "MinDelayForRandomValue": "minDelayForRandomValue",
        "NoRRDYAfter": "noRRDYAfter",
        "Ppm": "ppm",
        "RrdyResponseDelays": "rrdyResponseDelays",
        "SelectedSpeeds": "selectedSpeeds",
        "Speed": "speed",
        "TxIgnoreAvailableCredits": "txIgnoreAvailableCredits",
        "TxIgnoreRxLinkFaults": "txIgnoreRxLinkFaults",
    }
    _SDM_ENUM_MAP = {
        "forceErrors": ["noErrors", "noRRDY", "noRRDYEvery"],
        "rrdyResponseDelays": [
            "noDelay",
            "fixedDelay",
            "randomDelay",
            "creditStarvation",
        ],
        "speed": ["speed2000", "speed4000", "speed8000"],
    }

    def __init__(self, parent, list_op=False):
        super(Fc, self).__init__(parent, list_op)

    @property
    def AvailableSpeeds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[speed2000 | speed4000 | speed8000]): Which speeds are available for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AvailableSpeeds"])

    @property
    def CanModifySpeed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Returns true/false depending upon if the port can change speed for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CanModifySpeed"])

    @property
    def CanSetMultipleSpeeds(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Can this port selectmultiple speeds for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CanSetMultipleSpeeds"])

    @property
    def CreditStarvationValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: f selected, programs encounter a delay value specified in the Hold R_RDY field. The counter starts counting down after it receives the first frame. The port holds R_RDY for all frames received until counter reaches to 0. After counter reaches 0, the port sends out all accumulated R_RDY.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CreditStarvationValue"])

    @CreditStarvationValue.setter
    def CreditStarvationValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["CreditStarvationValue"], value)

    @property
    def EnableEmissionLoweringProtocol(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableEmissionLoweringProtocol"])

    @EnableEmissionLoweringProtocol.setter
    def EnableEmissionLoweringProtocol(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableEmissionLoweringProtocol"], value)

    @property
    def EnablePPM(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: If true, enables the portsppm.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePPM"])

    @EnablePPM.setter
    def EnablePPM(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePPM"], value)

    @property
    def FixedDelayValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Internally delays the R_RDY primitive signals with X ms. X is between 0 and 20000 milliseconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FixedDelayValue"])

    @FixedDelayValue.setter
    def FixedDelayValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FixedDelayValue"], value)

    @property
    def ForceErrors(self):
        # type: () -> str
        """
        Returns
        -------
        - str(noErrors | noRRDY | noRRDYEvery): Helps to configure the port to introduce errors in the transmission of R_RDY Primitive Signals
        """
        return self._get_attribute(self._SDM_ATT_MAP["ForceErrors"])

    @ForceErrors.setter
    def ForceErrors(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ForceErrors"], value)

    @property
    def Loopback(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the port is set to internally loopback from transmit to receive.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Loopback"])

    @Loopback.setter
    def Loopback(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Loopback"], value)

    @property
    def MaxDelayForRandomValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum random delay value for the R_RDY primitives. The maximum value is 1,000,000 microseconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxDelayForRandomValue"])

    @MaxDelayForRandomValue.setter
    def MaxDelayForRandomValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxDelayForRandomValue"], value)

    @property
    def MinDelayForRandomValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The minimum random delay value for the R_RDY primitives. The minimum value is 0 microseconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinDelayForRandomValue"])

    @MinDelayForRandomValue.setter
    def MinDelayForRandomValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinDelayForRandomValue"], value)

    @property
    def NoRRDYAfter(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sends R_RDY primitive signals without any delay.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoRRDYAfter"])

    @NoRRDYAfter.setter
    def NoRRDYAfter(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoRRDYAfter"], value)

    @property
    def Ppm(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: Indicates the value that needs to be adjusted for the line transmit frequency.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ppm"])

    @Ppm.setter
    def Ppm(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ppm"], value)

    @property
    def RrdyResponseDelays(self):
        # type: () -> str
        """
        Returns
        -------
        - str(noDelay | fixedDelay | randomDelay | creditStarvation): Helps to set internal delays for the transmission of R_RDY Primitive Signals.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RrdyResponseDelays"])

    @RrdyResponseDelays.setter
    def RrdyResponseDelays(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RrdyResponseDelays"], value)

    @property
    def SelectedSpeeds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[speed2000 | speed4000 | speed8000]): Which speeds are selected for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SelectedSpeeds"])

    @SelectedSpeeds.setter
    def SelectedSpeeds(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["SelectedSpeeds"], value)

    @property
    def Speed(self):
        # type: () -> str
        """
        Returns
        -------
        - str(speed2000 | speed4000 | speed8000): Indicates the line speed.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Speed"])

    @Speed.setter
    def Speed(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Speed"], value)

    @property
    def TxIgnoreAvailableCredits(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: The transmitting port does not listen to flow control. It keeps transmitting packets irrespective of available credits. For example, if two Fibre Channel ports are connected back-to-back and Transmitignoreavailablecredits option is true on the transmitting port and DontsendR_RDY option is true on the receiving port, and the transmit is started, the port transmits at full rate even though it does not have credits.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxIgnoreAvailableCredits"])

    @TxIgnoreAvailableCredits.setter
    def TxIgnoreAvailableCredits(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxIgnoreAvailableCredits"], value)

    @property
    def TxIgnoreRxLinkFaults(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, allows transmission of packets even if the receive link is down.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxIgnoreRxLinkFaults"])

    @TxIgnoreRxLinkFaults.setter
    def TxIgnoreRxLinkFaults(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxIgnoreRxLinkFaults"], value)

    def update(
        self,
        CreditStarvationValue=None,
        EnableEmissionLoweringProtocol=None,
        EnablePPM=None,
        FixedDelayValue=None,
        ForceErrors=None,
        Loopback=None,
        MaxDelayForRandomValue=None,
        MinDelayForRandomValue=None,
        NoRRDYAfter=None,
        Ppm=None,
        RrdyResponseDelays=None,
        SelectedSpeeds=None,
        Speed=None,
        TxIgnoreAvailableCredits=None,
        TxIgnoreRxLinkFaults=None,
    ):
        # type: (int, bool, bool, int, str, bool, int, int, int, int, str, List[str], str, bool, bool) -> Fc
        """Updates fc resource on the server.

        Args
        ----
        - CreditStarvationValue (number): f selected, programs encounter a delay value specified in the Hold R_RDY field. The counter starts counting down after it receives the first frame. The port holds R_RDY for all frames received until counter reaches to 0. After counter reaches 0, the port sends out all accumulated R_RDY.
        - EnableEmissionLoweringProtocol (bool): NOT DEFINED
        - EnablePPM (bool): If true, enables the portsppm.
        - FixedDelayValue (number): Internally delays the R_RDY primitive signals with X ms. X is between 0 and 20000 milliseconds.
        - ForceErrors (str(noErrors | noRRDY | noRRDYEvery)): Helps to configure the port to introduce errors in the transmission of R_RDY Primitive Signals
        - Loopback (bool): If true, the port is set to internally loopback from transmit to receive.
        - MaxDelayForRandomValue (number): The maximum random delay value for the R_RDY primitives. The maximum value is 1,000,000 microseconds.
        - MinDelayForRandomValue (number): The minimum random delay value for the R_RDY primitives. The minimum value is 0 microseconds.
        - NoRRDYAfter (number): Sends R_RDY primitive signals without any delay.
        - Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency.
        - RrdyResponseDelays (str(noDelay | fixedDelay | randomDelay | creditStarvation)): Helps to set internal delays for the transmission of R_RDY Primitive Signals.
        - SelectedSpeeds (list(str[speed2000 | speed4000 | speed8000])): Which speeds are selected for the current media and AN settings.
        - Speed (str(speed2000 | speed4000 | speed8000)): Indicates the line speed.
        - TxIgnoreAvailableCredits (bool): The transmitting port does not listen to flow control. It keeps transmitting packets irrespective of available credits. For example, if two Fibre Channel ports are connected back-to-back and Transmitignoreavailablecredits option is true on the transmitting port and DontsendR_RDY option is true on the receiving port, and the transmit is started, the port transmits at full rate even though it does not have credits.
        - TxIgnoreRxLinkFaults (bool): If true, allows transmission of packets even if the receive link is down.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AvailableSpeeds=None,
        CanModifySpeed=None,
        CanSetMultipleSpeeds=None,
        CreditStarvationValue=None,
        EnableEmissionLoweringProtocol=None,
        EnablePPM=None,
        FixedDelayValue=None,
        ForceErrors=None,
        Loopback=None,
        MaxDelayForRandomValue=None,
        MinDelayForRandomValue=None,
        NoRRDYAfter=None,
        Ppm=None,
        RrdyResponseDelays=None,
        SelectedSpeeds=None,
        Speed=None,
        TxIgnoreAvailableCredits=None,
        TxIgnoreRxLinkFaults=None,
    ):
        # type: (List[str], bool, bool, int, bool, bool, int, str, bool, int, int, int, int, str, List[str], str, bool, bool) -> Fc
        """Finds and retrieves fc resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve fc resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all fc resources from the server.

        Args
        ----
        - AvailableSpeeds (list(str[speed2000 | speed4000 | speed8000])): Which speeds are available for the current media and AN settings.
        - CanModifySpeed (bool): Returns true/false depending upon if the port can change speed for the current media and AN settings.
        - CanSetMultipleSpeeds (bool): Can this port selectmultiple speeds for the current media and AN settings.
        - CreditStarvationValue (number): f selected, programs encounter a delay value specified in the Hold R_RDY field. The counter starts counting down after it receives the first frame. The port holds R_RDY for all frames received until counter reaches to 0. After counter reaches 0, the port sends out all accumulated R_RDY.
        - EnableEmissionLoweringProtocol (bool): NOT DEFINED
        - EnablePPM (bool): If true, enables the portsppm.
        - FixedDelayValue (number): Internally delays the R_RDY primitive signals with X ms. X is between 0 and 20000 milliseconds.
        - ForceErrors (str(noErrors | noRRDY | noRRDYEvery)): Helps to configure the port to introduce errors in the transmission of R_RDY Primitive Signals
        - Loopback (bool): If true, the port is set to internally loopback from transmit to receive.
        - MaxDelayForRandomValue (number): The maximum random delay value for the R_RDY primitives. The maximum value is 1,000,000 microseconds.
        - MinDelayForRandomValue (number): The minimum random delay value for the R_RDY primitives. The minimum value is 0 microseconds.
        - NoRRDYAfter (number): Sends R_RDY primitive signals without any delay.
        - Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency.
        - RrdyResponseDelays (str(noDelay | fixedDelay | randomDelay | creditStarvation)): Helps to set internal delays for the transmission of R_RDY Primitive Signals.
        - SelectedSpeeds (list(str[speed2000 | speed4000 | speed8000])): Which speeds are selected for the current media and AN settings.
        - Speed (str(speed2000 | speed4000 | speed8000)): Indicates the line speed.
        - TxIgnoreAvailableCredits (bool): The transmitting port does not listen to flow control. It keeps transmitting packets irrespective of available credits. For example, if two Fibre Channel ports are connected back-to-back and Transmitignoreavailablecredits option is true on the transmitting port and DontsendR_RDY option is true on the receiving port, and the transmit is started, the port transmits at full rate even though it does not have credits.
        - TxIgnoreRxLinkFaults (bool): If true, allows transmission of packets even if the receive link is down.

        Returns
        -------
        - self: This instance with matching fc resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of fc data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the fc resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
