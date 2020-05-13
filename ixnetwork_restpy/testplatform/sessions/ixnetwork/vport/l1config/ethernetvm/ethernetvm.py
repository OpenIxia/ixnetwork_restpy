# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class Ethernetvm(Base):
    """Layer 1 Configuration for Ethernet VM
    The Ethernetvm class encapsulates a required ethernetvm resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ethernetvm'
    _SDM_ATT_MAP = {
        'AutoInstrumentation': 'autoInstrumentation',
        'EnablePPM': 'enablePPM',
        'Loopback': 'loopback',
        'Mtu': 'mtu',
        'Ppm': 'ppm',
        'PromiscuousMode': 'promiscuousMode',
        'Speed': 'speed',
    }

    def __init__(self, parent):
        super(Ethernetvm, self).__init__(parent)

    @property
    def AutoInstrumentation(self):
        """
        Returns
        -------
        - str(endOfFrame | floating): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoInstrumentation'])
    @AutoInstrumentation.setter
    def AutoInstrumentation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AutoInstrumentation'], value)

    @property
    def EnablePPM(self):
        """
        Returns
        -------
        - bool: If true, enables the portsppm.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePPM'])

    @property
    def Loopback(self):
        """
        Returns
        -------
        - bool: If true, enables the ports ppm
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
        - number: Indicates the value that needs to be adjusted for the line transmit frequency
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
    @PromiscuousMode.setter
    def PromiscuousMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PromiscuousMode'], value)

    @property
    def Speed(self):
        """
        Returns
        -------
        - str(speed100 | speed1000 | speed10g | speed2000 | speed20g | speed25g | speed3000 | speed30g | speed4000 | speed40g | speed5000 | speed50g | speed6000 | speed7000 | speed8000 | speed9000): Select one of the enums to set the speed of the ethernet vm
        """
        return self._get_attribute(self._SDM_ATT_MAP['Speed'])
    @Speed.setter
    def Speed(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Speed'], value)

    def update(self, AutoInstrumentation=None, Loopback=None, Mtu=None, PromiscuousMode=None, Speed=None):
        """Updates ethernetvm resource on the server.

        Args
        ----
        - AutoInstrumentation (str(endOfFrame | floating)): NOT DEFINED
        - Loopback (bool): If true, enables the ports ppm
        - Mtu (number): 
        - PromiscuousMode (bool): 
        - Speed (str(speed100 | speed1000 | speed10g | speed2000 | speed20g | speed25g | speed3000 | speed30g | speed4000 | speed40g | speed5000 | speed50g | speed6000 | speed7000 | speed8000 | speed9000)): Select one of the enums to set the speed of the ethernet vm

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
