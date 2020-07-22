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


class UhdOneHundredGigLan(Base):
    """
    The UhdOneHundredGigLan class encapsulates a required uhdOneHundredGigLan resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'uhdOneHundredGigLan'
    _SDM_ATT_MAP = {
        'AutoInstrumentation': 'autoInstrumentation',
        'AvailableSpeeds': 'availableSpeeds',
        'CanModifySpeed': 'canModifySpeed',
        'CanSetMultipleSpeeds': 'canSetMultipleSpeeds',
        'EnableAutoNegotiation': 'enableAutoNegotiation',
        'EnablePPM': 'enablePPM',
        'EnableRsFec': 'enableRsFec',
        'EnableRsFecStats': 'enableRsFecStats',
        'FirecodeAdvertise': 'firecodeAdvertise',
        'FirecodeForceOff': 'firecodeForceOff',
        'FirecodeForceOn': 'firecodeForceOn',
        'FirecodeRequest': 'firecodeRequest',
        'ForceDisableFEC': 'forceDisableFEC',
        'IeeeL1Defaults': 'ieeeL1Defaults',
        'LaserOn': 'laserOn',
        'LinkTraining': 'linkTraining',
        'Loopback': 'loopback',
        'Mtu': 'mtu',
        'Ppm': 'ppm',
        'PromiscuousMode': 'promiscuousMode',
        'RsFecAdvertise': 'rsFecAdvertise',
        'RsFecForceOn': 'rsFecForceOn',
        'RsFecRequest': 'rsFecRequest',
        'SelectedSpeeds': 'selectedSpeeds',
        'Speed': 'speed',
        'UseANResults': 'useANResults',
    }

    def __init__(self, parent):
        super(UhdOneHundredGigLan, self).__init__(parent)

    @property
    def AutoInstrumentation(self):
        """
        Returns
        -------
        - str(endOfFrame | floating): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoInstrumentation'])
    @AutoInstrumentation.setter
    def AutoInstrumentation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AutoInstrumentation'], value)

    @property
    def AvailableSpeeds(self):
        """
        Returns
        -------
        - list(str[speed100g | speed25g | speed50g | speed10g | speed40g]): Which speeds are available for the current media and AN settings.
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
    def EnableAutoNegotiation(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAutoNegotiation'])
    @EnableAutoNegotiation.setter
    def EnableAutoNegotiation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAutoNegotiation'], value)

    @property
    def EnablePPM(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePPM'])

    @property
    def EnableRsFec(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableRsFec'])
    @EnableRsFec.setter
    def EnableRsFec(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableRsFec'], value)

    @property
    def EnableRsFecStats(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableRsFecStats'])
    @EnableRsFecStats.setter
    def EnableRsFecStats(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableRsFecStats'], value)

    @property
    def FirecodeAdvertise(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FirecodeAdvertise'])
    @FirecodeAdvertise.setter
    def FirecodeAdvertise(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FirecodeAdvertise'], value)

    @property
    def FirecodeForceOff(self):
        """DEPRECATED 
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FirecodeForceOff'])
    @FirecodeForceOff.setter
    def FirecodeForceOff(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FirecodeForceOff'], value)

    @property
    def FirecodeForceOn(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FirecodeForceOn'])
    @FirecodeForceOn.setter
    def FirecodeForceOn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FirecodeForceOn'], value)

    @property
    def FirecodeRequest(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FirecodeRequest'])
    @FirecodeRequest.setter
    def FirecodeRequest(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FirecodeRequest'], value)

    @property
    def ForceDisableFEC(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ForceDisableFEC'])
    @ForceDisableFEC.setter
    def ForceDisableFEC(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ForceDisableFEC'], value)

    @property
    def IeeeL1Defaults(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IeeeL1Defaults'])
    @IeeeL1Defaults.setter
    def IeeeL1Defaults(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IeeeL1Defaults'], value)

    @property
    def LaserOn(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LaserOn'])
    @LaserOn.setter
    def LaserOn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LaserOn'], value)

    @property
    def LinkTraining(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkTraining'])
    @LinkTraining.setter
    def LinkTraining(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkTraining'], value)

    @property
    def Loopback(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Loopback'])
    @Loopback.setter
    def Loopback(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Loopback'], value)

    @property
    def Mtu(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mtu'])
    @Mtu.setter
    def Mtu(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mtu'], value)

    @property
    def Ppm(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ppm'])

    @property
    def PromiscuousMode(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PromiscuousMode'])

    @property
    def RsFecAdvertise(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RsFecAdvertise'])
    @RsFecAdvertise.setter
    def RsFecAdvertise(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RsFecAdvertise'], value)

    @property
    def RsFecForceOn(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RsFecForceOn'])
    @RsFecForceOn.setter
    def RsFecForceOn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RsFecForceOn'], value)

    @property
    def RsFecRequest(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RsFecRequest'])
    @RsFecRequest.setter
    def RsFecRequest(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RsFecRequest'], value)

    @property
    def SelectedSpeeds(self):
        """
        Returns
        -------
        - list(str[speed100g | speed25g | speed50g | speed10g | speed40g]): Which speeds are selected for the current media and AN settings.
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
        - str(speed100g | speed10g | speed25g | speed40g | speed50g): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Speed'])
    @Speed.setter
    def Speed(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Speed'], value)

    @property
    def UseANResults(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseANResults'])
    @UseANResults.setter
    def UseANResults(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseANResults'], value)

    def update(self, AutoInstrumentation=None, EnableAutoNegotiation=None, EnableRsFec=None, EnableRsFecStats=None, FirecodeAdvertise=None, FirecodeForceOff=None, FirecodeForceOn=None, FirecodeRequest=None, ForceDisableFEC=None, IeeeL1Defaults=None, LaserOn=None, LinkTraining=None, Loopback=None, Mtu=None, RsFecAdvertise=None, RsFecForceOn=None, RsFecRequest=None, SelectedSpeeds=None, Speed=None, UseANResults=None):
        """Updates uhdOneHundredGigLan resource on the server.

        Args
        ----
        - AutoInstrumentation (str(endOfFrame | floating)): 
        - EnableAutoNegotiation (bool): 
        - EnableRsFec (bool): 
        - EnableRsFecStats (bool): 
        - FirecodeAdvertise (bool): 
        - FirecodeForceOff (bool): 
        - FirecodeForceOn (bool): 
        - FirecodeRequest (bool): 
        - ForceDisableFEC (bool): 
        - IeeeL1Defaults (bool): 
        - LaserOn (bool): 
        - LinkTraining (bool): 
        - Loopback (bool): 
        - Mtu (number): 
        - RsFecAdvertise (bool): 
        - RsFecForceOn (bool): 
        - RsFecRequest (bool): 
        - SelectedSpeeds (list(str[speed100g | speed25g | speed50g | speed10g | speed40g])): Which speeds are selected for the current media and AN settings.
        - Speed (str(speed100g | speed10g | speed25g | speed40g | speed50g)): 
        - UseANResults (bool): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
