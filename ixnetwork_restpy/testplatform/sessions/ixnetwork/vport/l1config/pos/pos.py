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


class Pos(Base):
    """Layer 1 (physical) parameters for a POS (Packet over SONET) port.
    The Pos class encapsulates a required pos resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'pos'
    _SDM_ATT_MAP = {
        'AvailableSpeeds': 'availableSpeeds',
        'C2Expected': 'c2Expected',
        'C2Tx': 'c2Tx',
        'CanModifySpeed': 'canModifySpeed',
        'CanSetMultipleSpeeds': 'canSetMultipleSpeeds',
        'CrcSize': 'crcSize',
        'DataScrambling': 'dataScrambling',
        'EnablePPM': 'enablePPM',
        'InterfaceType': 'interfaceType',
        'Loopback': 'loopback',
        'PayloadType': 'payloadType',
        'Ppm': 'ppm',
        'SelectedSpeeds': 'selectedSpeeds',
        'TrafficMapType': 'trafficMapType',
        'TransmitClocking': 'transmitClocking',
    }

    def __init__(self, parent):
        super(Pos, self).__init__(parent)

    @property
    def Dcc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.pos.dcc.dcc.Dcc): An instance of the Dcc class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.pos.dcc.dcc import Dcc
        return Dcc(self)._select()

    @property
    def Ppp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.pos.ppp.ppp.Ppp): An instance of the Ppp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.pos.ppp.ppp import Ppp
        return Ppp(self)._select()

    @property
    def AvailableSpeeds(self):
        """
        Returns
        -------
        - list(str[]): Which speeds are available for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableSpeeds'])

    @property
    def C2Expected(self):
        """
        Returns
        -------
        - number: C2 Byte
        """
        return self._get_attribute(self._SDM_ATT_MAP['C2Expected'])
    @C2Expected.setter
    def C2Expected(self, value):
        self._set_attribute(self._SDM_ATT_MAP['C2Expected'], value)

    @property
    def C2Tx(self):
        """
        Returns
        -------
        - number: C2 Byte
        """
        return self._get_attribute(self._SDM_ATT_MAP['C2Tx'])
    @C2Tx.setter
    def C2Tx(self, value):
        self._set_attribute(self._SDM_ATT_MAP['C2Tx'], value)

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
    def CrcSize(self):
        """
        Returns
        -------
        - str(crc16 | crc32): The type of cyclic redundancy check (CRC) to be used.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CrcSize'])
    @CrcSize.setter
    def CrcSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CrcSize'], value)

    @property
    def DataScrambling(self):
        """
        Returns
        -------
        - bool: Data scrambling is enabled on this POS port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataScrambling'])
    @DataScrambling.setter
    def DataScrambling(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DataScrambling'], value)

    @property
    def EnablePPM(self):
        """
        Returns
        -------
        - bool: If true, enables the portsppm
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePPM'])
    @EnablePPM.setter
    def EnablePPM(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePPM'], value)

    @property
    def InterfaceType(self):
        """
        Returns
        -------
        - str(oc12 | oc192 | oc3 | oc48 | stm1 | stm16 | stm4 | stm64): The POS interface type for the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceType'])
    @InterfaceType.setter
    def InterfaceType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceType'], value)

    @property
    def Loopback(self):
        """
        Returns
        -------
        - bool: If enabled, the port is set to internally loopback from transmit to receive.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Loopback'])
    @Loopback.setter
    def Loopback(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Loopback'], value)

    @property
    def PayloadType(self):
        """
        Returns
        -------
        - str(ciscoFrameRelay | ciscoHdlc | frameRelay | ppp): The POS payload type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PayloadType'])
    @PayloadType.setter
    def PayloadType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PayloadType'], value)

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
    def SelectedSpeeds(self):
        """
        Returns
        -------
        - list(str[]): Which speeds are selected for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SelectedSpeeds'])
    @SelectedSpeeds.setter
    def SelectedSpeeds(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SelectedSpeeds'], value)

    @property
    def TrafficMapType(self):
        """
        Returns
        -------
        - str(dcc | spe): The POS traffic map type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficMapType'])
    @TrafficMapType.setter
    def TrafficMapType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficMapType'], value)

    @property
    def TransmitClocking(self):
        """
        Returns
        -------
        - str(external | internal | recovered): The POS transmit clocking type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransmitClocking'])
    @TransmitClocking.setter
    def TransmitClocking(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TransmitClocking'], value)

    def update(self, C2Expected=None, C2Tx=None, CrcSize=None, DataScrambling=None, EnablePPM=None, InterfaceType=None, Loopback=None, PayloadType=None, Ppm=None, SelectedSpeeds=None, TrafficMapType=None, TransmitClocking=None):
        """Updates pos resource on the server.

        Args
        ----
        - C2Expected (number): C2 Byte
        - C2Tx (number): C2 Byte
        - CrcSize (str(crc16 | crc32)): The type of cyclic redundancy check (CRC) to be used.
        - DataScrambling (bool): Data scrambling is enabled on this POS port.
        - EnablePPM (bool): If true, enables the portsppm
        - InterfaceType (str(oc12 | oc192 | oc3 | oc48 | stm1 | stm16 | stm4 | stm64)): The POS interface type for the port.
        - Loopback (bool): If enabled, the port is set to internally loopback from transmit to receive.
        - PayloadType (str(ciscoFrameRelay | ciscoHdlc | frameRelay | ppp)): The POS payload type.
        - Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency.
        - SelectedSpeeds (list(str[])): Which speeds are selected for the current media and AN settings.
        - TrafficMapType (str(dcc | spe)): The POS traffic map type.
        - TransmitClocking (str(external | internal | recovered)): The POS transmit clocking type.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
