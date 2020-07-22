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


class Ethernet(Base):
    """Ethernet Layer 1 configuration settings.
    The Ethernet class encapsulates a required ethernet resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ethernet'
    _SDM_ATT_MAP = {
        'AutoInstrumentation': 'autoInstrumentation',
        'AutoNegotiate': 'autoNegotiate',
        'AvailableSpeeds': 'availableSpeeds',
        'CanModifySpeed': 'canModifySpeed',
        'CanSetMultipleSpeeds': 'canSetMultipleSpeeds',
        'EnablePPM': 'enablePPM',
        'EnabledFlowControl': 'enabledFlowControl',
        'FlowControlDirectedAddress': 'flowControlDirectedAddress',
        'Loopback': 'loopback',
        'MasterSlaveMode': 'masterSlaveMode',
        'Media': 'media',
        'NegotiateMasterSlave': 'negotiateMasterSlave',
        'Ppm': 'ppm',
        'SelectedSpeeds': 'selectedSpeeds',
        'Speed': 'speed',
        'SpeedAuto': 'speedAuto',
    }

    def __init__(self, parent):
        super(Ethernet, self).__init__(parent)

    @property
    def Fcoe(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernet.fcoe.fcoe.Fcoe): An instance of the Fcoe class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernet.fcoe.fcoe import Fcoe
        return Fcoe(self)._select()

    @property
    def Oam(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernet.oam.oam.Oam): An instance of the Oam class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernet.oam.oam import Oam
        return Oam(self)._select()

    @property
    def TxLane(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernet.txlane.txlane.TxLane): An instance of the TxLane class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernet.txlane.txlane import TxLane
        return TxLane(self)._select()

    @property
    def AutoInstrumentation(self):
        """
        Returns
        -------
        - str(endOfFrame | floating): The auto instrumentation mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoInstrumentation'])
    @AutoInstrumentation.setter
    def AutoInstrumentation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AutoInstrumentation'], value)

    @property
    def AutoNegotiate(self):
        """
        Returns
        -------
        - bool: If enabled, allows autonegotiation between ports for speed and duplex operation based on the various choices. The selected capabilities are advertised during AutoNegotiation
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoNegotiate'])
    @AutoNegotiate.setter
    def AutoNegotiate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AutoNegotiate'], value)

    @property
    def AvailableSpeeds(self):
        """
        Returns
        -------
        - list(str[speed10fd | speed10hd | speed100fd | speed100hd | speed1000]): Which speeds are available for the current media and AN settings.
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
    def EnabledFlowControl(self):
        """
        Returns
        -------
        - bool: If true, enables the port's MAC flow control and mechanisms to listen for a directed address pause message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnabledFlowControl'])
    @EnabledFlowControl.setter
    def EnabledFlowControl(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnabledFlowControl'], value)

    @property
    def FlowControlDirectedAddress(self):
        """
        Returns
        -------
        - str: The 48-bit MAC address that the port listens on for a directed pause.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowControlDirectedAddress'])
    @FlowControlDirectedAddress.setter
    def FlowControlDirectedAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowControlDirectedAddress'], value)

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
    def MasterSlaveMode(self):
        """
        Returns
        -------
        - str(master | slave): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MasterSlaveMode'])
    @MasterSlaveMode.setter
    def MasterSlaveMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MasterSlaveMode'], value)

    @property
    def Media(self):
        """
        Returns
        -------
        - str(copper | fiber | sgmii): Available only for Ethernet cards that support this dual-PHY capability.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Media'])
    @Media.setter
    def Media(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Media'], value)

    @property
    def NegotiateMasterSlave(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['NegotiateMasterSlave'])
    @NegotiateMasterSlave.setter
    def NegotiateMasterSlave(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NegotiateMasterSlave'], value)

    @property
    def Ppm(self):
        """
        Returns
        -------
        - number: Indicates the value that needs to be adjusted for the line transmit frequency
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
        - list(str[speed10fd | speed10hd | speed100fd | speed100hd | speed1000]): Which speeds are selected for the current media and AN settings.
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
        - str(auto | speed1000 | speed100fd | speed100hd | speed10fd | speed10hd): The speed and duplex operation options.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Speed'])
    @Speed.setter
    def Speed(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Speed'], value)

    @property
    def SpeedAuto(self):
        """
        Returns
        -------
        - list(str[all | speed1000 | speed100fd | speed100hd | speed10fd | speed10hd]): If selected, allows auto negotiation between ports for speed and duplex operation based on the various choices. The selected capabilities are advertised during AutoNegotiation.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SpeedAuto'])
    @SpeedAuto.setter
    def SpeedAuto(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SpeedAuto'], value)

    def update(self, AutoInstrumentation=None, AutoNegotiate=None, EnablePPM=None, EnabledFlowControl=None, FlowControlDirectedAddress=None, Loopback=None, MasterSlaveMode=None, Media=None, NegotiateMasterSlave=None, Ppm=None, SelectedSpeeds=None, Speed=None, SpeedAuto=None):
        """Updates ethernet resource on the server.

        Args
        ----
        - AutoInstrumentation (str(endOfFrame | floating)): The auto instrumentation mode.
        - AutoNegotiate (bool): If enabled, allows autonegotiation between ports for speed and duplex operation based on the various choices. The selected capabilities are advertised during AutoNegotiation
        - EnablePPM (bool): If true, enables the portsppm.
        - EnabledFlowControl (bool): If true, enables the port's MAC flow control and mechanisms to listen for a directed address pause message.
        - FlowControlDirectedAddress (str): The 48-bit MAC address that the port listens on for a directed pause.
        - Loopback (bool): If enabled, the port is set to internally loopback from transmit to receive.
        - MasterSlaveMode (str(master | slave)): NOT DEFINED
        - Media (str(copper | fiber | sgmii)): Available only for Ethernet cards that support this dual-PHY capability.
        - NegotiateMasterSlave (bool): NOT DEFINED
        - Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency
        - SelectedSpeeds (list(str[speed10fd | speed10hd | speed100fd | speed100hd | speed1000])): Which speeds are selected for the current media and AN settings.
        - Speed (str(auto | speed1000 | speed100fd | speed100hd | speed10fd | speed10hd)): The speed and duplex operation options.
        - SpeedAuto (list(str[all | speed1000 | speed100fd | speed100hd | speed10fd | speed10hd])): If selected, allows auto negotiation between ports for speed and duplex operation based on the various choices. The selected capabilities are advertised during AutoNegotiation.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
