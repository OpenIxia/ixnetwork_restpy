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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Fc(Base):
    """Fibre Channel configuration settings.
    The Fc class encapsulates a required fc resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'fc'
    _SDM_ATT_MAP = {
        'AvailableSpeeds': 'availableSpeeds',
        'CanModifySpeed': 'canModifySpeed',
        'CanSetMultipleSpeeds': 'canSetMultipleSpeeds',
        'CreditStarvationValue': 'creditStarvationValue',
        'EnableEmissionLoweringProtocol': 'enableEmissionLoweringProtocol',
        'EnablePPM': 'enablePPM',
        'FixedDelayValue': 'fixedDelayValue',
        'ForceErrors': 'forceErrors',
        'Loopback': 'loopback',
        'MaxDelayForRandomValue': 'maxDelayForRandomValue',
        'MinDelayForRandomValue': 'minDelayForRandomValue',
        'NoRRDYAfter': 'noRRDYAfter',
        'Ppm': 'ppm',
        'RrdyResponseDelays': 'rrdyResponseDelays',
        'SelectedSpeeds': 'selectedSpeeds',
        'Speed': 'speed',
        'TxIgnoreAvailableCredits': 'txIgnoreAvailableCredits',
        'TxIgnoreRxLinkFaults': 'txIgnoreRxLinkFaults',
    }

    def __init__(self, parent):
        super(Fc, self).__init__(parent)

    @property
    def AvailableSpeeds(self):
        """
        Returns
        -------
        - list(str[speed2000 | speed4000 | speed8000]): Which speeds are available for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableSpeeds'])

    @property
    def CanModifySpeed(self):
        """
        Returns
        -------
        - bool: Returns true/false depending upon if the port can change speed for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CanModifySpeed'])

    @property
    def CanSetMultipleSpeeds(self):
        """
        Returns
        -------
        - bool: Can this port selectmultiple speeds for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CanSetMultipleSpeeds'])

    @property
    def CreditStarvationValue(self):
        """
        Returns
        -------
        - number: If selected, programs encounter a delay value specified in the Hold R_RDY field. The counter starts counting down after it receives the first frame. The port holds R_RDY for all frames received until counter reaches to 0. After counter reaches 0, the port sends out all accumulated R_RDY.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CreditStarvationValue'])
    @CreditStarvationValue.setter
    def CreditStarvationValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CreditStarvationValue'], value)

    @property
    def EnableEmissionLoweringProtocol(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableEmissionLoweringProtocol'])
    @EnableEmissionLoweringProtocol.setter
    def EnableEmissionLoweringProtocol(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableEmissionLoweringProtocol'], value)

    @property
    def EnablePPM(self):
        """
        Returns
        -------
        - bool: If true, enables the portsppm.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePPM'])
    @EnablePPM.setter
    def EnablePPM(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePPM'], value)

    @property
    def FixedDelayValue(self):
        """
        Returns
        -------
        - number: Internally delays the R_RDY primitive signals with X ms. X is between 0 and 20000 milliseconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FixedDelayValue'])
    @FixedDelayValue.setter
    def FixedDelayValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FixedDelayValue'], value)

    @property
    def ForceErrors(self):
        """
        Returns
        -------
        - str(noErrors | noRRDY | noRRDYEvery): Helps to configure the port to introduce errors in the transmission of R_RDYPrimitive Signals
        """
        return self._get_attribute(self._SDM_ATT_MAP['ForceErrors'])
    @ForceErrors.setter
    def ForceErrors(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ForceErrors'], value)

    @property
    def Loopback(self):
        """
        Returns
        -------
        - bool: If true, the port is set to internally loopback from transmit to receive.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Loopback'])
    @Loopback.setter
    def Loopback(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Loopback'], value)

    @property
    def MaxDelayForRandomValue(self):
        """
        Returns
        -------
        - number: The maximum random delay value for the R_RDY primitives. The maximum value is 1,000,000 microseconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxDelayForRandomValue'])
    @MaxDelayForRandomValue.setter
    def MaxDelayForRandomValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxDelayForRandomValue'], value)

    @property
    def MinDelayForRandomValue(self):
        """
        Returns
        -------
        - number: The minimum random delay value for the R_RDY primitives. The minimum value is 0 microseconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinDelayForRandomValue'])
    @MinDelayForRandomValue.setter
    def MinDelayForRandomValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinDelayForRandomValue'], value)

    @property
    def NoRRDYAfter(self):
        """
        Returns
        -------
        - number: Sends R_RDY primitive signals without any delay.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoRRDYAfter'])
    @NoRRDYAfter.setter
    def NoRRDYAfter(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoRRDYAfter'], value)

    @property
    def Ppm(self):
        """
        Returns
        -------
        - number: Indicates the value that needs to be adjusted for the line transmit frequency.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ppm'])
    @Ppm.setter
    def Ppm(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ppm'], value)

    @property
    def RrdyResponseDelays(self):
        """
        Returns
        -------
        - str(creditStarvation | fixedDelay | noDelay | randomDelay): Helps to set internal delays for the transmission of R_RDY Primitive Signals.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RrdyResponseDelays'])
    @RrdyResponseDelays.setter
    def RrdyResponseDelays(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RrdyResponseDelays'], value)

    @property
    def SelectedSpeeds(self):
        """
        Returns
        -------
        - list(str[speed2000 | speed4000 | speed8000]): Which speeds are selected for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SelectedSpeeds'])
    @SelectedSpeeds.setter
    def SelectedSpeeds(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SelectedSpeeds'], value)

    @property
    def Speed(self):
        """
        Returns
        -------
        - str(speed2000 | speed4000 | speed8000): Indicates the line speed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Speed'])
    @Speed.setter
    def Speed(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Speed'], value)

    @property
    def TxIgnoreAvailableCredits(self):
        """
        Returns
        -------
        - bool: The transmitting port does not listen to flow control. It keeps transmittingpackets irrespective of available credits. For example, if two Fibre Channel portsare connected back-to-back andTransmitignoreavailablecredits'optionistrueonthetransmittingportand'Don'tsendR_RDY'optionistrueonthereceivingport,andthentransmitisstarted,theporttransmitsatfullrateeventhoughitdoesnothavecredits.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxIgnoreAvailableCredits'])
    @TxIgnoreAvailableCredits.setter
    def TxIgnoreAvailableCredits(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TxIgnoreAvailableCredits'], value)

    @property
    def TxIgnoreRxLinkFaults(self):
        """
        Returns
        -------
        - bool: If true, allows transmission of packets even if the receive link is down.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxIgnoreRxLinkFaults'])
    @TxIgnoreRxLinkFaults.setter
    def TxIgnoreRxLinkFaults(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TxIgnoreRxLinkFaults'], value)

    def update(self, CreditStarvationValue=None, EnableEmissionLoweringProtocol=None, EnablePPM=None, FixedDelayValue=None, ForceErrors=None, Loopback=None, MaxDelayForRandomValue=None, MinDelayForRandomValue=None, NoRRDYAfter=None, Ppm=None, RrdyResponseDelays=None, SelectedSpeeds=None, Speed=None, TxIgnoreAvailableCredits=None, TxIgnoreRxLinkFaults=None):
        """Updates fc resource on the server.

        Args
        ----
        - CreditStarvationValue (number): If selected, programs encounter a delay value specified in the Hold R_RDY field. The counter starts counting down after it receives the first frame. The port holds R_RDY for all frames received until counter reaches to 0. After counter reaches 0, the port sends out all accumulated R_RDY.
        - EnableEmissionLoweringProtocol (bool): NOT DEFINED
        - EnablePPM (bool): If true, enables the portsppm.
        - FixedDelayValue (number): Internally delays the R_RDY primitive signals with X ms. X is between 0 and 20000 milliseconds.
        - ForceErrors (str(noErrors | noRRDY | noRRDYEvery)): Helps to configure the port to introduce errors in the transmission of R_RDYPrimitive Signals
        - Loopback (bool): If true, the port is set to internally loopback from transmit to receive.
        - MaxDelayForRandomValue (number): The maximum random delay value for the R_RDY primitives. The maximum value is 1,000,000 microseconds.
        - MinDelayForRandomValue (number): The minimum random delay value for the R_RDY primitives. The minimum value is 0 microseconds.
        - NoRRDYAfter (number): Sends R_RDY primitive signals without any delay.
        - Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency.
        - RrdyResponseDelays (str(creditStarvation | fixedDelay | noDelay | randomDelay)): Helps to set internal delays for the transmission of R_RDY Primitive Signals.
        - SelectedSpeeds (list(str[speed2000 | speed4000 | speed8000])): Which speeds are selected for the current media and AN settings.
        - Speed (str(speed2000 | speed4000 | speed8000)): Indicates the line speed.
        - TxIgnoreAvailableCredits (bool): The transmitting port does not listen to flow control. It keeps transmittingpackets irrespective of available credits. For example, if two Fibre Channel portsare connected back-to-back andTransmitignoreavailablecredits'optionistrueonthetransmittingportand'Don'tsendR_RDY'optionistrueonthereceivingport,andthentransmitisstarted,theporttransmitsatfullrateeventhoughitdoesnothavecredits.
        - TxIgnoreRxLinkFaults (bool): If true, allows transmission of packets even if the receive link is down.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
